import React from 'react';
import { X, Cpu } from 'lucide-react';
import type { ModelInfo } from '../types';

interface ModelInfoModalProps {
  info: ModelInfo | null;
  isOpen: boolean;
  onClose: () => void;
}

export const ModelInfoModal: React.FC<ModelInfoModalProps> = ({ info, isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <div className="flex-row">
            <Cpu size={20} className="text-primary" />
            <h3 className="modal-title">Model Architecture & Artifact Metadata</h3>
          </div>
          <button onClick={onClose} className="btn-icon">
            <X size={20} />
          </button>
        </div>

        <div className="modal-body">
          <div className="info-grid">
            <div className="info-item">
              <span className="info-label">Architecture</span>
              <span className="info-value">{info?.model_name || 'tf_efficientnetv2_s'}</span>
            </div>
            <div className="info-item">
              <span className="info-label">Input Resolution</span>
              <span className="info-value">{info?.image_size || 224} x {info?.image_size || 224} RGB</span>
            </div>
            <div className="info-item">
              <span className="info-label">Target Classes</span>
              <span className="info-value">{info?.classes?.length || 7} Multi-Class</span>
            </div>
            <div className="info-item">
              <span className="info-label">Inference Device</span>
              <span className="info-value uppercase">{info?.device || 'CPU'}</span>
            </div>
            {info?.parameters_total && (
              <div className="info-item">
                <span className="info-label">Total Parameters</span>
                <span className="info-value">{info.parameters_total.toLocaleString()}</span>
              </div>
            )}
            {info?.best_macro_f1 && (
              <div className="info-item">
                <span className="info-label">Best Macro F1</span>
                <span className="info-value">{info.best_macro_f1.toFixed(4)}</span>
              </div>
            )}
          </div>

          <div className="modal-section">
            <h4 className="modal-subheading">Class Diagnostic Index</h4>
            <div className="classes-tags">
              {info?.classes?.map((c) => (
                <span key={c} className="tag">
                  {c.toUpperCase()}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
