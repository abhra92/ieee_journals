from typing import List, Tuple
from torchvision import transforms

from ml.src.preprocessing import IMAGENET_MEAN, IMAGENET_STD


def get_train_transforms(image_size: int = 224) -> transforms.Compose:
    """
    Data augmentation transforms for training:
    - Resize & slight random cropping
    - Horizontal and vertical flips (dermoscopy images are invariant to orientation)
    - Gentle rotation & affine transform
    - Color jitter for illumination variations
    - ImageNet normalization
    """
    return transforms.Compose(
        [
            transforms.Resize((image_size, image_size)),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomVerticalFlip(p=0.5),
            transforms.RandomRotation(degrees=20),
            transforms.ColorJitter(brightness=0.15, contrast=0.15, saturation=0.15, hue=0.05),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
        ]
    )


def get_val_transforms(image_size: int = 224) -> transforms.Compose:
    """
    Standard validation transforms: deterministic resizing and normalization.
    """
    return transforms.Compose(
        [
            transforms.Resize((image_size, image_size)),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
        ]
    )


def get_inference_transforms(image_size: int = 224) -> transforms.Compose:
    """
    Inference transforms identical to validation transforms.
    """
    return get_val_transforms(image_size=image_size)
