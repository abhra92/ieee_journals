import json
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
import torch
import torch.nn as nn
from torch.cuda.amp import GradScaler, autocast
from torch.optim import AdamW
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch.utils.data import DataLoader

from ml.src.preprocessing import CLASSES, CLASS_TO_IDX, IMAGENET_MEAN, IMAGENET_STD
from ml.src.validate import validate_epoch


def train_model(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    criterion: nn.Module,
    device: torch.device,
    epochs: int = 15,
    learning_rate: float = 0.0003,
    weight_decay: float = 0.01,
    accumulate_grad_batches: int = 2,
    gradient_clip_val: float = 1.0,
    use_amp: bool = True,
    checkpoint_dir: str = "ml/checkpoints",
    best_model_path: str = "models/best_model.pth",
    final_model_path: str = "models/final_model.pth",
    metadata_path: str = "models/model_metadata.json",
    model_name: str = "tf_efficientnetv2_s",
    image_size: int = 224,
    resume_from_checkpoint: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Execute full training loop with AMP, gradient accumulation, and checkpoint management.
    Handles CUDA OOM gracefully with cache clearing.
    """
    os.makedirs(checkpoint_dir, exist_ok=True)
    os.makedirs(Path(best_model_path).parent, exist_ok=True)

    optimizer = AdamW(
        [p for p in model.parameters() if p.requires_grad],
        lr=learning_rate,
        weight_decay=weight_decay,
    )
    scheduler = CosineAnnealingLR(optimizer, T_max=epochs, eta_min=1e-6)
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp and device.type == "cuda")

    start_epoch = 0
    best_macro_f1 = 0.0
    history: List[Dict[str, Any]] = []

    # Checkpoint resumption
    if resume_from_checkpoint and os.path.isfile(resume_from_checkpoint):
        print(f"Resuming training from checkpoint: {resume_from_checkpoint}")
        ckpt = torch.load(resume_from_checkpoint, map_location=device)
        model.load_state_dict(ckpt["model_state"])
        optimizer.load_state_dict(ckpt["optimizer_state"])
        scheduler.load_state_dict(ckpt["scheduler_state"])
        if "scaler_state" in ckpt and ckpt["scaler_state"] is not None:
            scaler.load_state_dict(ckpt["scaler_state"])
        start_epoch = ckpt.get("epoch", 0) + 1
        best_macro_f1 = ckpt.get("best_macro_f1", 0.0)
        history = ckpt.get("history", [])

    model.to(device)

    total_start_time = time.time()

    for epoch in range(start_epoch, epochs):
        epoch_start_time = time.time()
        model.train()
        running_train_loss = 0.0
        train_samples = 0
        optimizer.zero_grad(set_to_none=True)

        try:
            for batch_idx, batch in enumerate(train_loader):
                images = batch["image"].to(device, non_blocking=True)
                targets = batch["label"].to(device, non_blocking=True)

                with torch.amp.autocast("cuda", enabled=use_amp and device.type == "cuda"):
                    outputs = model(images)
                    if hasattr(outputs, "logits"):
                        outputs = outputs.logits
                    loss = criterion(outputs, targets)
                    # Normalize for gradient accumulation
                    loss = loss / accumulate_grad_batches

                scaler.scale(loss).backward()

                if (batch_idx + 1) % accumulate_grad_batches == 0 or (batch_idx + 1) == len(train_loader):
                    if gradient_clip_val > 0.0:
                        scaler.unscale_(optimizer)
                        torch.nn.utils.clip_grad_norm_(model.parameters(), gradient_clip_val)

                    scaler.step(optimizer)
                    scaler.update()
                    optimizer.zero_grad(set_to_none=True)

                running_train_loss += loss.item() * accumulate_grad_batches * images.size(0)
                train_samples += images.size(0)

        except torch.cuda.OutOfMemoryError as oom_err:
            torch.cuda.empty_cache()
            print(f"\n[CUDA OOM] Caught OutOfMemoryError at epoch {epoch + 1}: {oom_err}")
            print("Cleared CUDA cache. Consider lowering batch_size or increasing accumulate_grad_batches.")
            raise oom_err

        scheduler.step()

        train_loss = running_train_loss / max(train_samples, 1)

        # Validation
        val_loss, val_metrics, _, _, _ = validate_epoch(model, val_loader, criterion, device)
        epoch_duration = time.time() - epoch_start_time

        macro_f1 = val_metrics["macro_f1"]
        balanced_acc = val_metrics["balanced_accuracy"]
        mel_f1 = val_metrics["melanoma_f1"]

        print(
            f"Epoch [{epoch + 1}/{epochs}] ({epoch_duration:.1f}s) - "
            f"Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | "
            f"Macro F1: {macro_f1:.4f} | Bal Acc: {balanced_acc:.4f} | Mel F1: {mel_f1:.4f}"
        )

        epoch_record = {
            "epoch": epoch + 1,
            "train_loss": train_loss,
            "val_loss": val_loss,
            "accuracy": val_metrics["accuracy"],
            "balanced_accuracy": balanced_acc,
            "macro_f1": macro_f1,
            "macro_recall": val_metrics["macro_recall"],
            "melanoma_recall": val_metrics["melanoma_recall"],
            "melanoma_f1": mel_f1,
            "duration_sec": epoch_duration,
        }
        history.append(epoch_record)

        # Save latest checkpoint for resumption
        latest_ckpt_path = os.path.join(checkpoint_dir, "latest_checkpoint.pth")
        torch.save(
            {
                "epoch": epoch,
                "model_state": model.state_dict(),
                "optimizer_state": optimizer.state_dict(),
                "scheduler_state": scheduler.state_dict(),
                "scaler_state": scaler.state_dict() if scaler.is_enabled() else None,
                "best_macro_f1": best_macro_f1,
                "history": history,
            },
            latest_ckpt_path,
        )

        # Check if best model
        if macro_f1 > best_macro_f1:
            best_macro_f1 = macro_f1
            print(f"--> Best Macro F1 improved to {best_macro_f1:.4f}. Saving {best_model_path}")
            torch.save(model.state_dict(), best_model_path)

    total_duration = time.time() - total_start_time

    # Save final model
    torch.save(model.state_dict(), final_model_path)

    # Save history to CSV
    history_df = pd.DataFrame(history)
    reports_dir = Path("ml/reports")
    reports_dir.mkdir(parents=True, exist_ok=True)
    history_df.to_csv(reports_dir / "training_history.csv", index=False)

    # Save model metadata
    metadata = {
        "model_name": model_name,
        "image_size": image_size,
        "num_classes": len(CLASSES),
        "classes": CLASSES,
        "class_to_idx": CLASS_TO_IDX,
        "mean": IMAGENET_MEAN,
        "std": IMAGENET_STD,
        "best_macro_f1": float(best_macro_f1),
        "total_epochs": epochs,
        "total_train_time_sec": float(total_duration),
        "device": device.type,
    }
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    return {
        "best_macro_f1": best_macro_f1,
        "history": history,
        "total_duration_sec": total_duration,
        "metadata": metadata,
    }
