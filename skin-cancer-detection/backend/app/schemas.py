from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(..., json_schema_extra={"example": "healthy"})
    model_loaded: bool = Field(..., json_schema_extra={"example": True})
    model_name: str = Field(..., json_schema_extra={"example": "tf_efficientnetv2_s"})
    device: str = Field(..., json_schema_extra={"example": "cpu"})
    environment: str = Field(..., json_schema_extra={"example": "local"})


class ClassPrediction(BaseModel):
    dx_class: str = Field(..., json_schema_extra={"example": "mel"}, alias="class")
    label: str = Field(..., json_schema_extra={"example": "Melanoma (Malignant)"})
    probability: float = Field(..., json_schema_extra={"example": 0.8842})
    percentage: float = Field(..., json_schema_extra={"example": 88.42})

    model_config = {"populate_by_name": True}


class PredictionResponse(BaseModel):
    predicted_class: str = Field(..., json_schema_extra={"example": "mel"})
    predicted_label: str = Field(..., json_schema_extra={"example": "Melanoma (Malignant)"})
    confidence: float = Field(..., json_schema_extra={"example": 0.8842})
    confidence_percentage: float = Field(..., json_schema_extra={"example": 88.42})
    top_predictions: List[ClassPrediction]
    all_probabilities: Dict[str, float]
    model: str = Field(..., json_schema_extra={"example": "tf_efficientnetv2_s"})
    device: str = Field(..., json_schema_extra={"example": "cpu"})
    disclaimer: str = Field(
        ...,
        json_schema_extra={
            "example": "This system is a research prototype and is not a substitute for professional medical diagnosis. Professional clinical evaluation is required."
        },
    )


class ExplainResponse(BaseModel):
    prediction: PredictionResponse
    overlay_base64: str = Field(..., description="Base64 encoded data URI of Grad-CAM overlay")
    target_class: str = Field(..., json_schema_extra={"example": "mel"})
    disclaimer: str


class ModelInfoResponse(BaseModel):
    model_name: str
    classes: List[str]
    image_size: int
    mean: List[float]
    std: List[float]
    device: str
    best_macro_f1: Optional[float] = None
    parameters_total: Optional[int] = None
    parameters_trainable: Optional[int] = None
