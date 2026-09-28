from typing import Any, Dict, Optional
from PIL import Image

from backend.app.services.model_registry import ModelRegistry
from ml.src.explainability import generate_gradcam_explanation


def run_model_explanation(
    image: Image.Image, target_class_idx: Optional[int] = None
) -> Dict[str, Any]:
    """Generate Grad-CAM explanation using the registered model."""
    classifier = ModelRegistry.get_classifier()
    explanation = generate_gradcam_explanation(
        model=classifier.model,
        image=image,
        image_size=classifier.image_size,
        device=classifier.device,
        target_class_idx=target_class_idx,
    )
    prediction = classifier.predict_image(image, top_k=3)
    return {
        "prediction": prediction,
        "overlay_base64": explanation["overlay_base64"],
        "target_class": prediction["predicted_class"],
        "disclaimer": prediction["disclaimer"],
    }
