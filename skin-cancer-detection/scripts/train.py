import argparse
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
import torch

from ml.src.augmentation import get_train_transforms, get_val_transforms
from ml.src.dataset import create_dataloader
from ml.src.losses import compute_class_weights, get_loss_fn
from ml.src.models import count_parameters, create_model
from ml.src.train import train_model
from ml.src.utils import get_device, load_config, set_seed


def main():
    parser = argparse.ArgumentParser(description="HAM10000 Skin Lesion Model Training")
    parser.add_argument("--config", type=str, default="ml/configs/default_config.yaml")
    parser.add_argument("--smoke-test", action="store_true", help="Run 1 batch smoke test")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--model", type=str, default=None)
    parser.add_argument("--resume", type=str, default=None)
    args = parser.parse_args()

    config = load_config(args.config)
    set_seed(config["project"].get("seed", 42))

    device = get_device()
    print("=" * 60)
    print(f"TRAINING PIPELINE INITIALIZATION | Device: {device.type.upper()}")
    print("=" * 60)

    # Resolve paths
    train_split_path = Path(config["data"]["train_split"])
    val_split_path = Path(config["data"]["val_split"])

    if not train_split_path.is_file() or not val_split_path.is_file():
        print("Split files not found. Please run 'python scripts/create_splits.py' first.")
        sys.exit(1)

    train_df = pd.read_csv(train_split_path)
    val_df = pd.read_csv(val_split_path)

    # Handle smoke-test mode
    if args.smoke_test:
        print("[SMOKE TEST MODE] Selecting 16 samples for rapid CPU/GPU verification...")
        train_df = train_df.head(16)
        val_df = val_df.head(8)
        epochs = 1
        batch_size = 4
        accumulate_grad_batches = 1
    else:
        epochs = args.epochs or config["training"]["epochs"]
        batch_size = args.batch_size or config["training"]["batch_size"]
        accumulate_grad_batches = config["training"]["accumulate_grad_batches"]

    model_name = args.model or config["model"]["name"]
    image_size = config["data"]["image_size"]

    print(f"Model:                   {model_name}")
    print(f"Epochs:                  {epochs}")
    print(f"Batch Size:              {batch_size}")
    print(f"Accumulate Grad Batches: {accumulate_grad_batches}")
    print(f"Image Size:              {image_size}x{image_size}")
    print(f"Train Samples:           {len(train_df)}")
    print(f"Validation Samples:      {len(val_df)}")

    # Transforms & DataLoaders
    train_transform = get_train_transforms(image_size=image_size)
    val_transform = get_val_transforms(image_size=image_size)

    train_loader = create_dataloader(
        train_df,
        transform=train_transform,
        batch_size=batch_size,
        shuffle=True,
        num_workers=0 if device.type == "cpu" else 2,
    )
    val_loader = create_dataloader(
        val_df,
        transform=val_transform,
        batch_size=batch_size,
        shuffle=False,
        num_workers=0 if device.type == "cpu" else 2,
    )

    # Loss function with train-only class weights
    class_weights = compute_class_weights(
        train_df, num_classes=config["data"]["num_classes"], device=device
    )
    criterion = get_loss_fn(
        loss_type=config["training"]["loss_type"],
        class_weights=class_weights,
        gamma=config["training"].get("focal_loss_gamma", 2.0),
    )

    # Model construction
    model = create_model(
        model_name=model_name,
        num_classes=config["data"]["num_classes"],
        pretrained=config["model"]["pretrained"],
        drop_rate=config["model"]["drop_rate"],
        drop_path_rate=config["model"]["drop_path_rate"],
    )
    param_counts = count_parameters(model)
    print(f"Parameters: Total={param_counts['total']:,} | Trainable={param_counts['trainable']:,}")

    # Train
    result = train_model(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        criterion=criterion,
        device=device,
        epochs=epochs,
        learning_rate=config["training"]["learning_rate"],
        weight_decay=config["training"]["weight_decay"],
        accumulate_grad_batches=accumulate_grad_batches,
        gradient_clip_val=config["training"]["gradient_clip_val"],
        use_amp=config["training"]["mixed_precision"] and device.type == "cuda",
        checkpoint_dir=config["model"]["checkpoint_dir"],
        best_model_path=config["model"]["best_model_path"],
        final_model_path=config["model"]["final_model_path"],
        metadata_path=config["model"]["metadata_path"],
        model_name=model_name,
        image_size=image_size,
        resume_from_checkpoint=args.resume,
    )

    print("\nTraining complete!")
    print(f"Best Macro F1: {result['best_macro_f1']:.4f}")
    print(f"Total Duration: {result['total_duration_sec']:.1f}s")


if __name__ == "__main__":
    main()
