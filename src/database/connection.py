from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sys
import os

# Add config to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from config.settings import DATABASE_URL

Base = declarative_base()

# Disable echo in production for better performance
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Get database session with proper cleanup"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database and create all tables"""
    from src.models.patient import Patient
    from src.models.appointment import Doctor, Appointment, Schedule
    
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully!")