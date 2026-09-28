import argparse
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from PIL import Image

from ml.src.explainability import generate_gradcam_explanation
from ml.src.inference import SkinCancerClassifier


def main():
    parser = argparse.ArgumentParser(description="Run skin cancer inference & Grad-CAM demo")
    parser.add_argument("--image-path", type=str, default=None)
    parser.add_argument("--model-path", type=str, default="models/best_model.pth")
    parser.add_argument("--output-dir", type=str, default="outputs/explanations")
    args = parser.parse_args()

    image_path = args.image_path
    if image_path is None:
        # Pick first test image from test split if available
        test_csv = Path("ml/data/splits/test.csv")
        if test_csv.is_file():
            df = pd.read_csv(test_csv)
            image_path = df.iloc[0]["file_path"]
        else:
            # Pick an image from archive
            from scripts.verify_dataset import find_dataset_paths

            _, image_dirs = find_dataset_paths()
            for img_dir in image_dirs:
                imgs = list(img_dir.glob("*.jpg"))
                if imgs:
                    image_path = str(imgs[0])
                    break

    if not image_path or not Path(image_path).is_file():
        raise FileNotFoundError(f"Could not find valid image: {image_path}")

    print("=" * 60)
    print("DEMO: INFERENCE & GRAD-CAM EXPLAINABILITY")
    print("=" * 60)
    print(f"Input Image: {image_path}")

    # Load classifier
    classifier = SkinCancerClassifier(model_path=args.model_path)
    result = classifier.predict_image(image_path, top_k=3)

    print("\nPrediction Results:")
    print(f"  Predicted Class: {result['predicted_class'].upper()}")
    print(f"  Diagnosis:       {result['predicted_label']}")
    print(f"  Confidence:      {result['confidence_percentage']}%")
    print("\nTop-3 Differential:")
    for idx, p in enumerate(result["top_predictions"]):
        print(f"  {idx + 1}. {p['class'].upper()} ({p['percentage']}%): {p['label']}")

    # Grad-CAM
    print("\nGenerating Grad-CAM visualization...")
    img = Image.open(image_path).convert("RGB")
    explanation = generate_gradcam_explanation(
        classifier.model, img, image_size=classifier.image_size, device=classifier.device
    )

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    save_file = out_dir / "demo_gradcam.png"
    explanation["overlay_image"].save(save_file)
    print(f"Saved Grad-CAM overlay to: {save_file.resolve()}")
    print("=" * 60)


if __name__ == "__main__":
    main()
