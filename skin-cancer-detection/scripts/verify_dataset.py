import json
import os
import sys
from pathlib import Path
from typing import List, Tuple

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from PIL import Image
from tqdm import tqdm

from ml.src.preprocessing import (
    CLASS_DESCRIPTIONS,
    CLASSES,
    clean_metadata,
    resolve_image_paths,
)


def find_dataset_paths() -> Tuple[Path, List[Path]]:
    """Locate HAM10000 metadata CSV and image directories across candidate locations."""
    candidate_metadata = [
        Path("archive/HAM10000_metadata.csv"),
        Path("../archive/HAM10000_metadata.csv"),
        Path("ml/data/raw/HAM10000_metadata.csv"),
        Path("HAM10000_metadata.csv"),
    ]

    metadata_file: Path | None = None
    for p in candidate_metadata:
        if p.is_file():
            metadata_file = p.resolve()
            break

    if metadata_file is None:
        raise FileNotFoundError("Could not find HAM10000_metadata.csv in candidate locations.")

    # Image directories
    archive_dir = metadata_file.parent
    candidate_image_dirs = [
        archive_dir / "HAM10000_images_part_1",
        archive_dir / "HAM10000_images_part_2",
        archive_dir / "images",
        Path("ml/data/raw/HAM10000_images_part_1"),
        Path("ml/data/raw/HAM10000_images_part_2"),
    ]

    image_dirs = [d.resolve() for d in candidate_image_dirs if d.is_dir()]
    if not image_dirs:
        raise FileNotFoundError(f"Could not find HAM10000 image folders under {archive_dir}.")

    return metadata_file, image_dirs


def verify_dataset(check_all_images: bool = True):
    print("=" * 60)
    print("HAM10000 DATASET AUDIT & INTEGRITY VERIFICATION")
    print("=" * 60)

    metadata_path, image_dirs = find_dataset_paths()
    print(f"Metadata File: {metadata_path}")
    print(f"Image Dirs:    {[str(d) for d in image_dirs]}")

    df_raw = pd.read_csv(metadata_path)
    print(f"Raw CSV Rows:  {len(df_raw)}")
    print(f"Raw Columns:   {df_raw.columns.tolist()}")

    # Clean whitespace
    df = clean_metadata(df_raw)
    print(f"Clean Columns: {df.columns.tolist()}")

    # Resolve paths
    df = resolve_image_paths(df, image_dirs)
    print(f"Resolved paths for all {len(df)} images successfully.")

    # Check for corruption if requested
    corrupted_count = 0
    if check_all_images:
        print("Checking image file integrity...")
        for p in tqdm(df["file_path"], desc="Verifying images"):
            try:
                with Image.open(p) as img:
                    img.verify()
            except Exception as e:
                print(f"[CORRUPTED IMAGE] {p}: {e}")
                corrupted_count += 1
        print(f"Image integrity check completed. Corrupted count: {corrupted_count}")

    # Compute statistics
    unique_lesions = int(df["lesion_id"].nunique())
    unique_images = int(df["image_id"].nunique())
    class_counts = df["dx"].value_counts().to_dict()

    print("\nClass Distribution:")
    for cls in CLASSES:
        count = class_counts.get(cls, 0)
        pct = (count / len(df)) * 100
        print(f"  {cls:6s}: {count:5d} ({pct:5.2f}%) - {CLASS_DESCRIPTIONS.get(cls, '')}")

    print(f"\nUnique Lesions: {unique_lesions}")
    print(f"Unique Images:  {unique_images}")

    # Age and Sex distributions
    age_desc = df["age"].describe().to_dict()
    sex_dist = df["sex"].value_counts().to_dict()
    loc_dist = df["localization"].value_counts().to_dict()

    # Save report
    reports_dir = Path("ml/reports")
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_data = {
        "metadata_path": str(metadata_path),
        "total_images": len(df),
        "unique_lesions": unique_lesions,
        "unique_images": unique_images,
        "corrupted_images": corrupted_count,
        "class_distribution": class_counts,
        "sex_distribution": sex_dist,
        "localization_distribution": loc_dist,
        "age_summary": age_desc,
    }

    with open(reports_dir / "dataset_report.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)

    # Plot class distribution chart
    plt.figure(figsize=(9, 5))
    palette = sns.color_palette("viridis", len(CLASSES))
    bars = plt.bar(CLASSES, [class_counts.get(c, 0) for c in CLASSES], color=palette)
    plt.title("HAM10000 Class Distribution", fontsize=14, fontweight="bold", pad=12)
    plt.xlabel("Diagnostic Category (dx)", fontsize=12)
    plt.ylabel("Image Count", fontsize=12)
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 50,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=10,
        )
    plt.ylim(0, max(class_counts.values()) + 600)
    plt.tight_layout()
    plt.savefig(reports_dir / "class_distribution.png", dpi=300)
    plt.close()

    print(f"\nSaved dataset report to: {reports_dir / 'dataset_report.json'}")
    print(f"Saved class distribution plot to: {reports_dir / 'class_distribution.png'}")
    print("=" * 60)
    return report_data


if __name__ == "__main__":
    verify_dataset(check_all_images=True)
