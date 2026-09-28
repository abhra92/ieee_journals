import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import psutil
import torch

from ml.src.utils import detect_environment


def main():
    print("=" * 60)
    print("HARDWARE & COMPUTE ENVIRONMENT VERIFICATION")
    print("=" * 60)
    env = detect_environment()
    print(f"Environment:        {env.upper()}")
    print(f"Python Version:     {sys.version.split()[0]}")
    print(f"PyTorch Version:    {torch.__version__}")
    print(f"CUDA Available:     {torch.cuda.is_available()}")

    # RAM
    ram = psutil.virtual_memory()
    print(f"System RAM Total:   {ram.total / (1024**3):.2f} GB")
    print(f"System RAM Avail:   {ram.available / (1024**3):.2f} GB")

    if torch.cuda.is_available():
        num_devices = torch.cuda.device_count()
        print(f"CUDA Device Count:  {num_devices}")
        for i in range(num_devices):
            props = torch.cuda.get_device_properties(i)
            print(f"  Device [{i}]:      {props.name}")
            print(f"  VRAM Total:       {props.total_memory / (1024**3):.2f} GB")
            print(f"  Compute Capability:{props.major}.{props.minor}")
    else:
        print("Note: No CUDA GPU detected in current execution context.")
        print("Running in CPU mode. (Heavy training must be dispatched to Google Colab GPU).")
    print("=" * 60)


if __name__ == "__main__":
    main()
