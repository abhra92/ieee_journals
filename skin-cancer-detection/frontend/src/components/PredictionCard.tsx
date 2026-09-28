import React from 'react';
import type { PredictionResponse } from '../types';

interface PredictionCardProps {
  prediction: PredictionResponse;
}

export const PredictionCard: React.FC<PredictionCardProps> = ({ prediction }) => {
  const isMalignant = ['mel', 'bcc', 'akiec'].includes(prediction.predicted_class);

  return (
    <div className="card prediction-card">
      <div className="prediction-header">
        <div>
          <span className="section-eyebrow">Top Predicted Diagnosis</span>
          <div className="predicted-label-row">
            <h2 className="predicted-name">{prediction.predicted_label}</h2>
            <span className={`badge ${isMalignant ? 'badge-malignant' : 'badge-benign'}`}>
              {isMalignant ? 'Malignant / Precancerous Risk' : 'Benign / Non-Malignant'}
            </span>
          </div>
        </div>

        <div className="confidence-badge-box">
          <span className="confidence-value">{prediction.confidence_percentage}%</span>
          <span className="confidence-label">Model Confidence</span>
        </div>
      </div>

      <div className="top-k-section">
        <h3 className="sub-title">Differential Diagnosis Ranking (Top-3)</h3>
        <div className="top-k-list">
          {prediction.top_predictions.map((p, idx) => {
            const isMal = ['mel', 'bcc', 'akiec'].includes(p.class);
            return (
              <div key={p.class} className="top-k-item">
                <div className="top-k-info">
                  <span className="top-k-rank">#{idx + 1}</span>
                  <div>
                    <span className="top-k-class">{p.class.toUpperCase()}</span>
                    <span className="top-k-desc">{p.label}</span>
                  </div>
                </div>
                <div className="top-k-metric">
                  <span className={`top-k-pct ${isMal ? 'text-malignant' : 'text-benign'}`}>
                    {p.percentage}%
                  </span>
                  <div className="progress-bar-bg">
                    <div
                      className={`progress-bar-fill ${isMal ? 'fill-malignant' : 'fill-benign'}`}
                      style={{ width: `${Math.max(p.percentage, 4)}%` }}
                    ></div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
