from typing import Optional, Union

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F


def compute_class_weights(
    train_df: pd.DataFrame, num_classes: int = 7, device: Optional[torch.device] = None
) -> torch.Tensor:
    """
    Calculate inverse frequency class weights derived STRICTLY from the training set.
    Weight formula: w_c = Total_Samples / (num_classes * count_c)
    """
    if "label" not in train_df.columns:
        raise KeyError("train_df must contain 'label' column to compute class weights.")

    counts = train_df["label"].value_counts().to_dict()
    total_samples = len(train_df)

    weights = np.zeros(num_classes, dtype=np.float32)
    for c in range(num_classes):
        count = counts.get(c, 1)
        weights[c] = total_samples / (num_classes * count)

    # Normalize weights so mean is 1.0
    weights = weights / weights.mean()

    tensor_weights = torch.tensor(weights, dtype=torch.float32)
    if device is not None:
        tensor_weights = tensor_weights.to(device)

    return tensor_weights


class FocalLoss(nn.Module):
    """
    Multi-class Focal Loss to address extreme class imbalance:
    FL(p_t) = -alpha_t * (1 - p_t)^gamma * log(p_t)
    """

    def __init__(
        self,
        weight: Optional[torch.Tensor] = None,
        gamma: float = 2.0,
        reduction: str = "mean",
    ):
        super().__init__()
        self.weight = weight
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, inputs: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        # inputs: [B, C], targets: [B]
        ce_loss = F.cross_entropy(inputs, targets, reduction="none", weight=self.weight)
        pt = torch.exp(-ce_loss)
        focal_loss = ((1.0 - pt) ** self.gamma) * ce_loss

        if self.reduction == "mean":
            return focal_loss.mean()
        elif self.reduction == "sum":
            return focal_loss.sum()
        return focal_loss


def get_loss_fn(
    loss_type: str = "weighted_ce",
    class_weights: Optional[torch.Tensor] = None,
    gamma: float = 2.0,
) -> nn.Module:
    """Factory function for loss functions."""
    if loss_type == "weighted_ce":
        return nn.CrossEntropyLoss(weight=class_weights)
    elif loss_type == "focal":
        return FocalLoss(weight=class_weights, gamma=gamma)
    elif loss_type == "ce":
        return nn.CrossEntropyLoss()
    else:
        raise ValueError(f"Unknown loss_type: '{loss_type}'. Choose 'weighted_ce', 'focal', or 'ce'.")
