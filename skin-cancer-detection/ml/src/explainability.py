import base64
import io
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

import cv2
import numpy as np
import torch
import torch.nn as nn
from PIL import Image

from ml.src.augmentation import get_inference_transforms
from ml.src.preprocessing import CLASS_DESCRIPTIONS, CLASSES, IDX_TO_CLASS


class GradCAM:
    """
    Gradient-weighted Class Activation Mapping (Grad-CAM) for CNN models.
    Produces visual explanations of decisions by highlighting regions relevant to prediction.
    """

    def __init__(self, model: nn.Module, target_layer: Optional[nn.Module] = None):
        self.model = model
        self.model.eval()

        # Find target layer automatically if not specified
        if target_layer is None:
            self.target_layer = self._find_target_layer()
        else:
            self.target_layer = target_layer

        self.gradients: Optional[torch.Tensor] = None
        self.activations: Optional[torch.Tensor] = None

        # Register forward and backward hooks
        self.fwd_hook = self.target_layer.register_forward_hook(self._save_activations)
        self.bwd_hook = self.target_layer.register_full_backward_hook(self._save_gradients)

    def _find_target_layer(self) -> nn.Module:
        """Find the last convolutional layer in the architecture."""
        target = None
        for name, module in self.model.named_modules():
            if isinstance(module, (nn.Conv2d, nn.BatchNorm2d)):
                target = module
        if target is None:
            raise ValueError("Could not find a convolutional layer for Grad-CAM.")
        return target

    def _save_activations(self, module, input, output):
        self.activations = output.detach()

    def _save_gradients(self, module, grad_input, grad_output):
        self.gradients = grad_output[0].detach()

    def generate_heatmap(
        self,
        input_tensor: torch.Tensor,
        target_class_idx: Optional[int] = None,
    ) -> np.ndarray:
        """
        Generate raw Grad-CAM heatmap for the specified class index.
        """
        self.model.zero_grad()
        output = self.model(input_tensor)
        if hasattr(output, "logits"):
            output = output.logits

        if target_class_idx is None:
            target_class_idx = int(torch.argmax(output, dim=1).item())

        score = output[:, target_class_idx]
        score.backward(retain_graph=True)

        gradients = self.gradients  # [B, C, H, W]
        activations = self.activations  # [B, C, H, W]

        # Global average pooling over spatial dimensions
        weights = torch.mean(gradients, dim=(2, 3), keepdim=True)  # [B, C, 1, 1]
        cam = torch.sum(weights * activations, dim=1, keepdim=True)  # [B, 1, H, W]

        cam = torch.relu(cam)
        cam = cam.squeeze().cpu().numpy()

        # Normalize to [0, 1]
        cam_min, cam_max = cam.min(), cam.max()
        if cam_max - cam_min > 1e-7:
            cam = (cam - cam_min) / (cam_max - cam_min)
        else:
            cam = np.zeros_like(cam)

        return cam

    def remove_hooks(self):
        self.fwd_hook.remove()
        self.bwd_hook.remove()


def overlay_cam_on_image(
    image: Image.Image,
    cam_heatmap: np.ndarray,
    alpha: float = 0.5,
    colormap: int = cv2.COLORMAP_JET,
) -> Image.Image:
    """
    Superimpose Grad-CAM heatmap over original PIL image.
    """
    img_np = np.array(image.convert("RGB"))
    h, w, _ = img_np.shape

    # Resize heatmap to match image size
    heatmap_resized = cv2.resize(cam_heatmap, (w, h))
    heatmap_colored = cv2.applyColorMap(np.uint8(255 * heatmap_resized), colormap)
    heatmap_colored = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)

    overlay = np.uint8(alpha * heatmap_colored + (1.0 - alpha) * img_np)
    return Image.fromarray(overlay)


def generate_gradcam_explanation(
    model: nn.Module,
    image: Image.Image,
    image_size: int = 224,
    device: Optional[torch.device] = None,
    target_class_idx: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Full explanation pipeline: takes PIL Image, computes Grad-CAM, and returns
    overlay PIL Image, base64 encoded image, and top prediction metadata.
    """
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model.to(device)
    gradcam = GradCAM(model)

    transform = get_inference_transforms(image_size=image_size)
    tensor = transform(image).unsqueeze(0).to(device)

    try:
        heatmap = gradcam.generate_heatmap(tensor, target_class_idx=target_class_idx)
    finally:
        gradcam.remove_hooks()

    overlay_img = overlay_cam_on_image(image, heatmap, alpha=0.45)

    # Encode overlay to base64 for API / React
    buffered = io.BytesIO()
    overlay_img.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return {
        "overlay_image": overlay_img,
        "overlay_base64": f"data:image/png;base64,{img_b64}",
        "heatmap_raw": heatmap,
    }
