from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "sqlite:///./skills_mirage.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class JobListing(Base):
    __tablename__ = "job_listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    location = Column(String, index=True)
    skills_required = Column(Text) # Comma separated
    tools_mentioned = Column(Text) # Comma separated
    date_posted = Column(DateTime, default=datetime.datetime.utcnow)
    sector = Column(String)

class SkillsDemand(Base):
    __tablename__ = "skills_demand"

    id = Column(Integer, primary_key=True, index=True)
    skill = Column(String, index=True)
    demand_score = Column(Float) # Calculated demand metric
    date = Column(DateTime, default=datetime.datetime.utcnow)

class VulnerabilityScore(Base):
    __tablename__ = "vulnerability_scores"

    id = Column(Integer, primary_key=True, index=True)
    job_category = Column(String, index=True)
    location = Column(String, index=True)
    score = Column(Float) # 0-100
    hiring_trend_pct = Column(Float) # e.g., -34 for 34% decline
    ai_tool_mention_pct = Column(Float) # e.g., 40 for 40% increase
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    provider = Column(String) # NPTEL, SWAYAM, PMKVY
    duration_weeks = Column(Integer)
    skills_taught = Column(Text) # Comma separated
    url = Column(String)
    location = Column(String, nullable=True) # For offline PMKVY centers

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
