import React, { useRef, useState } from 'react';
import { UploadCloud, X, AlertCircle } from 'lucide-react';

interface ImageUploaderProps {
  onImageSelected: (file: File) => void;
  selectedFile: File | null;
  onClear: () => void;
  isLoading: boolean;
}

export const ImageUploader: React.FC<ImageUploaderProps> = ({
  onImageSelected,
  selectedFile,
  onClear,
  isLoading,
}) => {
  const [isDragOver, setIsDragOver] = useState(false);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (file: File) => {
    setError(null);
    const validExtensions = ['image/jpeg', 'image/png', 'image/bmp', 'image/webp'];
    if (!validExtensions.includes(file.type)) {
      setError('Please select a valid image format (JPEG, PNG, WebP).');
      return;
    }
    if (file.size > 15 * 1024 * 1024) {
      setError('File size must be under 15MB.');
      return;
    }

    const url = URL.createObjectURL(file);
    setPreviewUrl(url);
    onImageSelected(file);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFileChange(e.dataTransfer.files[0]);
    }
  };

  const handleReset = () => {
    if (previewUrl) URL.revokeObjectURL(previewUrl);
    setPreviewUrl(null);
    setError(null);
    if (fileInputRef.current) fileInputRef.current.value = '';
    onClear();
  };

  return (
    <div className="card upload-card">
      <h2 className="card-title">Dermoscopic Image Input</h2>
      <p className="card-subtitle">Upload a macroscopic or dermoscopic skin lesion photograph</p>

      {error && (
        <div className="alert-error">
          <AlertCircle size={16} />
          <span>{error}</span>
        </div>
      )}

      {!previewUrl ? (
        <div
          className={`dropzone ${isDragOver ? 'dropzone-active' : ''}`}
          onDragOver={(e) => {
            e.preventDefault();
            setIsDragOver(true);
          }}
          onDragLeave={() => setIsDragOver(false)}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
        >
          <input
            ref={fileInputRef}
            type="file"
            accept="image/jpeg,image/png,image/webp"
            style={{ display: 'none' }}
            onChange={(e) => e.target.files?.[0] && handleFileChange(e.target.files[0])}
          />
          <div className="dropzone-content">
            <UploadCloud className="dropzone-icon" size={48} />
            <p className="dropzone-text">Drag & drop lesion image here or click to browse</p>
            <p className="dropzone-hint">Supports JPEG, PNG up to 15MB</p>
          </div>
        </div>
      ) : (
        <div className="preview-container">
          <img src={previewUrl} alt="Lesion Preview" className="image-preview" />
          <div className="preview-overlay">
            <span className="preview-name">{selectedFile?.name}</span>
            <button
              onClick={handleReset}
              disabled={isLoading}
              className="btn-icon-danger"
              title="Remove image"
            >
              <X size={18} />
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
