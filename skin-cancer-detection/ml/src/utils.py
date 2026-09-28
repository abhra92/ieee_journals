import os
import random
import sys
from pathlib import Path
from typing import Any, Dict

import numpy as np
import torch
import yaml


def set_seed(seed: int = 42) -> None:
    """Fix random seeds for reproducible experiments."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def detect_environment() -> str:
    """Detect whether code is running on Google Colab or Local machine."""
    if "google.colab" in sys.modules or os.path.exists("/content"):
        return "colab"
    return "local"


def get_device() -> torch.device:
    """Return available torch device (CUDA if available, otherwise CPU)."""
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def load_config(config_path: str = "ml/configs/default_config.yaml") -> Dict[str, Any]:
    """Load YAML configuration file."""
    path = Path(config_path)
    if not path.is_file():
        # Fallback search from project root or parent
        possible = [
            Path("skin-cancer-detection") / config_path,
            Path("..") / config_path,
        ]
        for p in possible:
            if p.is_file():
                path = p
                break
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config


def print_env_info() -> Dict[str, Any]:
    """Inspect and return system and compute information."""
    env = detect_environment()
    info = {
        "environment": env,
        "python_version": sys.version.split()[0],
        "torch_version": torch.__version__,
        "cuda_available": torch.cuda.is_available(),
        "device_count": torch.cuda.device_count() if torch.cuda.is_available() else 0,
        "device_name": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU",
        "total_memory_gb": round(torch.cuda.get_device_properties(0).total_memory / (1024**3), 2)
        if torch.cuda.is_available()
        else 0.0,
    }
    return info
