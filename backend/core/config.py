import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()

class Settings:
    PROJECT_TITLE: str = "Traceon-AI Backend API"
    # Kodun içine hardcode yazmak yerine güvenli şekilde çevreden okuyoruz
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    EMBEDDING_MODEL: str = "models/embedding-001"
    LLM_MODEL: str = "gemini-pro"

settings = Settings()