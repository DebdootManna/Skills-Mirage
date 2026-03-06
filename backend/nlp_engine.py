import re

KNOWN_SKILLS = ["python", "excel", "communication", "data analysis", "java", "sql", "machine learning", "customer support", "digital marketing", "seo", "leadership", "typing", "management", "reporting"]
KNOWN_TOOLS = ["chatgpt", "copilot", "midjourney", "claude", "gemini", "tensorflow", "pytorch", "huggingface", "tally", "salesforce", "zendesk"]

def extract_insights_from_writeup(text: str):
    text_lower = text.lower()
    
    # Extract skills
    extracted_skills = []
    for skill in KNOWN_SKILLS:
        if skill in text_lower:
            extracted_skills.append(skill.title())
            
    # Extract tools
    extracted_tools = []
    for tool in KNOWN_TOOLS:
        if tool in text_lower:
            extracted_tools.append(tool.title())
            
    # Aspiration heuristic
    aspirations = []
    aspiration_keywords = ["want to learn", "aspire to", "looking to move into", "interested in", "hoping to become", "want to be", "move toward"]
    for keyword in aspiration_keywords:
        if keyword in text_lower:
            # simple extraction of the next few words
            parts = text_lower.split(keyword)
            if len(parts) > 1:
                after_keyword = parts[1].strip().split(".")[0].split(",")[0]
                aspirations.append(after_keyword.strip().title())

    if not aspirations:
        aspirations.append("Upskilling in current domain") # Default fallback
        
    return {
        "skills": extracted_skills,
        "tools": extracted_tools,
        "aspirations": aspirations
    }

def calculate_personal_risk_score(job_title: str, city: str, exp_years: int, writeup: str, base_vulnerability_score: float):
    # Base score comes from Layer 1
    # Adjust score based on experience and extracted skills
    insights = extract_insights_from_writeup(writeup)
    
    score = base_vulnerability_score
    
    # Experience factor: very junior (0-2) or very senior (15+) might be less adaptable or more expensive
    if exp_years < 2:
        score += 5
    elif exp_years > 10:
        score += 10
        
    # Skills factor: knowing AI tools reduces risk
    if insights["tools"]:
        score -= len(insights["tools"]) * 5
        
    # If they already have modern skills, reduce risk
    modern_skills = ["Python", "Machine Learning", "Data Analysis", "Digital Marketing"]
    for skill in insights["skills"]:
        if skill in modern_skills:
            score -= 10
            
    # Cap between 0 and 100
    return max(0, min(100, score)), insights
