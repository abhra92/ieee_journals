# Research Problem Analysis

## 1. What problem are existing researchers trying to solve?
Researchers are primarily focusing on the automated detection and classification of skin cancer, particularly melanoma, using dermoscopic images. The overarching goal is to develop highly accurate, objective, and efficient deep learning systems to assist dermatologists in early diagnosis, thereby improving patient outcomes. 

## 2. What approaches are commonly used?
- **Datasets:** The HAM10000 dataset is the most widely used (16 papers, e.g., Papers 3, 5, 9, 11), followed by ISIC 2018 (8 papers) and ISIC 2019 (6 papers).
- **Architectures:** Transfer learning with pre-trained models is heavily utilized, including ResNet-50 (Papers 2, 5, 7, 8, 10, 16, 18, 22, 28), VGG-16/19 (Papers 2, 7, 8, 10, 16, 39), DenseNet (Papers 6, 7, 12, 15, 22), and custom CNNs (Papers 1, 3, 5, 20).
- **Preprocessing:** Techniques include hair removal such as Dull Razor (Papers 6, 12, 16, 23, 27, 39), color normalization (Papers 7, 9, 10, 19, 26), and resizing to standardized dimensions like 224x224 (Papers 5, 8, 13, 16, 19, 26, 28, 36).
- **Data Augmentation:** Geometric augmentations (rotation, flip, zoom) are standard (Papers 2, 3, 5, 6, 7, 8, 9, 12, 13, 16, 19, 21, 22, 26, 36). Some methods use GANs for synthetic data generation (Papers 15, 39).

## 3. What limitations repeatedly appear?
- **Class Imbalance:** Many datasets suffer from severe class imbalance which is often inadequately addressed (Papers 3, 5, 7, 9, 10, 11, 13, 33).
- **Lack of Interpretability:** The majority of papers do not incorporate explainable AI techniques, operating as black boxes.
- **Limited Scope:** Many models focus only on binary classification instead of multi-class diagnosis (Papers 1, 2, 4, 8, 16, 17).
- **Computational Overhead:** Complex models often have high computational demands (Papers 6, 8, 10, 11, 13, 15, 19, 25, 26, 29).
- **Clinical Validation:** A persistent lack of multi-center or clinical validation (Papers 1, 2, 3, 5, 7, 9, 12, 15, 18, 19, 21, 37, 39).

## 4. What problems remain unresolved?
- **Inter-class Similarity:** High confusion rates persist between visually similar classes, such as melanoma and benign keratosis (Papers 3, 5).
- **Generalization:** Models trained on specific datasets often struggle to generalize to non-dermoscopic or smartphone images (Papers 9, 12, 16, 33).
- **Edge Deployment:** Lack of optimization for deployment on edge devices (Papers 5, 19, 26, 29).

## 5. What areas require further investigation?
- Systematic comparison of transfer learning architectures on standardized datasets like HAM10000 (suggested by Papers 5, 7, 12).
- Integration of Explainable AI (XAI) to improve clinical trust, as very few studies utilize these tools (Only Paper 3 uses Grad-CAM on HAM10000).
- Insufficient evaluation of preprocessing pipelines and their direct impact on classification (Papers 6, 12, 14).
- Systematic evaluation of data augmentation strategies (Papers 7, 15, 39).

## 6. Which gaps are realistically addressable using HAM10000?
- **Handling Class Imbalance:** Implementing and evaluating targeted augmentation or class weighting strategies on the heavily imbalanced HAM10000 dataset.
- **Multi-class Classification vs Binary:** Developing robust multi-class classification models to differentiate all seven classes in HAM10000, addressing the over-reliance on binary models.
- **Model Comparison:** Conducting a systematic comparison of standard transfer learning architectures (e.g., ResNet, VGG) on HAM10000.
- **Interpretability:** Applying explainability techniques like Grad-CAM to models trained on HAM10000.

---

### Summary of Findings

#### Established Research Areas
- Use of large-scale public datasets like HAM10000 (16 papers) and ISIC archives.
- Application of transfer learning using standard architectures like ResNet-50, VGG, and DenseNet.
- Standard geometric data augmentation and basic preprocessing.

#### Common Limitations
- Inadequate handling of class imbalance (Papers 3, 5, 7, 9, 10, 11, 13, 33).
- Binary classification only (Papers 1, 2, 4, 8, 16, 17).
- Lack of multi-center clinical validation (Papers 1, 2, 3, 5, 7, 9, 12, 15, 18, 19, 21, 37, 39).
- High computational overhead (Papers 6, 8, 10, 11, 13, 15, 19, 25, 26, 29).
- No model interpretability (majority of papers).

#### Recurring Research Gaps
- Severe class imbalance in HAM10000 (melanocytic nevi dominates at ~67%) - identified in Papers 3, 7, 9, 10, 11, 13, 33.
- Limited systematic comparison of transfer learning architectures on HAM10000 - Papers 5, 7, 12 suggest this.
- Insufficient preprocessing pipeline evaluation - Papers 6, 12, 14.
- Most studies lack interpretability/explainability - Only Paper 3 uses Grad-CAM on HAM10000.
- Few studies systematically evaluate data augmentation strategies - Papers 7, 15, 39.
- Binary classification dominates despite multi-class need - Papers 1, 2, 4, 8, 16, 17.
- Confusion between visually similar classes like melanoma and benign keratosis - Papers 3, 5.

#### Potential Research Opportunities
- Developing a systematic comparative study of transfer learning models on HAM10000.
- Integrating XAI techniques (e.g., Grad-CAM) into multi-class pipelines to enhance model transparency.
- Formulating effective data augmentation or class weighting strategies to handle HAM10000's severe class imbalance.
