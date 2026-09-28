import React, { useEffect, useState } from 'react';
import { Header } from './components/Header';
import { MedicalDisclaimer } from './components/MedicalDisclaimer';
import { ImageUploader } from './components/ImageUploader';
import { PredictionCard } from './components/PredictionCard';
import { ProbabilityChart } from './components/ProbabilityChart';
import { GradCamViewer } from './components/GradCamViewer';
import { ModelInfoModal } from './components/ModelInfoModal';
import { checkHealth, explainImage, getModelInfo } from './services/api';
import type { ExplainResponse, HealthStatus, ModelInfo } from './types';
import { Sparkles, RefreshCw, AlertCircle } from 'lucide-react';
import './index.css';

export const App: React.FC = () => {
  const [health, setHealth] = useState<HealthStatus | null>(null);
  const [modelInfo, setModelInfo] = useState<ModelInfo | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);

  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<ExplainResponse | null>(null);

  useEffect(() => {
    // Initial health check
    checkHealth()
      .then((h) => setHealth(h))
      .catch((err) => console.warn('Backend not responding yet:', err));

    getModelInfo()
      .then((m) => setModelInfo(m))
      .catch((err) => console.warn('Could not load model info:', err));

    const timer = setInterval(() => {
      checkHealth().then(setHealth).catch(() => setHealth(null));
    }, 10000);
    return () => clearInterval(timer);
  }, []);

  const handleImageSelected = (file: File) => {
    setSelectedFile(file);
    setPreviewUrl(URL.createObjectURL(file));
    setResult(null);
    setError(null);
  };

  const handleClear = () => {
    setSelectedFile(null);
    if (previewUrl) URL.revokeObjectURL(previewUrl);
    setPreviewUrl(null);
    setResult(null);
    setError(null);
  };

  const handleAnalyze = async () => {
    if (!selectedFile) return;
    setIsLoading(true);
    setError(null);

    try {
      const resp = await explainImage(selectedFile);
      setResult(resp);
    } catch (err: any) {
      setError(err.message || 'An error occurred during diagnosis analysis.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-layout">
      <Header health={health} onOpenModelInfo={() => setIsModalOpen(true)} />

      <main className="main-content">
        <MedicalDisclaimer />

        <div className="content-grid">
          {/* Left Column: Input & Controls */}
          <div className="left-column">
            <ImageUploader
              onImageSelected={handleImageSelected}
              selectedFile={selectedFile}
              onClear={handleClear}
              isLoading={isLoading}
            />

            {selectedFile && (
              <div className="action-card card">
                <button
                  onClick={handleAnalyze}
                  disabled={isLoading}
                  className="btn-primary btn-large"
                >
                  {isLoading ? (
                    <>
                      <RefreshCw className="animate-spin" size={20} />
                      <span>Computing Prediction & Grad-CAM...</span>
                    </>
                  ) : (
                    <>
                      <Sparkles size={20} />
                      <span>Analyze Skin Lesion</span>
                    </>
                  )}
                </button>
              </div>
            )}

            {error && (
              <div className="alert-error-box">
                <AlertCircle size={20} />
                <div>
                  <strong>Analysis Error</strong>
                  <p>{error}</p>
                </div>
              </div>
            )}
          </div>

          {/* Right Column: Prediction, Explainability, Charts */}
          <div className="right-column">
            {!result && !isLoading && (
              <div className="placeholder-card card">
                <div className="placeholder-content">
                  <div className="placeholder-pulse"></div>
                  <h3>Ready for Analysis</h3>
                  <p>Upload a dermoscopic skin image on the left and click "Analyze Skin Lesion".</p>
                </div>
              </div>
            )}

            {isLoading && (
              <div className="loading-card card">
                <div className="spinner"></div>
                <h3>Analyzing Morphological Patterns...</h3>
                <p>Generating Softmax confidence distribution and computing Grad-CAM layer activations.</p>
              </div>
            )}

            {result && (
              <div className="results-container">
                <PredictionCard prediction={result.prediction} />
                <GradCamViewer
                  originalImageUrl={previewUrl}
                  overlayBase64={result.overlay_base64}
                  targetClass={result.target_class}
                />
                <ProbabilityChart
                  probabilities={result.prediction.all_probabilities}
                  predictedClass={result.prediction.predicted_class}
                />
              </div>
            )}
          </div>
        </div>
      </main>

      <ModelInfoModal
        info={modelInfo}
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
      />

      <footer className="footer">
        <p>HAM10000 Skin Cancer Diagnostic Support &bull; Deep Learning Transfer Pipeline &bull; Research Prototype</p>
      </footer>
    </div>
  );
};

export default App;
