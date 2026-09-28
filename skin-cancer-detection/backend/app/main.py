from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api import health, prediction
from backend.app.config import settings
from backend.app.services.model_registry import ModelRegistry


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event: load deep learning model into memory once on startup."""
    print("=" * 60)
    print("FASTAPI STARTUP: Initializing Deep Learning Inference Engine")
    print("=" * 60)
    ModelRegistry.initialize()
    yield
    print("FASTAPI SHUTDOWN: Cleaning up resources.")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Research-grade Skin Lesion Classification and Clinical Explainability API for HAM10000.",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Endpoints
app.include_router(health.router)
app.include_router(prediction.router)


@app.get("/")
async def root():
    return {
        "title": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "online",
        "docs_url": "/docs",
        "disclaimer": (
            "This system is a research prototype and is not a substitute for professional medical diagnosis."
        ),
    }
