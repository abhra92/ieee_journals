import React from 'react';
import { AlertTriangle } from 'lucide-react';

export const MedicalDisclaimer: React.FC = () => {
  return (
    <aside aria-label="Medical safety notice" className="disclaimer-banner">
      <div className="disclaimer-icon-col">
        <AlertTriangle className="disclaimer-icon" />
      </div>
      <div className="disclaimer-content">
        <h2 className="disclaimer-title">MANDATORY CLINICAL SAFETY NOTICE</h2>
        <p className="disclaimer-text">
          This system is an investigational deep learning research tool developed on the HAM10000 dataset and is{' '}
          <strong>NOT a substitute for professional clinical medical diagnosis</strong>. Model confidence represents
          statistical probability, not clinical certainty. Any suspicious skin lesion requires prompt physical evaluation
          and dermoscopic examination by a qualified dermatologist or medical practitioner.
        </p>
      </div>
    </aside>
  );
};
