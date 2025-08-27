import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Online Cinema"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_super_secret_key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.example.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER: str = os.getenv("SMTP_USER", "your@email.com")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "yourpassword")
    FROM_EMAIL: str = os.getenv("FROM_EMAIL", "no-reply@cinema.com")
    BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")

settings = Settings()