from typing import Any, Dict
from PIL import Image

from backend.app.services.model_registry import ModelRegistry


def run_model_inference(image: Image.Image, top_k: int = 3) -> Dict[str, Any]:
    """Execute prediction using the registered SkinCancerClassifier."""
    classifier = ModelRegistry.get_classifier()
    return classifier.predict_image(image, top_k=top_k)
