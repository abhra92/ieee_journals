import React from 'react';
import { Activity, Cpu } from 'lucide-react';
import type { HealthStatus } from '../types';

interface HeaderProps {
  health: HealthStatus | null;
  onOpenModelInfo: () => void;
}

export const Header: React.FC<HeaderProps> = ({ health, onOpenModelInfo }) => {
  return (
    <header className="header">
      <div className="header-container">
        <div className="header-brand">
          <div className="header-icon-box">
            <Activity className="header-icon" />
          </div>
          <div>
            <div className="header-title-row">
              <h1 className="header-title">DermAI Skin Lesion Classifier</h1>
              <span className="badge badge-research">Research Prototype</span>
            </div>
            <p className="header-subtitle">
              HAM10000 7-Class Deep Learning Diagnostic Support & Grad-CAM Visual Explainability
            </p>
          </div>
        </div>

        <div className="header-actions">
          <div className={`status-pill ${health?.status === 'healthy' ? 'status-online' : 'status-offline'}`}>
            <span className="status-dot"></span>
            <span>{health?.status === 'healthy' ? `API Online (${health.device.toUpperCase()})` : 'Connecting...'}</span>
          </div>

          <button onClick={onOpenModelInfo} className="btn-secondary">
            <Cpu size={16} />
            <span>Model Details</span>
          </button>
        </div>
      </div>
    </header>
  );
};
