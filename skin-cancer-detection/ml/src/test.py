import json
from pathlib import Path
from typing import Any, Dict, Optional

import pandas as pd
import torch
import torch.nn as nn
from sklearn.metrics import classification_report
from torch.utils.data import DataLoader

from ml.src.metrics import calculate_metrics, plot_confusion_matrix, plot_roc_curves
from ml.src.preprocessing import CLASSES


def evaluate_test_set(
    model: nn.Module,
    test_loader: DataLoader,
    device: torch.device,
    reports_dir: str = "ml/reports",
) -> Dict[str, Any]:
    """
    Perform full evaluation on the hold-out test set.
    Generates test_metrics.json, classification_report.csv, confusion_matrix.png, roc_curve.png.
    """
    model.to(device)
    model.eval()

    all_preds = []
    all_targets = []
    all_probs = []

    with torch.inference_mode():
        for batch in test_loader:
            images = batch["image"].to(device)
            targets = batch["label"].to(device)

            outputs = model(images)
            if hasattr(outputs, "logits"):
                outputs = outputs.logits

            probs = torch.softmax(outputs, dim=1)
            preds = torch.argmax(probs, dim=1)

            all_probs.append(probs.cpu().numpy())
            all_preds.append(preds.cpu().numpy())
            all_targets.append(targets.cpu().numpy())

    import numpy as np

    y_true = np.concatenate(all_targets)
    y_pred = np.concatenate(all_preds)
    y_prob = np.concatenate(all_probs)

    metrics = calculate_metrics(y_true, y_pred, y_prob, class_names=CLASSES)

    out_dir = Path(reports_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Save test metrics JSON
    with open(out_dir / "test_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    # Save classification report as CSV
    clf_dict = classification_report(
        y_true, y_pred, target_names=CLASSES, output_dict=True, zero_division=0
    )
    clf_df = pd.DataFrame(clf_dict).transpose()
    clf_df.to_csv(out_dir / "classification_report.csv")

    # Generate and save Confusion Matrix plot
    plot_confusion_matrix(
        y_true, y_pred, class_names=CLASSES, save_path=str(out_dir / "confusion_matrix.png")
    )

    # Generate and save ROC Curve plot
    plot_roc_curves(
        y_true, y_prob, class_names=CLASSES, save_path=str(out_dir / "roc_curve.png")
    )

    print(f"\n[Test Evaluation Summary]")
    print(f"Accuracy:          {metrics['accuracy']:.4f}")
    print(f"Balanced Accuracy: {metrics['balanced_accuracy']:.4f}")
    print(f"Macro F1:          {metrics['macro_f1']:.4f}")
    print(f"Melanoma Recall:   {metrics['melanoma_recall']:.4f}")
    print(f"Melanoma F1:       {metrics['melanoma_f1']:.4f}")
    if metrics.get("macro_roc_auc"):
        print(f"Macro ROC-AUC:     {metrics['macro_roc_auc']:.4f}")

    return metrics
