export interface ClassPrediction {
  class: string;
  label: string;
  probability: number;
  percentage: number;
}

export interface PredictionResponse {
  predicted_class: string;
  predicted_label: string;
  confidence: number;
  confidence_percentage: number;
  top_predictions: ClassPrediction[];
  all_probabilities: Record<string, number>;
  model: string;
  device: string;
  disclaimer: string;
}

export interface ExplainResponse {
  prediction: PredictionResponse;
  overlay_base64: string;
  target_class: string;
  disclaimer: string;
}

export interface ModelInfo {
  model_name: string;
  classes: string[];
  image_size: number;
  mean: number[];
  std: number[];
  device: string;
  best_macro_f1?: number;
  parameters_total?: number;
  parameters_trainable?: number;
}

export interface HealthStatus {
  status: string;
  model_loaded: boolean;
  model_name: string;
  device: string;
  environment: string;
}
