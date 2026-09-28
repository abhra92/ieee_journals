from fastapi import APIRouter
from backend.app.schemas import HealthResponse
from backend.app.services.model_registry import ModelRegistry
from ml.src.utils import detect_environment

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Liveness and model readiness probe."""
    clf = ModelRegistry.get_classifier()
    return HealthResponse(
        status="healthy",
        model_loaded=clf.model is not None,
        model_name=clf.model_name,
        device=clf.device.type,
        environment=detect_environment(),
    )
