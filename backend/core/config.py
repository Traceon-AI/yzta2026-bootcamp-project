import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()

class Settings:
    PROJECT_TITLE: str = "Traceon-AI Backend API"
    # Kodun içine hardcode yazmak yerine güvenli şekilde çevreden okuyoruz
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    EMBEDDING_MODEL: str = "models/embedding-001"
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gemini-2.0-flash")
    LLM_TIMEOUT_SECONDS: int = int(os.getenv("LLM_TIMEOUT_SECONDS", "60"))
    LLM_MAX_RETRIES: int = int(os.getenv("LLM_MAX_RETRIES", "4"))
    LLM_BACKOFF_BASE_SECONDS: float = float(os.getenv("LLM_BACKOFF_BASE_SECONDS", "2"))
    LLM_MAX_DOC_CHUNKS: int = int(os.getenv("LLM_MAX_DOC_CHUNKS", "40"))
    LLM_MAX_CHARS_PER_CHUNK: int = int(os.getenv("LLM_MAX_CHARS_PER_CHUNK", "800"))

settings = Settings()