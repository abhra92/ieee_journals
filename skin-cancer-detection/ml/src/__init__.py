"""
Core ML source package for HAM10000 Skin Cancer Detection.
Serves as the Single Source of Truth across Colab, Local, Notebook, and FastAPI.
"""

from ml.src.preprocessing import (
    CLASSES,
    CLASS_TO_IDX,
    IDX_TO_CLASS,
    CLASS_DESCRIPTIONS,
    IMAGENET_MEAN,
    IMAGENET_STD,
    clean_metadata,
    resolve_image_paths,
)
from ml.src.dataset import HAM10000Dataset, create_dataloader
from ml.src.augmentation import get_train_transforms, get_val_transforms, get_inference_transforms
from ml.src.models import create_model, count_parameters
from ml.src.losses import compute_class_weights, FocalLoss, get_loss_fn
from ml.src.metrics import calculate_metrics, plot_confusion_matrix, plot_roc_curves
from ml.src.inference import SkinCancerClassifier
from ml.src.explainability import GradCAM, generate_gradcam_explanation
from ml.src.utils import set_seed, detect_environment, get_device, load_config
