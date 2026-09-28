from typing import Any, Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)

from ml.src.preprocessing import CLASSES


def calculate_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: Optional[np.ndarray] = None,
    class_names: List[str] = CLASSES,
) -> Dict[str, Any]:
    """
    Calculate comprehensive evaluation metrics for multi-class skin lesion classification.
    Explicitly tracks Balanced Accuracy, Macro F1, and Melanoma-specific Recall and F1.
    """
    acc = accuracy_score(y_true, y_pred)
    bal_acc = balanced_accuracy_score(y_true, y_pred)
    macro_prec = precision_score(y_true, y_pred, average="macro", zero_division=0)
    macro_rec = recall_score(y_true, y_pred, average="macro", zero_division=0)
    macro_f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)
    weighted_f1 = f1_score(y_true, y_pred, average="weighted", zero_division=0)

    # Per-class metrics
    per_class_prec = precision_score(y_true, y_pred, average=None, zero_division=0)
    per_class_rec = recall_score(y_true, y_pred, average=None, zero_division=0)
    per_class_f1 = f1_score(y_true, y_pred, average=None, zero_division=0)

    per_class_dict = {}
    for idx, name in enumerate(class_names):
        per_class_dict[name] = {
            "precision": float(per_class_prec[idx]) if idx < len(per_class_prec) else 0.0,
            "recall": float(per_class_rec[idx]) if idx < len(per_class_rec) else 0.0,
            "f1": float(per_class_f1[idx]) if idx < len(per_class_f1) else 0.0,
        }

    # Melanoma specific metrics ('mel' index)
    mel_idx = class_names.index("mel") if "mel" in class_names else 4
    melanoma_recall = float(per_class_rec[mel_idx]) if mel_idx < len(per_class_rec) else 0.0
    melanoma_f1 = float(per_class_f1[mel_idx]) if mel_idx < len(per_class_f1) else 0.0

    metrics: Dict[str, Any] = {
        "accuracy": float(acc),
        "balanced_accuracy": float(bal_acc),
        "macro_precision": float(macro_prec),
        "macro_recall": float(macro_rec),
        "macro_f1": float(macro_f1),
        "weighted_f1": float(weighted_f1),
        "melanoma_recall": melanoma_recall,
        "melanoma_f1": melanoma_f1,
        "per_class": per_class_dict,
    }

    # Multiclass ROC-AUC (one-vs-rest)
    if y_prob is not None:
        try:
            auc = roc_auc_score(
                y_true, y_prob, multi_class="ovr", average="macro"
            )
            metrics["macro_roc_auc"] = float(auc)
        except Exception:
            metrics["macro_roc_auc"] = None

    return metrics


def plot_confusion_matrix(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    class_names: List[str] = CLASSES,
    save_path: Optional[str] = None,
    normalize: bool = True,
) -> plt.Figure:
    """Plot and optionally save normalized confusion matrix heatmap."""
    cm = confusion_matrix(y_true, y_pred)
    if normalize:
        cm_norm = cm.astype("float") / (cm.sum(axis=1)[:, np.newaxis] + 1e-7)
        display_data = cm_norm
        fmt = ".2f"
        title = "Normalized Confusion Matrix"
    else:
        display_data = cm
        fmt = "d"
        title = "Confusion Matrix (Counts)"

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        display_data,
        annot=True,
        fmt=fmt,
        cmap="Blues",
        xticklabels=class_names,
        yticklabels=class_names,
        ax=ax,
    )
    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Predicted Label", fontsize=12)
    ax.set_ylabel("True Label", fontsize=12)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")
        plt.close(fig)

    return fig


def plot_roc_curves(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    class_names: List[str] = CLASSES,
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot One-vs-Rest ROC curves for all classes."""
    fig, ax = plt.subplots(figsize=(9, 7))

    for idx, name in enumerate(class_names):
        # Binarize labels for current class
        y_true_binary = (y_true == idx).astype(int)
        fpr, tpr, _ = roc_curve(y_true_binary, y_prob[:, idx])
        try:
            auc_val = roc_auc_score(y_true_binary, y_prob[:, idx])
        except Exception:
            auc_val = 0.0
        ax.plot(fpr, tpr, label=f"{name} (AUC = {auc_val:.3f})")

    ax.plot([0, 1], [0, 1], "k--", alpha=0.7, label="Chance")
    ax.set_xlabel("False Positive Rate", fontsize=12)
    ax.set_ylabel("True Positive Rate", fontsize=12)
    ax.set_title("Multi-class ROC Curves (One-vs-Rest)", fontsize=14, fontweight="bold", pad=12)
    ax.legend(loc="lower right")
    ax.grid(alpha=0.3)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")
        plt.close(fig)

    return fig
