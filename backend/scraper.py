import time
import random
import datetime
from sqlalchemy.orm import Session
from backend.database import SessionLocal, JobListing, VulnerabilityScore, Course, init_db

CITIES = ["Pune", "Jaipur", "Indore", "Bangalore", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Surat", "Lucknow", "Kanpur", "Nagpur", "Visakhapatnam", "Bhopal", "Patna", "Ludhiana", "Agra", "Nashik"]
SECTORS = ["IT", "BPO", "Finance", "Healthcare", "Manufacturing", "Retail"]
ROLES = ["Data Entry", "BPO Voice", "Data Analyst", "Software Engineer", "HR Executive", "AI Content Reviewer"]
SKILLS = ["Python", "Excel", "Communication", "Data Analysis", "Java", "SQL", "Machine Learning", "Customer Support", "Digital Marketing", "SEO"]
AI_TOOLS = ["ChatGPT", "Copilot", "Midjourney", "Claude", "Gemini", "TensorFlow", "PyTorch", "HuggingFace"]

def seed_courses(db: Session):
    if db.query(Course).count() == 0:
        courses = [
            Course(title="Data Basics", provider="NPTEL", duration_weeks=3, skills_taught="Data Analysis,Excel,Python", url="https://nptel.ac.in", location="Online"),
            Course(title="AI Fundamentals", provider="SWAYAM", duration_weeks=2, skills_taught="AI,ChatGPT,Machine Learning", url="https://swayam.gov.in", location="Online"),
            Course(title="Digital Marketing", provider="PMKVY", duration_weeks=4, skills_taught="Digital Marketing,SEO", url="https://pmkvyofficial.org", location="Nagpur centre, Wardha Rd"),
            Course(title="Advanced Python", provider="NPTEL", duration_weeks=8, skills_taught="Python,Software Engineering", url="https://nptel.ac.in", location="Online"),
            Course(title="Customer Success Management", provider="SWAYAM", duration_weeks=4, skills_taught="Customer Support,Communication", url="https://swayam.gov.in", location="Online"),
            Course(title="AI Content Creation", provider="SWAYAM", duration_weeks=3, skills_taught="AI,ChatGPT,Content Creation", url="https://swayam.gov.in", location="Online"),
        ]
        db.add_all(courses)
        db.commit()

def generate_mock_job(db: Session, date: datetime.datetime = None):
    if not date:
        date = datetime.datetime.now(datetime.UTC)
    role = random.choice(ROLES)
    city = random.choice(CITIES)
    sector = random.choice(SECTORS)
    req_skills = ",".join(random.sample(SKILLS, k=random.randint(2, 5)))
    tools = ",".join(random.sample(AI_TOOLS, k=random.randint(0, 3))) if random.random() > 0.5 else ""
    
    job = JobListing(
        title=role,
        company=f"Company_{random.randint(1,100)}",
        location=city,
        skills_required=req_skills,
        tools_mentioned=tools,
        date_posted=date,
        sector=sector
    )
    db.add(job)
    return job

def recalculate_vulnerabilities(db: Session):
    for role in ROLES:
        for city in random.sample(CITIES, k=5): # Update 5 cities per role per tick
            score_entry = db.query(VulnerabilityScore).filter(
                VulnerabilityScore.job_category == role,
                VulnerabilityScore.location == city
            ).first()
            
            if not score_entry:
                score_entry = VulnerabilityScore(job_category=role, location=city)
                db.add(score_entry)
            
            # Simulated calculation mimicking real-world shifts
            if role in ["BPO Voice", "Data Entry"]:
                score_entry.score = random.uniform(70, 95)
                score_entry.hiring_trend_pct = random.uniform(-40, -10)
                score_entry.ai_tool_mention_pct = random.uniform(20, 50)
            elif role in ["Data Analyst", "HR Executive"]:
                score_entry.score = random.uniform(40, 60)
                score_entry.hiring_trend_pct = random.uniform(-10, 10)
                score_entry.ai_tool_mention_pct = random.uniform(10, 30)
            else:
                score_entry.score = random.uniform(10, 30)
                score_entry.hiring_trend_pct = random.uniform(10, 30)
                score_entry.ai_tool_mention_pct = random.uniform(40, 80)
                
            score_entry.updated_at = datetime.datetime.now(datetime.UTC)
            
    db.commit()

def run_scraper_loop():
    init_db()
    db = SessionLocal()
    seed_courses(db)
    
    print("Backfilling initial job data...")
    if db.query(JobListing).count() < 1000:
        for _ in range(1000):
            past_date = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=random.randint(0, 365))
            generate_mock_job(db, past_date)
        db.commit()
        
    print("Starting live scraper simulation loop...")
    while True:
        for _ in range(random.randint(5, 15)):
            generate_mock_job(db)
        db.commit()
        
        recalculate_vulnerabilities(db)
        print(f"[{datetime.datetime.now(datetime.UTC)}] Added new jobs and updated vulnerability scores.")
        time.sleep(10)

if __name__ == "__main__":
    run_scraper_loop()
