import React from 'react';

interface ProbabilityChartProps {
  probabilities: Record<string, number>;
  predictedClass: string;
}

const CLASS_DESCRIPTIONS: Record<string, { name: string; isMalignant: boolean }> = {
  akiec: { name: 'Actinic keratoses / Intraepithelial (akiec)', isMalignant: true },
  bcc: { name: 'Basal cell carcinoma (bcc)', isMalignant: true },
  bkl: { name: 'Benign keratosis-like (bkl)', isMalignant: false },
  df: { name: 'Dermatofibroma (df)', isMalignant: false },
  mel: { name: 'Melanoma (mel)', isMalignant: true },
  nv: { name: 'Melanocytic nevi (nv)', isMalignant: false },
  vasc: { name: 'Vascular lesions (vasc)', isMalignant: false },
};

export const ProbabilityChart: React.FC<ProbabilityChartProps> = ({ probabilities, predictedClass }) => {
  const classes = Object.keys(CLASS_DESCRIPTIONS);

  return (
    <div className="card chart-card">
      <h3 className="card-title">Full Diagnostic Probability Spectrum</h3>
      <p className="card-subtitle">One-vs-all Softmax probability across the 7 HAM10000 classes</p>

      <div className="chart-list">
        {classes.map((cls) => {
          const prob = probabilities[cls] || 0;
          const pct = (prob * 100).toFixed(2);
          const meta = CLASS_DESCRIPTIONS[cls];
          const isSelected = cls === predictedClass;

          return (
            <div key={cls} className={`chart-row ${isSelected ? 'chart-row-selected' : ''}`}>
              <div className="chart-label-col">
                <span className="chart-label-code">{cls.toUpperCase()}</span>
                <span className="chart-label-desc">{meta.name}</span>
              </div>
              <div className="chart-bar-container">
                <div
                  className={`chart-bar-fill ${meta.isMalignant ? 'fill-malignant' : 'fill-benign'}`}
                  style={{ width: `${Math.max(parseFloat(pct), 2)}%` }}
                ></div>
              </div>
              <div className="chart-value-col">
                <span className="chart-value-text">{pct}%</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
