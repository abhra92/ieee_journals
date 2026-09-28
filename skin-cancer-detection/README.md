# Skin Cancer Detection System (HAM10000)

Research-grade, reproducible, deep learning-based skin-lesion classification system using the HAM10000 dataset, featuring a Single Source of Truth (`ml/src/`), Google Colab GPU training, a local FastAPI backend, and a React + Vite frontend with Grad-CAM explainability.

---

## Clinical Categories (HAM10000)
1. **akiec**: Actinic keratoses and intraepithelial carcinoma (Precancerous/Malignant)
2. **bcc**: Basal cell carcinoma (Malignant)
3. **bkl**: Benign keratosis-like lesions (Benign)
4. **df**: Dermatofibroma (Benign)
5. **mel**: Melanoma (Malignant)
6. **nv**: Melanocytic nevi (Benign)
7. **vasc**: Vascular lesions (Benign)

---

## Hardware Strategy
- **Google Colab (GPU)**: Benchmark training, transfer learning, heavy model fine-tuning.
- **Local Development (CPU / Intel Iris Xe)**: Dataset validation, lesion-aware zero-leakage splitting, smoke tests, FastAPI inference, and React interface.

---

## Medical Safety Notice
> **DISCLAIMER**: This system is a research prototype and is NOT a substitute for professional medical diagnosis. Professional clinical evaluation by a certified dermatologist is required for any skin lesion.
