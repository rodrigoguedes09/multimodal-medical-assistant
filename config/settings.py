"""
Configuration settings for Medical Automation API
"""
import os

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///medical_automation.db")

# Application settings
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here_change_in_production")
API_VERSION = "v1"

# Redis configuration (optional)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

# Cache TTL settings (in seconds)
CACHE_TTL_DEFAULT = 300  # 5 minutes
CACHE_TTL_SCHEDULES = 300  # 5 minutes
CACHE_TTL_DOCTORS = 3600  # 1 hour