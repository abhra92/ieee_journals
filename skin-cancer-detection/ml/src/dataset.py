from pathlib import Path
from typing import Callable, Dict, Optional, Tuple, Union

import pandas as pd
import torch
from PIL import Image
from torch.utils.data import DataLoader, Dataset


class HAM10000Dataset(Dataset):
    """
    PyTorch Dataset for HAM10000 dermoscopy images.
    Expects a DataFrame with 'file_path' and 'label' columns.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        transform: Optional[Callable] = None,
        is_test: bool = False,
    ):
        self.df = df.reset_index(drop=True)
        self.transform = transform
        self.is_test = is_test

        if "file_path" not in self.df.columns:
            raise KeyError("DataFrame must contain 'file_path' column.")
        if not is_test and "label" not in self.df.columns:
            raise KeyError("DataFrame must contain 'label' column for training/validation.")

    def __len__(self) -> int:
        return len(self.df)

    def __getitem__(self, idx: int) -> Dict[str, Union[torch.Tensor, int, str]]:
        row = self.df.iloc[idx]
        image_path = row["file_path"]

        try:
            image = Image.open(image_path).convert("RGB")
        except Exception as e:
            raise RuntimeError(f"Error loading image at path '{image_path}': {e}")

        if self.transform is not None:
            image_tensor = self.transform(image)
        else:
            from torchvision.transforms.functional import to_tensor
            image_tensor = to_tensor(image)

        item = {
            "image": image_tensor,
            "image_id": str(row.get("image_id", Path(image_path).stem)),
            "lesion_id": str(row.get("lesion_id", "")),
        }

        if "label" in row and pd.notna(row["label"]):
            item["label"] = torch.tensor(int(row["label"]), dtype=torch.long)

        if "dx" in row and pd.notna(row["dx"]):
            item["dx"] = str(row["dx"])

        return item


def create_dataloader(
    df: pd.DataFrame,
    transform: Optional[Callable],
    batch_size: int = 16,
    shuffle: bool = True,
    num_workers: int = 2,
    pin_memory: bool = True,
    drop_last: bool = False,
) -> DataLoader:
    """Convenience helper to create a PyTorch DataLoader."""
    dataset = HAM10000Dataset(df=df, transform=transform)
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        pin_memory=pin_memory and torch.cuda.is_available(),
        drop_last=drop_last,
    )
