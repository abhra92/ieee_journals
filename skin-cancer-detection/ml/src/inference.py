import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import torch
import torch.nn as nn
from PIL import Image

from ml.src.augmentation import get_inference_transforms
from ml.src.models import create_model
from ml.src.preprocessing import CLASS_DESCRIPTIONS, CLASSES, IDX_TO_CLASS


class SkinCancerClassifier:
    """
    Production-grade inference engine for HAM10000 Skin Lesion Classification.
    Runs efficiently on CPU or GPU using torch.inference_mode().
    """

    def __init__(
        self,
        model_path: str = "models/best_model.pth",
        metadata_path: str = "models/model_metadata.json",
        model_name: str = "tf_efficientnetv2_s",
        image_size: int = 224,
        device: Optional[torch.device] = None,
    ):
        if device is None:
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        else:
            self.device = device

        self.image_size = image_size
        self.model_name = model_name

        # Load metadata if exists
        if os.path.isfile(metadata_path):
            with open(metadata_path, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)
                self.model_name = self.metadata.get("model_name", self.model_name)
                self.image_size = self.metadata.get("image_size", self.image_size)
        else:
            self.metadata = {"model_name": self.model_name, "image_size": self.image_size}

        self.transform = get_inference_transforms(image_size=self.image_size)

        # Build model and load weights
        self.model = create_model(
            model_name=self.model_name,
            num_classes=len(CLASSES),
            pretrained=False,
        )

        if os.path.isfile(model_path):
            state_dict = torch.load(model_path, map_location=self.device)
            self.model.load_state_dict(state_dict)
            print(f"Loaded trained model weights from: {model_path}")
        else:
            print(f"[Warning] Model weights '{model_path}' not found. Initialized with random weights.")

        self.model.to(self.device)
        self.model.eval()

    def predict_image(
        self, image: Union[Image.Image, str, Path], top_k: int = 3
    ) -> Dict[str, Any]:
        """
        Predict skin lesion class for a given PIL Image or image file path.
        Returns top prediction, confidence, top_k predictions, and clinical details.
        """
        if isinstance(image, (str, Path)):
            image = Image.open(image).convert("RGB")
        elif not isinstance(image, Image.Image):
            raise TypeError("Input must be a PIL Image or file path.")

        image_tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.inference_mode():
            outputs = self.model(image_tensor)
            if hasattr(outputs, "logits"):
                outputs = outputs.logits

            probabilities = torch.softmax(outputs, dim=1).squeeze(0)

        probs_np = probabilities.cpu().numpy()
        top_indices = np.argsort(probs_np)[::-1]

        predicted_idx = int(top_indices[0])
        predicted_class = IDX_TO_CLASS[predicted_idx]
        confidence = float(probs_np[predicted_idx])

        top_k_list: List[Dict[str, Any]] = []
        for i in range(min(top_k, len(CLASSES))):
            idx = int(top_indices[i])
            cls_code = IDX_TO_CLASS[idx]
            top_k_list.append(
                {
                    "class": cls_code,
                    "label": CLASS_DESCRIPTIONS.get(cls_code, cls_code),
                    "probability": round(float(probs_np[idx]), 4),
                    "percentage": round(float(probs_np[idx]) * 100, 2),
                }
            )

        all_probs = {
            IDX_TO_CLASS[i]: round(float(probs_np[i]), 4) for i in range(len(CLASSES))
        }

        return {
            "predicted_class": predicted_class,
            "predicted_label": CLASS_DESCRIPTIONS.get(predicted_class, predicted_class),
            "confidence": round(confidence, 4),
            "confidence_percentage": round(confidence * 100, 2),
            "top_predictions": top_k_list,
            "all_probabilities": all_probs,
            "model": self.model_name,
            "device": self.device.type,
            "disclaimer": (
                "This system is a research prototype and is not a substitute for professional medical diagnosis. "
                "Professional clinical evaluation is required."
            ),
        }
