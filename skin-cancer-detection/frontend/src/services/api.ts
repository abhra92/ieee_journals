import type { ExplainResponse, HealthStatus, ModelInfo, PredictionResponse } from '../types';

const API_BASE = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

export async function checkHealth(): Promise<HealthStatus> {
  const res = await fetch(`${API_BASE}/health`);
  if (!res.ok) throw new Error(`Health check failed: ${res.statusText}`);
  return res.json();
}

export async function getModelInfo(): Promise<ModelInfo> {
  const res = await fetch(`${API_BASE}/model-info`);
  if (!res.ok) throw new Error(`Failed to load model info: ${res.statusText}`);
  return res.json();
}

export async function predictImage(file: File, k: number = 3): Promise<PredictionResponse> {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('k', k.toString());

  const res = await fetch(`${API_BASE}/predict/top-k`, {
    method: 'POST',
    body: formData,
  });

  if (!res.ok) {
    const errorData = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(errorData.detail || 'Prediction failed');
  }

  return res.json();
}

export async function explainImage(file: File): Promise<ExplainResponse> {
  const formData = new FormData();
  formData.append('file', file);

  const res = await fetch(`${API_BASE}/explain`, {
    method: 'POST',
    body: formData,
  });

  if (!res.ok) {
    const errorData = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(errorData.detail || 'Explainability computation failed');
  }

  return res.json();
}
