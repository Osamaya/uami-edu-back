from pathlib import Path
import os
from dotenv import load_dotenv
from typing import Optional

# Carga automática de .env
BASE_DIR = Path(__file__).parent.parent.parent
load_dotenv(BASE_DIR / ".env")

class Settings:
    # MongoDB
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DB: str = os.getenv("MONGO_DB")
    # SQL Server
    SQL_SERVER: Optional[str] = os.getenv("SQL_SERVER")
    SQL_DB: Optional[str] = os.getenv("SQL_DB")
    SQL_USER: Optional[str] = os.getenv("SQL_USER")
    SQL_PWD: Optional[str] = os.getenv("SQL_PWD")
    
    # Auth
    SECRET_KEY: str = os.getenv("SECRET_KEY", "fallback-secret-key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    
settings = Settings()