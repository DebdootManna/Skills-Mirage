from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
import datetime
import os
from dotenv import load_dotenv

from backend.database import SessionLocal, JobListing, VulnerabilityScore, Course
from backend.nlp_engine import calculate_personal_risk_score, extract_insights_from_writeup
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

app = FastAPI(title="Skills Mirage API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Models
class WorkerProfile(BaseModel):
    job_title: str
    city: str
    exp_years: int
    writeup: str

class ChatRequest(BaseModel):
    message: str
    context: dict

# Dashboard Endpoints (Layer 1)
@app.get("/api/dashboard/hiring-trends")
def get_hiring_trends(db: Session = Depends(get_db)):
    # Group by sector and date to show volume trends
    # For demo, we just fetch counts by sector
    sector_counts = db.query(JobListing.sector, func.count(JobListing.id)).group_by(JobListing.sector).all()
    city_counts = db.query(JobListing.location, func.count(JobListing.id)).group_by(JobListing.location).all()
    
    return {
        "sector_trends": [{"sector": s, "count": c} for s, c in sector_counts],
        "city_trends": [{"city": c, "count": cnt} for c, cnt in city_counts]
    }

@app.get("/api/dashboard/vulnerability")
def get_vulnerabilities(db: Session = Depends(get_db)):
    scores = db.query(VulnerabilityScore).all()
    return [{"job_category": s.job_category, "location": s.location, "score": s.score, "hiring_trend_pct": s.hiring_trend_pct, "ai_tool_mention_pct": s.ai_tool_mention_pct} for s in scores]

# Worker Engine Endpoints (Layer 2)
@app.post("/api/worker/analyze")
def analyze_worker(profile: WorkerProfile, db: Session = Depends(get_db)):
    # Find base vulnerability for the role/city
    # To handle slight mismatches, we can do an ILIKE or exact match
    # For simplicity, let's look for a partial match
    vuln = db.query(VulnerabilityScore).filter(
        func.lower(VulnerabilityScore.location) == profile.city.lower()
    ).all()
    
    base_score_obj = None
    for v in vuln:
        if v.job_category.lower() in profile.job_title.lower() or profile.job_title.lower() in v.job_category.lower():
            base_score_obj = v
            break
            
    base_score = base_score_obj.score if base_score_obj else 50.0
    
    risk_score, insights = calculate_personal_risk_score(
        profile.job_title, profile.city, profile.exp_years, profile.writeup, base_score
    )
    
    # Generate Reskilling Path
    # Find courses that teach skills the user doesn't have, or modern skills
    # Simple logic: suggest AI or Data courses if risk is high
    courses = db.query(Course).all()
    
    # Filter courses based on user's extracted aspirations or general upskilling
    path = []
    current_week = 1
    for c in courses:
        if current_week > 12: # limit path
            break
        # If user wants Data, give Data courses, etc.
        # Here we just give a structured path
        path.append({
            "week": f"Week {current_week}-{current_week + c.duration_weeks - 1}",
            "course": c.title,
            "provider": c.provider,
            "location": c.location,
            "url": c.url,
            "duration": c.duration_weeks
        })
        current_week += c.duration_weeks

    # Ensure the target role (implied by path) is verified from L1 data
    # We find a low-risk role in L1 to suggest
    low_risk_roles = db.query(VulnerabilityScore).filter(
        func.lower(VulnerabilityScore.location) == profile.city.lower(),
        VulnerabilityScore.score < 40
    ).order_by(VulnerabilityScore.score).first()
    
    target_role = low_risk_roles.job_category if low_risk_roles else "Software Engineer"
    
    return {
        "risk_score": round(risk_score, 1),
        "insights": insights,
        "base_metrics": {
            "hiring_trend": base_score_obj.hiring_trend_pct if base_score_obj else 0,
            "ai_mentions": base_score_obj.ai_tool_mention_pct if base_score_obj else 0
        },
        "target_role": target_role,
        "reskilling_path": path
    }

@app.post("/api/worker/chat")
def chat_with_worker(req: ChatRequest, db: Session = Depends(get_db)):
    msg = req.message.lower()
    
    # Simple query check for specific L1 data question (e.g., "How many BPO jobs in Indore?")
    if "bpo jobs" in msg and "indore" in msg:
        count = db.query(JobListing).filter(
            JobListing.location.ilike("%indore%"),
            JobListing.sector.ilike("%bpo%")
        ).count()
        return {"response": f"Based on live data, there are currently {count} active BPO job listings in Indore."}
        
    if "मुझे क्या करना चाहिए" in msg or "hindi" in req.context.get("profile", {}).get("writeup", "").lower():
        # Handle hindi query
        return {"response": "आपकी प्रोफाइल के आधार पर आपका रिस्क स्कोर उच्च है। आपको AI और Data Analysis जैसे नए कौशल सीखने चाहिए। आप NPTEL या SWAYAM से मुफ्त कोर्स शुरू कर सकते हैं।"}

    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        try:
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
            system_prompt = f"""You are an AI career advisor for the Indian workforce.
User Profile: {req.context.get('profile')}
Live Market Context: {req.context.get('market')}
Answer the user's questions based on this exact context. If asked about risk score, cite the hiring trend and AI tool mentions. If asked about safe jobs, cite low-risk jobs in their city. If asked in Hindi, respond in Hindi.
            """
            response = llm([SystemMessage(content=system_prompt), HumanMessage(content=req.message)])
            return {"response": response.content}
        except Exception as e:
            print("LLM Error:", e)
            
    # Fallback if no API key or error
    if "risk score" in msg:
        hiring_trend = req.context.get('market', {}).get('base_metrics', {}).get('hiring_trend', 0)
        ai_mentions = req.context.get('market', {}).get('base_metrics', {}).get('ai_mentions', 0)
        return {"response": f"Your risk score is calculated based on live market signals. In your city and role, hiring has shifted by {round(hiring_trend, 1)}% and AI tool mentions in job descriptions have changed by {round(ai_mentions, 1)}%."}
    elif "safer" in msg or "safe" in msg:
        target = req.context.get('market', {}).get('target_role', 'Data Analyst')
        return {"response": f"Based on the Vulnerability Index for your city, '{target}' is a much safer role right now with a low risk score and active hiring."}
    elif "3 months" in msg or "less than" in msg:
        return {"response": "You can complete the 'Data Basics' (3 weeks) and 'AI Fundamentals' (2 weeks) courses via NPTEL and SWAYAM in under 2 months total. This perfectly fits your timeline."}
        
    return {"response": "I am here to help you navigate your career and upskill. What specific questions do you have about your risk score or reskilling path?"}
