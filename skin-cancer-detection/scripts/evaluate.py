import argparse
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
import torch

from ml.src.augmentation import get_val_transforms
from ml.src.dataset import create_dataloader
from ml.src.models import create_model
from ml.src.test import evaluate_test_set
from ml.src.utils import get_device, load_config


def main():
    parser = argparse.ArgumentParser(description="Evaluate Skin Cancer Model on Test Set")
    parser.add_argument("--config", type=str, default="ml/configs/default_config.yaml")
    parser.add_argument("--model-path", type=str, default="models/best_model.pth")
    parser.add_argument("--test-split", type=str, default="ml/data/splits/test.csv")
    args = parser.parse_args()

    config = load_config(args.config)
    device = get_device()

    test_path = Path(args.test_split)
    if not test_path.is_file():
        print(f"Test split not found at: {test_path}")
        sys.exit(1)

    model_path = Path(args.model_path)
    if not model_path.is_file():
        print(f"Model checkpoint not found at: {model_path}")
        sys.exit(1)

    test_df = pd.read_csv(test_path)
    image_size = config["data"]["image_size"]
    test_transform = get_val_transforms(image_size=image_size)

    test_loader = create_dataloader(
        test_df,
        transform=test_transform,
        batch_size=config["training"]["batch_size"],
        shuffle=False,
        num_workers=0 if device.type == "cpu" else 2,
    )

    model = create_model(
        model_name=config["model"]["name"],
        num_classes=config["data"]["num_classes"],
        pretrained=False,
    )
    state_dict = torch.load(model_path, map_location=device)
    model.load_state_dict(state_dict)

    evaluate_test_set(
        model=model,
        test_loader=test_loader,
        device=device,
        reports_dir="ml/reports",
    )


if __name__ == "__main__":
    main()
