import json
import os
from pathlib import Path
from typing import Optional

from ml.src.inference import SkinCancerClassifier
from ml.src.models import count_parameters
from backend.app.config import settings


class ModelRegistry:
    """Singleton registry holding the loaded model instance across the API lifecycle."""

    _classifier: Optional[SkinCancerClassifier] = None

    @classmethod
    def initialize(cls) -> SkinCancerClassifier:
        if cls._classifier is None:
            print(f"Loading SkinCancerClassifier from: {settings.MODEL_PATH}")
            cls._classifier = SkinCancerClassifier(
                model_path=settings.MODEL_PATH,
                metadata_path=settings.METADATA_PATH,
            )
        return cls._classifier

    @classmethod
    def get_classifier(cls) -> SkinCancerClassifier:
        if cls._classifier is None:
            return cls.initialize()
        return cls._classifier

    @classmethod
    def get_info(cls) -> dict:
        clf = cls.get_classifier()
        counts = count_parameters(clf.model)
        metadata = clf.metadata
        return {
            "model_name": clf.model_name,
            "classes": metadata.get("classes", ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]),
            "image_size": clf.image_size,
            "mean": metadata.get("mean", [0.485, 0.456, 0.406]),
            "std": metadata.get("std", [0.229, 0.224, 0.225]),
            "device": clf.device.type,
            "best_macro_f1": metadata.get("best_macro_f1"),
            "parameters_total": counts["total"],
            "parameters_trainable": counts["trainable"],
        }
