from typing import Any, Dict, Tuple

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from ml.src.metrics import calculate_metrics


def validate_epoch(
    model: nn.Module,
    val_loader: DataLoader,
    criterion: nn.Module,
    device: torch.device,
) -> Tuple[float, Dict[str, Any], np.ndarray, np.ndarray, np.ndarray]:
    """
    Run one full validation pass over val_loader.
    Returns: (val_loss, metrics_dict, y_true, y_pred, y_prob)
    """
    model.eval()
    running_loss = 0.0
    total_samples = 0

    all_preds = []
    all_targets = []
    all_probs = []

    with torch.inference_mode():
        for batch in val_loader:
            images = batch["image"].to(device)
            targets = batch["label"].to(device)

            outputs = model(images)
            # Support huggingface model output objects
            if hasattr(outputs, "logits"):
                outputs = outputs.logits

            loss = criterion(outputs, targets)
            running_loss += loss.item() * images.size(0)
            total_samples += images.size(0)

            probs = torch.softmax(outputs, dim=1)
            preds = torch.argmax(probs, dim=1)

            all_probs.append(probs.cpu().numpy())
            all_preds.append(preds.cpu().numpy())
            all_targets.append(targets.cpu().numpy())

    epoch_loss = running_loss / max(total_samples, 1)
    y_true = np.concatenate(all_targets)
    y_pred = np.concatenate(all_preds)
    y_prob = np.concatenate(all_probs)

    metrics = calculate_metrics(y_true, y_pred, y_prob)

    return epoch_loss, metrics, y_true, y_pred, y_prob
