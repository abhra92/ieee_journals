import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

from ml.src.preprocessing import clean_metadata, resolve_image_paths
from ml.src.split import create_lesion_aware_splits, save_splits, verify_splits
from scripts.verify_dataset import find_dataset_paths


def main():
    print("=" * 60)
    print("GENERATING LESION-AWARE STRATIFIED SPLITS (NO LEAKAGE)")
    print("=" * 60)

    metadata_path, image_dirs = find_dataset_paths()
    raw_df = pd.read_csv(metadata_path)

    df = clean_metadata(raw_df)
    df = resolve_image_paths(df, image_dirs)

    print(f"Total verified samples: {len(df)}")
    print(f"Total unique lesions:   {df['lesion_id'].nunique()}")

    train_df, val_df, test_df = create_lesion_aware_splits(
        df, seed=42, test_size=0.2, val_size=0.1
    )

    stats = verify_splits(train_df, val_df, test_df)

    print("\nSplit Statistics:")
    print(f"  Train:      {stats['train_images']:5d} images ({stats['train_lesions']:5d} lesions)")
    print(f"  Validation: {stats['val_images']:5d} images ({stats['val_lesions']:5d} lesions)")
    print(f"  Test:       {stats['test_images']:5d} images ({stats['test_lesions']:5d} lesions)")
    print(f"  Total:      {stats['total_images']:5d} images ({stats['total_lesions']:5d} lesions)")

    # Print class distribution per split
    print("\nClass Distribution Across Splits:")
    class_df = pd.DataFrame(
        {
            "Train": train_df["dx"].value_counts(),
            "Validation": val_df["dx"].value_counts(),
            "Test": test_df["dx"].value_counts(),
        }
    ).fillna(0).astype(int)
    print(class_df)

    output_dir = Path("ml/data/splits")
    save_splits(train_df, val_df, test_df, output_dir=output_dir)
    print(f"\nSuccessfully saved splits to: {output_dir.resolve()}")
    print("Zero-leakage invariant verified: Train intersection Val = 0, Train intersection Test = 0, Val intersection Test = 0.")
    print("=" * 60)


if __name__ == "__main__":
    main()
