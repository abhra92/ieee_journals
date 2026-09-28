# Comprehensive Catalog of Research Questions in Deep Learning for Skin Lesion Analysis
## Systematic 39-Paper Methodological Extraction & Empirical Benchmark Catalog

> **Course:** Research Methodology (BCA / Computer Science)  
> **Repository:** `downloaded_journals/` (39 Verified Publications)  
> **Output Directory:** `latex_research_questions/`  
> **Standard:** 100% Evidence-Bound, Zero Extrapolation, Standardized 4D Extraction Schema  

---

## Table of Contents
1. [Methodology & Extraction Schema](#1-methodology--extraction-schema)
2. [Cross-Study Taxonomy & RQ Matrix](#2-cross-study-taxonomy--rq-matrix)
3. [Individual Paper Catalog (Papers 1 to 39)](#3-individual-paper-catalog-papers-1-to-39)
4. [Thematic Synthesis Across Literature](#4-thematic-synthesis-across-literature)
5. [Consolidated Open Research Questions Agenda](#5-consolidated-open-research-questions-agenda)

---

## 1. Methodology & Extraction Schema
Every paper is analyzed across four canonical dimensions:
- **RQ1 [Architectural Innovation & Model Design]:** Core structural novelty or loss formulation.
- **RQ2 [Preprocessing, Representation & Artifacts]:** Image enhancement, segmentation, or multimodal alignment.
- **RQ3 [Clinical Diagnostic Performance]:** Quantitative benchmark metrics (Accuracy, Sensitivity, Specificity, AUC).
- **RQ4 [Explainability, Efficiency & Translation]:** Visual interpretability, latency, and point-of-care constraints.

---

## 2. Cross-Study Taxonomy & RQ Matrix

| # | Paper Citation | Thematic Category | Core Investigated Research Question (RQ1) | Peak Metric |
|---|---|---|---|---|
| 1 | **M. A. Albahar et al.** (2019) | Regularized & Lightweight CNNs | Can a lightweight custom Convolutional Neural Network with an embedded novel weight-controlling regularizer pr... | Accuracy: 97.49% |
| 2 | **R. Ashraf et al.** (2020) | ROI Localization & Transfer Learning | Does isolating the lesion Region of Interest (ROI) via an improved k-means clustering segmentation algorithm i... | Accuracy (DermIS): 97.9% |
| 3 | **K. Mridha et al.** (2023) | Explainable AI (XAI) & Mobile Healthcare | What combination of optimization algorithms (Adam vs. RMSprop) and activation functions (ReLU, Swish, Tanh) ma... | Accuracy: 82.0% |
| 4 | **L. Wei et al.** (2020) | Lightweight Networks & Ensemble Learning | Can a lightweight ensemble deep learning framework drastically reduce model parameters while maintaining state... | Accuracy: 87.3% |
| 5 | **H. L. Gururaj et al.** (2023) | Residual Custom Architectures & Multi-Class Screening | Can a tailored custom CNN with residual skip connections ('DeepSkin') match or surpass standard transfer learn... | Accuracy: 88.0% |
| 6 | **A. A. Adegun et al.** (2020) | Integrated Segmentation & Dense Feature Reuse | Does cascading a Fully Convolutional Network (FCN) segmentation model with a DenseNet classification network i... | Segmentation Accuracy: 98.5% |
| 7 | **A. Naeem et al.** (2020) | Systematic Literature Review (Kitchenham SLR) | What type of deep learning based classifiers are used for diagnosing melanoma disease? | Highest Benchmark Accuracy: 93.4% |
| 8 | **A. Imran et al.** (2022) | Ensemble Fusion & Capsule Networks | Can combining heterogeneous deep learning architectures (custom VGG-16, residual ResNet-50, and Capsule Networ... | Accuracy: 93.50% |
| 9 | **Z. Lan et al.** (2022) | Capsule Networks & Attention Routing | Can replacing iterative dynamic routing with a fixed matrix transformation routing mechanism ('FixCaps') elimi... | Accuracy: 96.49% |
| 10 | **Ş. Öztürk et al.** (2022) | Deep Metric Learning & Imbalance Mitigation | How does a Center-Oriented Margin-Free Triplet Loss (COMF-TL) overcome the hyperparameter tuning instability a... | Balanced Accuracy: 83.7% |
| 11 | **A. Kwasigroch et al.** (2020) | Neural Architecture Search (NAS) | Can Neural Architecture Search (NAS) using network morphism automatically discover optimal CNN topologies tail... | Multiclass Accuracy: 82.8% |
| 12 | **A. Magdy et al.** (2023) | Computer Vision Enhancement & Multi-Model Transfer | Does integrating Contrast Limited Adaptive Histogram Equalization (CLAHE) and color constancy improve deep tra... | Accuracy (EfficientNet-B0): 94.6% |
| 13 | **Z. Ji et al.** (2024) | Multi-Scale Attention & Feature Fusion | Can combining Enhanced Feature Fusion with Spatial and Channel Attention Mechanisms ('EFAM-Net') simultaneousl... | Accuracy: 94.28% |
| 14 | **L. Talavera-Martínez et al.** (2021) | Artifact Removal & Deep Inpainting | Can a deep learning-based hair segmentation network outperform classical morphological filtering (DullRazor) i... | Hair Dice Coefficient: 92.8% |
| 15 | **A. Gong et al.** (2020) | Generative Data Augmentation & GANs | Can high-resolution StyleGANs synthesize photorealistic dermoscopic images of minority skin lesions to resolve... | Accuracy: 91.2% |
| 16 | **L. Riaz et al.** (2023) | Joint Multi-Task Learning | Can a comprehensive joint learning framework simultaneously optimize boundary segmentation and malignancy clas... | Classification Accuracy: 95.3% |
| 17 | **L. Ichim et al.** (2020) | Multiple Connected Neural Networks & Texture Fusion | Can an objective diagnostic system based on Multiple Connected Neural Networks (MCNN) effectively fuse hand-cr... | Accuracy (PH2): 96.7% |
| 18 | **R. Mittal et al.** (2024) | Clinical Decision Support & Spiking Neural Networks | Can a systematic Clinical Decision Support Model ('DermCDSM') combining machine learning, deep learning, and S... | Accuracy: 95.7% |
| 19 | **R. Karthik et al.** (2024) | Vision Transformers & Non-Local Attention | Can a hybrid framework combining Swin Transformer backbones with Dense Group Shuffle Non-Local Attention Netwo... | Accuracy: 96.8% |
| 20 | **D. Połap et al.** (2019) | Internet of Medical Things (IoMT) & Edge CAD | Can an Internet of Medical Things (IoMT) framework execute decentralized skin mark screening directly on embed... | Embedded Screening Accuracy: 92.1% |
| 21 | **S. Chatterjee et al.** (2024) | Multi-Scale Transfer Ensembles | Does fusing multi-scale feature representations from Inception-v3 and Xception into a unified ensemble ('Incep... | Accuracy: 95.8% |
| 22 | **A. Gong et al.** (2020) | Architectural Advantage Mining & Group Decision | Can an ensemble strategy explicitly identify and exploit the individual class-specific advantages of distinct ... | Accuracy: 92.8% |
| 23 | **V. S. S. B. T. Sathvika et al.** (2024) | Hybrid Deep Features & Handcrafted Textures | Does extracting bi-sectional textural features across divided lesion halves capture dermatological ABCD asymme... | Accuracy: 94.6% |
| 24 | **M. I. Faizi et al.** (2024) | Lesion Segmentation & Normalized Cross-Correlation | Can Normalized Cross-Correlation (NCC)-based k-means clustering improve the boundary segmentation accuracy of ... | Segmentation Accuracy (PH2): 96.8% |
| 25 | **P. M. M. Pereira et al.** (2022) | 3D Topography & Multiple Instance Learning | Can 3D surface elevation and roughness profiles reconstructed from photometric stereo dermoscopy provide discr... | Accuracy: 91.5% |
| 26 | **X. Qian et al.** (2024) | Pyramid Attention & Higher-Order Pooling | Can a Self-Interactive Attention Pyramid Network ('SPCB-Net') capture cross-scale feature correlations to reso... | Accuracy: 95.6% |
| 27 | **V. S. Narayanan et al.** (2024) | Interpretable Semantic Segmentation & Attention Skips | Can embedding Interpretable Attention gates within Residual Skip Connections ('IARS SegNet') filter out backgr... | Pixel Segmentation Accuracy: 97.1% |
| 28 | **T. Kim et al.** (2023) | Cross-Modal Clinical Fusion & Multi-Fusion Networks | Can a multimodal multi-fusion deep learning framework combining high-resolution visual imagery with quantitati... | Multimodal Accuracy: 94.8% |
| 29 | **Farhatullah et al.** (2024) | Quantum Orthogonal Polynomials & Wavelet Autoencoders | Can Quantum Chebyshev Polynomials (QCP) extracted from wavelet-transformed dermoscopic images capture non-stat... | Accuracy: 96.2% |
| 30 | **Y. Wang et al.** (2026) | Neuro-Symbolic AI & Clinical Knowledge Graphs | Can integrating a structured clinical Knowledge Graph (KG) representing the dermatological Seven-Point Checkli... | Multi-Criteria Diagnostic Accuracy: 89.4% |
| 31 | **M. I. Marie et al.** (2025) | Hybrid Object Detection & Anchor-Free Architectures | Does integrating YOLOv9 (real-time anchor-free detection) with Faster R-CNN (two-stage region proposal) improv... | Detection mAP@0.5: 96.5% |
| 32 | **L. Chakrabarti et al.** (2025) | Vision-Language Models & Automated Report Generation | Can a compact, knowledge-distilled Vision-Language Model (VLM) generate clinically accurate, structured dermat... | Clinical Reporting Accuracy: 93.4% |
| 33 | **G. Wang et al.** (2024) | Multi-Scale CNNs & Dynamic Loss Weighting | Can a Part Cross-Entropy Loss (P-CEL) combined with dynamic loss weighting force deep networks to attend to fi... | Accuracy: 95.1% |
| 34 | **E. Soares Flores et al.** (2025) | Unsupervised Matrix Factorization & Graph Cuts | Can Nonnegative Matrix Factorization (NMF) combined with Mutual Information (MI) segment skin lesions in clini... | Pixel Segmentation Accuracy: 94.6% |
| 35 | **Z. Tabatabaei et al.** (2025) | Siamese Metric Retrieval & Explainable Diagnosis | Can a Siamese Neural Network framework for Content-Based Image Retrieval (CBIR) provide transparent diagnostic... | Top-5 Retrieval Precision: 94.2% |
| 36 | **F. Bibi et al.** (2026) | Focal Modulation & Non-Dermoscopic Screening | Can a dual-stream architecture integrating Focal Modulation and Local Feature Integration ('FoMoSkinNet') accu... | Classification Accuracy: 99.46% |
| 37 | **U. Mittal et al.** (2026) | Multimodal Vision Transformers & Distillation | Can a multimodal Vision Transformer ('MSPE-DeiT') integrating Data-efficient Image Transformers (DeiT) with pa... | Accuracy: 96.7% |
| 38 | **K. Younis et al.** (2026) | Parameter-Efficient Tuning & Visual Question Answering | Can a Mixture-of-LoRA Experts ('MoLE') architecture achieve parameter-efficient adaptation for dermoscopic Vis... | VQA Answer Accuracy: 88.7% |
| 39 | **M. U. Zafar et al.** (2026) | GAN-Based Image Enhancement & Diagnostic Improvement | Can a specialized Generative Adversarial Network ('SLGAN-EID') enhance low-quality skin lesion images by remov... | PSNR: 34.2 dB |

---

## 3. Individual Paper Catalog (Papers 1 to 39)

### Paper 1: Skin Lesion Classification Using Convolutional Neural Network With Novel Regularizer
**Authors:** M. A. Albahar  
**Venue:** *IEEE Access* (2019) | **DOI:** [10.1109/ACCESS.2019.2906241](https://doi.org/10.1109/ACCESS.2019.2906241) | **IEEE Article Number:** `8669763`  
**Category:** `Regularized & Lightweight CNNs`  

> **Problem Formulation:** Fine-grained morphological overlaps between benign and malignant skin lesions cause catastrophic overfitting in traditional unregularized deep CNNs.

#### Formulated Research Questions & Findings:
- **RQ1 [Architectural Innovation]:** *Can a lightweight custom Convolutional Neural Network with an embedded novel weight-controlling regularizer prevent weight explosion and mitigate overfitting in binary skin lesion classification without requiring multi-million parameter backbones?*
  - **Methodology:** Constructed a 2-layer convolutional network embedded with a novel weight regularizer (penalty hyperparameter lambda = 0.02), coupled with max pooling, dropout, a 128-neuron dense layer, and softmax output.
  - **Answer & Findings:** Yes. The novel regularizer successfully stabilized weight trajectories during 100 training epochs, achieving an average validation weighted accuracy of 97.49% and preventing divergence on fine-grained lesion classes.
- **RQ2 [Preprocessing & Data Transformation]:** *How does nonlinear power-law transformation (gamma correction) affect image contrast and convergence speed in automated dermoscopic image classification?*
  - **Methodology:** Applied power-law transformation to standardize 300x300x3 dermoscopic images, balancing illumination differences and highlighting subtle boundary gradations prior to convolution.
  - **Answer & Findings:** Power-law transformation accelerated gradient descent convergence and reduced training loss fluctuations across varying lighting conditions across the ISIC dataset.
- **RQ3 [Clinical Diagnostic Performance]:** *What diagnostic discrimination capability (ROC-AUC) does the regularized model achieve across specific pairwise benign versus malignant lesion types?*
  - **Methodology:** Partitioned 23,906 ISIC archive images into ~8,000 image subsets (70% train, 30% val) across binary clinical pairings.
  - **Answer & Findings:** Achieved ROC-AUC of 0.77 for nevus vs. melanoma, 0.93 for seborrheic keratosis vs. basal cell carcinoma, 0.85 for seborrheic keratosis vs. melanoma, and 0.86 for solar lentigo vs. melanoma.
- **RQ4 [Clinical Translation & Scalability]:** *What are the structural constraints of pairwise binary classification when translating computer-aided diagnostic systems to multi-class clinical triage?*
  - **Methodology:** Analyzed model inference across disparate clinical presentations against practical dermatologist triage needs.
  - **Answer & Findings:** The binary pairwise formulation cannot holistically evaluate complex multi-class differential diagnoses, and the lack of external prospective multi-center testing limits generalizability.

- **Datasets:** ISIC Archive (23,906 images; 8,000 subset, 70/30 split)
- **Quantitative Results:** **Accuracy:** 97.49% | **AUC (Nevus vs Mel):** 0.77 | **AUC (SK vs BCC):** 0.93 | **AUC (SK vs Mel):** 0.85
- **Open Research Questions / Gaps:**
  - *How can the weight regularizer be generalized to unified multi-class differential diagnosis without loss of per-class sensitivity?*
  - *How does the model perform prospectively across diverse patient phototypes in multi-center clinical trials?*

---

### Paper 2: Region-of-Interest Based Transfer Learning Assisted Framework for Skin Cancer Detection
**Authors:** R. Ashraf; S. Afzal; A. U. Rehman; S. Gul; J. Baber; M. Bakhtyar; I. Mehmood; O. -Y. Song; M. Maqsood  
**Venue:** *IEEE Access* (2020) | **DOI:** [10.1109/ACCESS.2020.3014701](https://doi.org/10.1109/ACCESS.2020.3014701) | **IEEE Article Number:** `9160933`  
**Category:** `ROI Localization & Transfer Learning`  

> **Problem Formulation:** Surrounding healthy skin, lighting variations, and hair artifacts introduce confounding background noise when deep networks process full unsegmented dermoscopic images.

#### Formulated Research Questions & Findings:
- **RQ1 [Preprocessing & ROI Segmentation]:** *Does isolating the lesion Region of Interest (ROI) via an improved k-means clustering segmentation algorithm improve transfer learning feature discrimination over using full unsegmented images?*
  - **Methodology:** Implemented improved k-means clustering to segment lesion borders, followed by ROI cropping and offline data augmentation (rotations, flips, zooming, contrast adjustments).
  - **Answer & Findings:** Yes. Eliminating healthy skin artifacts allowed feature extraction networks to focus exclusively on lesion texture, boosting accuracy to 97.9% on DermIS and 97.4% on DermQuest.
- **RQ2 [Architectural Backbone Evaluation]:** *How do deep pre-trained CNN backbones (AlexNet vs. VGG-16) compare in feature transferability when fine-tuned strictly on segmented dermatoscopic lesion ROIs?*
  - **Methodology:** Fine-tuned pre-trained AlexNet and VGG-16 architectures on isolated lesion patches across two clinical benchmark datasets under identical training protocols.
  - **Answer & Findings:** Both architectures demonstrated strong transferability; VGG-16 captured finer textural details, yielding 96.3% sensitivity and 98.7% specificity on DermIS and 95.8% sensitivity and 98.1% specificity on DermQuest.
- **RQ3 [Benchmark Generalization]:** *Can an ROI-based transfer learning framework achieve robust, consistent diagnostic performance across independent clinical benchmark datasets?*
  - **Methodology:** Evaluated the pipeline on DermIS (705 images: 448 benign, 257 melanoma) and DermQuest (667 images: 434 nevus, 233 melanoma) using AUC, precision, and F1-score.
  - **Answer & Findings:** Demonstrated exceptional consistency across datasets: AUC reached 0.97 on DermIS and 0.96 on DermQuest, with F1-scores of 96.3% and 95.8% respectively.
- **RQ4 [Methodological Limitations]:** *Under what clinical conditions does k-means ROI segmentation fail, and how does this affect downstream melanoma detection?*
  - **Methodology:** Error analysis of segmentation failures on difficult border topologies and dense hair artifacts.
  - **Answer & Findings:** k-means clustering degrades in the presence of severe hair occlusion and diffuse, poorly demarcated lesion margins, leading to border over-clipping or under-segmentation.

- **Datasets:** DermIS (705 images), DermQuest (667 images)
- **Quantitative Results:** **Accuracy (DermIS):** 97.9% | **Sensitivity:** 96.3% | **Specificity:** 98.7% | **AUC (DermIS):** 0.97 | **Accuracy (DermQuest):** 97.4% | **AUC (DermQuest):** 0.96
- **Open Research Questions / Gaps:**
  - *Can automated deep semantic segmentation replace k-means to eliminate manual tuning in the presence of dense hair?*
  - *Can the framework scale to multi-class classification beyond binary melanoma vs. nevus distinction?*

---

### Paper 3: An Interpretable Skin Cancer Classification Using Optimized Convolutional Neural Network for a Smart Healthcare System
**Authors:** K. Mridha; M. M. Uddin; J. Shin; S. Khadka; M. F. Mridha  
**Venue:** *IEEE Access* (2023) | **DOI:** [10.1109/ACCESS.2023.3269694](https://doi.org/10.1109/ACCESS.2023.3269694) | **IEEE Article Number:** `10107401`  
**Category:** `Explainable AI (XAI) & Mobile Healthcare`  

> **Problem Formulation:** Deep learning CAD systems act as 'black boxes', lacking visual transparency and suffering from severe performance drops on underrepresented minority classes in multi-class dermatological screening.

#### Formulated Research Questions & Findings:
- **RQ1 [Optimization & Activation Engineering]:** *What combination of optimization algorithms (Adam vs. RMSprop) and activation functions (ReLU, Swish, Tanh) maximizes multi-class lesion classification accuracy on HAM10000?*
  - **Methodology:** Trained a custom CNN with batch normalization, max pooling, and dropout across systematic combinations of optimizers and activation functions.
  - **Answer & Findings:** The custom CNN achieved peak overall accuracy of 82.0% and specificity of 94.17% with Adam optimizer and Swish/ReLU activations, with a loss accuracy of 0.47%.
- **RQ2 [Explainable AI & Visual Attribution]:** *Can post-hoc visual attribution maps (Grad-CAM and Grad-CAM++) accurately highlight clinically relevant lesion structures to build clinician trust?*
  - **Methodology:** Generated localized gradient attribution heatmaps at the final convolutional layer to visualize discriminative regions for each of the 7 diagnostic classes.
  - **Answer & Findings:** Grad-CAM and Grad-CAM++ successfully localized pigmented network patterns and atypical margins matching dermatologist inspection criteria.
- **RQ3 [Class Imbalance Impact]:** *How significantly does class imbalance affect per-class sensitivity across common (melanocytic nevi) versus rare (dermatofibroma, vascular) skin lesions?*
  - **Methodology:** Analyzed confusion matrices across all 7 classes of HAM10000 (10,015 images) following geometric data augmentation.
  - **Answer & Findings:** Sensitivity remained high for dominant classes but dropped on minority classes (df and vasc), demonstrating that geometric augmentation alone is insufficient to resolve extreme skew.
- **RQ4 [Point-of-Care Mobile Feasibility]:** *Can an explainable deep CNN be integrated into an Android smart healthcare application for real-time mobile clinical triage?*
  - **Methodology:** Exported the optimized lightweight CNN model and embedded it within an end-to-end Android mobile screening application.
  - **Answer & Findings:** Successfully validated end-to-end mobile execution with near real-time inference latency suitable for decentralized point-of-care screening.

- **Datasets:** HAM10000 (10,015 images across 7 classes)
- **Quantitative Results:** **Accuracy:** 82.0% | **Specificity:** 94.17% | **Sensitivity:** 82.0% | **Loss Accuracy:** 0.47%
- **Open Research Questions / Gaps:**
  - *How can synthetic metric oversampling or cost-sensitive losses improve minority class sensitivity in mobile models?*
  - *What is the diagnostic accuracy of the Android application when tested prospectively in multi-ethnic outpatient clinics?*

---

### Paper 4: Automatic Skin Cancer Detection in Dermoscopy Images Based on Ensemble Lightweight Deep Learning Network
**Authors:** L. Wei; K. Ding; H. Hu  
**Venue:** *IEEE Access* (2020) | **DOI:** [10.1109/ACCESS.2020.2997710](https://doi.org/10.1109/ACCESS.2020.2997710) | **IEEE Article Number:** `9099799`  
**Category:** `Lightweight Networks & Ensemble Learning`  

> **Problem Formulation:** High computational complexity and massive parameter counts prevent deployment of state-of-the-art deep networks on resource-constrained clinical workstations and edge devices.

#### Formulated Research Questions & Findings:
- **RQ1 [Lightweight Architecture Efficiency]:** *Can a lightweight ensemble deep learning framework drastically reduce model parameters while maintaining state-of-the-art diagnostic accuracy on benchmark dermoscopic challenges?*
  - **Methodology:** Designed a parameter-efficient ensemble using lightweight CNN feature extractors, a lightweight U-Net segmentation module, and a fine-grained discrimination network.
  - **Answer & Findings:** Yes. The framework achieved an accuracy of 87.3% and an AUC of 0.886 on ISBI 2016 with orders-of-magnitude fewer parameters than standard heavyweight baselines.
- **RQ2 [Pair-Based Feature Discrimination]:** *How does pair-based feature extraction and fine-grained metric learning improve discrimination between visually ambiguous benign nevi and malignant melanoma?*
  - **Methodology:** Trained a feature discrimination network on positive and negative sample pairs using fine-grained classification principles to learn subtle boundary differences.
  - **Answer & Findings:** Pair-based learning effectively separated subtle boundary patterns, yielding a test sensitivity of 83.2%, specificity of 89.1%, and average precision of 0.732 on ISBI 2016.
- **RQ3 [Integrated Semantic Segmentation]:** *Does integrating a lightweight U-Net trained via transfer learning eliminate the need for manual hair and artifact preprocessing?*
  - **Methodology:** Trained an end-to-end lightweight U-Net to isolate lesion contours directly from raw dermoscopic imagery without heuristic artifact filtering.
  - **Answer & Findings:** Automated segmentation successfully isolated lesion contours end-to-end, providing clean input patches to downstream pair-based classification networks.
- **RQ4 [Boundary Sensitivity & Complexity]:** *What are the diagnostic failure modes on lesions with highly indistinct, diffuse boundaries, and what is the training overhead of ensemble decision fusion?*
  - **Methodology:** Evaluated ensemble convergence, training memory footprint, and false-negative edge cases on ISBI 2016 and ISBI 2017.
  - **Answer & Findings:** Performance modestly degraded on lesions with fuzzy, diffuse boundaries, and training multiple lightweight networks sequentially introduced non-negligible training time overhead.

- **Datasets:** ISBI 2016 (900 train, 379 test), ISBI 2017 Challenge Dataset
- **Quantitative Results:** **Accuracy:** 87.3% | **AUC:** 0.886 | **Sensitivity:** 83.2% | **Specificity:** 89.1% | **Average Precision:** 0.732
- **Open Research Questions / Gaps:**
  - *Can pair-based lightweight feature discrimination scale effectively to 8-class multi-category classification?*
  - *Can knowledge distillation compress the lightweight ensemble into a single ultra-compact inference model?*

---

### Paper 5: DeepSkin: A Deep Learning Approach for Skin Cancer Classification
**Authors:** H. L. Gururaj; N. Manju; A. Nagarjun; V. N. M. Aradhya; F. Flammini  
**Venue:** *IEEE Access* (2023) | **DOI:** [10.1109/ACCESS.2023.3274848](https://doi.org/10.1109/ACCESS.2023.3274848) | **IEEE Article Number:** `10122533`  
**Category:** `Residual Custom Architectures & Multi-Class Screening`  

> **Problem Formulation:** Existing CAD systems suffer from accuracy degradation in multi-class classification and require heavy pre-trained backbones that struggle with class-imbalanced dermoscopic archives.

#### Formulated Research Questions & Findings:
- **RQ1 [Architectural Design]:** *Can a tailored custom CNN with residual skip connections ('DeepSkin') match or surpass standard transfer learning models (VGG-16, ResNet-50, MobileNet) on multi-class dermoscopic screening?*
  - **Methodology:** Architected DeepSkin with residual skip connections to preserve low-level textural gradients, benchmarked comparatively against VGG-16, ResNet-50, and MobileNet.
  - **Answer & Findings:** DeepSkin achieved 88.0% overall accuracy, outperforming several heavier pre-trained models while maintaining architectural simplicity and compact parameterization.
- **RQ2 [Multiclass Performance & Imbalance]:** *How effectively does DeepSkin handle the 7 diagnostic classes of HAM10000 under Min-Max scaling and geometric data augmentation?*
  - **Methodology:** Preprocessed 10,015 images with Min-Max intensity scaling, 224x224 resizing, and spatial augmentations (rotations, flips, zooms, brightness adjustments).
  - **Answer & Findings:** Achieved overall sensitivity of 86.2%, specificity of 85.0%, and precision of 86.4% across all 7 pathological categories.
- **RQ3 [Diagnostic Confusion Patterns]:** *Which pathological categories exhibit the highest cross-class confusion within the DeepSkin architecture?*
  - **Methodology:** Evaluated class-wise confusion matrices and classification errors across benign keratosis, melanocytic nevi, and malignant melanoma.
  - **Answer & Findings:** The primary clinical confusion occurred between benign keratosis and melanoma due to morphological and chromatic overlaps in early-stage lesions.
- **RQ4 [Edge Profiling & Clinical Readiness]:** *What deployment barriers remain before DeepSkin can be integrated into resource-constrained point-of-care settings?*
  - **Methodology:** Assessed deployment requirements, edge hardware profiling, and demographic population diversity.
  - **Answer & Findings:** Identified lack of hardware edge-profiling (FPS, RAM consumption) and absence of multi-ethnic clinical validation cohorts as critical deployment gaps.

- **Datasets:** ISIC 2018 / HAM10000 (10,015 images, 7 classes)
- **Quantitative Results:** **Accuracy:** 88.0% | **Sensitivity:** 86.2% | **Specificity:** 85.0% | **Precision:** 86.4%
- **Open Research Questions / Gaps:**
  - *How can attention gates be added to DeepSkin to resolve confusion between benign keratosis and melanoma?*
  - *What is the inference latency of DeepSkin on embedded microcontroller and edge-TPU hardware?*

---

### Paper 6: FCN-Based DenseNet Framework for Automated Detection and Classification of Skin Lesions in Dermoscopy Images
**Authors:** A. A. Adegun; S. Viriri  
**Venue:** *IEEE Access* (2020) | **DOI:** [10.1109/ACCESS.2020.3016651](https://doi.org/10.1109/ACCESS.2020.3016651) | **IEEE Article Number:** `9167192`  
**Category:** `Integrated Segmentation & Dense Feature Reuse`  

> **Problem Formulation:** Fuzzy lesion margins, irregular pigment borders, and occluding hair shafts degrade end-to-end classifiers that lack prior semantic lesion localization.

#### Formulated Research Questions & Findings:
- **RQ1 [Integrated Two-Stage Pipeline]:** *Does cascading a Fully Convolutional Network (FCN) segmentation model with a DenseNet classification network improve multi-class skin lesion recognition over single-stage models?*
  - **Methodology:** Built an integrated pipeline where an FCN with encoder-decoder residual skips segments the lesion mask to crop input patches for a DenseNet classifier.
  - **Answer & Findings:** Yes. The pipeline achieved state-of-the-art classification accuracy of 95.0% on ISIC 2017 and 98.5% on ISIC 2018, with 96.0% sensitivity and 0.98 AUC.
- **RQ2 [Dense Connectivity & Feature Reuse]:** *What is the architectural advantage of DenseNet's dense connectivity and feature reuse in capturing subtle dermoscopic biomarkers?*
  - **Methodology:** Leveraged dense connectivity blocks to concatenate feature maps from all preceding layers, maximizing gradient flow and feature reuse.
  - **Answer & Findings:** Dense feature reuse preserved fine textural and micro-vascular details, leading to 97.0% specificity and 95.0% F1-score across 3-class lesion classification.
- **RQ3 [Artifact Suppression Preprocessing]:** *Does DullRazor morphological hair artifact suppression improve FCN segmentation accuracy and boundary delineation?*
  - **Methodology:** Applied DullRazor morphological filtering followed by contrast enhancement and affine augmentations before feeding images to the FCN.
  - **Answer & Findings:** DullRazor artifact removal significantly boosted segmentation quality, yielding a 98.5% segmentation accuracy, 92.5% Dice coefficient, and 86.8% Jaccard index.
- **RQ4 [Computational Complexity]:** *What is the computational overhead of two-stage FCN + DenseNet training, and how does it handle diffuse, poorly demarcated lesion boundaries?*
  - **Methodology:** Benchmarked training memory requirements, inference latency, and segmentation error on ambiguous lesion margins.
  - **Answer & Findings:** The two-stage framework demands substantial GPU memory during sequential training, and exhibits slight boundary over-segmentation on lesions with faint, diffuse margins.

- **Datasets:** ISIC 2017 (2,750 images), ISIC 2018 (3,694 images), DermQuest
- **Quantitative Results:** **Segmentation Accuracy:** 98.5% | **Dice Coefficient:** 92.5% | **Jaccard Index:** 86.8% | **Classification Accuracy (2018):** 98.5% | **Classification Accuracy (2017):** 95.0% | **AUC:** 0.98
- **Open Research Questions / Gaps:**
  - *Can the FCN and DenseNet stages be trained end-to-end with joint loss backpropagation to reduce training time?*
  - *How robust is the FCN segmentation when tested on low-contrast, non-dermoscopic smartphone images?*

---

### Paper 7: Malignant Melanoma Classification Using Deep Learning: Datasets, Performance Measurements, Challenges and Opportunities
**Authors:** A. Naeem; M. S. Farooq; A. Khelifi; A. Abid  
**Venue:** *IEEE Access* (2020) | **DOI:** [10.1109/ACCESS.2020.3001507](https://doi.org/10.1109/ACCESS.2020.3001507) | **IEEE Article Number:** `9113301`  
**Category:** `Systematic Literature Review (Kitchenham SLR)`  

> **Problem Formulation:** Lack of standardized evaluation protocols, heterogeneous dataset partitions, and unaddressed class imbalance prevent objective comparison of deep learning melanoma diagnostic algorithms.

#### Formulated Research Questions & Findings:
- **RQ1 [SLR Explicit RQ1: Model Taxonomy]:** *What type of deep learning based classifiers are used for diagnosing melanoma disease?*
  - **Methodology:** Conducted a systematic literature review following the Kitchenham protocol across IEEE, Springer, Elsevier, ACM, ScienceDirect, and Medline from 2014 to 2020.
  - **Answer & Findings:** Pre-trained CNN architectures dominate the literature (ResNet-50, VGG-16, Inception-v3, and DenseNet-121), with transfer learning being the preferred strategy to overcome medical image scarcity.
- **RQ2 [SLR Explicit RQ2: Performance Measurement]:** *What is the performance measurement used for the evaluation of deep learning models in melanoma diagnosis?*
  - **Methodology:** Analyzed performance metric reporting standards across 52 finalized peer-reviewed publications.
  - **Answer & Findings:** Accuracy, Sensitivity (Recall), Specificity, and ROC-AUC are the primary metrics; best models achieve ~93.4% accuracy and 0.95 AUC, but precision and F1 are inconsistently reported.
- **RQ3 [SLR Explicit RQ3: Dataset Taxonomy]:** *What type of datasets are used for melanoma diagnosis in existing literature?*
  - **Methodology:** Categorized benchmark repositories, sample sizes, class distributions, and data accessibility across published studies.
  - **Answer & Findings:** Public benchmarks dominate: ISIC Challenge archives (2016-2018), HAM10000, and PH2 are universally used, but severe class imbalance (benign nevi >> melanoma) universally distorts accuracy.
- **RQ4 [SLR Research Gaps & Opportunities]:** *What are the critical open challenges and future research opportunities identified in deep learning melanoma diagnosis?*
  - **Methodology:** Synthesized unresolved methodological and clinical gaps across the systematic review corpus.
  - **Answer & Findings:** Identified 3 major gaps: (1) lack of prospective multi-center clinical validation, (2) failure to integrate clinical demographic metadata, and (3) vulnerability to adversarial artifacts and hair occlusions.

- **Datasets:** PH2 (200 images), ISIC 2016 (1,279 images), ISIC 2017 (2,000 images), ISIC 2018 (10,015 images), HAM10000
- **Quantitative Results:** **Highest Benchmark Accuracy:** 93.4% | **Average Sensitivity:** 91.0% | **Average Specificity:** 94.2% | **Peak AUC:** 0.95
- **Open Research Questions / Gaps:**
  - *How can standardized cross-validation benchmarks be enforced across IEEE and medical AI publications?*
  - *What multimodal architectures best fuse clinical patient metadata with deep dermoscopic visual embeddings?*

---

### Paper 8: Skin Cancer Detection Using Combined Decision of Deep Learners
**Authors:** A. Imran; A. Nasir; M. Bilal; G. Sun; A. Alzahrani; A. Almuhaimeed  
**Venue:** *IEEE Access* (2022) | **DOI:** [10.1109/ACCESS.2022.3220329](https://doi.org/10.1109/ACCESS.2022.3220329) | **IEEE Article Number:** `9940917`  
**Category:** `Ensemble Fusion & Capsule Networks`  

> **Problem Formulation:** Subtle chromatic and textural similarities between benign and malignant lesions yield high false-positive rates in single-model CAD systems.

#### Formulated Research Questions & Findings:
- **RQ1 [Architectural Heterogeneity]:** *Can combining heterogeneous deep learning architectures (custom VGG-16, residual ResNet-50, and Capsule Network) outperform individual standalone classifiers in melanoma detection?*
  - **Methodology:** Trained three distinct models capturing spatial textures (CNNs) and spatial-relational hierarchies (CapsNet) on a curated balanced dataset.
  - **Answer & Findings:** Yes. Fusing CNN feature representations with Capsule Network spatial equivariance achieved superior discriminative reliability, boosting accuracy to 93.50%.
- **RQ2 [Ensemble Decision Mechanics]:** *How does an ensemble soft-voting decision mechanism reconcile divergent predictions between conventional CNNs and Capsule Networks?*
  - **Methodology:** Aggregated output probability vectors from VGG-16, ResNet-50, and CapsNet using weighted soft-voting to produce final class labels.
  - **Answer & Findings:** Soft-voting reduced individual model variance and eliminated single-model outlier misclassifications, yielding 94.80% specificity and 94.30% precision.
- **RQ3 [Diagnostic Balance & Sensitivity]:** *What sensitivity and F1-score are achieved on a balanced dermoscopic benchmark of 2,800 images?*
  - **Methodology:** Evaluated the combined system on a balanced subset of 1,400 benign and 1,400 malignant ISIC images with extensive geometric augmentations.
  - **Answer & Findings:** Achieved a sensitivity of 87.25%, an F1-score of 90.64%, and an overall classification accuracy of 93.50%.
- **RQ4 [Computational Latency Trade-Offs]:** *What is the inference latency overhead of concurrently executing three deep networks during clinical point-of-care screening?*
  - **Methodology:** Analyzed GPU runtime, model parameter scaling, and memory footprint of concurrent inference across the three learners.
  - **Answer & Findings:** Concurrent execution of three deep networks triples memory consumption and increases inference latency, requiring high-end GPUs that may restrict point-of-care mobile deployment.

- **Datasets:** ISIC Archive Curated Balanced Dataset (2,800 images: 1,400 benign, 1,400 malignant)
- **Quantitative Results:** **Accuracy:** 93.50% | **Sensitivity:** 87.25% | **Specificity:** 94.80% | **Precision:** 94.30% | **F1-Score:** 90.64%
- **Open Research Questions / Gaps:**
  - *Can model pruning or knowledge distillation distill the three-model ensemble into a single fast inference network?*
  - *How does the combined decision framework perform when deployed on imbalanced multi-class benchmarks?*

---

### Paper 9: FixCaps: An Improved Capsules Network for Diagnosis of Skin Cancer
**Authors:** Z. Lan; S. Cai; X. He; X. Wen  
**Venue:** *IEEE Access* (2022) | **DOI:** [10.1109/ACCESS.2022.3181225](https://doi.org/10.1109/ACCESS.2022.3181225) | **IEEE Article Number:** `9791221`  
**Category:** `Capsule Networks & Attention Routing`  

> **Problem Formulation:** Standard CNN pooling layers discard critical spatial part-whole relationships, while traditional Capsule Networks suffer from slow convergence and high compute latency due to iterative dynamic routing.

#### Formulated Research Questions & Findings:
- **RQ1 [Routing Algorithm Innovation]:** *Can replacing iterative dynamic routing with a fixed matrix transformation routing mechanism ('FixCaps') eliminate the computational bottleneck of Capsule Networks in dermoscopy?*
  - **Methodology:** Replaced dynamic routing with fixed matrix transformation and incorporated convolutional attention modules to maintain transformation equivariance without routing iterations.
  - **Answer & Findings:** Yes. FixCaps dramatically accelerated training convergence while retaining vector capsule representations, achieving an extraordinary peak accuracy of 96.49% on HAM10000.
- **RQ2 [Spatial Hierarchy & Equivariance]:** *How does vector capsule representation enhance feature discrimination across multi-class skin lesions with complex spatial sub-structures?*
  - **Methodology:** Evaluated vector activation norms for encoding lesion pose, orientation, and subtle textural patterns across 7 diagnostic categories.
  - **Answer & Findings:** Vector capsules effectively captured spatial part-whole relationships (pigment network to border), yielding 93.47% sensitivity, 98.13% specificity, and 0.98 AUC.
- **RQ3 [Diagnostic Precision & F1]:** *What precision and F1-score are attained by FixCaps across the 10,015 images of the HAM10000 benchmark?*
  - **Methodology:** Benchmarked FixCaps using 5-fold cross-validation on color-normalized and augmented HAM10000 images.
  - **Answer & Findings:** FixCaps achieved 93.64% precision and 93.55% F1-score, establishing state-of-the-art capsule performance in dermatological CAD.
- **RQ4 [Minority Class Robustness]:** *What are the performance limitations of FixCaps on severely underrepresented minority classes such as dermatofibroma?*
  - **Methodology:** Class-wise sensitivity breakdown and evaluation on out-of-distribution clinical photography.
  - **Answer & Findings:** Minor sensitivity degradation was observed on rare classes (dermatofibroma), and the architecture was not validated on clinical (non-dermoscopic) photographs.

- **Datasets:** HAM10000 (10,015 images across 7 classes)
- **Quantitative Results:** **Accuracy:** 96.49% | **Sensitivity:** 93.47% | **Specificity:** 98.13% | **Precision:** 93.64% | **F1-Score:** 93.55% | **AUC:** 0.98
- **Open Research Questions / Gaps:**
  - *Can FixCaps be adapted to segment lesion boundaries directly from capsule activation lengths?*
  - *How does FixCaps perform on non-dermoscopic smartphone images taken under variable clinical lighting?*

---

### Paper 10: Deep Clustering via Center-Oriented Margin Free-Triplet Loss for Skin Lesion Detection in Highly Imbalanced Datasets
**Authors:** Ş. Öztürk; T. Çukur  
**Venue:** *IEEE Journal of Biomedical and Health Informatics* (2022) | **DOI:** [10.1109/JBHI.2022.3187215](https://doi.org/10.1109/JBHI.2022.3187215) | **IEEE Article Number:** `9810181`  
**Category:** `Deep Metric Learning & Imbalance Mitigation`  

> **Problem Formulation:** Extreme sample imbalance between common benign lesions and rare malignant melanoma severely biases deep classifiers toward majority classes under standard cross-entropy loss.

#### Formulated Research Questions & Findings:
- **RQ1 [Loss Function Innovation]:** *How does a Center-Oriented Margin-Free Triplet Loss (COMF-TL) overcome the hyperparameter tuning instability and gradient saturation of standard triplet losses in skewed dermatological datasets?*
  - **Methodology:** Formulated COMF-TL to adaptively pull feature embeddings toward dynamically updated class centers while repelling negative clusters without requiring a manually tuned fixed margin.
  - **Answer & Findings:** COMF-TL eliminated the sensitivity to margin selection and stabilized embedding clustering, yielding a 4.58% AUC improvement over standard cross-entropy baselines.
- **RQ2 [Metric Space Clustering]:** *Can deep metric clustering separate minority cancer classes without requiring synthetic oversampling techniques (SMOTE, GANs) that risk introducing artifacts?*
  - **Methodology:** Trained ResNet-50 and VGG-16 backbones using COMF-TL to learn discriminative metric spaces directly from unaugmented, imbalanced feature distributions.
  - **Answer & Findings:** Yes. Deep clustering achieved robust boundary separation, attaining a balanced multi-class accuracy of 83.7%, sensitivity of 82.4%, and specificity of 92.1% on ISIC 2018.
- **RQ3 [Large-Scale Scaling]:** *Does COMF-TL scale effectively when tested on the massive 8-class ISIC 2019 benchmark (25,331 images)?*
  - **Methodology:** Evaluated the framework on ISIC 2019 across ResNet-50 and VGG-16 backbones using mean AUC and macro-averaged F1-score.
  - **Answer & Findings:** Demonstrated strong scalability, achieving an overall AUC of 0.912 and an F1-score of 81.9% on ISIC 2019, consistently outperforming standard cross-entropy baselines.
- **RQ4 [Computational Overhead]:** *What is the training latency and memory overhead introduced by continuous cluster center recalculation and online triplet mining?*
  - **Methodology:** Profiled epoch training times, triplet mining complexity, and cluster center synchronization during backpropagation.
  - **Answer & Findings:** Dynamic cluster center recalculation and online semi-hard triplet mining increased per-epoch training time by ~30% compared to standard cross-entropy.

- **Datasets:** ISIC 2018 (10,015 images, 7 classes), ISIC 2019 (25,331 images, 8 classes)
- **Quantitative Results:** **Balanced Accuracy:** 83.7% | **AUC:** 0.912 | **AUC Improvement:** +4.58% | **Sensitivity:** 82.4% | **Specificity:** 92.1% | **F1-Score:** 81.9%
- **Open Research Questions / Gaps:**
  - *Can COMF-TL be integrated with Vision Transformers to cluster patch tokens directly in self-attention layers?*
  - *How does COMF-TL perform under open-set conditions where unseen skin disease classes are encountered during inference?*

---

### Paper 11: Neural Architecture Search for Skin Lesion Classification
**Authors:** A. Kwasigroch; M. Grochowski; A. Mikołajczyk  
**Venue:** *IEEE Access* (2020) | **DOI:** [10.1109/ACCESS.2020.2964424](https://doi.org/10.1109/ACCESS.2020.2964424) | **IEEE Article Number:** `8950333`  
**Category:** `Neural Architecture Search (NAS)`  

> **Problem Formulation:** Manual trial-and-error design of deep CNN architectures for dermatological diagnosis is computationally inefficient, subjective, and sub-optimal for complex multi-class benchmarks.

#### Formulated Research Questions & Findings:
- **RQ1 [Automated Architecture Discovery]:** *Can Neural Architecture Search (NAS) using network morphism automatically discover optimal CNN topologies tailored for skin lesion classification that outperform hand-crafted networks?*
  - **Methodology:** Applied network morphism operations (inserting layers, widening channels) guided by hill-climbing search optimization on the ISIC 2018 benchmark.
  - **Answer & Findings:** Yes. The morphologically discovered CNN achieved 82.8% multiclass accuracy and 81.5% balanced accuracy, rivaling or exceeding hand-engineered ResNet-50 while requiring 34% fewer parameters.
- **RQ2 [Search Efficiency & Network Morphism]:** *How does network morphism preserve learned model knowledge during architectural mutations to reduce search compute costs?*
  - **Methodology:** Inherited weights from parent architectures during layer insertions and dimensional expansions, training mutant models incrementally.
  - **Answer & Findings:** Knowledge inheritance prevented re-training from scratch, enabling search convergence in orders of magnitude fewer GPU hours than standard reinforcement-learning NAS.
- **RQ3 [AUC & Diagnostic Generalization]:** *What mean ROC-AUC across the 7 classes of ISIC 2018 is attained by the NAS-derived architecture?*
  - **Methodology:** Evaluated the final searched architecture across 10,015 images using macro-averaged ROC-AUC and balanced accuracy metrics.
  - **Answer & Findings:** Achieved a mean ROC-AUC of 0.914, demonstrating robust discriminative capability across both majority nevi and minority malignancy classes.
- **RQ4 [Search Space Constraints]:** *What are the computational limitations and search space sensitivity issues encountered during dermatological NAS?*
  - **Methodology:** Analyzed GPU day resource consumption and search trajectory dependence on initial seed architecture.
  - **Answer & Findings:** The search process required multiple dedicated GPU days and exhibited sensitivity to seed model selection, with the search space restricted to feedforward convolutional operations.

- **Datasets:** ISIC 2018 Challenge Task 3 (10,015 images, 7 classes)
- **Quantitative Results:** **Multiclass Accuracy:** 82.8% | **Balanced Accuracy:** 81.5% | **Mean AUC:** 0.914 | **Parameter Reduction:** 34%
- **Open Research Questions / Gaps:**
  - *Can NAS search spaces be expanded to discover hybrid attention blocks and vision transformer tokens automatically?*
  - *Can multi-objective NAS optimize simultaneously for diagnostic accuracy and mobile inference latency?*

---

### Paper 12: Performance Enhancement of Skin Cancer Classification Using Computer Vision
**Authors:** A. Magdy; H. Hussein; R. F. Abdel-Kader; K. A. E. Salam  
**Venue:** *IEEE Access* (2023) | **DOI:** [10.1109/ACCESS.2023.3294974](https://doi.org/10.1109/ACCESS.2023.3294974) | **IEEE Article Number:** `10181245`  
**Category:** `Computer Vision Enhancement & Multi-Model Transfer`  

> **Problem Formulation:** Poor image contrast, irregular illumination, and skin artifacts degrade deep feature representations in transfer learning models.

#### Formulated Research Questions & Findings:
- **RQ1 [Preprocessing & Contrast Enhancement]:** *Does integrating Contrast Limited Adaptive Histogram Equalization (CLAHE) and color constancy improve deep transfer learning accuracy on dermoscopic images?*
  - **Methodology:** Implemented a computer vision pipeline incorporating Gray World color constancy and CLAHE contrast enhancement prior to transfer learning classification.
  - **Answer & Findings:** Yes. CLAHE significantly improved edge gradient contrast, boosting downstream classification accuracy by 3.8% across pre-trained backbones.
- **RQ2 [Comparative Backbone Benchmarking]:** *How do modern CNN architectures (ResNet-50, DenseNet-201, EfficientNet-B0) compare when processing contrast-enhanced dermoscopic lesions?*
  - **Methodology:** Fine-tuned ResNet-50, DenseNet-201, and EfficientNet-B0 on enhanced ISIC 2019 and HAM10000 images under standardized hyperparameter protocols.
  - **Answer & Findings:** EfficientNet-B0 achieved the superior trade-off of accuracy and parameter efficiency, reaching 94.6% accuracy, 93.2% sensitivity, 95.8% specificity, and 0.965 AUC.
- **RQ3 [Precision & F1 Verification]:** *What precision and F1-score are delivered by the optimized EfficientNet pipeline across dermoscopic benchmarks?*
  - **Methodology:** Measured precision and macro-averaged F1-scores across 5-fold cross-validation runs on benchmark datasets.
  - **Answer & Findings:** EfficientNet-B0 with CLAHE delivered an F1-score of 94.0% and balanced diagnostic precision across benign and malignant classes.
- **RQ4 [Preprocessing Latency & Artifacts]:** *What are the computational trade-offs of multi-stage contrast enhancement pipelines during high-throughput clinical screening?*
  - **Methodology:** Profiled preprocessing execution time per image and analyzed false-positive edge artifacts generated by aggressive local histogram equalization.
  - **Answer & Findings:** CLAHE can amplify high-frequency background noise (skin pores, hair stubble) in low-contrast images, requiring careful clipping limit tuning that increases per-image preprocessing time.

- **Datasets:** ISIC 2019, HAM10000
- **Quantitative Results:** **Accuracy (EfficientNet-B0):** 94.6% | **Sensitivity:** 93.2% | **Specificity:** 95.8% | **F1-Score:** 94.0% | **AUC:** 0.965
- **Open Research Questions / Gaps:**
  - *Can contrast enhancement parameters be learned end-to-end via a differentiable image processing layer?*
  - *How does the CLAHE-enhanced pipeline perform on non-dermoscopic smartphone camera images?*

---

### Paper 13: EFAM-Net: A Multi-Class Skin Lesion Classification Model Utilizing Enhanced Feature Fusion and Attention Mechanisms
**Authors:** Z. Ji; X. Wang; C. Liu; Z. Wang; N. Yuan; I. Ganchev  
**Venue:** *IEEE Access* (2024) | **DOI:** [10.1109/ACCESS.2024.3468612](https://doi.org/10.1109/ACCESS.2024.3468612) | **IEEE Article Number:** `10695064`  
**Category:** `Multi-Scale Attention & Feature Fusion`  

> **Problem Formulation:** Single-scale deep networks fail to capture both macroscopic lesion contour geometry and microscopic pigment network textures simultaneously.

#### Formulated Research Questions & Findings:
- **RQ1 [Dual-Branch Attention Innovation]:** *Can combining Enhanced Feature Fusion with Spatial and Channel Attention Mechanisms ('EFAM-Net') simultaneously capture global lesion boundaries and fine-grained dermoscopic textures?*
  - **Methodology:** Designed EFAM-Net featuring a multi-scale feature pyramid, a channel attention module (CAM) for inter-channel dependencies, and a spatial attention module (SAM) for lesion localization.
  - **Answer & Findings:** Yes. EFAM-Net achieved a top-tier multi-class classification accuracy of 94.28% on HAM10000, significantly outperforming single-scale CNN baselines.
- **RQ2 [Attention-Driven Feature Separation]:** *How do spatial and channel attention mechanisms suppress irrelevant peripheral healthy skin artifacts while accentuating subtle atypical pigment networks?*
  - **Methodology:** Visualized attention weight maps across intermediate stages of the multi-scale pyramid on ambiguous lesion boundaries.
  - **Answer & Findings:** Channel attention dynamically weighted discriminative pigment feature maps, while spatial attention effectively masked surrounding healthy tissue and vignetting artifacts.
- **RQ3 [Multiclass Diagnostic Performance]:** *What mean sensitivity, specificity, and AUC are attained by EFAM-Net across the 7 diagnostic classes of ISIC 2018 / HAM10000?*
  - **Methodology:** Evaluated EFAM-Net across 10,015 images using aspect-ratio preserving resizing, affine augmentations, and cross-entropy loss.
  - **Answer & Findings:** Achieved mean sensitivity of 91.85%, mean specificity of 95.40%, F1-score of 93.12%, and an impressive ROC-AUC of 0.973.
- **RQ4 [Computational Complexity]:** *What is the memory and FLOP overhead of dual-branch multi-scale attention modules during model training and inference?*
  - **Methodology:** Benchmarked FLOP count, parameter scaling, and GPU inference latency against standard ResNet and MobileNet architectures.
  - **Answer & Findings:** Dual attention branches increase computational complexity and training GPU memory requirements, demanding optimization before deployment on embedded medical devices.

- **Datasets:** ISIC 2018 / HAM10000 (10,015 images across 7 classes)
- **Quantitative Results:** **Accuracy:** 94.28% | **Mean Sensitivity:** 91.85% | **Mean Specificity:** 95.40% | **F1-Score:** 93.12% | **AUC:** 0.973
- **Open Research Questions / Gaps:**
  - *Can EFAM-Net's multi-scale attention modules be distilled into a lightweight backbone for real-time mobile triage?*
  - *How does EFAM-Net perform on clinical photography with heavy shadow occlusions?*

---

### Paper 14: Hair Segmentation and Removal in Dermoscopic Images Using Deep Learning
**Authors:** L. Talavera-Martínez; P. Bibiloni; M. González-Hidalgo  
**Venue:** *IEEE Access* (2021) | **DOI:** [10.1109/ACCESS.2020.3047258](https://doi.org/10.1109/ACCESS.2020.3047258) | **IEEE Article Number:** `9306830`  
**Category:** `Artifact Removal & Deep Inpainting`  

> **Problem Formulation:** Occluding hair shafts distort lesion borders and corrupt textural feature extraction; traditional heuristic filters like DullRazor blur underlying micro-vascular patterns.

#### Formulated Research Questions & Findings:
- **RQ1 [Deep Segmentation vs. Classical Filters]:** *Can a deep learning-based hair segmentation network outperform classical morphological filtering (DullRazor) in isolating fine and coarse hair artifacts without destroying genuine lesion borders?*
  - **Methodology:** Trained a modified U-Net architecture on a curated dataset of dermoscopic images with synthetically generated and annotated real hair masks.
  - **Answer & Findings:** Yes. Deep hair segmentation achieved a 92.8% Dice coefficient and 87.2% Jaccard index, preserving underlying lesion borders far more accurately than DullRazor.
- **RQ2 [Deep Inpainting & Texture Reconstruction]:** *How does deep context-aware inpainting of occluded hair pixels affect the discriminability of downstream skin cancer classification models?*
  - **Methodology:** Evaluated classification accuracy on images preprocessed by deep inpainting vs. classical inpainting vs. raw occluded images.
  - **Answer & Findings:** Deep inpainting improved downstream classification accuracy by 4.2% compared to raw hair-occluded images, and by 2.1% compared to traditional DullRazor filtering.
- **RQ3 [Synthetic Hair Training Strategy]:** *Does training deep segmentation networks on realistic synthetic hair masks generalize reliably to real-world clinical hair occlusions?*
  - **Methodology:** Constructed realistic synthetic hair models with variable thickness, curvature, and translucency to train the U-Net, tested on real hair benchmarks.
  - **Answer & Findings:** Synthetic hair training generalized well, demonstrating robust segmentation across real dermoscopic hair artifacts without manual clinical mask annotations.
- **RQ4 [Inpainting Blur & Feature Distortion]:** *What are the limitations of deep inpainting when hair shafts occlude ultra-fine atypical pigment networks or micro-vessels?*
  - **Methodology:** Examined high-magnification dermoscopic edge cases where hair directly traverses critical diagnostic criteria.
  - **Answer & Findings:** Deep inpainting can introduce subtle local blurring or interpolation artifacts across fine pigment lines, potentially masking micro-vascular structures.

- **Datasets:** ISIC 2018 Hair Dataset Subsets (Synthetic and Real Annotated Hair)
- **Quantitative Results:** **Hair Dice Coefficient:** 92.8% | **Jaccard Index:** 87.2% | **Downstream Accuracy Gain:** +4.2% vs raw | **Gain vs DullRazor:** +2.1%
- **Open Research Questions / Gaps:**
  - *Can generative adversarial inpainting reconstruct occluded pigment networks without any blurring?*
  - *How can hair removal be integrated end-to-end into classification backbones as a differentiable layer?*

---

### Paper 15: Dermoscopy Image Classification Based on StyleGANs and Decision Fusion
**Authors:** A. Gong; X. Yao; W. Lin  
**Venue:** *IEEE Access* (2020) | **DOI:** [10.1109/ACCESS.2020.2986916](https://doi.org/10.1109/ACCESS.2020.2986916) | **IEEE Article Number:** `9062473`  
**Category:** `Generative Data Augmentation & GANs`  

> **Problem Formulation:** Severe underrepresentation of malignant melanoma and rare lesion categories creates acute training bias and high false-negative rates in deep classifiers.

#### Formulated Research Questions & Findings:
- **RQ1 [High-Fidelity Synthetic Augmentation]:** *Can high-resolution StyleGANs synthesize photorealistic dermoscopic images of minority skin lesions to resolve class imbalance without generating unrealistic clinical artifacts?*
  - **Methodology:** Trained StyleGAN on ISIC 2018 dermoscopic images to generate high-resolution synthetic samples for minority diagnostic classes, screening sample quality using Fréchet Inception Distance (FID).
  - **Answer & Findings:** Yes. StyleGAN generated photorealistic lesions with an FID of 18.4, successfully capturing subtle pigment networks and atypical border gradations.
- **RQ2 [Multi-Block Decision Fusion]:** *How does combining multiple deep CNN feature extraction blocks with decision-level fusion improve classification stability on GAN-augmented datasets?*
  - **Methodology:** Integrated feature representations from distinct CNN backbones and applied weighted decision fusion to predict multi-class lesion probabilities.
  - **Answer & Findings:** Decision fusion achieved an overall classification accuracy of 91.2% and mean sensitivity of 89.6%, outperforming standalone models trained on imbalanced data by 6.8% accuracy.
- **RQ3 [Benchmark Diagnostic AUC]:** *What overall ROC-AUC is achieved across the 7 classes of ISIC 2018 Task 3 by the StyleGAN-augmented ensemble framework?*
  - **Methodology:** Evaluated the synthesized balanced dataset across 7 diagnostic categories using macro-averaged ROC-AUC metrics.
  - **Answer & Findings:** Achieved a macro-averaged ROC-AUC of 0.948, demonstrating balanced discrimination across both common nevi and rare dermatological malignancies.
- **RQ4 [Generative Hallucination Risks]:** *What clinical risks arise from subtle generative hallucinations in synthetic training images, and what are the GPU training costs?*
  - **Methodology:** Clinical review of synthesized lesion morphologies and profiling of high-resolution GAN training compute requirements.
  - **Answer & Findings:** GAN training demands extensive multi-GPU compute resources, and subtle generative hallucinations (e.g. artificial pigment patterns) risk training networks on non-physiological visual features.

- **Datasets:** ISIC 2018 Challenge Task 3 (Dermoscopic Image Classification)
- **Quantitative Results:** **Accuracy:** 91.2% | **Mean Sensitivity:** 89.6% | **AUC:** 0.948 | **StyleGAN FID:** 18.4 | **Accuracy Improvement:** +6.8%
- **Open Research Questions / Gaps:**
  - *Can diffusion models (DDPM) surpass StyleGAN in fidelity and diversity while eliminating generative hallucination?*
  - *What regulatory criteria are necessary to certify synthetic medical data for training clinical CAD systems?*

---

### Paper 16: A Comprehensive Joint Learning System to Detect Skin Cancer
**Authors:** L. Riaz; H. M. Qadir; G. Ali; M. Ali; M. A. Raza; A. D. Jurcut; J. Ali  
**Venue:** *IEEE Access* (2023) | **DOI:** [10.1109/ACCESS.2023.3297644](https://doi.org/10.1109/ACCESS.2023.3297644) | **IEEE Article Number:** `10189856`  
**Category:** `Joint Multi-Task Learning`  

> **Problem Formulation:** Treating lesion segmentation and malignancy classification as isolated sequential pipelines compounds errors from segmentation to classification.

#### Formulated Research Questions & Findings:
- **RQ1 [Multi-Task Joint Architecture]:** *Can a comprehensive joint learning framework simultaneously optimize boundary segmentation and malignancy classification to exploit cross-task feature synergies?*
  - **Methodology:** Constructed a multi-task convolutional architecture with a shared encoder backbone that branches into a semantic segmentation decoder and a classification head.
  - **Answer & Findings:** Yes. Joint optimization forced the encoder to learn mutually beneficial geometric and textural representations, achieving 95.3% classification accuracy and 91.4% segmentation Dice.
- **RQ2 [Cross-Task Feature Regularization]:** *Does auxiliary segmentation loss act as an effective regularizer to prevent the classification head from overfitting to spurious background artifacts?*
  - **Methodology:** Trained models with and without auxiliary segmentation supervision, analyzing intermediate feature activation maps and gradient stability.
  - **Answer & Findings:** Auxiliary segmentation supervision effectively regularized classification gradients, boosting sensitivity to 94.1% and specificity to 96.5% on ISIC benchmarks.
- **RQ3 [Benchmark Diagnostic AUC]:** *What diagnostic discrimination (ROC-AUC) is achieved by the joint learning system on ISIC 2016 and ISIC 2017?*
  - **Methodology:** Evaluated the joint framework across ISIC 2016 (379 test) and ISIC 2017 (600 test) using ROC-AUC and F1-score.
  - **Answer & Findings:** Achieved a high ROC-AUC of 0.962 on ISIC benchmarks, significantly surpassing single-task classification baselines.
- **RQ4 [Loss Balancing & Ambiguous Borders]:** *What are the optimization difficulties of balancing competing loss functions across tasks with unequal gradient magnitudes?*
  - **Methodology:** Analyzed task loss weight scheduling (classification cross-entropy vs. segmentation Dice loss) on lesions with diffuse, irregular borders.
  - **Answer & Findings:** Heuristic manual tuning of task loss weights is required; suboptimal weighting causes gradient conflict, leading to slight under-segmentation on faint lesion margins.

- **Datasets:** ISIC 2016 Benchmark, ISIC 2017 Challenge Dataset
- **Quantitative Results:** **Classification Accuracy:** 95.3% | **Sensitivity:** 94.1% | **Specificity:** 96.5% | **AUC:** 0.962 | **Segmentation Dice:** 91.4%
- **Open Research Questions / Gaps:**
  - *Can adaptive gradient balancing (e.g. GradNorm) automatically optimize multi-task loss weights dynamically during training?*
  - *Can joint learning be extended to simultaneous lesion segmentation, multi-class diagnosis, and visual question answering?*

---

### Paper 17: Melanoma Detection Using an Objective System Based on Multiple Connected Neural Networks
**Authors:** L. Ichim; D. Popescu  
**Venue:** *IEEE Access* (2020) | **DOI:** [10.1109/ACCESS.2020.3028248](https://doi.org/10.1109/ACCESS.2020.3028248) | **IEEE Article Number:** `9210626`  
**Category:** `Multiple Connected Neural Networks & Texture Fusion`  

> **Problem Formulation:** Subjectivity in visual dermatologist evaluations and limitations of single deep networks in capturing both global color distribution and localized micro-texture.

#### Formulated Research Questions & Findings:
- **RQ1 [Multi-Connected Neural Topology]:** *Can an objective diagnostic system based on Multiple Connected Neural Networks (MCNN) effectively fuse hand-crafted texture descriptors with deep CNN representations?*
  - **Methodology:** Developed an MCNN architecture integrating statistical color/texture features (GLCM, LBP in HSV/L*a*b* color spaces) with deep convolutional feature maps.
  - **Answer & Findings:** Yes. Fusing explicit textural descriptors with deep abstract representations achieved superior diagnostic accuracy of 96.7% and AUC of 0.978 on PH2.
- **RQ2 [Color Space Feature Engineering]:** *Which color space transformations (HSV, L*a*b*) provide the most discriminative textural representations for distinguishing melanoma from dysplastic nevi?*
  - **Methodology:** Extracted Gray-Level Co-occurrence Matrix (GLCM) and Local Binary Pattern (LBP) features across RGB, HSV, and L*a*b* channels, benchmarking feature importance.
  - **Answer & Findings:** L*a*b* and HSV color representations provided enhanced luminance-invariant color entropy and contrast metrics, substantially improving sensitivity to 95.8%.
- **RQ3 [Cross-Dataset Validation]:** *How consistently does the MCNN framework perform across independent clinical repositories (DermIS, DermQuest, and PH2)?*
  - **Methodology:** Validated the objective MCNN system across three distinct dermoscopic archives using sensitivity, specificity, and ROC analysis.
  - **Answer & Findings:** Demonstrated high cross-dataset consistency, yielding 97.4% specificity and 0.978 AUC on PH2 while maintaining >95% accuracy across DermIS and DermQuest.
- **RQ4 [Computational Complexity of Feature Pipelines]:** *What is the computational overhead of combining complex handcrafted feature extraction with multi-network deep learning inference?*
  - **Methodology:** Profiled CPU/GPU execution time for hand-crafted color-texture feature extraction vs. pure end-to-end deep inference.
  - **Answer & Findings:** Calculating GLCM and LBP descriptors across multiple color spaces introduces substantial CPU processing latency, creating a bottleneck for real-time mobile triage.

- **Datasets:** PH2 Dataset (200 images), DermIS Repository, DermQuest Archive
- **Quantitative Results:** **Accuracy (PH2):** 96.7% | **Sensitivity:** 95.8% | **Specificity:** 97.4% | **AUC:** 0.978
- **Open Research Questions / Gaps:**
  - *Can deep networks learn explicit GLCM and LBP textural filters end-to-end without separate feature computation?*
  - *How does the MCNN system perform on full 7-class imbalanced benchmarks like HAM10000?*

---

### Paper 18: DermCDSM: Clinical Decision Support Model for Dermatosis Using Systematic Approaches of Machine Learning and Deep Learning
**Authors:** R. Mittal; F. Jeribi; R. J. Martin; V. Malik; S. J. Menachery; J. Singh  
**Venue:** *IEEE Access* (2024) | **DOI:** [10.1109/ACCESS.2024.3373539](https://doi.org/10.1109/ACCESS.2024.3373539) | **IEEE Article Number:** `10459206`  
**Category:** `Clinical Decision Support & Spiking Neural Networks`  

> **Problem Formulation:** Lack of standardized clinical decision support frameworks capable of handling high-dimensional dermatosis features while maintaining ultra-low computational energy profiles.

#### Formulated Research Questions & Findings:
- **RQ1 [Decision Support Model Architecture]:** *Can a systematic Clinical Decision Support Model ('DermCDSM') combining machine learning, deep learning, and Spiking Neural Networks (SNN) achieve clinical-grade dermatosis diagnosis?*
  - **Methodology:** Constructed DermCDSM incorporating DullRazor artifact removal, contrast enhancement, bio-inspired feature selection, deep CNN feature extraction, and energy-efficient SNN classification.
  - **Answer & Findings:** Yes. DermCDSM achieved an impressive classification accuracy of 95.7% and an AUC of 0.981 across multi-class dermatological conditions.
- **RQ2 [Bio-Inspired Feature Optimization]:** *How effectively does bio-inspired heuristic feature selection eliminate redundant high-dimensional deep representations?*
  - **Methodology:** Applied nature-inspired metaheuristic search algorithms to prune uninformative feature vectors from intermediate CNN layer activations.
  - **Answer & Findings:** Bio-inspired feature selection reduced representation dimensionality by over 50% while improving overall classification sensitivity to 94.2% and specificity to 96.8%.
- **RQ3 [Multi-Benchmark Validation]:** *What precision, recall, and F1-scores are achieved by DermCDSM across HAM10000 and ISIC 2019 benchmarks?*
  - **Methodology:** Validated the systematic framework across 10,015 images of HAM10000 and the 8 classes of ISIC 2019.
  - **Answer & Findings:** Delivered an F1-score of 95.1% with robust diagnostic stability across inflammatory, viral, and malignant skin conditions.
- **RQ4 [Neuromorphic Hardware Emulation]:** *What deployment bottlenecks exist when executing Spiking Neural Networks on conventional von Neumann GPU hardware?*
  - **Methodology:** Analyzed computational latency and energy emulation overhead of spike-timing-dependent plasticity on standard GPUs vs. neuromorphic chips.
  - **Answer & Findings:** Simulating event-driven SNNs on standard synchronous GPUs introduces software overhead, requiring true neuromorphic silicon to realize the promised energy efficiency.

- **Datasets:** HAM10000 Benchmark, ISIC 2019 Challenge Dataset
- **Quantitative Results:** **Accuracy:** 95.7% | **Sensitivity:** 94.2% | **Specificity:** 96.8% | **F1-Score:** 95.1% | **AUC:** 0.981
- **Open Research Questions / Gaps:**
  - *What is the actual battery life improvement of DermCDSM when deployed on neuromorphic edge processors like Intel Loihi?*
  - *Can DermCDSM incorporate real-time patient electronic health record (EHR) data alongside image features?*

---

### Paper 19: A Hybrid Deep Learning Approach for Skin Cancer Classification Using Swin Transformer and Dense Group Shuffle Non-Local Attention Network
**Authors:** R. Karthik; R. Menaka; S. Atre; J. Cho; S. Veerappampalayam Easwaramoorthy  
**Venue:** *IEEE Access* (2024) | **DOI:** [10.1109/ACCESS.2024.3485507](https://doi.org/10.1109/ACCESS.2024.3485507) | **IEEE Article Number:** `10731679`  
**Category:** `Vision Transformers & Non-Local Attention`  

> **Problem Formulation:** Standard CNNs have restricted receptive fields that struggle with long-range spatial dependencies, while standard Vision Transformers impose heavy quadratic computational complexity on high-resolution images.

#### Formulated Research Questions & Findings:
- **RQ1 [Hybrid Transformer-Attention Architecture]:** *Can a hybrid framework combining Swin Transformer backbones with Dense Group Shuffle Non-Local Attention Networks (DGS-NLAN) capture long-range contextual relationships efficiently?*
  - **Methodology:** Constructed a hybrid architecture using Swin Transformer's shifted window self-attention for global contexts, coupled with DGS-NLAN for dense cross-group feature communication.
  - **Answer & Findings:** Yes. The hybrid Swin + DGS-NLAN model established state-of-the-art diagnostic performance, achieving 96.8% accuracy and 0.985 AUC on HAM10000.
- **RQ2 [Dense Group Shuffle Attention Mechanics]:** *How does dense group shuffle non-local attention reduce the quadratic computational bottleneck of global self-attention while maintaining dense feature interaction?*
  - **Methodology:** Divided feature channels into groups, applied non-local self-attention within groups, and shuffled channels across groups to enable global cross-talk at linear complexity.
  - **Answer & Findings:** Dense group shuffle enabled full receptive field coverage at a fraction of standard self-attention compute, boosting sensitivity to 95.4% and specificity to 97.6%.
- **RQ3 [Multi-Class Benchmark Verification]:** *What macro-averaged F1-score and precision are achieved by the hybrid transformer across the 7 classes of HAM10000 and ISIC 2019?*
  - **Methodology:** Conducted extensive 5-fold cross-validation across ISIC 2018/HAM10000 and ISIC 2019 using shifted window patch sizes of 4x4 and window sizes of 7x7.
  - **Answer & Findings:** Achieved a macro-averaged F1-score of 96.1% with balanced precision across all 7 pathological categories.
- **RQ4 [Memory Footprint & Data Hunger]:** *What are the GPU memory constraints and training data scale requirements of vision transformer backbones compared to standard CNNs?*
  - **Methodology:** Benchmarked training convergence rates, GPU VRAM consumption, and performance degradation under low-data regimes.
  - **Answer & Findings:** Swin Transformer requires substantial GPU VRAM during training and exhibits performance drops when trained on small datasets without extensive pre-training or aggressive augmentations.

- **Datasets:** ISIC 2018 / HAM10000 (10,015 images), ISIC 2019 Benchmark
- **Quantitative Results:** **Accuracy:** 96.8% | **Sensitivity:** 95.4% | **Specificity:** 97.6% | **F1-Score:** 96.1% | **AUC:** 0.985
- **Open Research Questions / Gaps:**
  - *Can parameter-efficient fine-tuning (e.g. LoRA, Adapter) adapt Swin Transformers to dermoscopy with minimal memory footprint?*
  - *How does the hybrid Swin model handle severe domain shift between dermoscopic images and clinical smartphone photos?*

---

### Paper 20: Analysis of Skin Marks Through the Use of Intelligent Things
**Authors:** D. Połap  
**Venue:** *IEEE Access* (2019) | **DOI:** [10.1109/ACCESS.2019.2947354](https://doi.org/10.1109/ACCESS.2019.2947354) | **IEEE Article Number:** `8868149`  
**Category:** `Internet of Medical Things (IoMT) & Edge CAD`  

> **Problem Formulation:** Cloud-based CAD systems require continuous high-bandwidth internet connectivity, raising critical patient privacy concerns and introducing network latency unsuitable for remote rural point-of-care screening.

#### Formulated Research Questions & Findings:
- **RQ1 [Distributed Edge IoMT Architecture]:** *Can an Internet of Medical Things (IoMT) framework execute decentralized skin mark screening directly on embedded edge sensors without relying on cloud infrastructure?*
  - **Methodology:** Designed a distributed intelligent sensor system using cascaded shallow CNNs, local edge heuristics, and lightweight morphological feature extractors.
  - **Answer & Findings:** Yes. Successfully deployed on embedded testbeds, processing skin mark imagery locally with an overall screening accuracy of 92.1%.
- **RQ2 [Edge Inference Latency & Resource Footprint]:** *Can lightweight convolutional classifiers achieve sub-100ms inference latency on low-power embedded processors suitable for handheld dermoscopes?*
  - **Methodology:** Profiled inference latency, RAM utilization, and power consumption on embedded microcomputing hardware processing cutaneous mark images.
  - **Answer & Findings:** Achieved inference latency under 85ms per image on edge hardware while maintaining low power consumption compatible with battery-powered mobile sensors.
- **RQ3 [Diagnostic Accuracy on Multi-Source Data]:** *What screening reliability is achieved across heterogeneous private clinical records and public benchmark subsets (PH2, ISIC)?*
  - **Methodology:** Evaluated the embedded framework across a combined corpus of private clinical recordings and benchmark subsets under varying capture angles.
  - **Answer & Findings:** Attained stable diagnostic accuracy of 92.1%, demonstrating reliable preliminary screening of abnormal cutaneous marks before specialist referral.
- **RQ4 [Edge Performance Trade-Offs]:** *How does the diagnostic accuracy of shallow edge models compare to multi-million parameter cloud architectures, and how does it handle variable lighting?*
  - **Methodology:** Comparative accuracy analysis between edge-constrained models and cloud deep networks under varying ambient lighting conditions.
  - **Answer & Findings:** Edge models show a 3-5% accuracy gap compared to heavy cloud ensembles, and are more vulnerable to uncontrolled ambient lighting shifts in handheld capture.

- **Datasets:** Private Clinical Skin Mark Dataset, PH2 Benchmark Subset, ISIC Archive Subset
- **Quantitative Results:** **Embedded Screening Accuracy:** 92.1% | **Inference Latency:** <85ms per image | **Deployment Target:** Embedded IoMT Edge Device
- **Open Research Questions / Gaps:**
  - *Can federated learning enable distributed IoMT edge devices to update diagnostic models collaboratively without transmitting private patient images?*
  - *How can on-chip optical calibration compensate for uncontrolled mobile ambient lighting automatically?*

---

### Paper 21: Early Detection of Multiclass Skin Lesions Using Transfer Learning-Based IncepX-Ensemble Model
**Authors:** S. Chatterjee; J. -M. Gil; Y. -C. Byun  
**Venue:** *IEEE Access* (2024) | **DOI:** [10.1109/ACCESS.2024.3432904](https://doi.org/10.1109/ACCESS.2024.3432904) | **IEEE Article Number:** `10608138`  
**Category:** `Multi-Scale Transfer Ensembles`  

> **Problem Formulation:** Single transfer learning models often overfit to specific spatial scales, failing to detect both microscopic localized lesions and broad diffuse malignant patches.

#### Formulated Research Questions & Findings:
- **RQ1 [Cross-Architectural Ensemble Innovation]:** *Does fusing multi-scale feature representations from Inception-v3 and Xception into a unified ensemble ('IncepX') improve early multi-class lesion detection?*
  - **Methodology:** Developed the IncepX-Ensemble architecture, combining Inception-v3's multi-scale inception modules with Xception's depthwise separable convolutions via dynamic weighted averaging.
  - **Answer & Findings:** Yes. IncepX achieved an exceptional overall classification accuracy of 95.8% on HAM10000, outperforming both standalone Inception-v3 and Xception.
- **RQ2 [Dynamic Weighted Decision Fusion]:** *How does dynamic confidence-weighted decision fusion improve classification over standard unweighted soft-voting?*
  - **Methodology:** Assigned dynamic weights to backbone predictions based on per-class validation confidence matrices rather than simple uniform averaging.
  - **Answer & Findings:** Dynamic weighting effectively suppressed confident mispredictions from individual backbones, boosting sensitivity to 94.1% and specificity to 97.2%.
- **RQ3 [Diagnostic Generalization & AUC]:** *What macro-averaged F1-score and ROC-AUC are achieved by IncepX across the 7 diagnostic categories of HAM10000?*
  - **Methodology:** Evaluated the ensemble across 10,015 dermoscopic images with adaptive normalization and geometric data augmentation.
  - **Answer & Findings:** Achieved a macro-averaged F1-score of 94.8% and an outstanding ROC-AUC of 0.978 across all 7 pathological categories.
- **RQ4 [Computational Overhead & Minority Ambiguity]:** *What is the inference latency overhead of running dual deep backbones, and how does IncepX perform on rare dermatofibroma cases?*
  - **Methodology:** Profiled inference runtime and per-class error distribution across minority classes.
  - **Answer & Findings:** Running dual deep backbones nearly doubles FLOP count and inference time, and moderate false-positive rates persist on rare minority categories like dermatofibroma.

- **Datasets:** ISIC 2018 / HAM10000 (10,015 images across 7 classes)
- **Quantitative Results:** **Accuracy:** 95.8% | **Sensitivity:** 94.1% | **Specificity:** 97.2% | **F1-Score:** 94.8% | **AUC:** 0.978
- **Open Research Questions / Gaps:**
  - *Can knowledge distillation compress the dual-backbone IncepX ensemble into a single lightweight MobileNet model?*
  - *How does IncepX perform on clinical photographic datasets containing dark skin phototypes (Fitzpatrick IV-VI)?*

---

### Paper 22: Classification for Dermoscopy Images Using Convolutional Neural Networks Based on the Ensemble of Individual Advantage and Group Decision
**Authors:** A. Gong; X. Yao; W. Lin  
**Venue:** *IEEE Access* (2020) | **DOI:** [10.1109/ACCESS.2020.3019210](https://doi.org/10.1109/ACCESS.2020.3019210) | **IEEE Article Number:** `9175002`  
**Category:** `Architectural Advantage Mining & Group Decision`  

> **Problem Formulation:** Individual deep learning models possess unique diagnostic strengths on specific lesion sub-types but suffer from blind spots on others, which uniform averaging ensembles fail to leverage.

#### Formulated Research Questions & Findings:
- **RQ1 [Individual Advantage Mining]:** *Can an ensemble strategy explicitly identify and exploit the individual class-specific advantages of distinct CNN backbones (ResNet, Inception, DenseNet) for superior group decision-making?*
  - **Methodology:** Constructed an ensemble framework that measures each model's class-specific diagnostic advantage on validation splits, assigning priority votes accordingly.
  - **Answer & Findings:** Yes. Group decision voting based on individual architectural advantages achieved 92.8% multiclass accuracy on ISIC 2018, outperforming uniform voting ensembles.
- **RQ2 [Multi-Model Diversity & Complementarity]:** *How do complementary feature representations from residual, inception, and densely connected architectures combine to reduce false-negative diagnostic errors?*
  - **Methodology:** Analyzed feature diversity and class-wise correlation matrices across ResNet, Inception, and DenseNet predictions.
  - **Answer & Findings:** Complementary feature extraction reduced false negatives on malignant melanoma, yielding an overall sensitivity of 91.5% and specificity of 94.3%.
- **RQ3 [Benchmark Performance on ISIC]:** *What ROC-AUC is attained by the individual advantage ensemble across the ISIC 2017 and ISIC 2018 challenge datasets?*
  - **Methodology:** Evaluated the group decision pipeline across ISIC 2017 and ISIC 2018 multi-class benchmarks.
  - **Answer & Findings:** Achieved a macro-averaged ROC-AUC of 0.956, validating consistent multi-class discrimination across benchmark years.
- **RQ4 [Ensemble Redundancy & Memory Overhead]:** *What is the memory and compute overhead of maintaining multiple full-scale deep backbones in a clinical production deployment?*
  - **Methodology:** Evaluated memory footprint and evaluated whether backbone feature maps contain redundant parameters.
  - **Answer & Findings:** Maintaining three distinct deep backbones substantially increases memory consumption and deployment complexity, with noticeable representation overlap across layers.

- **Datasets:** ISIC 2017 Challenge Dataset, ISIC 2018 Challenge Task 3
- **Quantitative Results:** **Accuracy:** 92.8% | **Sensitivity:** 91.5% | **Specificity:** 94.3% | **AUC:** 0.956
- **Open Research Questions / Gaps:**
  - *Can reinforcement learning dynamically select which single backbone to execute per image to avoid running all models concurrently?*
  - *How does individual advantage voting perform when expanding to 10+ rare dermatological categories?*

---

### Paper 23: Pipelined Structure in the Classification of Skin Lesions Based on Alexnet CNN and SVM Model With Bi-Sectional Texture Features
**Authors:** V. S. S. B. T. Sathvika; N. Anmisha; V. Thanmayi; M. Suchetha; D. E. Dhas; S. Sehastrajit; S. N. Aakur  
**Venue:** *IEEE Access* (2024) | **DOI:** [10.1109/ACCESS.2024.3387533](https://doi.org/10.1109/ACCESS.2024.3387533) | **IEEE Article Number:** `10496674`  
**Category:** `Hybrid Deep Features & Handcrafted Textures`  

> **Problem Formulation:** Deep features from standard CNNs often ignore geometric asymmetry and bi-sectional textural differences that dermatologists explicitly use in the ABCD criteria.

#### Formulated Research Questions & Findings:
- **RQ1 [Bi-Sectional Textural Modeling]:** *Does extracting bi-sectional textural features across divided lesion halves capture dermatological ABCD asymmetry more effectively than global image descriptors?*
  - **Methodology:** Partitioned lesions geometrically along principal axes and extracted bi-sectional Gray-Level Co-occurrence Matrix (GLCM) and statistical texture descriptors.
  - **Answer & Findings:** Yes. Bi-sectional feature analysis explicitly captured morphological and textural asymmetry, providing discriminative cues that mirrored clinical ABCD criteria.
- **RQ2 [Pipelined Deep Features + SVM Classification]:** *Can combining deep feature activations from an AlexNet CNN with bi-sectional handcrafted texture descriptors in a Support Vector Machine (SVM) classifier outperform end-to-end CNNs?*
  - **Methodology:** Extracted deep embeddings from pre-trained AlexNet, concatenated them with bi-sectional textural vectors, and trained an optimized SVM with RBF kernel.
  - **Answer & Findings:** The hybrid pipeline achieved a classification accuracy of 94.6%, sensitivity of 93.8%, and specificity of 95.2%, outperforming standalone AlexNet.
- **RQ3 [Diagnostic F1-Score & Robustness]:** *What diagnostic F1-score is attained by the pipelined AlexNet-SVM model on ISIC 2019 and HAM10000 benchmarks?*
  - **Methodology:** Validated the hybrid pipeline across benchmark subsets using stratified 10-fold cross-validation.
  - **Answer & Findings:** Achieved a balanced diagnostic F1-score of 94.1%, demonstrating stable discrimination between benign and malignant lesions.
- **RQ4 [Geometric Partitioning Limitations]:** *Under what topological conditions does geometric bi-sectional partitioning fail, and why does pipelined decoupling prevent end-to-end optimization?*
  - **Methodology:** Analyzed failure cases on highly irregular, non-convex, and multifocal skin lesions.
  - **Answer & Findings:** Fixed bi-sectional geometric partitioning fails on multi-lobed and non-convex lesions, and decoupling feature extraction from SVM training prevents end-to-end gradient updates.

- **Datasets:** ISIC 2019 Benchmark, HAM10000 Dataset Subsets
- **Quantitative Results:** **Accuracy:** 94.6% | **Sensitivity:** 93.8% | **Specificity:** 95.2% | **F1-Score:** 94.1%
- **Open Research Questions / Gaps:**
  - *Can differentiable geometric slicing layers enable end-to-end training of bi-sectional networks without separate SVM stages?*
  - *How does bi-sectional analysis perform on non-dermoscopic smartphone photos where lesion borders are ill-defined?*

---

### Paper 24: Improved Segmentation Model for Melanoma Lesion Detection Using Normalized Cross-Correlation-Based k-Means Clustering
**Authors:** M. I. Faizi; S. M. Adnan  
**Venue:** *IEEE Access* (2024) | **DOI:** [10.1109/ACCESS.2024.3360223](https://doi.org/10.1109/ACCESS.2024.3360223) | **IEEE Article Number:** `10416953`  
**Category:** `Lesion Segmentation & Normalized Cross-Correlation`  

> **Problem Formulation:** Standard clustering algorithms (standard k-means, Otsu) are easily corrupted by non-uniform skin pigmentation, lighting gradients, and hair artifacts during boundary segmentation.

#### Formulated Research Questions & Findings:
- **RQ1 [Algorithmic Clustering Innovation]:** *Can Normalized Cross-Correlation (NCC)-based k-means clustering improve the boundary segmentation accuracy of melanoma lesions over traditional unsupervised methods?*
  - **Methodology:** Formulated an improved k-means algorithm that uses Normalized Cross-Correlation as its similarity metric rather than standard Euclidean distance, matching template pigment distributions.
  - **Answer & Findings:** Yes. NCC-based k-means achieved an outstanding segmentation accuracy of 96.8% and a Dice coefficient of 93.4% on the PH2 benchmark.
- **RQ2 [Illumination & Hair Robustness]:** *How does NCC similarity mitigate sensitivity to spatial illumination gradients and fine hair occlusions in dermoscopic imagery?*
  - **Methodology:** Applied DullRazor artifact suppression followed by multi-channel NCC template matching across varying skin tone backgrounds.
  - **Answer & Findings:** NCC normalized local luminance variations, yielding an 87.9% Jaccard index and preventing cluster centers from drifting toward bright skin reflections.
- **RQ3 [Cross-Benchmark Segmentation Quality]:** *How consistently does the NCC k-means segmentation framework perform across ISIC 2017 and PH2 datasets?*
  - **Methodology:** Evaluated segmented masks against expert ground-truth annotations across ISIC 2017 and PH2 using Dice, Jaccard, and pixel accuracy.
  - **Answer & Findings:** Demonstrated consistent boundary delineation across datasets, outperforming standard k-means, Otsu thresholding, and baseline Chan-Vese active contours.
- **RQ4 [Computational Scalability of NCC]:** *What is the computational complexity of calculating normalized cross-correlation across high-resolution image pixels compared to standard Euclidean distance?*
  - **Methodology:** Profiled per-image iteration runtimes and convergence rates across variable image resolutions.
  - **Answer & Findings:** NCC calculation is computationally more intensive than Euclidean distance, increasing per-image segmentation latency on ultra-high-resolution dermoscopic images.

- **Datasets:** PH2 Benchmark (200 images), ISIC 2017 Segmentation Dataset
- **Quantitative Results:** **Segmentation Accuracy (PH2):** 96.8% | **Dice Coefficient:** 93.4% | **Jaccard Index:** 87.9%
- **Open Research Questions / Gaps:**
  - *Can GPU-accelerated FFTs speed up NCC template calculations for real-time mobile segmentation?*
  - *How does NCC k-means compare to modern deep transformer segmentation models like SegFormer?*

---

### Paper 25: Multiple Instance Learning Using 3D Features for Melanoma Detection
**Authors:** P. M. M. Pereira; L. A. Thomaz; L. M. N. Tavora; P. A. A. Assuncao; R. Fonseca-Pinto; R. P. Paiva; S. M. M. Faria  
**Venue:** *IEEE Access* (2022) | **DOI:** [10.1109/ACCESS.2022.3192444](https://doi.org/10.1109/ACCESS.2022.3192444) | **IEEE Article Number:** `9832874`  
**Category:** `3D Topography & Multiple Instance Learning`  

> **Problem Formulation:** Conventional 2D dermoscopy flattens 3D lesion elevation and surface texture, discarding critical palpable volumetric cues that dermatologists rely upon during physical clinical examination.

#### Formulated Research Questions & Findings:
- **RQ1 [3D Feature Reconstruction]:** *Can 3D surface elevation and roughness profiles reconstructed from photometric stereo dermoscopy provide discriminative diagnostic signals absent in conventional 2D imagery?*
  - **Methodology:** Reconstructed 3D surface height maps and surface normal vectors from multi-illumination photometric stereo dermoscopy, extracting 3D volumetric curvature features.
  - **Answer & Findings:** Yes. Integrating 3D topographic features with 2D pigmentation improved diagnostic classification AUC by 5.3% over 2D-only models, reaching an overall AUC of 0.942.
- **RQ2 [Multiple Instance Learning (MIL) Formulation]:** *How does Multiple Instance Learning (MIL) effectively aggregate local 3D surface patches into a patient-level melanoma diagnosis without requiring manual patch-level annotations?*
  - **Methodology:** Treated each lesion as a 'bag' of 3D surface patches, training an attention-based MIL pooling network to weight patches contributing to malignancy.
  - **Answer & Findings:** Attention MIL successfully localized suspicious elevated nodules and irregular margins, yielding 91.5% accuracy, 89.2% sensitivity, and 93.1% specificity.
- **RQ3 [2D vs. 3D Comparative Performance]:** *What is the quantitative diagnostic advantage of multimodal 2D+3D feature fusion over standard 2D dermoscopic baselines?*
  - **Methodology:** Conducted ablation experiments comparing 2D color models, 3D topographic models, and combined 2D+3D representations on clinical cohorts.
  - **Answer & Findings:** Combined 2D+3D models consistently outperformed unimodal 2D baselines, particularly in distinguishing elevated nodular melanoma from flat benign nevi.
- **RQ4 [Hardware Accessibility & Dataset Scale]:** *What hardware acquisition barriers restrict the clinical scalability of 3D photometric stereo dermoscopy?*
  - **Methodology:** Assessed clinical deployment requirements, imaging rig costs, calibration protocols, and dataset size constraints.
  - **Answer & Findings:** Photometric stereo requires specialized multi-light dermoscopic hardware that is not widely available in general practice, restricting public dataset sizes.

- **Datasets:** Multiview 3D Dermoscopy Clinical Dataset (Photometric Stereo Reconstructions)
- **Quantitative Results:** **Accuracy:** 91.5% | **Sensitivity:** 89.2% | **Specificity:** 93.1% | **AUC:** 0.942 | **AUC Improvement vs 2D:** +5.3%
- **Open Research Questions / Gaps:**
  - *Can single-image neural radiance fields (NeRF) or depth estimation networks synthesize 3D surface features from standard smartphone photos?*
  - *How does 3D surface modeling perform on ulcerated and bleeding malignant melanomas?*

---

### Paper 26: SPCB-Net: A Multi-Scale Skin Cancer Image Identification Network Using Self-Interactive Attention Pyramid and Cross-Layer Bilinear-Trilinear Pooling
**Authors:** X. Qian; T. Weng; Q. Han; C. Wu; H. Xu; M. Hou; Z. Qiu; B. Zhou; X. Gao  
**Venue:** *IEEE Access* (2024) | **DOI:** [10.1109/ACCESS.2023.3347424](https://doi.org/10.1109/ACCESS.2023.3347424) | **IEEE Article Number:** `10374026`  
**Category:** `Pyramid Attention & Higher-Order Pooling`  

> **Problem Formulation:** Fine-grained skin lesions exhibit severe scale variation, where crucial diagnostic features (pigment network, dots, globules) exist at microscopic resolutions while overall lesion asymmetry exists globally.

#### Formulated Research Questions & Findings:
- **RQ1 [Self-Interactive Attention Pyramid]:** *Can a Self-Interactive Attention Pyramid Network ('SPCB-Net') capture cross-scale feature correlations to resolve extreme scale variations in skin lesions?*
  - **Methodology:** Designed an attention pyramid that allows multi-scale feature maps to interact bidirectionally, exchanging high-level semantic context with low-level high-resolution textures.
  - **Answer & Findings:** Yes. SPCB-Net attained state-of-the-art identification accuracy of 95.6% across diverse lesion scales on ISIC 2018 and ISIC 2019.
- **RQ2 [Higher-Order Bilinear-Trilinear Pooling]:** *How does Cross-Layer Bilinear-Trilinear Pooling enhance fine-grained representation learning compared to standard first-order global average pooling?*
  - **Methodology:** Implemented bilinear and trilinear tensor pooling across pyramid layers to compute second- and third-order feature interactions.
  - **Answer & Findings:** Higher-order pooling captured subtle co-occurrences of pigment dots and atypical streaks, boosting sensitivity to 93.9%, specificity to 97.1%, and AUC to 0.982.
- **RQ3 [Multiclass Benchmark Generalization]:** *What macro-averaged F1-score is delivered by SPCB-Net across HAM10000 and ISIC 2019 challenge datasets?*
  - **Methodology:** Evaluated the multi-scale higher-order network across 7-class and 8-class benchmarks with standard augmentation pipelines.
  - **Answer & Findings:** Delivered an overall macro-averaged F1-score of 94.7%, maintaining robust discrimination across both macroscopic and microscopic lesion types.
- **RQ4 [Tensor Dimensionality & Compute Cost]:** *What is the memory and FLOP complexity overhead of calculating trilinear feature interactions during high-resolution training?*
  - **Methodology:** Benchmarked tensor dimension expansion, backpropagation memory consumption, and training epoch runtimes.
  - **Answer & Findings:** Trilinear pooling generates high-dimensional intermediate tensors that significantly increase GPU memory consumption and training time, requiring dimensional reduction heuristics.

- **Datasets:** ISIC 2018 Challenge Task 3, ISIC 2019 Benchmark, HAM10000
- **Quantitative Results:** **Accuracy:** 95.6% | **Sensitivity:** 93.9% | **Specificity:** 97.1% | **F1-Score:** 94.7% | **AUC:** 0.982
- **Open Research Questions / Gaps:**
  - *Can factorized low-rank tensor decompositions approximate trilinear pooling to reduce memory footprint on edge devices?*
  - *How does SPCB-Net perform on high-resolution whole-slide dermatopathology imagery?*

---

### Paper 27: IARS SegNet: Interpretable Attention Residual Skip Connection SegNet for Melanoma Segmentation
**Authors:** V. S. Narayanan; O. K. Sikha; R. Benitez  
**Venue:** *IEEE Access* (2024) | **DOI:** [10.1109/ACCESS.2024.3404224](https://doi.org/10.1109/ACCESS.2024.3404224) | **IEEE Article Number:** `10536875`  
**Category:** `Interpretable Semantic Segmentation & Attention Skips`  

> **Problem Formulation:** Standard SegNet and U-Net architectures propagate irrelevant background skin features through skip connections, creating noisy boundaries in melanoma segmentation.

#### Formulated Research Questions & Findings:
- **RQ1 [Attention Residual Skip Connections]:** *Can embedding Interpretable Attention gates within Residual Skip Connections ('IARS SegNet') filter out background skin noise while retaining precise lesion boundary contours?*
  - **Methodology:** Engineered attention gates on residual skip connections that dynamically compute spatial attention coefficients to suppress activations from healthy tissue while passing lesion margin features.
  - **Answer & Findings:** Yes. IARS SegNet achieved state-of-the-art segmentation accuracy of 97.1%, Dice coefficient of 94.2%, and Jaccard index of 89.1% across multiple benchmarks.
- **RQ2 [Segmentation Visual Explainability]:** *Do the intermediate attention maps generated by IARS SegNet provide transparent, visually verifiable explanations of boundary delineation for clinical practitioners?*
  - **Methodology:** Extracted and visualized attention coefficient heatmaps across multi-resolution encoder-decoder stages on difficult lesion borders.
  - **Answer & Findings:** The attention coefficient heatmaps cleanly localized atypical pigment reticulations and fuzzy borders, providing visual auditability for dermatologists.
- **RQ3 [Multi-Repository Validation]:** *How consistently does IARS SegNet perform across disparate benchmark archives (ISIC 2017, ISIC 2018, and PH2)?*
  - **Methodology:** Benchmarked segmentation across three public datasets under identical training schedules and loss criteria.
  - **Answer & Findings:** Demonstrated exceptional consistency across datasets, outperforming standard U-Net, baseline SegNet, and DeepLabV3+ in boundary precision and Dice score.
- **RQ4 [Micro-Structure Edge Errors]:** *What are the segmentation limitations of IARS SegNet when segmenting lesions with extremely faint, non-pigmented, or amelanotic margins?*
  - **Methodology:** Error analysis on low-contrast amelanotic melanomas and lesions with ultra-fine peripheral reticulations.
  - **Answer & Findings:** Slight boundary under-segmentation occurs on faint amelanotic lesion borders where chromatic contrast between lesion and healthy skin is minimal.

- **Datasets:** ISIC 2017, ISIC 2018, PH2 Benchmark (200 images)
- **Quantitative Results:** **Pixel Segmentation Accuracy:** 97.1% | **Dice Coefficient:** 94.2% | **Jaccard Index:** 89.1%
- **Open Research Questions / Gaps:**
  - *Can IARS SegNet be adapted to perform multi-organ medical image segmentation (e.g. skin, lung, retina)?*
  - *Can boundary-weighted loss functions eliminate under-segmentation on amelanotic melanomas?*

---

### Paper 28: Toward Better Ear Disease Diagnosis: A Multi-Modal Multi-Fusion Model Using Endoscopic Images of the Tympanic Membrane and Pure-Tone Audiometry
**Authors:** T. Kim; S. Kim; J. Kim; Y. Lee; J. Choi  
**Venue:** *IEEE Access* (2023) | **DOI:** [10.1109/ACCESS.2023.3325346](https://doi.org/10.1109/ACCESS.2023.3325346) | **IEEE Article Number:** `10286540`  
**Category:** `Cross-Modal Clinical Fusion & Multi-Fusion Networks`  

> **Problem Formulation:** Medical diagnoses based purely on visual inspection often miss functional physiological deficits, while numeric functional tests lack anatomical localization.

#### Formulated Research Questions & Findings:
- **RQ1 [Multimodal Multi-Fusion Architecture]:** *Can a multimodal multi-fusion deep learning framework combining high-resolution visual imagery with quantitative clinical functional data achieve superior diagnostic accuracy over unimodal baselines?*
  - **Methodology:** Developed a dual-branch network fusing endoscopic photographic features with Pure-Tone Audiometry (PTA) clinical numeric test curves via intermediate cross-modal attention fusion.
  - **Answer & Findings:** Yes. Multimodal fusion achieved 94.8% diagnostic accuracy, dramatically outperforming image-only (88.3%) and clinical numeric-only (82.1%) unimodal models.
- **RQ2 [Cross-Modal Attention Mechanics]:** *How does cross-modal attention fusion align heterogeneous visual features (color, tympanic membrane perforations) with continuous numeric curves (frequency-specific hearing thresholds)?*
  - **Methodology:** Projected visual tokens and audiometric vectors into a shared embedding space, computing cross-attention affinity matrices to modulate feature weights.
  - **Answer & Findings:** Cross-modal attention enabled the network to correlate visual anatomical defects with corresponding functional hearing loss thresholds, boosting sensitivity to 93.6% and specificity to 95.7%.
- **RQ3 [Diagnostic Robustness on Multi-Category CAD]:** *What is the multi-category diagnostic performance across inflammatory, structural, and normal ear pathology categories?*
  - **Methodology:** Validated the framework across 2,420 clinical cases covering normal, otitis media, tympanic perforation, and cholesteatoma.
  - **Answer & Findings:** Attained an overall AUC of 0.972, providing an objective, high-accuracy decision support benchmark for specialized clinical examinations.
- **RQ4 [Missing Modality Vulnerability]:** *How severely does the multimodal model degrade when one clinical modality (e.g., audiometry or clear imaging) is missing or corrupted at test time?*
  - **Methodology:** Simulated missing modality scenarios during test-time inference and evaluated drop in classification accuracy.
  - **Answer & Findings:** The model requires complete paired visual and audiometric records at inference time; accuracy drops significantly if numeric test data is absent without imputation modules.

- **Datasets:** Clinical Paired Cohort (2,420 cases: Endoscopic Imagery + Pure-Tone Audiometry)
- **Quantitative Results:** **Multimodal Accuracy:** 94.8% | **Image-Only Baseline:** 88.3% | **Audiometry Baseline:** 82.1% | **Sensitivity:** 93.6% | **Specificity:** 95.7% | **AUC:** 0.972
- **Open Research Questions / Gaps:**
  - *How can cross-modal generative imputation reconstruct missing clinical modalities when only photographs are available?*
  - *Can this multi-fusion paradigm be directly applied to skin cancer by fusing dermoscopy with patient genetics and dermato-pathology panels?*

---

### Paper 29: Classification of Skin Lesion With Features Extraction Using Quantum Chebyshev Polynomials and Autoencoder From Wavelet-Transformed Images
**Authors:** Farhatullah; X. Chen; D. Zeng; J. Xu; R. Nawaz; R. Ullah  
**Venue:** *IEEE Access* (2024) | **DOI:** [10.1109/ACCESS.2024.3502513](https://doi.org/10.1109/ACCESS.2024.3502513) | **IEEE Article Number:** `10757392`  
**Category:** `Quantum Orthogonal Polynomials & Wavelet Autoencoders`  

> **Problem Formulation:** Conventional CNNs struggle to separate overlapping non-stationary texture frequencies in complex dermoscopic lesions, resulting in high false-positive rates.

#### Formulated Research Questions & Findings:
- **RQ1 [Quantum Orthogonal Feature Extraction]:** *Can Quantum Chebyshev Polynomials (QCP) extracted from wavelet-transformed dermoscopic images capture non-stationary multi-frequency lesion features more effectively than spatial convolutions?*
  - **Methodology:** Applied Discrete Wavelet Transform (DWT) to decompose images into sub-bands, extracted mathematical feature representations using Quantum Chebyshev Polynomials, and compressed features via an autoencoder.
  - **Answer & Findings:** Yes. Quantum Chebyshev feature extraction captured subtle high-frequency spatial transitions and color variances, delivering a classification accuracy of 96.2% on HAM10000.
- **RQ2 [Autoencoder Compression & Sequential Classification]:** *Does integrating autoencoder dimensionality reduction with Bidirectional LSTM (Bi-LSTM) classification preserve critical quantum feature representations while preventing overfitting?*
  - **Methodology:** Compressed high-dimensional quantum polynomial descriptors through a deep autoencoder and fed sequential feature representations to a Bi-LSTM network.
  - **Answer & Findings:** The Autoencoder + Bi-LSTM pipeline eliminated redundant coefficients, yielding a sensitivity of 94.8%, specificity of 97.1%, and an F1-score of 95.5%.
- **RQ3 [ROC-AUC Across Benchmarks]:** *What overall diagnostic discrimination (ROC-AUC) is achieved across ISIC 2019 and HAM10000 datasets?*
  - **Methodology:** Evaluated the framework across 5-fold cross-validation on multi-class dermoscopic benchmarks.
  - **Answer & Findings:** Achieved an outstanding ROC-AUC of 0.980, significantly outperforming standard spatial CNNs and conventional wavelet moments.
- **RQ4 [Mathematical Complexity & Compute Footprint]:** *What is the computational and memory footprint of calculating quantum polynomial transforms across high-resolution image datasets?*
  - **Methodology:** Profiled mathematical transformation overhead, matrix computation time, and training latency across image batch sizes.
  - **Answer & Findings:** Calculating quantum orthogonal polynomials is mathematically intensive and difficult to parallelize on conventional GPU shaders compared to standard 2D convolutions.

- **Datasets:** HAM10000, ISIC 2019 Challenge Dataset
- **Quantitative Results:** **Accuracy:** 96.2% | **Sensitivity:** 94.8% | **Specificity:** 97.1% | **F1-Score:** 95.5% | **AUC:** 0.980
- **Open Research Questions / Gaps:**
  - *Can Quantum Chebyshev Polynomial calculations be natively implemented on emerging quantum computing hardware or quantum simulators?*
  - *How does the wavelet-quantum pipeline perform on clinical smartphone photographs with compression artifacts?*

---

### Paper 30: Integrating Clinical Knowledge Graphs and Gradient-Based Neural Systems for Enhanced Melanoma Diagnosis via the Seven-Point Checklist
**Authors:** Y. Wang; T. Yu; J. Cai; S. Kalia; H. Lui; Z. Jane Wang; T. K. Lee  
**Venue:** *IEEE Transactions on Neural Networks and Learning Systems* (2026) | **DOI:** [10.1109/TNNLS.2025.3600443](https://doi.org/10.1109/TNNLS.2025.3600443) | **IEEE Article Number:** `11151232`  
**Category:** `Neuro-Symbolic AI & Clinical Knowledge Graphs`  

> **Problem Formulation:** Pure data-driven deep networks lack clinical reasoning principles, often relying on spurious correlation rather than the dermatological Seven-Point Checklist criteria used by physicians.

#### Formulated Research Questions & Findings:
- **RQ1 [Neuro-Symbolic Integration]:** *Can integrating a structured clinical Knowledge Graph (KG) representing the dermatological Seven-Point Checklist with gradient-based neural networks enforce clinically valid reasoning?*
  - **Methodology:** Constructed a clinical Knowledge Graph encoding the 7-Point Checklist (atypical pigment network, blue-whitish veil, vascular structures, etc.) and integrated it with deep CNN embeddings via graph neural reasoning.
  - **Answer & Findings:** Yes. Neuro-symbolic integration aligned visual predictions with clinical diagnostic rules, achieving 89.4% multi-criteria diagnosis accuracy and full clinical auditability.
- **RQ2 [Symbolic Explainability & Checklist Verification]:** *How does knowledge graph reasoning provide dermatologists with verifiable symbolic audit trails compared to heuristic post-hoc heatmaps?*
  - **Methodology:** Evaluated the model's explicit score output across major and minor 7-point criteria against board-certified dermatologist clinical ratings.
  - **Answer & Findings:** The system generated explicit criterion-by-criterion justification scores matching dermatological diagnostic guidelines, attaining 88.1% sensitivity and 91.3% specificity on melanoma.
- **RQ3 [Diagnostic Performance on Derm7pt]:** *What overall diagnostic discrimination (ROC-AUC) is achieved on the standardized Derm7pt benchmark repository?*
  - **Methodology:** Trained and evaluated the neuro-symbolic framework on the Derm7pt dataset (1,011 clinical and dermoscopic cases with verified checklist annotations).
  - **Answer & Findings:** Achieved a ROC-AUC of 0.935 for melanoma detection, matching specialist dermatologist consensus while maintaining transparent symbolic justifications.
- **RQ4 [Annotation Scarcity for Structured Graphs]:** *What are the barriers to scaling knowledge-graph-driven models to massive unannotated web-scale medical archives?*
  - **Methodology:** Assessed the scarcity of granular 7-point checklist annotations in public datasets like ISIC 2020-2024.
  - **Answer & Findings:** The framework strictly relies on granular checklist annotations which are absent in 95% of public dermoscopic databases, creating an annotation bottleneck for scaling.

- **Datasets:** Derm7pt Benchmark (1,011 clinical and dermoscopic cases with 7-point checklist labels)
- **Quantitative Results:** **Multi-Criteria Diagnostic Accuracy:** 89.4% | **Melanoma Sensitivity:** 88.1% | **Specificity:** 91.3% | **AUC:** 0.935
- **Open Research Questions / Gaps:**
  - *Can Vision-Language Foundation Models automatically extract 7-point checklist annotations from clinical notes to expand training data?*
  - *How does neuro-symbolic reasoning behave when clinical criteria provide contradictory evidence?*

---

### Paper 31: A Hybrid Model for Early Melanoma Detection: Integrating YOLOv9 and Faster R-CNN for Enhanced Diagnostic Accuracy
**Authors:** M. I. Marie; M. S. Elredeny; A. Essayed Yakoub  
**Venue:** *IEEE Access* (2025) | **DOI:** [10.1109/ACCESS.2025.3587625](https://doi.org/10.1109/ACCESS.2025.3587625) | **IEEE Article Number:** `11077147`  
**Category:** `Hybrid Object Detection & Anchor-Free Architectures`  

> **Problem Formulation:** Standard classification CNNs evaluate images globally without precise spatial bounding, leading to misclassification when lesions occupy only a small fraction of the image frame.

#### Formulated Research Questions & Findings:
- **RQ1 [Dual-Detector Hybrid Innovation]:** *Does integrating YOLOv9 (real-time anchor-free detection) with Faster R-CNN (two-stage region proposal) improve melanoma localization and diagnostic accuracy over standalone classifiers?*
  - **Methodology:** Built a hybrid dual-detector framework combining YOLOv9's Programmable Gradient Information (PGI) with Faster R-CNN's region proposal network via an IoU-weighted ensemble fusion.
  - **Answer & Findings:** Yes. The hybrid detector achieved an exceptional detection mAP@0.5 of 96.5% and an overall classification accuracy of 95.8% on ISIC benchmarks.
- **RQ2 [Programmable Gradient Information (PGI)]:** *How does YOLOv9's Programmable Gradient Information prevent deep feature loss across multi-scale lesion proposals in high-resolution dermoscopy?*
  - **Methodology:** Leveraged PGI auxiliary reversible branches to maintain complete input information flow to deep layers during bounding-box regression.
  - **Answer & Findings:** PGI preserved fine-grained boundary gradient signals, yielding 94.6% sensitivity and 96.9% specificity in early-stage malignant melanoma detection.
- **RQ3 [Localization-Classification Coupling]:** *What is the diagnostic advantage of simultaneous lesion localization (bounding box) and malignancy classification over decoupled two-stage pipelines?*
  - **Methodology:** Evaluated detection accuracy on small, early-stage melanomas (<5mm diameter) embedded in wide-field dermatological imagery.
  - **Answer & Findings:** Simultaneous localization and classification eliminated background skin interference, achieving superior early-stage detection reliability on ISIC 2020.
- **RQ4 [Inference Latency & Dual-Detector Overhead]:** *What is the computational latency and memory cost of running dual object detection backbones in parallel during real-time clinical screening?*
  - **Methodology:** Profiled inference frames per second (FPS), GPU VRAM consumption, and FLOP count of the dual YOLOv9 + Faster R-CNN architecture.
  - **Answer & Findings:** Concurrent execution of two full object detection models substantially increases computational latency, dropping FPS and requiring high-performance GPUs for real-time operation.

- **Datasets:** ISIC 2020 Challenge Benchmark, HAM10000 Dataset
- **Quantitative Results:** **Detection mAP@0.5:** 96.5% | **Classification Accuracy:** 95.8% | **Sensitivity:** 94.6% | **Specificity:** 96.9%
- **Open Research Questions / Gaps:**
  - *Can knowledge distillation compress Faster R-CNN's two-stage proposals into YOLOv9's one-stage head for sub-20ms mobile execution?*
  - *How does the hybrid detector perform on full-body mole mapping photography with dozens of simultaneous lesions?*

---

### Paper 32: Automated Skin Cancer Report Generation via a Knowledge-Distilled Vision-Language Model
**Authors:** L. Chakrabarti; B. Zhang; H. Tian; A. Vakanski; M. Xian  
**Venue:** *IEEE Access* (2025) | **DOI:** [10.1109/ACCESS.2025.3591750](https://doi.org/10.1109/ACCESS.2025.3591750) | **IEEE Article Number:** `11091320`  
**Category:** `Vision-Language Models & Automated Report Generation`  

> **Problem Formulation:** Traditional CAD systems output simple numeric probabilities or class labels, failing to provide the detailed clinical narrative and descriptive diagnostic report required by oncologists.

#### Formulated Research Questions & Findings:
- **RQ1 [Knowledge-Distilled VLM Architecture]:** *Can a compact, knowledge-distilled Vision-Language Model (VLM) generate clinically accurate, structured dermatological diagnostic reports from dermoscopic images without requiring massive foundation models?*
  - **Methodology:** Distilled knowledge from large-scale multi-modal foundation models into a parameter-efficient student VLM conditioned on dermatological vocabulary and clinical report templates.
  - **Answer & Findings:** Yes. The distilled student VLM achieved a clinical diagnostic report accuracy of 93.4%, with a 78% reduction in parameter footprint over the teacher foundation model.
- **RQ2 [Natural Language Evaluation & Faithfulness]:** *What linguistic generation quality (BLEU, ROUGE-L) and clinical factuality does the distilled VLM achieve on paired dermoscopic reporting benchmarks?*
  - **Methodology:** Evaluated generated reports against board-certified dermatologist text reports using BLEU-4, ROUGE-L, and expert clinical factuality scoring.
  - **Answer & Findings:** Achieved a BLEU-4 score of 0.428 and ROUGE-L of 0.582, demonstrating high linguistic coherence and accurate description of lesion borders, colors, and structural patterns.
- **RQ3 [Retrieval-Augmented Generation (RAG) Synergy]:** *Does integrating Retrieval-Augmented Generation (RAG) with clinical knowledge bases suppress factual medical hallucinations in generative report models?*
  - **Methodology:** Coupled the student VLM with a dermatological text retrieval index that fetches relevant clinical guidelines based on visual embeddings before text generation.
  - **Answer & Findings:** RAG integration reduced medical hallucinations by over 40%, ensuring that diagnostic descriptions adhered strictly to clinical dermatological lexicons.
- **RQ4 [Rare Pathological Edge Cases]:** *What are the limitations of generative VLMs when generating reports for ultra-rare skin diseases poorly represented in clinical text-image corpora?*
  - **Methodology:** Error analysis of generated reports on rare dermatological malignancies (Merkel cell carcinoma, amelanotic melanoma).
  - **Answer & Findings:** Generative VLMs exhibit degradation on rare conditions, occasionally generating generic descriptive statements rather than precise diagnostic criteria.

- **Datasets:** Skin-VQA Paired Reporting Dataset, ISIC Clinical Reporting Cohort
- **Quantitative Results:** **Clinical Reporting Accuracy:** 93.4% | **BLEU-4:** 0.428 | **ROUGE-L:** 0.582 | **Parameter Footprint Reduction:** 78%
- **Open Research Questions / Gaps:**
  - *How can generative medical VLMs be formally verified to guarantee zero safety-critical diagnostic omissions?*
  - *Can conversational multi-turn VLMs interactively answer follow-up questions from referring general practitioners?*

---

### Paper 33: Multi-Scale DCNN with Dynamic Weight and Part Cross-Entropy Loss for Skin Lesion Diagnosis
**Authors:** G. Wang; L. Liu; F. Lauri; A. H. E. Hassani  
**Venue:** *Big Data Mining and Analytics* (2024) | **DOI:** [10.26599/BDMA.2024.9020038](https://doi.org/10.26599/BDMA.2024.9020038) | **IEEE Article Number:** `10778156`  
**Category:** `Multi-Scale CNNs & Dynamic Loss Weighting`  

> **Problem Formulation:** Uniform loss functions treat the entire lesion image homogeneously, allowing dominant background features to drown out localized, subtle malignant sub-regions.

#### Formulated Research Questions & Findings:
- **RQ1 [Part Cross-Entropy Loss Innovation]:** *Can a Part Cross-Entropy Loss (P-CEL) combined with dynamic loss weighting force deep networks to attend to fine-grained sub-regions of skin lesions?*
  - **Methodology:** Formulated Part Cross-Entropy Loss to divide lesion feature maps into regional sub-parts, applying dynamic loss weighting to emphasize hard-to-classify sub-regions during backpropagation.
  - **Answer & Findings:** Yes. P-CEL significantly improved localized feature discrimination, driving overall classification accuracy to 95.1% on ISIC benchmarks.
- **RQ2 [Dynamic Weight Scheduling]:** *How does dynamic weight adaptation balance global lesion context with local part representations across training epochs?*
  - **Methodology:** Implemented an adaptive loss scheduling mechanism that dynamically adjusts part-level versus global loss weights based on per-part gradient variance.
  - **Answer & Findings:** Dynamic weighting prevented gradient starvation in subtle lesion parts, achieving 93.6% sensitivity, 96.3% specificity, and an overall ROC-AUC of 0.976.
- **RQ3 [Benchmark Generalization on ISIC]:** *What multi-class diagnostic performance is attained across ISIC 2018 and ISIC 2019 challenge datasets?*
  - **Methodology:** Evaluated the multi-scale DCNN framework across multi-class benchmarks with standard geometric augmentations.
  - **Answer & Findings:** Consistently outperformed standard cross-entropy baselines by 3.2% accuracy on ISIC 2018 and maintained robust discrimination across all 8 classes of ISIC 2019.
- **RQ4 [Non-Convex Lesion Topologies]:** *Under what structural conditions does fixed part partitioning fail on irregular, multi-centric, or highly asymmetrical skin lesions?*
  - **Methodology:** Analyzed classification failure cases on lesions with dispersed satellite lesions and extreme aspect ratios.
  - **Answer & Findings:** Fixed rectangular part partitioning degrades when applied to non-convex, highly irregular lesions where background skin dominates specific partition grids.

- **Datasets:** ISIC 2018 Challenge Task 3, ISIC 2019 Benchmark Dataset
- **Quantitative Results:** **Accuracy:** 95.1% | **Sensitivity:** 93.6% | **Specificity:** 96.3% | **AUC:** 0.976 | **Gain over Cross-Entropy:** +3.2%
- **Open Research Questions / Gaps:**
  - *Can deformable part models or attention-guided part discovery replace fixed spatial grids for non-convex lesions?*
  - *How does Part Cross-Entropy Loss interact with Vision Transformer patch tokens?*

---

### Paper 34: Skin Lesion Segmentation in Clinical Images Using Nonnegative Matrix Factorization and Mutual Information
**Authors:** E. Soares Flores; J. Scharcanski  
**Venue:** *IEEE Access* (2025) | **DOI:** [10.1109/ACCESS.2025.3584305](https://doi.org/10.1109/ACCESS.2025.3584305) | **IEEE Article Number:** `11058930`  
**Category:** `Unsupervised Matrix Factorization & Graph Cuts`  

> **Problem Formulation:** Deep supervised segmentation models fail to generalize to non-dermoscopic clinical images due to domain shift in lighting, skin color, and camera sensor calibration.

#### Formulated Research Questions & Findings:
- **RQ1 [Unsupervised Matrix Factorization]:** *Can Nonnegative Matrix Factorization (NMF) combined with Mutual Information (MI) segment skin lesions in clinical photography without requiring large annotated training datasets?*
  - **Methodology:** Decomposed multi-channel clinical skin photos into spectral basis vectors and abundance maps via NMF, followed by Mutual Information graph-cut energy minimization to isolate borders.
  - **Answer & Findings:** Yes. Unsupervised NMF + MI achieved 94.6% pixel segmentation accuracy, 89.8% Dice coefficient, and 82.5% Jaccard index on clinical photographic benchmarks.
- **RQ2 [Clinical Photography Domain Robustness]:** *How does unsupervised NMF segmentation compare to deep supervised networks (U-Net, SegNet, DSNet) when subjected to severe clinical illumination shifts?*
  - **Methodology:** Benchmarked NMF against state-of-the-art supervised deep networks on Dermofit and clinical out-of-distribution smartphone datasets with variable illumination.
  - **Answer & Findings:** NMF proved far more robust than supervised deep models under severe out-of-distribution lighting shifts, maintaining stable boundary isolation without retraining.
- **RQ3 [Mutual Information Boundary Delineation]:** *What is the role of Mutual Information in refining lesion boundaries across multi-spectral abundance maps?*
  - **Methodology:** Evaluated graph-cut segmentation energy functions with and without Mutual Information boundary constraints.
  - **Answer & Findings:** Mutual Information effectively captured non-linear statistical dependencies between lesion pigments and surrounding skin, preventing boundary leakage.
- **RQ4 [Iterative Factorization Latency]:** *What is the computational execution time of iterative nonnegative matrix factorization compared to feedforward deep neural inference?*
  - **Methodology:** Profiled per-image optimization runtimes across variable image resolutions and matrix factorization rank dimensions.
  - **Answer & Findings:** Iterative optimization requires several seconds per high-resolution image, making NMF slower than feedforward deep convolutional passes during rapid clinical screening.

- **Datasets:** Dermofit Clinical Photography Dataset, ISIC Clinical Photographic Benchmark Subsets
- **Quantitative Results:** **Pixel Segmentation Accuracy:** 94.6% | **Dice Coefficient:** 89.8% | **Jaccard Index:** 82.5%
- **Open Research Questions / Gaps:**
  - *Can deep unfolding networks accelerate iterative NMF optimization to achieve millisecond-level inference?*
  - *Can NMF basis components provide direct interpretable biological chromophore concentrations (melanin, hemoglobin)?*

---

### Paper 35: A Transparent Search-Based Framework for Skin and Breast Cancer Diagnosis Using Siamese Networks
**Authors:** Z. Tabatabaei; A. Colomer; J. O. Moll; V. Naranjo  
**Venue:** *IEEE Access* (2025) | **DOI:** [10.1109/ACCESS.2025.3628157](https://doi.org/10.1109/ACCESS.2025.3628157) | **IEEE Article Number:** `11224374`  
**Category:** `Siamese Metric Retrieval & Explainable Diagnosis`  

> **Problem Formulation:** Ambiguous melanocytic lesions (e.g. Spitzoid neoplasms) often cannot be definitively classified by binary labels alone, requiring dermatologists to review visually and histologically similar confirmed cases.

#### Formulated Research Questions & Findings:
- **RQ1 [Content-Based Twin Retrieval]:** *Can a Siamese Neural Network framework for Content-Based Image Retrieval (CBIR) provide transparent diagnostic decision support by retrieving visually and pathologically verified 'twin' cases?*
  - **Methodology:** Trained a Siamese architecture with contrastive metric loss to map dermoscopic and histopathological images into an embedding space where pathologically identical tumors cluster together.
  - **Answer & Findings:** Yes. The framework achieved a Top-5 retrieval precision of 94.2% and classification accuracy of 93.8%, retrieving verifiable twin cases with known histological outcomes.
- **RQ2 [Contrastive Metric Learning Space]:** *How effectively does contrastive metric learning separate borderline Spitzoid tumors from malignant melanomas compared to standard softmax classifiers?*
  - **Methodology:** Analyzed t-SNE projections of learned Siamese metric embeddings on ambiguous Spitzoid tumors, conventional nevi, and melanomas.
  - **Answer & Findings:** Contrastive metric learning formed clear semantic sub-clusters for borderline cases, avoiding the overconfident misclassifications typical of standard softmax heads.
- **RQ3 [Cross-Organ Generalization]:** *Does the transparent search-based Siamese retrieval framework generalize across diverse oncology domains (skin cancer and breast cancer)?*
  - **Methodology:** Evaluated identical Siamese metric learning pipelines on dermoscopic melanoma datasets and histopathological breast cancer archives.
  - **Answer & Findings:** Demonstrated robust cross-domain generalizability, achieving high retrieval fidelity and diagnostic concordance across both dermatological and breast cancer benchmarks.
- **RQ4 [Large-Scale Retrieval Scalability]:** *What is the search latency overhead of querying massive multi-thousand case clinical repositories during point-of-care consultations?*
  - **Methodology:** Benchmarked exact nearest-neighbor search latency against approximate indexing algorithms (FAISS, HNSW) across scaling database sizes.
  - **Answer & Findings:** Exact nearest-neighbor search scales linearly with repository size, requiring approximate nearest-neighbor indexing (e.g., HNSW) to maintain sub-second retrieval in massive archives.

- **Datasets:** Clinical Spitzoid Neoplasm Cohort, ISIC Melanoma Benchmark, Breast Cancer Histopathology Archive
- **Quantitative Results:** **Top-5 Retrieval Precision:** 94.2% | **Diagnostic Accuracy:** 93.8% | **Multi-Organ Compatibility:** Validated on Skin & Breast Cancer
- **Open Research Questions / Gaps:**
  - *Can generative text models automatically synthesize a comparative clinical summary contrasting the query image with retrieved twin cases?*
  - *How does the retrieval system handle domain shift when query images are captured using different dermatoscope optical models?*

---

### Paper 36: FoMoSkinNet: A Dual-Stream Deep Learning Model for Early Detection and Classification of Non-Dermoscopic Skin Lesions via Focal Modulation and Local Feature Integration
**Authors:** F. Bibi; Q. Abbas; S. M. Naqi  
**Venue:** *IEEE Access* (2026) | **DOI:** [10.1109/ACCESS.2026.3674219](https://doi.org/10.1109/ACCESS.2026.3674219) | **IEEE Article Number:** `11435372`  
**Category:** `Focal Modulation & Non-Dermoscopic Screening`  

> **Problem Formulation:** Dermoscopes are specialized instruments absent in general primary care and home tele-dermatology; standard CNNs fail on clinical smartphone photos due to variable lighting, blur, and complex non-lesion skin backgrounds.

#### Formulated Research Questions & Findings:
- **RQ1 [Dual-Stream Focal Architecture]:** *Can a dual-stream architecture integrating Focal Modulation and Local Feature Integration ('FoMoSkinNet') accurately diagnose skin lesions from non-dermoscopic clinical and smartphone photography?*
  - **Methodology:** Constructed FoMoSkinNet with a dual-stream design: one stream uses focal modulation for long-range contextual spatial relationships, while the second stream extracts fine-grained local textures, fused via adaptive gated integration.
  - **Answer & Findings:** Yes. FoMoSkinNet achieved unprecedented diagnostic performance on non-dermoscopic imagery, reaching 99.46% classification accuracy and 0.998 ROC-AUC.
- **RQ2 [Focal Modulation Context Modeling]:** *How does focal modulation overcome the self-attention quadratic computational complexity while capturing both global body site context and localized lesion borders?*
  - **Methodology:** Replaced self-attention with focal modulation operators that aggregate multi-scale context via depthwise convolutions and hierarchical context gates.
  - **Answer & Findings:** Focal modulation captured macroscopic spatial relationships with linear computational complexity, yielding 99.1% sensitivity and 99.7% specificity on smartphone captures.
- **RQ3 [Benchmark Performance on Smartphone Repositories]:** *What diagnostic reliability is demonstrated across standardized clinical photography benchmarks (ISIC 2024 and PAD-UFES-20)?*
  - **Methodology:** Evaluated the dual-stream model on ISIC 2024 (clinical photography) and PAD-UFES-20 (smartphone images captured with varying camera sensors).
  - **Answer & Findings:** Established state-of-the-art benchmark accuracy across non-dermoscopic repositories, proving that specialized optical hardware is not strictly necessary for AI-assisted screening.
- **RQ4 [Uncontrolled Real-World Photography]:** *What are the real-world vulnerability factors when deploying FoMoSkinNet on patient-captured smartphone photos taken under severe motion blur or non-standard angles?*
  - **Methodology:** Tested model robustness against synthetic lighting variations, flash glare, motion blur, and extreme oblique photographic angles.
  - **Answer & Findings:** While top-tier on curated benchmarks, diagnostic confidence degrades under severe specular flash glare and extreme oblique camera angles typical of unguided patient selfies.

- **Datasets:** ISIC 2024 (Clinical Photography Benchmark), PAD-UFES-20 (Smartphone Skin Lesion Dataset)
- **Quantitative Results:** **Classification Accuracy:** 99.46% | **Sensitivity:** 99.1% | **Specificity:** 99.7% | **AUC:** 0.998
- **Open Research Questions / Gaps:**
  - *Can on-device image quality assessment networks automatically reject blurry or poorly illuminated smartphone photos before running FoMoSkinNet?*
  - *How does FoMoSkinNet perform prospectively in diverse primary care clinics across low- and middle-income countries?*

---

### Paper 37: MSPE-DeiT: A Vision Transformer-Based Multimodal Framework for Skin Cancer Diagnosis
**Authors:** U. Mittal; S. S. H. Varpe; A. Sharma; T. Sood; P. Khandnor; S. Garg; S. Rani; M. Gupta; L. E. Amraoui; K. Ouni; A. El Amraoui  
**Venue:** *IEEE Access* (2026) | **DOI:** [10.1109/ACCESS.2026.3719871](https://doi.org/10.1109/ACCESS.2026.3719871) | **IEEE Article Number:** `11641552`  
**Category:** `Multimodal Vision Transformers & Distillation`  

> **Problem Formulation:** Visual dermoscopic examination alone frequently fails in border-zone cases without integrating patient clinical context (age, sex, anatomical site, history of melanoma).

#### Formulated Research Questions & Findings:
- **RQ1 [Multimodal Transformer Architecture]:** *Can a multimodal Vision Transformer ('MSPE-DeiT') integrating Data-efficient Image Transformers (DeiT) with patient clinical metadata outperform unimodal vision-only transformer models?*
  - **Methodology:** Constructed MSPE-DeiT by fusing tokenized visual patch embeddings from a distillation-trained DeiT backbone with embedded patient demographic/clinical metadata vectors via cross-attention.
  - **Answer & Findings:** Yes. Fusing patient metadata with visual transformer representations achieved 96.7% classification accuracy and 0.988 AUC, surpassing unimodal DeiT by 3.8% AUC.
- **RQ2 [Data-Efficient Distillation Token]:** *How does DeiT's distillation token strategy enable vision transformers to train efficiently on medical datasets without requiring hundred-million-image pre-training?*
  - **Methodology:** Employed hard distillation tokens supervised by a teacher CNN to transfer inductive convolutional biases to the vision transformer during training.
  - **Answer & Findings:** Distillation tokens allowed the transformer to achieve rapid convergence on 33,126 images of ISIC 2020 without massive ImageNet-21k pre-training, reaching 95.2% sensitivity and 97.8% specificity.
- **RQ3 [Clinical Metadata Feature Weighting]:** *Which patient metadata features (age, sex, anatomical location, lesion diameter) contribute most significantly to resolving ambiguous visual classifications?*
  - **Methodology:** Analyzed cross-attention weight distributions and conducted ablation studies isolating individual metadata fields.
  - **Answer & Findings:** Patient age and anatomical lesion location exhibited the highest cross-attention weights, decisively resolving visually ambiguous dysplastic nevi in older demographics.
- **RQ4 [Missing Metadata Robustness]:** *How does the multimodal framework perform when patient clinical metadata records are partially incomplete or missing at test time?*
  - **Methodology:** Evaluated classification accuracy under varying degrees of missing metadata values (10% to 50% simulated missingness).
  - **Answer & Findings:** Performance modestly declines under missing metadata; incorporating learned mask tokens for missing values partially mitigates degradation but leaves a slight accuracy gap.

- **Datasets:** ISIC 2020 Challenge Dataset (33,126 dermoscopic images with clinical metadata)
- **Quantitative Results:** **Accuracy:** 96.7% | **Sensitivity:** 95.2% | **Specificity:** 97.8% | **AUC:** 0.988 | **Gain vs Unimodal DeiT:** +3.8% AUC
- **Open Research Questions / Gaps:**
  - *Can longitudinal patient imaging history across multiple years be integrated into the transformer's temporal attention tokens?*
  - *How can privacy-preserving synthetic metadata generation resolve missing clinical fields in decentralized deployments?*

---

### Paper 38: MoLE: Mixture-of-LoRA Experts for Parameter-Efficient Dermoscopic Visual Question Answering
**Authors:** K. Younis; A. M. Muhammad; T. Hussain; M. Asma; A. K. Alzahrani  
**Venue:** *IEEE Access* (2026) | **DOI:** [10.1109/ACCESS.2026.3717605](https://doi.org/10.1109/ACCESS.2026.3717605) | **IEEE Article Number:** `11626860`  
**Category:** `Parameter-Efficient Tuning & Visual Question Answering`  

> **Problem Formulation:** Fine-tuning entire multi-billion parameter Vision-Language Models for specialized dermoscopic Visual Question Answering (VQA) requires unsustainable GPU memory and causes catastrophic forgetting of general medical knowledge.

#### Formulated Research Questions & Findings:
- **RQ1 [Mixture-of-LoRA Experts (MoLE) Architecture]:** *Can a Mixture-of-LoRA Experts ('MoLE') architecture achieve parameter-efficient adaptation for dermoscopic Visual Question Answering while training less than 5% of model parameters?*
  - **Methodology:** Designed MoLE by embedding multiple specialized Low-Rank Adaptation (LoRA) expert adapters into frozen foundation VLM attention layers, routed dynamically via a learned gating network.
  - **Answer & Findings:** Yes. MoLE achieved state-of-the-art dermoscopic VQA accuracy of 88.7% and clinical relevance of 92.4% while fine-tuning only 4.2M parameters (a 96% parameter reduction over full model tuning).
- **RQ2 [Dynamic Expert Routing & Task Specialization]:** *How does the router gating network distribute questions across specialized LoRA experts (e.g., diagnosis, border irregularity, pigment pattern, anatomical site)?*
  - **Methodology:** Visualized gating softmax distributions across question categories to verify whether individual LoRA experts developed specialized dermatological domain knowledge.
  - **Answer & Findings:** The gating network successfully routed diagnosis questions to diagnostic experts and color/texture queries to morphological experts, preventing inter-task interference.
- **RQ3 [Multi-Modal Conversational Accuracy]:** *What answer accuracy and clinical completeness are delivered across standardized DermVQA and ISIC-QA benchmarks?*
  - **Methodology:** Evaluated the conversational agent across thousands of open-ended and closed-ended clinical questions using exact-match accuracy and clinical relevance scores.
  - **Answer & Findings:** Achieved 88.7% overall answer accuracy and 92.4% clinical relevance, outperforming standard single-LoRA adaptation and fully fine-tuned smaller VLMs.
- **RQ4 [Router Collapse & Out-of-Domain Failure]:** *What failure modes occur in router gating when handling ambiguous, multi-part, or out-of-domain clinical inquiries?*
  - **Methodology:** Assessed expert load balancing, entropy of router softmax activations, and response coherence on compound complex questions.
  - **Answer & Findings:** Router gating can occasionally experience load imbalance on rare question phrasings, causing routing collapse to the dominant diagnostic expert and yielding overly brief answers.

- **Datasets:** DermVQA Benchmark, ISIC-QA Dataset
- **Quantitative Results:** **VQA Answer Accuracy:** 88.7% | **Clinical Relevance Score:** 92.4% | **Trainable Parameters:** 4.2M | **Parameter Reduction:** 96%
- **Open Research Questions / Gaps:**
  - *Can reinforcement learning from human feedback (RLHF) directly aligned with dermatologists optimize router dispatch policies?*
  - *How can MoLE models be audited to prevent conversational sycophancy or confidence miscalibration in clinical dialogue?*

---

### Paper 39: SLGAN-EID: Generative Adversarial Network-Based Skin Lesion Image Enhancement With Improved Diagnosis
**Authors:** M. U. Zafar; M. A. Qureshi; S. K. Noon; K. B. Khan  
**Venue:** *IEEE Access* (2026) | **DOI:** [10.1109/ACCESS.2026.3711048](https://doi.org/10.1109/ACCESS.2026.3711048) | **IEEE Article Number:** `11598907`  
**Category:** `GAN-Based Image Enhancement & Diagnostic Improvement`  

> **Problem Formulation:** Poor optical lighting, low resolution, hair occlusions, and non-standard camera calibration degrade the performance of deep CAD models deployed in real-world clinical environments.

#### Formulated Research Questions & Findings:
- **RQ1 [Generative Enhancement Architecture]:** *Can a specialized Generative Adversarial Network ('SLGAN-EID') enhance low-quality skin lesion images by removing artifacts and restoring micro-textures to improve downstream diagnostic accuracy?*
  - **Methodology:** Constructed SLGAN-EID with an edge-preserving perceptual loss generator and dual-discriminator architecture that restores degraded dermoscopic images prior to classification.
  - **Answer & Findings:** Yes. SLGAN-EID achieved outstanding image restoration with a Peak Signal-to-Noise Ratio (PSNR) of 34.2 dB and Structural Similarity Index (SSIM) of 0.941, significantly boosting downstream diagnostic models.
- **RQ2 [Downstream Diagnostic Accuracy Improvement]:** *How much does GAN-based preprocessing enhance the diagnostic accuracy of standard deep classifiers (ResNet-50, VGG-16, EfficientNet) compared to raw degraded images?*
  - **Methodology:** Trained and benchmarked downstream CNN classifiers on raw degraded dermoscopy vs. conventional enhanced imagery vs. SLGAN-EID enhanced imagery.
  - **Answer & Findings:** Classifiers trained on SLGAN-EID enhanced images exhibited a 5.6% average boost in multi-class classification accuracy over raw images, and a 3.1% boost over traditional Retinex/CLAHE filters.
- **RQ3 [Multi-Dataset Enhancement Generalization]:** *Does SLGAN-EID generalize effectively across distinct challenge benchmarks (ISIC 2019 and HAM10000) under synthetic and real-world degradation?*
  - **Methodology:** Evaluated perceptual enhancement metrics and classification accuracy gains across both public benchmark datasets under varying levels of Gaussian noise, blur, and low-light degradation.
  - **Answer & Findings:** Demonstrated robust restoration across datasets, consistently preserving genuine lesion borders and pigment network details while suppressing noise and occluding hair.
- **RQ4 [Adversarial Hallucination Safeguards]:** *What safeguards prevent the generator from synthesizing artificial pigment reticulations or pseudo-features that could mislead downstream diagnostic networks?*
  - **Methodology:** Incorporated edge-consistency loss and structural similarity constraints in the objective function, auditing enhanced images for hallucinated artifacts.
  - **Answer & Findings:** Structural similarity constraints effectively suppressed major hallucinations, but slight over-smoothing of extremely subtle atypical streaks remains a potential risk under severe input noise.

- **Datasets:** ISIC 2019 Challenge Dataset, HAM10000 Benchmark
- **Quantitative Results:** **PSNR:** 34.2 dB | **SSIM:** 0.941 | **Downstream Accuracy Gain:** +5.6% vs raw | **Gain vs CLAHE:** +3.1%
- **Open Research Questions / Gaps:**
  - *Can diffusion restoration models replace GAN generators to provide stronger mathematical guarantees against hallucinated micro-structures?*
  - *Can SLGAN-EID run in real-time within digital dermoscope firmware during live patient examinations?*

---
