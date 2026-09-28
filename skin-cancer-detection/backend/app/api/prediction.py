from typing import Optional
from fastapi import APIRouter, File, Form, UploadFile

from backend.app.schemas import (
    ExplainResponse,
    ModelInfoResponse,
    PredictionResponse,
)
from backend.app.services.explainability import run_model_explanation
from backend.app.services.inference import run_model_inference
from backend.app.services.model_registry import ModelRegistry
from backend.app.services.preprocessing import validate_and_load_image

router = APIRouter(tags=["Prediction"])


@router.get("/model-info", response_model=ModelInfoResponse)
async def get_model_info():
    """Retrieve metadata, parameters, and configuration of the active model."""
    return ModelRegistry.get_info()


@router.post("/predict", response_model=PredictionResponse)
async def predict_single(file: UploadFile = File(...)):
    """Predict skin lesion category and return top-1 diagnosis with full distribution."""
    image = await validate_and_load_image(file)
    result = run_model_inference(image, top_k=1)
    return result


@router.post("/predict/top-k", response_model=PredictionResponse)
async def predict_top_k(
    file: UploadFile = File(...),
    k: int = Form(default=3),
):
    """Predict skin lesion category and return top-K differential diagnosis."""
    image = await validate_and_load_image(file)
    result = run_model_inference(image, top_k=k)
    return result


@router.post("/explain", response_model=ExplainResponse)
async def explain_prediction(
    file: UploadFile = File(...),
    target_class_idx: Optional[int] = Form(default=None),
):
    """Compute prediction and generate visual Grad-CAM clinical heatmap overlay."""
    image = await validate_and_load_image(file)
    explanation = run_model_explanation(image, target_class_idx=target_class_idx)
    return explanation
