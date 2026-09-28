import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import pandas as pd

# The 7 canonical HAM10000 classes sorted alphabetically
CLASSES: List[str] = ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]

CLASS_TO_IDX: Dict[str, int] = {cls_name: idx for idx, cls_name in enumerate(CLASSES)}
IDX_TO_CLASS: Dict[int, str] = {idx: cls_name for idx, cls_name in enumerate(CLASSES)}

CLASS_DESCRIPTIONS: Dict[str, str] = {
    "akiec": "Actinic keratoses and intraepithelial carcinoma (Precancerous/Malignant)",
    "bcc": "Basal cell carcinoma (Malignant)",
    "bkl": "Benign keratosis-like lesions (Benign)",
    "df": "Dermatofibroma (Benign)",
    "mel": "Melanoma (Malignant)",
    "nv": "Melanocytic nevi (Benign)",
    "vasc": "Vascular lesions (Benign)",
}

# ImageNet normalization parameters
IMAGENET_MEAN: List[float] = [0.485, 0.456, 0.406]
IMAGENET_STD: List[float] = [0.229, 0.224, 0.225]


def clean_metadata(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean metadata DataFrame by stripping leading/trailing whitespace from column names
    and string columns. Handles raw HAM10000 CSV whitespace artifacts.
    """
    df = df.copy()
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Strip whitespace from string values
    for col in df.columns:
        if df[col].dtype == object or isinstance(df[col].dtype, pd.StringDtype):
            df[col] = df[col].astype(str).str.strip()

    # Drop potential 'Unnamed' or empty columns
    df = df.loc[:, ~df.columns.str.contains(r"^Unnamed")]

    # Validate mandatory columns
    required_cols = {"lesion_id", "image_id", "dx"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Metadata is missing required columns: {missing}")

    # Add numeric label column if 'dx' is present
    if "dx" in df.columns:
        df["label"] = df["dx"].map(CLASS_TO_IDX)

    return df


def build_image_path_index(image_dirs: List[Union[str, Path]]) -> Dict[str, str]:
    """
    Scan image directories and map image_id (without extension) to its absolute file path.
    Supports Part 1, Part 2, or single merged image folders.
    """
    path_map: Dict[str, str] = {}
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp"}

    for d in image_dirs:
        dir_path = Path(d)
        if not dir_path.is_dir():
            continue
        for entry in os.scandir(dir_path):
            if entry.is_file():
                p = Path(entry.path)
                if p.suffix.lower() in valid_extensions:
                    image_id = p.stem.strip()
                    path_map[image_id] = str(p.resolve())

    return path_map


def resolve_image_paths(
    metadata_df: pd.DataFrame, image_dirs: List[Union[str, Path]]
) -> pd.DataFrame:
    """
    Add a verified 'file_path' column to the metadata DataFrame.
    Raises FileNotFoundError if any image_id cannot be found in image_dirs.
    """
    df = clean_metadata(metadata_df)
    path_map = build_image_path_index(image_dirs)

    df["file_path"] = df["image_id"].map(path_map)

    missing = df[df["file_path"].isna()]
    if not missing.empty:
        sample_missing = missing["image_id"].head(5).tolist()
        raise FileNotFoundError(
            f"Failed to find {len(missing)} image files. Samples: {sample_missing}. "
            f"Searched directories: {[str(d) for d in image_dirs]}"
        )

    return df
