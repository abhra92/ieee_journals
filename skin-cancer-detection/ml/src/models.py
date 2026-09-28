from typing import Any, Dict, Optional, Tuple, Union

import timm
import torch
import torch.nn as nn

MODEL_REGISTRY: Dict[str, str] = {
    "tf_efficientnetv2_s": "tf_efficientnetv2_s.in21k_ft_in1k",
    "resnet50": "resnet50.a1_in1k",
    "densenet121": "densenet121.ra_in1k",
    "convnext_tiny": "convnext_tiny.fb_in22k_ft_in1k",
    "vit_base_patch16_224": "vit_base_patch16_224.augreg_in21k_ft_in1k",
    "swin_tiny": "swin_tiny_patch4_window7_224.ms_in1k",
    "hf_vit_large": "Kuldeepmishra3/vit-large-skin-cancer-ham10000",
}


def count_parameters(model: nn.Module) -> Dict[str, int]:
    """Return count of total, trainable, and frozen parameters."""
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    frozen = total - trainable
    return {"total": total, "trainable": trainable, "frozen": frozen}


def create_model(
    model_name: str = "tf_efficientnetv2_s",
    num_classes: int = 7,
    pretrained: bool = True,
    drop_rate: float = 0.2,
    drop_path_rate: float = 0.1,
    freeze_backbone: bool = False,
) -> nn.Module:
    """
    Factory to construct supported deep learning models for HAM10000 classification.
    Supports timm architectures and HuggingFace ViT models.
    """
    if model_name in ("hf_vit_large", "Kuldeepmishra3/vit-large-skin-cancer-ham10000"):
        from transformers import AutoModelForImageClassification

        hf_id = "Kuldeepmishra3/vit-large-skin-cancer-ham10000"
        model = AutoModelForImageClassification.from_pretrained(
            hf_id,
            num_labels=num_classes,
            ignore_mismatched_sizes=True,
        )
        if freeze_backbone:
            for param in model.vit.parameters():
                param.requires_grad = False
        return model

    # Map alias to timm identifier
    timm_name = MODEL_REGISTRY.get(model_name, model_name)

    try:
        model = timm.create_model(
            timm_name,
            pretrained=pretrained,
            num_classes=num_classes,
            drop_rate=drop_rate,
            drop_path_rate=drop_path_rate if "swin" in timm_name or "vit" in timm_name or "convnext" in timm_name else 0.0,
        )
    except Exception as e:
        # Fallback to base name without specific weights tag if unavailable
        model = timm.create_model(
            model_name,
            pretrained=pretrained,
            num_classes=num_classes,
            drop_rate=drop_rate,
        )

    if freeze_backbone:
        # Freeze all layers except final classification head
        for name, param in model.named_parameters():
            if not any(head in name for head in ["head", "fc", "classifier"]):
                param.requires_grad = False

    return model
