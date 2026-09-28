import React from 'react';
import { Layers } from 'lucide-react';

interface GradCamViewerProps {
  originalImageUrl: string | null;
  overlayBase64: string | null;
  targetClass: string | null;
}

export const GradCamViewer: React.FC<GradCamViewerProps> = ({
  originalImageUrl,
  overlayBase64,
  targetClass,
}) => {
  if (!overlayBase64) return null;

  return (
    <div className="card gradcam-card">
      <div className="gradcam-header">
        <div>
          <div className="flex-row">
            <Layers className="text-primary" size={20} />
            <h3 className="card-title">Grad-CAM Visual Explainability</h3>
          </div>
          <p className="card-subtitle">
            Class activation mapping highlights morphological regions responsible for the{' '}
            <strong>{targetClass?.toUpperCase()}</strong> diagnosis
          </p>
        </div>
      </div>

      <div className="gradcam-grid">
        <div className="gradcam-pane">
          <span className="pane-label">Original Dermoscopy Image</span>
          <div className="pane-img-box">
            {originalImageUrl && <img src={originalImageUrl} alt="Original" className="pane-img" />}
          </div>
        </div>

        <div className="gradcam-pane">
          <span className="pane-label">Clinical Heatmap Overlay</span>
          <div className="pane-img-box">
            <img src={overlayBase64} alt="Grad-CAM Overlay" className="pane-img" />
          </div>
        </div>
      </div>

      <div className="gradcam-legend">
        <span className="legend-text">Heatmap Activation Gradient:</span>
        <div className="legend-bar"></div>
        <div className="legend-labels">
          <span>Low Activation (Background / Normal Skin)</span>
          <span>High Morphological Significance</span>
        </div>
      </div>
    </div>
  );
};
