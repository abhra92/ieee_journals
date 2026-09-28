from pathlib import Path
from typing import Dict, Tuple, Union

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold

from ml.src.preprocessing import clean_metadata


def create_lesion_aware_splits(
    metadata_df: pd.DataFrame,
    seed: int = 42,
    test_size: float = 0.2,
    val_size: float = 0.1,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Perform lesion-aware stratified splitting using StratifiedGroupKFold grouped on lesion_id.
    Prevents data leakage: ensures images of the same lesion never appear across different splits.

    Target split sizes:
    - Train: ~70%
    - Validation: ~10%
    - Test: ~20%
    """
    df = clean_metadata(metadata_df)

    # Use 10 folds: 2 folds for test (20%), 1 fold for val (10%), 7 folds for train (70%)
    sgkf = StratifiedGroupKFold(n_splits=10, shuffle=True, random_state=seed)

    X = df.index.values
    y = df["label"].values
    groups = df["lesion_id"].values

    folds = np.zeros(len(df), dtype=int)
    for fold_idx, (_, test_indices) in enumerate(sgkf.split(X, y, groups)):
        folds[test_indices] = fold_idx

    df["fold"] = folds

    # Fold 0 and 1 -> Test (~20%)
    # Fold 2 -> Validation (~10%)
    # Folds 3..9 -> Train (~70%)
    test_df = df[df["fold"].isin([0, 1])].copy().reset_index(drop=True)
    val_df = df[df["fold"].isin([2])].copy().reset_index(drop=True)
    train_df = df[df["fold"].isin(range(3, 10))].copy().reset_index(drop=True)

    # Run strict verification
    verify_splits(train_df, val_df, test_df)

    return train_df, val_df, test_df


def verify_splits(
    train_df: pd.DataFrame, val_df: pd.DataFrame, test_df: pd.DataFrame
) -> Dict[str, int]:
    """
    Verify strict zero-leakage invariant between Train, Validation, and Test splits.
    Raises AssertionError if any lesion or image overlaps across splits.
    """
    train_lesions = set(train_df["lesion_id"].unique())
    val_lesions = set(val_df["lesion_id"].unique())
    test_lesions = set(test_df["lesion_id"].unique())

    train_images = set(train_df["image_id"].unique())
    val_images = set(val_df["image_id"].unique())
    test_images = set(test_df["image_id"].unique())

    # Check intersections
    tv_overlap = train_lesions.intersection(val_lesions)
    tt_overlap = train_lesions.intersection(test_lesions)
    vt_overlap = val_lesions.intersection(test_lesions)

    img_tv = train_images.intersection(val_images)
    img_tt = train_images.intersection(test_images)
    img_vt = val_images.intersection(test_images)

    if tv_overlap or tt_overlap or vt_overlap:
        raise AssertionError(
            f"Lesion leakage detected!\n"
            f"Train ∩ Val lesions: {len(tv_overlap)}\n"
            f"Train ∩ Test lesions: {len(tt_overlap)}\n"
            f"Val ∩ Test lesions: {len(vt_overlap)}"
        )

    if img_tv or img_tt or img_vt:
        raise AssertionError(
            f"Image ID leakage detected!\n"
            f"Train ∩ Val images: {len(img_tv)}\n"
            f"Train ∩ Test images: {len(img_tt)}\n"
            f"Val ∩ Test images: {len(img_vt)}"
        )

    stats = {
        "train_images": len(train_df),
        "val_images": len(val_df),
        "test_images": len(test_df),
        "train_lesions": len(train_lesions),
        "val_lesions": len(val_lesions),
        "test_lesions": len(test_lesions),
        "total_images": len(train_df) + len(val_df) + len(test_df),
        "total_lesions": len(train_lesions) + len(val_lesions) + len(test_lesions),
    }
    return stats


def save_splits(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    test_df: pd.DataFrame,
    output_dir: Union[str, Path] = "ml/data/splits",
) -> None:
    """Save the verified train, validation, and test split DataFrames to CSV."""
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    train_df.to_csv(out_path / "train.csv", index=False)
    val_df.to_csv(out_path / "validation.csv", index=False)
    test_df.to_csv(out_path / "test.csv", index=False)
