import os
from pathlib import Path
from pydantic import BaseModel


class Settings(BaseModel):
    PROJECT_NAME: str = "Skin Cancer Detection & Clinical Decision Support API"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"

    # Host & Port
    HOST: str = os.getenv("API_HOST", "127.0.0.1")
    PORT: int = int(os.getenv("API_PORT", 8000))

    # Model & Artifact paths
    MODEL_PATH: str = os.getenv("MODEL_PATH", "models/best_model.pth")
    METADATA_PATH: str = os.getenv("METADATA_PATH", "models/model_metadata.json")

    # Upload validation
    MAX_UPLOAD_SIZE_BYTES: int = 15 * 1024 * 1024  # 15 MB
    ALLOWED_IMAGE_EXTENSIONS: set = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
    ALLOWED_CONTENT_TYPES: set = {
        "image/jpeg",
        "image/png",
        "image/bmp",
        "image/webp",
    }

    CORS_ORIGINS: list = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "*",
    ]


settings = Settings()
