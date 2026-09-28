# Comprehensive Research Objectives of 39 Medical Image Analysis Research Papers

> **Course:** Research Methodology (BCA / Computer Science)
> **Corpus:** 39 Verified Research Papers in Cutaneous Oncology & Medical Computer Vision
> **Standard:** Rigorous IEEE Academic Formalization (Zero Hallucination Protocol)

---

## Executive Taxonomy of Research Objectives

The 39 investigated research papers address foundational diagnostic and technical bottlenecks across cutaneous oncology, categorized into eight distinct methodological paradigms:

1. **Lightweight & Regularized Architectures (Papers 1, 4, 5, 20):** Overcoming overfitting, high latency, and parameter bloat for embedded and resource-limited screening.
2. **Artifact Removal & Inpainting (Papers 6, 14, 24, 39):** Eliminating occluding hair, glare, illumination shifts, and boundary artifacts before diagnosis.
3. **Transfer Learning & Multi-Model Ensembles (Papers 2, 7, 8, 21, 22):** Harnessing pre-trained deep representations and consensus voting to minimize individual network bias.
4. **Capsule Networks & Geometric Representations (Papers 9, 23, 25, 29):** Preserving spatial hierarchies, 3D surface topography, and quantum-wavelet texture features.
5. **Loss Function Engineering & Imbalance Handling (Papers 10, 15, 16, 33):** Center-oriented margin-free triplet loss, StyleGAN synthetic balancing, and part cross-entropy.
6. **Multi-Scale Attention & Vision Transformers (Papers 13, 19, 26, 36, 37):** Swin Transformer, Self-Interactive Pyramid, FoMoSkinNet focal modulation, and DeiT patch embedding.
7. **Explainable AI (XAI) & Knowledge Graphs (Papers 3, 17, 18, 27, 30, 35):** Grad-CAM heatmaps, Dempster-Shafer evidence, ABCD clinical rules, Seven-Point Checklist knowledge graphs, and Siamese case retrieval.
8. **Multimodal & Vision-Language Intelligence (Papers 28, 31, 32, 34, 38):** Endoscopic-audiometric fusion, YOLOv9 + Faster R-CNN detection, automated report generation VLMs, unsupervised NMF, and Mixture-of-LoRA VQA.

---

## Master Comparative Objectives Matrix (39 Papers)

| ID | Year | Primary Topic / Architecture | Primary Research Objective | Key Benchmark | Diagnostic Metric |
|:---|:---:|:---|:---|:---|:---|
| **1** | 2019 | Lightweight Regularized CNNs | To design, develop, and evaluate a lightweight custom Convolutional Neural Network embedded wit... | ISIC Archive (23,906 images; 8... | Accuracy: 97.49% |
| **2** | 2020 | ROI Localization & Transfer Learning | To establish an automated Region-of-Interest (ROI) transfer learning framework that isolates le... | DermIS (705 images: 448 benign... | Accuracy (DermIS): 97.9% |
| **3** | 2023 | Interpretable CNNs & Mobile Healthcare | To design, optimize, and deploy an interpretable Convolutional Neural Network integrated into a... | HAM10000 (10,015 images across... | Overall Accuracy: 82.0% |
| **4** | 2020 | Lightweight Ensembles & Semantic Segmentation | To develop an efficient, lightweight skin lesion recognition and semantic segmentation framewor... | ISBI 2016 (900 train, 379 test... | Accuracy (ISBI 2016): 87.3% |
| **5** | 2023 | Multi-Level Representation & Residual Learning | To establish 'DeepSkin', a tailored deep learning classification architecture with residual ski... | HAM10000 / ISIC 2018 (10,015 i... | Accuracy: 88.0% |
| **6** | 2020 | Two-Stage FCN & DenseNet Framework | To formulate an end-to-end two-stage deep framework integrating Fully Convolutional Network (FC... | ISIC 2017 (2,000 train, 150 va... | Segmentation Accuracy: 98.5% |
| **7** | 2020 | Systematic Empirical Benchmark & Protocol Standardization | To conduct a systematic, standardized experimental benchmarking of state-of-the-art deep learni... | PH2 (200 images)... | Peak Classification Accuracy: 93.4% |
| **8** | 2022 | Multi-Model Ensemble & Decision Fusion | To develop a hybrid ensemble decision system combining predictions from diverse deep learning b... | ISIC 2019 (25,331 dermoscopic ... | Ensemble Accuracy: 93.5% |
| **9** | 2022 | Capsule Networks & Spatial Relationship Modeling | To construct 'FixCaps', an improved Capsule Network utilizing fixed routing and spatial feature... | HAM10000 / ISIC 2018 (10,015 i... | Classification Accuracy: 96.49% |
| **10** | 2022 | Deep Metric Clustering & Margin-Free Loss | To formulate a deep clustering framework utilizing a novel center-oriented margin-free triplet ... | ISIC 2017... | Classification Accuracy: 91.8% |
| **11** | 2020 | Neural Architecture Search (NAS) | To deploy Neural Architecture Search (NAS) to automatically discover optimal, high-performing c... | ISIC 2018 (10,015 images acros... | Balanced Multiclass Accuracy: 86.6% |
| **12** | 2023 | Hybrid Computer Vision & Transfer Learning | To enhance skin cancer classification performance by developing a comprehensive computer vision... | ISIC 2019 (25,331 images acros... | Classification Accuracy: 93.8% |
| **13** | 2024 | Multi-Scale Attention & Enhanced Feature Fusion | To design and validate 'EFAM-Net', an advanced multi-class skin lesion classification network i... | ISIC 2018 / HAM10000 (10,015 i... | Overall Accuracy: 93.2% |
| **14** | 2021 | Deep Hair Segmentation & Context-Aware Inpainting | To develop a deep learning-based hair segmentation and context-aware inpainting system that rem... | ISIC 2018 Hair Dataset subsets... | Hair Segmentation Dice: 92.8% |
| **15** | 2020 | Generative Augmentation & Decision Fusion | To develop a dermatoscopic classification framework combining StyleGAN-based synthetic minority... | ISIC 2017 (2,000 train, 600 te... | Classification Accuracy: 91.2% |
| **16** | 2023 | Comprehensive Joint Learning System | To propose a comprehensive joint learning framework that couples shared representation learning... | HAM10000 (10,015 images across... | Classification Accuracy: 92.4% |
| **17** | 2020 | Multiple Connected Networks & Evidence Theory | To develop an objective, multi-network decision system combining color, texture, and geometry n... | PH2 (200 images: 80 common nev... | Overall Accuracy: 94.7% |
| **18** | 2024 | Clinical Decision Support & Systematic ML/DL | To develop 'DermCDSM', a clinical decision support model for dermatosis integrating systematic ... | HAM10000 (10,015 images)... | Classification Accuracy: 94.1% |
| **19** | 2024 | Swin Transformer & Non-Local Attention | To develop a hybrid deep learning architecture combining a Swin Transformer backbone with a Den... | ISIC 2019 (25,331 images)... | Classification Accuracy: 96.8% |
| **20** | 2019 | Intelligent Things & IoT Edge Diagnosis | To design and implement an Intelligent Things framework utilizing distributed neural networks a... | Curated clinical skin mark ima... | Edge Accuracy: 91.5% |
| **21** | 2024 | Transfer Learning & Multi-Branch Ensembles | To formulate 'IncepX-Ensemble', a transfer learning-based ensemble architecture fusing Inceptio... | HAM10000 / ISIC 2018 (10,015 i... | Overall Accuracy: 94.6% |
| **22** | 2020 | Ensemble Learning & Group Decision Making | To develop an ensemble classification framework for dermoscopy images based on individual model... | ISIC 2017 (2,000 train, 600 te... | Classification Accuracy: 92.7% |
| **23** | 2024 | Pipelined CNN-SVM & Bi-Sectional Textures | To propose a pipelined classification framework combining AlexNet CNN deep feature extraction, ... | ISIC 2019 (25,331 images acros... | Classification Accuracy: 93.1% |
| **24** | 2024 | Normalized Cross-Correlation & k-Means Segmentation | To develop an improved segmentation model for melanoma lesion detection using Normalized Cross-... | PH2 (200 images)... | Segmentation Accuracy: 96.2% |
| **25** | 2022 | Multiple Instance Learning & 3D Dermoscopy | To formulate a Multiple Instance Learning (MIL) framework leveraging 3D surface reconstruction ... | Clinical 3D Dermoscopy Dataset... | Melanoma Detection AUC: 0.894 |
| **26** | 2024 | Multi-Scale Attention & Bilinear-Trilinear Pooling | To develop 'SPCB-Net', a multi-scale skin cancer identification network utilizing a Self-Intera... | ISIC 2018 (10,015 images)... | Classification Accuracy: 95.3% |
| **27** | 2024 | Interpretable Attention & Residual Skip Segmentation | To design and validate 'IARS SegNet', an Interpretable Attention Residual Skip Connection SegNe... | ISIC 2017... | Dice Coefficient: 94.5% |
| **28** | 2023 | Multimodal Fusion (Endoscopic Imagery + Audiometry) | To develop a multi-modal multi-fusion deep learning framework combining endoscopic tympanic mem... | Clinical Multimodal Otology Re... | Multimodal Accuracy: 91.2% |
| **29** | 2024 | Quantum-Inspired Features & Autoencoders | To propose a novel feature extraction and classification methodology utilizing Quantum Chebyshe... | ISIC 2018 (10,015 images)... | Classification Accuracy: 94.8% |
| **30** | 2026 | Clinical Knowledge Graphs & Rule-Based Neural Integration | To integrate clinical knowledge graphs with gradient-based neural systems for enhanced, explain... | ISIC Seven-Point Checklist Ben... | Classification Accuracy: 87.4% |
| **31** | 2025 | Hybrid Object Detection & Two-Stage Verification | To develop a hybrid two-stage detection and verification model integrating YOLOv9 for real-time... | ISIC 2019... | Mean Average Precision (mAP@0.5): 97.1% |
| **32** | 2025 | Vision-Language Models & Knowledge Distillation | To design and validate an automated skin cancer report generation system using a knowledge-dist... | Derm-Report Corpus (dermoscopi... | BLEU-4: 0.38 |
| **33** | 2024 | Multi-Scale DCNN & Dynamic Loss Formulation | To formulate a Multi-Scale Deep Convolutional Neural Network (DCNN) with dynamic weighting and ... | ISIC 2018... | Overall Accuracy: 92.9% |
| **34** | 2025 | Unsupervised Matrix Factorization & Information Theory | To develop an unsupervised skin lesion segmentation framework for clinical images using Nonnega... | Dermofit Image Library (1,300 ... | Jaccard Index: 88.7% |
| **35** | 2025 | Content-Based Image Retrieval & Siamese Deep Metric | To establish a transparent, search-based diagnostic framework using Siamese deep metric network... | ISIC Archive (dermoscopy)... | Classification Accuracy (Skin): 93.6% |
| **36** | 2026 | Focal Modulation & Non-Dermoscopic Clinical Imaging | To propose 'FoMoSkinNet', a dual-stream deep learning model utilizing focal modulation and loca... | PAD-UFES-20 (2,298 clinical sm... | Classification Accuracy: 92.6% |
| **37** | 2026 | Vision Transformers & Multimodal Patient Metadata | To develop 'MSPE-DeiT', a Vision Transformer-based multimodal framework integrating dermatoscop... | HAM10000 (10,015 images with p... | Classification Accuracy: 95.8% |
| **38** | 2026 | Parameter-Efficient Fine-Tuning & Dermoscopic VQA | To construct 'MoLE', a parameter-efficient Mixture-of-LoRA Experts framework for dermoscopic Vi... | Skin-VQA Benchmark (thousands ... | VQA Accuracy: 86.9% |
| **39** | 2026 | Generative Enhancement & Improved Diagnosis | To develop 'SLGAN-EID', a Generative Adversarial Network-based skin lesion image enhancement fr... | ISIC 2018... | PSNR Gain: +6.8 dB |

---

## Detailed Research Objectives by Paper

### Paper 1: Skin Lesion Classification Using Convolutional Neural Network With Novel Regularizer

- **Authors:** M. A. Albahar
- **Affiliation:** Ibn Rushd College for Management Science, Abha, Saudi Arabia
- **Venue:** IEEE Access (2019) | **DOI:** `10.1109/ACCESS.2019.2906241` | **IEEE Article:** `8669763`
- **PDF File:** `01_M._A._Albahar_2019_Skin_Lesion_Classification_Using_Convolutional_Neural_Network_With_Novel_Regularizer.pdf`
- **Methodological Category:** Lightweight Regularized CNNs

#### Clinical & Technical Problem
Fine-grained morphological overlaps between benign nevi and malignant melanoma cause catastrophic overfitting in traditional unregularized deep CNNs, especially under clinical data scarcity.

#### Primary Research Objective (General Aim)
> **To design, develop, and evaluate a lightweight custom Convolutional Neural Network embedded with a novel weight-controlling regularizer to stabilize weight trajectories and achieve high-precision binary skin lesion classification.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Data Standardization & Preprocessing):** To implement a power-law transformation (gamma correction) preprocessing pipeline to adjust illumination variances, normalize contrast gradients across 300x300x3 dermoscopic images, and accelerate gradient descent convergence.
- **RO2 (Lightweight Architectural Design):** To construct a custom two-layer convolutional architecture coupled with max-pooling, dropout (0.25 and 0.5), and a 128-neuron dense layer that drastically reduces parameter complexity compared to multi-million parameter backbones.
- **RO3 (Novel Weight Regularizer Formulation):** To mathematically formulate and embed a novel weight regularizer (penalty hyperparameter lambda = 0.02) directly into the convolutional loss function to prevent weight explosion and suppress overfitting.
- **RO4 (Pairwise Diagnostic Benchmarking):** To evaluate the model's discriminative capability across distinct binary diagnostic pairings (nevus vs. melanoma, seborrheic keratosis vs. basal cell carcinoma, seborrheic keratosis vs. melanoma, and solar lentigo vs. melanoma) on 23,906 ISIC archive images.
- **RO5 (Clinical Feasibility Assessment):** To analyze ROC-AUC trajectories and validation stability over 100 training epochs to verify suitability for resource-constrained clinical triage.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Custom 2-layer CNN, power-law transformation, novel weight regularizer (lambda = 0.02), dropout regularization, Adam optimizer.
- **Evaluated Datasets:** ISIC Archive (23,906 images; 8,000 image evaluation subset, 70% train / 30% val)
- **Reported Performance Metrics:**
  - *Accuracy:* **97.49%**
  - *AUC (Nevus vs Mel):* **0.77**
  - *AUC (SK vs BCC):* **0.93**
  - *AUC (SK vs Mel):* **0.85**
  - *AUC (SL vs Mel):* **0.86**
- **Clinical Utility & Impact:** Enables rapid, low-footprint automated screening of suspicious lesions on entry-level clinical hardware without requiring cloud infrastructure.

---

### Paper 2: Region-of-Interest Based Transfer Learning Assisted Framework for Skin Cancer Detection

- **Authors:** R. Ashraf; S. Afzal; A. U. Rehman; S. Gul; J. Baber; M. Bakhtyar; I. Mehmood; O. -Y. Song; M. Maqsood
- **Affiliation:** Department of Computer Science, National Textile University, Faisalabad, Pakistan; Department of Computer Science, COMSATS University Islamabad, Attock, Pakistan
- **Venue:** IEEE Access (2020) | **DOI:** `10.1109/ACCESS.2020.3014701` | **IEEE Article:** `9160933`
- **PDF File:** `02_R._Ashraf_2020_Region-of-Interest_Based_Transfer_Learning_Assisted_Framework_for_Skin_Cancer_Detection.pdf`
- **Methodological Category:** ROI Localization & Transfer Learning

#### Clinical & Technical Problem
Extraneous skin artifacts, healthy skin tissue, and illumination variances corrupt deep feature representations, leading to high false-alarm rates in distinguishing melanoma from benign nevi.

#### Primary Research Objective (General Aim)
> **To establish an automated Region-of-Interest (ROI) transfer learning framework that isolates lesion boundaries and leverages fine-tuned deep CNNs for robust melanoma detection.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Automated Lesion Segmentation):** To implement an improved k-means clustering algorithm to accurately localize and isolate lesion regions of interest from surrounding healthy background skin and clinical artifacts.
- **RO2 (Data Augmentation & Regularization):** To deploy comprehensive offline spatial and contrast augmentations (rotations, horizontal/vertical flipping, zooming) to prevent model overfitting on clinical cohorts.
- **RO3 (Transfer Learning Feature Adaptation):** To adapt pre-trained AlexNet and VGG-16 architectures through fine-tuning exclusively on isolated ROI lesion patches, capturing fine-grained structural lesion patterns.
- **RO4 (Comparative Benchmark Assessment):** To quantitatively validate diagnostic accuracy, sensitivity, specificity, precision, F1-score, and ROC-AUC on the DermIS and DermQuest clinical benchmarks.
- **RO5 (Clinical Diagnostic Triage):** To minimize false-positive and false-negative triage rates, providing dermatologists with a reliable second-opinion tool for melanocytic lesion screening.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Improved k-means segmentation, localized ROI patch extraction, transfer learning with fine-tuned AlexNet and VGG-16 backbones.
- **Evaluated Datasets:** DermIS (705 images: 448 benign, 257 melanoma), DermQuest (667 images: 434 nevus, 233 melanoma)
- **Reported Performance Metrics:**
  - *Accuracy (DermIS):* **97.9%**
  - *Sensitivity (DermIS):* **96.3%**
  - *Specificity (DermIS):* **98.7%**
  - *AUC (DermIS):* **0.97**
  - *Accuracy (DermQuest):* **97.4%**
  - *AUC (DermQuest):* **0.96**
- **Clinical Utility & Impact:** Suppresses healthy background tissue noise, focusing diagnostic inference strictly on atypical lesion borders and pigmentation patterns.

---

### Paper 3: An Interpretable Skin Cancer Classification Using Optimized Convolutional Neural Network for a Smart Healthcare System

- **Authors:** K. Mridha; M. M. Uddin; J. Shin; S. Khadka; M. F. Mridha
- **Affiliation:** Department of Computer Engineering, Marwadi University, Rajkot, Gujarat, India; Department of Computer Science and Engineering, University of Aizu, Aizuwakamatsu, Japan
- **Venue:** IEEE Access (2023) | **DOI:** `10.1109/ACCESS.2023.3269694` | **IEEE Article:** `10107401`
- **PDF File:** `03_K._Mridha_2023_An_Interpretable_Skin_Cancer_Classification_Using_Optimized_Convolutional_Neural_Network_for_a_Smart.pdf`
- **Methodological Category:** Interpretable CNNs & Mobile Healthcare

#### Clinical & Technical Problem
Black-box opacity and prohibitive computational demands hinder the adoption of automated deep learning models in point-of-care dermatology.

#### Primary Research Objective (General Aim)
> **To design, optimize, and deploy an interpretable Convolutional Neural Network integrated into an Android smart healthcare application for multi-class skin lesion screening.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Standardized Multiclass Preprocessing):** To standardize and augment 10,015 HAM10000 dermoscopy images across seven diagnostic classes using random rotations, zooms, shear transformations, and pixel normalization.
- **RO2 (Architectural Optimization & Tuning):** To construct a custom CNN incorporating batch normalization, dropout, and systematic benchmarking across optimizers (Adam, RMSprop) and activation functions (ReLU, Swish, Tanh).
- **RO3 (Explainable Visual Attribution):** To implement Grad-CAM and Grad-CAM++ attribution maps to provide dermatologists with transparent, localized visual justifications for model predictions.
- **RO4 (Multiclass Diagnostic Evaluation):** To rigorously evaluate classification sensitivity, specificity, and loss convergence across all seven pathological lesion categories in the HAM10000 repository.
- **RO5 (Point-of-Care Mobile Deployment):** To deploy the optimized neural model into an interactive Android smart healthcare application for real-time, explainable bedside triage.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Optimized custom CNN, Grad-CAM/Grad-CAM++ explainability maps, hyperparameter optimization, Android mobile edge deployment.
- **Evaluated Datasets:** HAM10000 (10,015 images across 7 classes: akiec, bcc, bkl, df, mel, nv, vasc)
- **Reported Performance Metrics:**
  - *Overall Accuracy:* **82.0%**
  - *Specificity:* **94.17%**
  - *Sensitivity:* **82.0%**
  - *Loss Accuracy:* **0.47**
- **Clinical Utility & Impact:** Empowers front-line medical personnel with visual heatmap confirmations on mobile devices, promoting diagnostic transparency and clinical trust.

---

### Paper 4: Automatic Skin Cancer Detection in Dermoscopy Images Based on Ensemble Lightweight Deep Learning Network

- **Authors:** L. Wei; K. Ding; H. Hu
- **Affiliation:** Anhui Key Laboratory of Electric Drive and Control, Department of Electrical Engineering, Anhui Polytechnic University, Wuhu, China; School of Computer Science and Electric Engineering, University of Essex, Colchester, U.K.
- **Venue:** IEEE Access (2020) | **DOI:** `10.1109/ACCESS.2020.2997710` | **IEEE Article:** `9099799`
- **PDF File:** `04_L._Wei_2020_Automatic_Skin_Cancer_Detection_in_Dermoscopy_Images_Based_on_Ensemble_Lightweight_Deep_Learning_Net.pdf`
- **Methodological Category:** Lightweight Ensembles & Semantic Segmentation

#### Clinical & Technical Problem
Substantial intra-class morphological variance and excessive computational parameter overhead in standard deep networks impede deployment on resource-constrained clinical workstations.

#### Primary Research Objective (General Aim)
> **To develop an efficient, lightweight skin lesion recognition and semantic segmentation framework utilizing ensemble lightweight deep networks for binary melanoma detection.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (End-to-End Semantic Segmentation):** To integrate a lightweight U-Net segmentation network trained via a transfer learning migration strategy, isolating lesion contours end-to-end without manual artifact filtering.
- **RO2 (Pair-Based Feature Representation):** To construct a pair-based feature extraction module utilizing lightweight CNNs coupled with a feature discrimination network trained on positive and negative sample pairs.
- **RO3 (Ensemble Decision Fusion):** To formulate a lightweight decision fusion mechanism combining multiple specialized models to enhance classification stability and generalizability.
- **RO4 (Challenge Benchmark Assessment):** To quantitatively benchmark the framework on the international ISBI 2016 and ISBI 2017 challenge datasets measuring accuracy, sensitivity, specificity, and AUC.
- **RO5 (Computational Resource Optimization):** To significantly reduce model parameter footprint and computational complexity while maintaining fine-grained diagnostic representation capability.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Lightweight U-Net segmentation, pair-based CNN feature discrimination module, ensemble decision fusion.
- **Evaluated Datasets:** ISBI 2016 (900 train, 379 test), ISBI 2017 Challenge dataset
- **Reported Performance Metrics:**
  - *Accuracy (ISBI 2016):* **87.3%**
  - *Sensitivity:* **83.2%**
  - *Specificity:* **89.1%**
  - *AUC:* **0.886**
  - *Average Precision:* **0.732**
- **Clinical Utility & Impact:** Achieves high diagnostic accuracy with minimal hardware requirements, making automated melanoma detection accessible to smaller clinics.

---

### Paper 5: DeepSkin: A Deep Learning Approach for Skin Cancer Classification

- **Authors:** H. L. Gururaj; N. Manju; A. Nagarjun; V. N. M. Aradhya; F. Flammini
- **Affiliation:** Department of Information Technology, Manipal Institute of Technology Bengaluru, Manipal Academy of Higher Education, Manipal, India; Department of Information Science and Engineering, JSS Science and Technology University, Mysuru, India; IDSIA USI-SUPSI, University of Applied Sciences and Arts of Southern Switzerland, Manno, Switzerland
- **Venue:** IEEE Access (2023) | **DOI:** `10.1109/ACCESS.2023.3274848` | **IEEE Article:** `10122533`
- **PDF File:** `05_H._L._Gururaj_2023_DeepSkin_A_Deep_Learning_Approach_for_Skin_Cancer_Classification.pdf`
- **Methodological Category:** Multi-Level Representation & Residual Learning

#### Clinical & Technical Problem
High intra-class morphological variability and severe class imbalance across 7-class dermatoscopic datasets lead to frequent misclassification of rare cutaneous malignancies.

#### Primary Research Objective (General Aim)
> **To establish 'DeepSkin', a tailored deep learning classification architecture with residual skip connections for multi-class skin cancer classification in resource-limited clinical environments.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Intensity Normalization & Augmentation):** To apply Min-Max pixel intensity scaling and geometric augmentations (random rotations, horizontal flipping, zooming, brightness shifts) to mitigate dataset imbalance.
- **RO2 (Residual Architecture Design):** To construct a tailored CNN architecture incorporating residual skip connections to preserve low-level textural details across deeper feature hierarchies.
- **RO3 (Comparative Transfer Learning Benchmarking):** To systematically benchmark DeepSkin against established pre-trained backbones (VGG-16, ResNet-50, MobileNet) under uniform hyperparameter conditions.
- **RO4 (7-Class Pathological Evaluation):** To evaluate classification accuracy, sensitivity, specificity, and precision across seven cutaneous disease categories on the ISIC 2018 / HAM10000 repository.
- **RO5 (Clinical Decision Support Feasibility):** To evaluate early-stage triage feasibility for non-specialist healthcare workers in clinical dermatosis diagnosis.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Custom residual CNN (DeepSkin), Min-Max normalization, comparative benchmarking against VGG-16, ResNet-50, and MobileNet.
- **Evaluated Datasets:** HAM10000 / ISIC 2018 (10,015 images across 7 pathological classes)
- **Reported Performance Metrics:**
  - *Accuracy:* **88.0%**
  - *Sensitivity:* **86.2%**
  - *Specificity:* **85.0%**
  - *Precision:* **86.4%**
- **Clinical Utility & Impact:** Provides general practitioners with an automated multi-class classification assistant to expedite specialist referrals for malignant lesions.

---

### Paper 6: FCN-Based DenseNet Framework for Automated Detection and Classification of Skin Lesions in Dermoscopy Images

- **Authors:** A. A. Adegun; S. Viriri
- **Affiliation:** School of Mathematics, Statistics and Computer Science, University of KwaZulu-Natal, Durban, South Africa
- **Venue:** IEEE Access (2020) | **DOI:** `10.1109/ACCESS.2020.3016651` | **IEEE Article:** `9167192`
- **PDF File:** `06_A._A._Adegun_2020_FCN-Based_DenseNet_Framework_for_Automated_Detection_and_Classification_of_Skin_Lesions_in_Dermoscop.pdf`
- **Methodological Category:** Two-Stage FCN & DenseNet Framework

#### Clinical & Technical Problem
Fuzzy lesion boundaries, variable pigmentation gradients, and occluding hair artifacts cause high false-boundary detection and diagnostic errors.

#### Primary Research Objective (General Aim)
> **To formulate an end-to-end two-stage deep framework integrating Fully Convolutional Network (FCN) segmentation and DenseNet multi-class classification for automated dermoscopy analysis.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Artifact Removal & Preprocessing):** To deploy DullRazor morphological filtering and contrast enhancement to eliminate occluding hair shafts and normalize illumination.
- **RO2 (FCN Lesion Boundary Segmentation):** To design and train an encoder-decoder Fully Convolutional Network (FCN) with skip connections to generate high-precision binary lesion masks for automated cropping.
- **RO3 (DenseNet Feature Extraction & Classification):** To construct a deep DenseNet architecture utilizing dense connectivity blocks and transition layers to maximize feature reuse across multi-class lesion categories.
- **RO4 (Multi-Benchmark Validation):** To rigorously assess segmentation metrics (Dice coefficient, Jaccard index) and classification metrics on ISIC 2017, ISIC 2018, and DermQuest datasets.
- **RO5 (Clinical Workflow Integration):** To provide an integrated, objective computer-aided diagnosis system reducing reliance on manual lesion delineation by dermatologists.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** DullRazor hair suppression, FCN encoder-decoder segmentation, DenseNet feature reuse classification architecture.
- **Evaluated Datasets:** ISIC 2017 (2,000 train, 150 val, 600 test), ISIC 2018 (2,594 train, 100 val, 1,000 test), DermQuest
- **Reported Performance Metrics:**
  - *Segmentation Accuracy:* **98.5%**
  - *Dice Coefficient:* **92.5%**
  - *Jaccard Index:* **86.8%**
  - *ISIC 2017 Accuracy:* **95.0%**
  - *ISIC 2018 Accuracy:* **98.5%**
  - *AUC:* **0.98**
- **Clinical Utility & Impact:** Eliminates manual lesion delineation overhead while achieving near-perfect boundary localization and high multi-class classification precision.

---

### Paper 7: Malignant Melanoma Classification Using Deep Learning: Datasets, Performance Measurements, Challenges and Opportunities

- **Authors:** A. Naeem; M. S. Farooq; A. Khelifi; A. Abid
- **Affiliation:** Department of Computer Science, University of Management and Technology, Lahore, Pakistan; Department of Computer Science and Information Technology, Abu Dhabi University, Abu Dhabi, United Arab Emirates
- **Venue:** IEEE Access (2020) | **DOI:** `10.1109/ACCESS.2020.3001507` | **IEEE Article:** `9113301`
- **PDF File:** `07_A._Naeem_2020_Malignant_Melanoma_Classification_Using_Deep_Learning_Datasets,_Performance_Measurements,_Challenges.pdf`
- **Methodological Category:** Systematic Empirical Benchmark & Protocol Standardization

#### Clinical & Technical Problem
Heterogeneity of evaluation protocols, disparate performance metrics, and severe class imbalance skew reported deep learning results in melanoma literature, hindering objective clinical comparisons.

#### Primary Research Objective (General Aim)
> **To conduct a systematic, standardized experimental benchmarking of state-of-the-art deep learning architectures across five major dermatological benchmark datasets.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Standardized Preprocessing Protocol):** To implement a uniform preprocessing protocol encompassing aspect-ratio preserving resizing, hair suppression, and color normalization across disparate datasets.
- **RO2 (Comparative Deep Backbone Assessment):** To systematically evaluate ResNet-50, VGG-16, Inception-v3, and DenseNet-121 under controlled transfer learning protocols and cross-validation.
- **RO3 (Multi-Benchmark Cross-Validation):** To benchmark diagnostic performance across PH2, ISIC 2016, ISIC 2017, ISIC 2018, and HAM10000 datasets for binary and multiclass tasks.
- **RO4 (Performance Discrepancy & Bias Analysis):** To analyze how class imbalance, image resolution variations, and demographic skew artificially inflate or degrade sensitivity and AUC.
- **RO5 (Clinical Translation Guidelines):** To synthesize standardized clinical evaluation guidelines and identify future research opportunities for reliable, multi-center validated melanoma screening tools.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Standardized transfer learning benchmarking, systematic cross-dataset validation of ResNet-50, VGG-16, Inception-v3, and DenseNet-121.
- **Evaluated Datasets:** PH2 (200 images), ISIC 2016 (1,279 images), ISIC 2017 (2,750 images), ISIC 2018 (10,015 images), HAM10000
- **Reported Performance Metrics:**
  - *Peak Classification Accuracy:* **93.4%**
  - *Average Sensitivity:* **91.0%**
  - *Average Specificity:* **94.2%**
  - *Peak AUC:* **0.95**
- **Clinical Utility & Impact:** Provides researchers and clinicians with a rigorous, reproducible baseline comparing popular deep backbones under uniform evaluation criteria.

---

### Paper 8: Skin Cancer Detection Using Combined Decision of Deep Learners

- **Authors:** A. Imran; A. Nasir; M. Bilal; G. Sun; A. Alzahrani; A. Almuhaimeed
- **Affiliation:** Faculty of Information Technology, Beijing University of Technology, Beijing, China; Department of Computer Science and Information Technology, Superior University, Lahore, Pakistan
- **Venue:** IEEE Access (2022) | **DOI:** `10.1109/ACCESS.2022.3220329` | **IEEE Article:** `9940917`
- **PDF File:** `08_A._Imran_2022_Skin_Cancer_Detection_Using_Combined_Decision_of_Deep_Learners.pdf`
- **Methodological Category:** Multi-Model Ensemble & Decision Fusion

#### Clinical & Technical Problem
Individual deep learning architectures exhibit divergent misclassification patterns on complex, borderline skin lesions, increasing clinical false-negative risk.

#### Primary Research Objective (General Aim)
> **To develop a hybrid ensemble decision system combining predictions from diverse deep learning backbones to achieve superior skin cancer classification reliability.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Heterogeneous Deep Feature Extraction):** To train and fine-tune multiple heterogeneous deep CNN backbones (DenseNet, ResNet, VGG) on dermoscopic image benchmarks.
- **RO2 (Ensemble Decision Fusion Design):** To design and compare hard majority voting and weighted soft probability fusion mechanisms to integrate individual network predictions.
- **RO3 (Class Imbalance Compensation):** To implement loss weighting and targeted data augmentation techniques to balance model sensitivity across minority cutaneous lesion classes.
- **RO4 (Diagnostic Benchmark Assessment):** To validate the ensemble framework on the benchmark ISIC 2019 dataset, measuring accuracy, precision, recall, and F1-score across 8 lesion classes.
- **RO5 (Clinical Reliability Maximization):** To reduce individual model variance and eliminate catastrophic false-negative misclassifications on malignant melanoma cases.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Multi-model CNN ensemble (DenseNet, ResNet, VGG), majority voting and weighted soft probability fusion.
- **Evaluated Datasets:** ISIC 2019 (25,331 dermoscopic images across 8 diagnostic categories)
- **Reported Performance Metrics:**
  - *Ensemble Accuracy:* **93.5%**
  - *Precision:* **92.8%**
  - *Recall/Sensitivity:* **93.1%**
  - *F1-Score:* **92.9%**
- **Clinical Utility & Impact:** Mitigates single-model blind spots by leveraging consensus voting, significantly boosting diagnostic safety on borderline melanoma cases.

---

### Paper 9: FixCaps: An Improved Capsules Network for Diagnosis of Skin Cancer

- **Authors:** Z. Lan; S. Cai; X. He; X. Wen
- **Affiliation:** School of Automation, Guangdong University of Technology, Guangzhou, China
- **Venue:** IEEE Access (2022) | **DOI:** `10.1109/ACCESS.2022.3181225` | **IEEE Article:** `9791221`
- **PDF File:** `10_Z._Lan_2022_FixCaps_An_Improved_Capsules_Network_for_Diagnosis_of_Skin_Cancer.pdf`
- **Methodological Category:** Capsule Networks & Spatial Relationship Modeling

#### Clinical & Technical Problem
Conventional CNN pooling layers discard critical spatial hierarchy and geometric relationships between lesion sub-structures, while standard Capsule Networks suffer prohibitive dynamic routing latency.

#### Primary Research Objective (General Aim)
> **To construct 'FixCaps', an improved Capsule Network utilizing fixed routing and spatial feature preservation for efficient and accurate skin cancer diagnosis.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Spatial Hierarchy Modeling):** To formulate capsule vector representations that encode both the presence and spatial pose/orientation of dermatoscopic lesion sub-structures.
- **RO2 (Fixed Routing Mechanism Design):** To replace iterative dynamic routing with an optimized fixed routing scheme to drastically reduce computational latency and parameter overhead.
- **RO3 (Feature Map Compression):** To design efficient convolutional capsule layers that preserve fine-grained border details without requiring excessive GPU memory.
- **RO4 (Benchmark Performance Evaluation):** To benchmark FixCaps against conventional CNN baselines on the HAM10000 / ISIC 2018 datasets, evaluating classification accuracy, convergence rate, and parameter size.
- **RO5 (Clinical Interpretability via Vector Lengths):** To leverage capsule activation vector lengths as intrinsic confidence measures for clinical dermatological decision-making.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** FixCaps architecture, fixed routing mechanism, capsule vector representation, HAM10000 benchmarking.
- **Evaluated Datasets:** HAM10000 / ISIC 2018 (10,015 images across 7 classes)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **96.49%**
  - *Inference Speedup:* **>3x vs Dynamic Routing CapsNet**
  - *Parameter Count:* **Significantly lower than traditional CapsNet**
- **Clinical Utility & Impact:** Preserves relative spatial orientation of atypical pigment networks without the computational bottleneck of standard capsule networks.

---

### Paper 10: Deep Clustering via Center-Oriented Margin Free-Triplet Loss for Skin Lesion Detection in Highly Imbalanced Datasets

- **Authors:** Ş. Öztürk; T. Çukur
- **Affiliation:** Department of Electrical and Electronics Engineering, Bilkent University, Ankara, Turkey; National Magnetic Resonance Research Center (UMRAM), Bilkent University, Ankara, Turkey
- **Venue:** IEEE Journal of Biomedical and Health Informatics (2022) | **DOI:** `10.1109/JBHI.2022.3187215` | **IEEE Article:** `9810181`
- **PDF File:** `11_S._Ozturk_2022_Deep_Clustering_via_Center-Oriented_Margin_Free-Triplet_Loss_for_Skin_Lesion_Det.pdf`
- **Methodological Category:** Deep Metric Clustering & Margin-Free Loss

#### Clinical & Technical Problem
Extreme class imbalance in dermatological archives causes standard cross-entropy models to collapse toward majority benign nevi, severely penalizing minority malignancies.

#### Primary Research Objective (General Aim)
> **To formulate a deep clustering framework utilizing a novel center-oriented margin-free triplet loss to enhance lesion discrimination in highly imbalanced datasets.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Latent Metric Embedding):** To develop a deep metric learning clustering mechanism that projects lesion embeddings into a compact latent space organized around distinct class centroids.
- **RO2 (Center-Oriented Margin-Free Triplet Loss):** To formulate a margin-free triplet loss that dynamically pulls samples toward their class centers while repelling other class clusters without requiring sensitive margin hyperparameter tuning.
- **RO3 (Class Imbalance Regularization):** To mitigate majority-class gradient dominance by enforcing equal cluster pull and geometric dispersion across all minority lesion categories.
- **RO4 (Multi-Benchmark Assessment):** To validate diagnostic sensitivity, specificity, and AUC on heavily skewed ISIC 2017 and ISIC 2018 datasets against state-of-the-art loss functions.
- **RO5 (Minority Malignancy Sensitivity):** To dramatically improve clinical recall on rare, lethal cutaneous conditions including dermatofibroma and vascular lesions.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Deep clustering, center-oriented margin-free triplet loss, metric learning embedding, class centroid optimization.
- **Evaluated Datasets:** ISIC 2017, ISIC 2018 / HAM10000 (highly imbalanced benchmark partitions)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **91.8%**
  - *Minority Class Sensitivity Gain:* **+14.2% vs Softmax Cross-Entropy**
  - *AUC:* **0.94**
- **Clinical Utility & Impact:** Prevents computer-aided diagnostic models from ignoring rare malignant lesions, ensuring high sensitivity across the full spectrum of skin diseases.

---

### Paper 11: Neural Architecture Search for Skin Lesion Classification

- **Authors:** A. Kwasigroch; M. Grochowski; A. Mikołajczyk
- **Affiliation:** Department of Control Systems Engineering, Gdańsk University of Technology, Gdańsk, Poland
- **Venue:** IEEE Access (2020) | **DOI:** `10.1109/ACCESS.2020.2964424` | **IEEE Article:** `8950333`
- **PDF File:** `12_A._Kwasigroch_2020_Neural_Architecture_Search_for_Skin_Lesion_Classification.pdf`
- **Methodological Category:** Neural Architecture Search (NAS)

#### Clinical & Technical Problem
Manual engineering of CNN architectures for skin lesion analysis is heuristic, computationally labor-intensive, and prone to sub-optimal inductive biases.

#### Primary Research Objective (General Aim)
> **To deploy Neural Architecture Search (NAS) to automatically discover optimal, high-performing convolutional network topologies tailored for skin lesion classification.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Search Space Formulation):** To define an expressive neural architectural search space encompassing diverse convolutional kernel sizes, dilated operations, residual connections, and pooling schemes.
- **RO2 (Automated Architecture Search):** To execute reinforcement learning and gradient-based search algorithms to identify optimal cell topologies balancing parameter efficiency and diagnostic accuracy.
- **RO3 (Transfer Learning Integration):** To benchmark NAS-discovered architectures against human-designed pre-trained backbones (ResNet, MobileNet, Inception) on dermatoscopic tasks.
- **RO4 (Benchmark Diagnostic Evaluation):** To assess classification accuracy, balanced accuracy, and computational throughput on the benchmark ISIC 2018 dataset.
- **RO5 (Automated Medical Model Engineering):** To establish an automated, reproducible pipeline for discovering task-specific neural backbones for clinical dermatological imaging.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Neural Architecture Search (NAS), cell-based search space, automated topology optimization, ISIC 2018 benchmarking.
- **Evaluated Datasets:** ISIC 2018 (10,015 images across 7 classes)
- **Reported Performance Metrics:**
  - *Balanced Multiclass Accuracy:* **86.6%**
  - *Top-1 Accuracy:* **89.2%**
  - *Parameter Efficiency:* **Comparable accuracy with 40% fewer parameters than ResNet-50**
- **Clinical Utility & Impact:** Removes human trial-and-error bias from network design, producing customized architectures optimized specifically for dermoscopic image characteristics.

---

### Paper 12: Performance Enhancement of Skin Cancer Classification Using Computer Vision

- **Authors:** A. Magdy; H. Hussein; R. F. Abdel-Kader; K. A. E. Salam
- **Affiliation:** Department of Computers and Systems Engineering, Faculty of Engineering, Zagazig University, Zagazig, Egypt
- **Venue:** IEEE Access (2023) | **DOI:** `10.1109/ACCESS.2023.3294974` | **IEEE Article:** `10181245`
- **PDF File:** `13_A._Magdy_2023_Performance_Enhancement_of_Skin_Cancer_Classification_Using_Computer_Vision.pdf`
- **Methodological Category:** Hybrid Computer Vision & Transfer Learning

#### Clinical & Technical Problem
Low contrast between lesions and healthy skin, illumination variations, and lack of explicit morphological texture descriptors degrade CNN diagnostic sensitivity.

#### Primary Research Objective (General Aim)
> **To enhance skin cancer classification performance by developing a comprehensive computer vision pipeline combining bilateral filtering, Otsu segmentation, GLCM texture features, and deep transfer learning.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Edge-Preserving Filtering):** To apply bilateral filtering to reduce sensor noise and suppress background artifacts while preserving sharp lesion margin boundaries.
- **RO2 (Automated Lesion Boundary Delineation):** To implement Otsu thresholding and morphological post-processing to automatically segment lesion contours from surrounding healthy skin.
- **RO3 (Handcrafted & Deep Feature Fusion):** To extract Gray-Level Co-occurrence Matrix (GLCM) texture descriptors and concatenate them with deep convolutional representations.
- **RO4 (Transfer Learning Classification Benchmarking):** To benchmark transfer learning models (ResNet, DenseNet, VGG) trained on the fused feature space using the ISIC 2019 dataset.
- **RO5 (Diagnostic Precision Enhancement):** To enhance overall classification accuracy and sensitivity, aiding clinicians in discriminating malignant melanoma from benign nevi.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Bilateral filtering, Otsu segmentation, GLCM texture descriptor extraction, deep transfer learning feature fusion.
- **Evaluated Datasets:** ISIC 2019 (25,331 images across 8 categories)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **93.8%**
  - *Sensitivity:* **92.4%**
  - *Specificity:* **94.6%**
  - *F1-Score:* **93.2%**
- **Clinical Utility & Impact:** Combines clinical domain texture knowledge (GLCM) with deep semantic abstractions, enhancing diagnostic explainability for border irregularities.

---

### Paper 13: EFAM-Net: A Multi-Class Skin Lesion Classification Model Utilizing Enhanced Feature Fusion and Attention Mechanisms

- **Authors:** Z. Ji; X. Wang; C. Liu; Z. Wang; N. Yuan; I. Ganchev
- **Affiliation:** College of Computer Science and Technology, Qingdao University, Qingdao, China
- **Venue:** IEEE Access (2024) | **DOI:** `10.1109/ACCESS.2024.3468612` | **IEEE Article:** `10695064`
- **PDF File:** `14_Z._Ji_2024_EFAM-Net_A_Multi-Class_Skin_Lesion_Classification_Model_Utilizing_Enhanced_Featu.pdf`
- **Methodological Category:** Multi-Scale Attention & Enhanced Feature Fusion

#### Clinical & Technical Problem
Subtle inter-class differences between malignant and benign lesions and multi-scale morphological variations hinder fine-grained multi-class classification.

#### Primary Research Objective (General Aim)
> **To design and validate 'EFAM-Net', an advanced multi-class skin lesion classification network integrating Enhanced Feature Fusion and Attention Mechanisms.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Multi-Scale Feature Extraction):** To construct multi-branch convolutional blocks capable of simultaneously extracting multi-scale spatial representations and fine micro-textural details.
- **RO2 (Channel & Spatial Attention Modules):** To integrate dual attention mechanisms that suppress background skin artifacts and dynamically highlight lesion-specific diagnostic patterns.
- **RO3 (Enhanced Feature Fusion Block):** To formulate an adaptive feature fusion module that seamlessly merges shallow boundary features with deep semantic representations.
- **RO4 (Multiclass Benchmark Validation):** To rigorously benchmark EFAM-Net on the ISIC 2018 and HAM10000 multi-class datasets measuring accuracy, precision, recall, and F1-score.
- **RO5 (Clinical Diagnostic Triage Support):** To deliver superior discrimination across seven lesion categories to support automated multi-class triage in dermatology clinics.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** EFAM-Net architecture, multi-scale convolutional branches, dual spatial/channel attention, adaptive feature fusion module.
- **Evaluated Datasets:** ISIC 2018 / HAM10000 (10,015 images across 7 classes)
- **Reported Performance Metrics:**
  - *Overall Accuracy:* **93.2%**
  - *Precision:* **92.8%**
  - *Recall:* **93.0%**
  - *F1-Score:* **92.9%**
- **Clinical Utility & Impact:** Dynamically attends to subtle clinical diagnostic structures (pigment networks, dots, globules) regardless of lesion size or magnification.

---

### Paper 14: Hair Segmentation and Removal in Dermoscopic Images Using Deep Learning

- **Authors:** L. Talavera-Martínez; P. Bibiloni; M. González-Hidalgo
- **Affiliation:** Department of Mathematics and Computer Science, University of the Balearic Islands, Palma, Spain; Health Research Institute of the Balearic Islands (IdISBa), Palma, Spain
- **Venue:** IEEE Access (2021) | **DOI:** `10.1109/ACCESS.2020.3047258` | **IEEE Article:** `9306830`
- **PDF File:** `15_L._Talavera-Martinez_2021_Hair_Segmentation_and_Removal_in_Dermoscopic_Images_Using_Deep_Learning.pdf`
- **Methodological Category:** Deep Hair Segmentation & Context-Aware Inpainting

#### Clinical & Technical Problem
Occluding hair shafts distort lesion borders and corrupt textural feature extraction, while classical heuristic filters like DullRazor blur underlying micro-vascular patterns.

#### Primary Research Objective (General Aim)
> **To develop a deep learning-based hair segmentation and context-aware inpainting system that removes hair artifacts from dermoscopic images without destroying genuine lesion borders.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Synthetic & Real Hair Data Modeling):** To construct a comprehensive training corpus of dermoscopic images paired with realistic synthetic and manually annotated real hair masks across diverse skin phototypes.
- **RO2 (Deep Hair Segmentation U-Net):** To design and train a modified U-Net architecture to precisely isolate both fine and coarse hair artifacts across variable lighting and skin tones.
- **RO3 (Context-Aware Deep Inpainting):** To formulate a deep inpainting network to reconstruct occluded underlying skin textures without inducing blurring or artificial edge boundaries.
- **RO4 (Comparative Benchmark Assessment):** To quantitatively evaluate hair segmentation (Dice coefficient, Jaccard index) and downstream classification impact against classical DullRazor on ISIC benchmarks.
- **RO5 (Artifact-Free Dermatoscopy Preservation):** To provide clean, artifact-free dermoscopic imagery that preserves delicate atypical pigment networks for accurate dermatologist evaluation.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Modified U-Net hair segmentation, realistic synthetic hair generation, context-aware deep inpainting, comparison with DullRazor.
- **Evaluated Datasets:** ISIC 2018 Hair Dataset subsets (annotated real hair masks + synthetic hair model)
- **Reported Performance Metrics:**
  - *Hair Segmentation Dice:* **92.8%**
  - *Jaccard Index:* **87.2%**
  - *Downstream Classification Accuracy Gain:* **+4.2% vs Raw Images, +2.1% vs DullRazor**
- **Clinical Utility & Impact:** Removes thick and translucent hair shafts without distorting lesion margins, preventing false-positive melanoma diagnoses caused by hair occlusions.

---

### Paper 15: Dermoscopy Image Classification Based on StyleGANs and Decision Fusion

- **Authors:** A. Gong; X. Yao; W. Lin
- **Affiliation:** College of Computer Science and Technology, China University of Petroleum (East China), Qingdao, China
- **Venue:** IEEE Access (2020) | **DOI:** `10.1109/ACCESS.2020.2986916` | **IEEE Article:** `9062473`
- **PDF File:** `16_A._Gong_2020_Dermoscopy_Image_Classification_Based_on_StyleGANs_and_Decision_Fusion.pdf`
- **Methodological Category:** Generative Augmentation & Decision Fusion

#### Clinical & Technical Problem
Severe shortage and skewed distribution of rare malignant skin lesion images restrict deep neural network generalization and cause biased clinical triage.

#### Primary Research Objective (General Aim)
> **To develop a dermatoscopic classification framework combining StyleGAN-based synthetic minority class image generation with multi-model decision fusion.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Photorealistic Synthetic Lesion Generation):** To train StyleGAN architectures on rare cutaneous lesion classes to synthesize photorealistic, high-resolution dermoscopic training samples.
- **RO2 (Dataset Balancing Strategy):** To augment unbalanced training distributions with synthesized minority samples to eliminate model bias toward majority benign nevi.
- **RO3 (Multi-Model Deep Feature Learning):** To train diverse deep CNN architectures (ResNet, Inception, DenseNet) on the balanced synthetic-augmented corpus to learn robust representations.
- **RO4 (Optimal Decision Fusion Design):** To formulate an optimal decision fusion scheme integrating individual network probability outputs for stabilized final classification.
- **RO5 (Benchmark Generalization Assessment):** To validate classification accuracy, sensitivity, and specificity improvements on the benchmark ISIC 2017 and ISIC 2018 datasets.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** StyleGAN synthetic generation, minority class balancing, multi-CNN ensemble (ResNet, Inception, DenseNet), probability decision fusion.
- **Evaluated Datasets:** ISIC 2017 (2,000 train, 600 test), ISIC 2018 (10,015 images)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **91.2%**
  - *Minority Sensitivity Gain:* **+9.5%**
  - *AUC:* **0.93**
- **Clinical Utility & Impact:** Overcomes extreme clinical data scarcity for rare skin malignancies by generating clinically realistic training samples that enhance model sensitivity.

---

### Paper 16: A Comprehensive Joint Learning System to Detect Skin Cancer

- **Authors:** L. Riaz; H. M. Qadir; G. Ali; M. Ali; M. A. Raza; A. D. Jurcut; J. Ali
- **Affiliation:** Department of Computer Science and Information Technology, Superior University, Lahore, Pakistan; School of Computer Science, University College Dublin, Dublin, Ireland
- **Venue:** IEEE Access (2023) | **DOI:** `10.1109/ACCESS.2023.3297644` | **IEEE Article:** `10189856`
- **PDF File:** `18_L._Riaz_2023_A_Comprehensive_Joint_Learning_System_to_Detect_Skin_Cancer.pdf`
- **Methodological Category:** Comprehensive Joint Learning System

#### Clinical & Technical Problem
Independent training of feature extraction and classification modules leads to suboptimal representations and vulnerability to noisy clinical dermatoscopic data.

#### Primary Research Objective (General Aim)
> **To propose a comprehensive joint learning framework that couples shared representation learning with multi-task objective optimization for robust skin cancer detection.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Joint Representation Architecture):** To construct a unified deep neural architecture that shares intermediate representations across auxiliary classification and feature-regularization tasks.
- **RO2 (Multi-Objective Loss Formulation):** To formulate a joint loss function balancing primary diagnostic cross-entropy with auxiliary representation consistency penalties.
- **RO3 (Noise-Robust Feature Extraction):** To enhance model robustness against dermoscopic sensor noise, illumination gradients, and boundary artifact variations.
- **RO4 (Comprehensive Benchmark Assessment):** To evaluate classification accuracy, sensitivity, specificity, and F1-score across all 7 pathological categories on the HAM10000 dataset.
- **RO5 (Diagnostic Stability Enhancement):** To stabilize diagnostic accuracy across all seven clinical lesion categories, preventing catastrophic false-negative underdiagnosis.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Joint multi-task deep learning architecture, shared latent representations, multi-objective loss function, HAM10000 benchmarking.
- **Evaluated Datasets:** HAM10000 (10,015 images across 7 classes: akiec, bcc, bkl, df, mel, nv, vasc)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **92.4%**
  - *Sensitivity:* **91.8%**
  - *Specificity:* **93.0%**
  - *F1-Score:* **92.1%**
- **Clinical Utility & Impact:** Delivers consistent, noise-tolerant diagnostic performance across varied imaging hardware in clinical dermatology departments.

---

### Paper 17: Melanoma Detection Using an Objective System Based on Multiple Connected Neural Networks

- **Authors:** L. Ichim; D. Popescu
- **Affiliation:** Department of Automatic Control and Electrical Engineering, National University of Science and Technology Politehnica Bucharest, Bucharest, Romania
- **Venue:** IEEE Access (2020) | **DOI:** `10.1109/ACCESS.2020.3028248` | **IEEE Article:** `9210626`
- **PDF File:** `20_L._Ichim_2020_Melanoma_Detection_Using_an_Objective_System_Based_on_Multiple_Connected_Neural_.pdf`
- **Methodological Category:** Multiple Connected Networks & Evidence Theory

#### Clinical & Technical Problem
Subjectivity, visual fatigue, and conflicting feature cues cause diagnostic variability among dermatologists and automated classifiers during melanoma screening.

#### Primary Research Objective (General Aim)
> **To develop an objective, multi-network decision system combining color, texture, and geometry neural networks with Dempster-Shafer evidence theory for melanoma detection.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Dedicated Morphological Sub-Networks):** To develop dedicated neural network branches specialized in extracting color, texture, and geometric lesion characteristics independently.
- **RO2 (Dempster-Shafer Evidence Integration):** To integrate Dempster-Shafer evidence theory to fuse uncertain, multi-source probability masses into a unified, mathematically rigorous diagnostic decision.
- **RO3 (Objective Diagnostic Scoring):** To establish an objective malignancy confidence score that eliminates subjective human interpretation bias.
- **RO4 (Multi-Benchmark Validation):** To benchmark the multi-network system on the PH2 and ISIC datasets, measuring accuracy, sensitivity, specificity, and ROC-AUC.
- **RO5 (Explainable Clinical Decision Support):** To provide clinicians with an objective second-opinion tool that explains diagnostic confidence across distinct morphological dimensions.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Three connected neural networks (color, texture, geometry branches), Dempster-Shafer evidence theory fusion, rule-based conflict resolution.
- **Evaluated Datasets:** PH2 (200 images: 80 common nevi, 80 atypical nevi, 40 melanomas), ISIC dataset subsets
- **Reported Performance Metrics:**
  - *Overall Accuracy:* **94.7%**
  - *Sensitivity:* **94.0%**
  - *Specificity:* **95.2%**
  - *AUC:* **0.96**
- **Clinical Utility & Impact:** Mimics the multi-faceted cognitive assessment of senior dermatologists by evaluating color, texture, and border irregularity in separate explainable streams.

---

### Paper 18: DermCDSM: Clinical Decision Support Model for Dermatosis Using Systematic Approaches of Machine Learning and Deep Learning

- **Authors:** R. Mittal; F. Jeribi; R. J. Martin; V. Malik; S. J. Menachery; J. Singh
- **Affiliation:** Department of Computer Science and Engineering, Chitkara University Institute of Engineering and Technology, Chitkara University, Punjab, India; College of Computer Science and Information Technology, King Khalid University, Abha, Saudi Arabia
- **Venue:** IEEE Access (2024) | **DOI:** `10.1109/ACCESS.2024.3373539` | **IEEE Article:** `10459206`
- **PDF File:** `21_R._Mittal_2024_DermCDSM_Clinical_Decision_Support_Model_for_Dermatosis_Using_Systematic_Approac.pdf`
- **Methodological Category:** Clinical Decision Support & Systematic ML/DL

#### Clinical & Technical Problem
Misalignment between purely data-driven deep features and established clinical dermatological diagnostic criteria (e.g., ABCD rules, patient demographics) creates physician distrust.

#### Primary Research Objective (General Aim)
> **To develop 'DermCDSM', a clinical decision support model for dermatosis integrating systematic machine learning and deep learning methodologies with clinical features.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Clinical ABCD Feature Engineering):** To extract clinically grounded morphological, geometric, and color descriptors strictly aligned with dermatological diagnostic rules (ABCD criteria).
- **RO2 (Deep Semantic Representation Extraction):** To extract deep semantic representations using pre-trained convolutional neural networks and fuse them with hand-crafted clinical descriptors.
- **RO3 (Systematic Machine Learning Benchmarking):** To systematically evaluate diverse machine learning algorithms (Random Forest, SVM, XGBoost) and deep networks on the fused feature space.
- **RO4 (Multi-Class Dermatosis Assessment):** To validate diagnostic performance on HAM10000 and DermNet datasets across diverse dermatosis conditions measuring accuracy and F1-score.
- **RO5 (Clinical Decision Support Tooling):** To establish a validated clinical decision support model that bridges the gap between deep learning outputs and real-world dermatological workflows.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** DermCDSM framework, clinical ABCD rule extraction, deep feature fusion, systematic ML comparison (SVM, RF, XGBoost, CNN).
- **Evaluated Datasets:** HAM10000 (10,015 images), DermNet clinical image repository
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **94.1%**
  - *Precision:* **93.8%**
  - *Recall:* **94.2%**
  - *F1-Score:* **94.0%**
- **Clinical Utility & Impact:** Aligns AI diagnostic reasoning with the ABCD clinical criteria that dermatologists are trained to inspect, facilitating immediate clinical interpretation.

---

### Paper 19: A Hybrid Deep Learning Approach for Skin Cancer Classification Using Swin Transformer and Dense Group Shuffle Non-Local Attention Network

- **Authors:** R. Karthik; R. Menaka; S. Atre; J. Cho; S. Veerappampalayam Easwaramoorthy
- **Affiliation:** School of Electronics Engineering, Vellore Institute of Technology, Chennai, India; Department of Computer Science and Engineering, Kyung Hee University, Yongin, South Korea
- **Venue:** IEEE Access (2024) | **DOI:** `10.1109/ACCESS.2024.3485507` | **IEEE Article:** `10731679`
- **PDF File:** `22_R._Karthik_2024_A_Hybrid_Deep_Learning_Approach_for_Skin_Cancer_Classification_Using_Swin_Transf.pdf`
- **Methodological Category:** Swin Transformer & Non-Local Attention

#### Clinical & Technical Problem
Standard CNNs struggle to capture long-range contextual dependencies and global spatial relationships across large, diffuse skin lesions.

#### Primary Research Objective (General Aim)
> **To develop a hybrid deep learning architecture combining a Swin Transformer backbone with a Dense Group Shuffle Non-Local Attention Network (DGS-NLNet) for skin cancer classification.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Hierarchical Vision Transformer Modeling):** To employ a Swin Transformer backbone with shifted window self-attention to model long-range spatial dependencies at multiple resolutions.
- **RO2 (Dense Group Shuffle Non-Local Attention):** To formulate a Dense Group Shuffle Non-Local Attention Network (DGS-NLNet) to enhance cross-channel information exchange and capture non-local contextual cues.
- **RO3 (Multi-Scale Local-Global Feature Fusion):** To fuse transformer self-attention representations with dense convolutional features to capture both fine local textures and global lesion topology.
- **RO4 (Diagnostic Benchmark Validation):** To quantitatively validate classification accuracy, sensitivity, specificity, and AUC on the ISIC 2019 and ISIC 2020 datasets.
- **RO5 (State-of-the-Art Lesion Discrimination):** To achieve superior diagnostic discrimination on challenging, borderline melanocytic and non-melanocytic lesions.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Swin Transformer backbone, shifted window self-attention, Dense Group Shuffle Non-Local Attention Network (DGS-NLNet), cross-scale feature fusion.
- **Evaluated Datasets:** ISIC 2019 (25,331 images), ISIC 2020 (33,126 images)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **96.8%**
  - *Sensitivity:* **95.9%**
  - *Specificity:* **97.4%**
  - *AUC:* **0.982**
- **Clinical Utility & Impact:** Captures both micro-dermatoscopic textural patterns and overall macro-lesion architecture, providing highly reliable classification for extensive, spreading lesions.

---

### Paper 20: Analysis of Skin Marks Through the Use of Intelligent Things

- **Authors:** D. Połap
- **Affiliation:** Institute of Mathematics, Silesian University of Technology, Gliwice, Poland
- **Venue:** IEEE Access (2019) | **DOI:** `10.1109/ACCESS.2019.2947354` | **IEEE Article:** `8868149`
- **PDF File:** `23_D._Poap_2019_Analysis_of_Skin_Marks_Through_the_Use_of_Intelligent_Things.pdf`
- **Methodological Category:** Intelligent Things & IoT Edge Diagnosis

#### Clinical & Technical Problem
High latency, cloud dependency, and resource constraints prevent the deployment of complex deep neural networks on portable Internet of Things (IoT) edge diagnostic hardware.

#### Primary Research Objective (General Aim)
> **To design and implement an Intelligent Things framework utilizing distributed neural networks and cascading classifiers for on-device skin mark analysis.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Distributed Edge Neural Architecture):** To design a lightweight, distributed neural processing architecture capable of executing on resource-constrained embedded edge devices.
- **RO2 (Cascading Classifier Formulation):** To formulate a cascading classification pipeline that triages lesions hierarchically, executing lightweight filters before invoking heavier neural modules.
- **RO3 (Real-Time Lesion Detection & Tracking):** To implement automated localization and tracking of cutaneous lesions from real-time smart device camera video streams.
- **RO4 (Embedded Prototype Benchmarking):** To measure diagnostic accuracy, inference latency, memory consumption, and battery efficiency on embedded hardware prototypes.
- **RO5 (Decentralized Healthcare Screening):** To enable continuous, decentralized skin health monitoring in remote and underserved populations without requiring cloud connectivity.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Intelligent Things distributed edge architecture, cascading neural classifiers, real-time video stream lesion tracking, embedded hardware execution.
- **Evaluated Datasets:** Curated clinical skin mark image repository and embedded camera video feeds
- **Reported Performance Metrics:**
  - *Edge Accuracy:* **91.5%**
  - *Inference Latency:* **<150ms on edge hardware**
  - *Energy Consumption:* **Optimized for mobile IoT battery life**
- **Clinical Utility & Impact:** Permits remote and rural healthcare workers to conduct instantaneous, offline dermatological screening without internet access.

---

### Paper 21: Early Detection of Multiclass Skin Lesions Using Transfer Learning-Based IncepX-Ensemble Model

- **Authors:** S. Chatterjee; J. -M. Gil; Y. -C. Byun
- **Affiliation:** Department of Computer Engineering, Jeju National University, Jeju, South Korea
- **Venue:** IEEE Access (2024) | **DOI:** `10.1109/ACCESS.2024.3432904` | **IEEE Article:** `10608138`
- **PDF File:** `24_S._Chatterjee_2024_Early_Detection_of_Multiclass_Skin_Lesions_Using_Transfer_Learning-Based_IncepX-.pdf`
- **Methodological Category:** Transfer Learning & Multi-Branch Ensembles

#### Clinical & Technical Problem
Single deep learning architectures often fail to generalize across diverse clinical dermatoscopic datasets due to specialized receptive field limitations.

#### Primary Research Objective (General Aim)
> **To formulate 'IncepX-Ensemble', a transfer learning-based ensemble architecture fusing InceptionV3, Xception, and ResNet models for early multi-class skin lesion detection.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Multi-Branch Deep Architecture):** To construct a multi-branch framework integrating pre-trained InceptionV3 (multi-scale kernels), Xception (depthwise separable convolutions), and ResNet (residual learning).
- **RO2 (Transfer Learning Domain Adaptation):** To fine-tune each constituent network using transfer learning protocols optimized for dermoscopic domain adaptation and class imbalance.
- **RO3 (Ensemble Soft-Voting Fusion):** To design an ensemble fusion strategy combining soft probability outputs to achieve robust multi-class prediction consensus.
- **RO4 (Multiclass Benchmark Assessment):** To evaluate diagnostic performance on the HAM10000 and ISIC 2018 datasets across 7 lesion classes, measuring accuracy, precision, recall, and F1-score.
- **RO5 (Early Malignancy Detection):** To maximize sensitivity for early malignant melanoma detection while maintaining high specificity across benign look-alikes.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** IncepX-Ensemble (InceptionV3 + Xception + ResNet), fine-tuned transfer learning, soft voting decision fusion.
- **Evaluated Datasets:** HAM10000 / ISIC 2018 (10,015 images across 7 classes)
- **Reported Performance Metrics:**
  - *Overall Accuracy:* **94.6%**
  - *Precision:* **94.1%**
  - *Recall:* **94.3%**
  - *F1-Score:* **94.2%**
- **Clinical Utility & Impact:** Synthesizes multi-scale receptive fields (Inception) and deep residual depth (ResNet) to prevent misdiagnosing early-stage melanomas as benign nevi.

---

### Paper 22: Classification for Dermoscopy Images Using Convolutional Neural Networks Based on the Ensemble of Individual Advantage and Group Decision

- **Authors:** A. Gong; X. Yao; W. Lin
- **Affiliation:** College of Computer Science and Technology, China University of Petroleum (East China), Qingdao, China
- **Venue:** IEEE Access (2020) | **DOI:** `10.1109/ACCESS.2020.3019210` | **IEEE Article:** `9175002`
- **PDF File:** `26_A._Gong_2020_Classification_for_Dermoscopy_Images_Using_Convolutional_Neural_Networks_Based_o.pdf`
- **Methodological Category:** Ensemble Learning & Group Decision Making

#### Clinical & Technical Problem
Different CNN architectures excel at recognizing specific lesion subclasses but perform poorly on others; simple averaging fails to exploit individual model strengths.

#### Primary Research Objective (General Aim)
> **To develop an ensemble classification framework for dermoscopy images based on individual model advantage weighting and collective group decision-making.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Per-Class Model Advantage Profiling):** To quantify and model the specific diagnostic advantages and per-class sensitivities of diverse deep CNN architectures.
- **RO2 (Dynamic Advantage Weighting):** To formulate an adaptive weighting mechanism that dynamically assigns higher voting power to the model with proven superiority for the predicted lesion class.
- **RO3 (Group Decision Consensus Rule):** To implement a group decision consensus algorithm that resolves classification conflicts and optimizes aggregate diagnostic precision.
- **RO4 (Comparative Benchmark Assessment):** To benchmark the framework against standalone CNNs and standard ensemble methods on ISIC 2017 and ISIC 2018 datasets.
- **RO5 (Diagnostic Stability Enhancement):** To demonstrate enhanced classification accuracy and balanced sensitivity across all evaluated skin cancer categories.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Individual advantage quantification, dynamic voting weighting, group decision consensus algorithm, multi-CNN ensemble.
- **Evaluated Datasets:** ISIC 2017 (2,000 train, 600 test), ISIC 2018 (10,015 images)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **92.7%**
  - *Balanced Accuracy:* **91.9%**
  - *Sensitivity Gain:* **+6.8% over uniform averaging**
- **Clinical Utility & Impact:** Emulates a medical board consultation by weighting each AI model according to its historical sub-specialty accuracy on specific disease types.

---

### Paper 23: Pipelined Structure in the Classification of Skin Lesions Based on Alexnet CNN and SVM Model With Bi-Sectional Texture Features

- **Authors:** V. S. S. B. T. Sathvika; N. Anmisha; V. Thanmayi; M. Suchetha; D. E. Dhas; S. Sehastrajit; S. N. Aakur
- **Affiliation:** Vellore Institute of Technology, Chennai, India; Centre for Healthcare Advancement, Innovation and Research, VIT, Chennai, India
- **Venue:** IEEE Access (2024) | **DOI:** `10.1109/ACCESS.2024.3387533` | **IEEE Article:** `10496674`
- **PDF File:** `27_V._S._S._B._T._Sathvika_2024_Pipelined_Structure_in_the_Classification_of_Skin_Lesions_Based_on_Alexnet_CNN_a.pdf`
- **Methodological Category:** Pipelined CNN-SVM & Bi-Sectional Textures

#### Clinical & Technical Problem
Pure end-to-end deep learning models often overlook subtle, hand-crafted directional texture variations and require massive datasets to learn fine surface patterns.

#### Primary Research Objective (General Aim)
> **To propose a pipelined classification framework combining AlexNet CNN deep feature extraction, bi-sectional texture feature engineering, and Support Vector Machine (SVM) classification.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Deep Convolutional Feature Extraction):** To utilize a pre-trained AlexNet CNN to extract high-level semantic representations from dermoscopic lesion images.
- **RO2 (Bi-Sectional Texture Engineering):** To formulate bi-sectional texture feature extraction algorithms to quantify directional surface irregularities and textural asymmetry across lesion halves.
- **RO3 (Hybrid Feature Concatenation):** To fuse deep CNN features with engineered bi-sectional texture descriptors into a unified, high-dimensional feature vector.
- **RO4 (SVM Kernel Classification):** To train and optimize a Support Vector Machine (SVM) classifier with kernel functions on the benchmark ISIC 2019 dataset.
- **RO5 (Diagnostic Sensitivity Validation):** To validate that combining explicit geometric-textural descriptors with deep features improves binary and multi-class lesion classification accuracy.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** AlexNet deep feature extraction, bi-sectional directional texture feature engineering, feature concatenation, SVM kernel classifier.
- **Evaluated Datasets:** ISIC 2019 (25,331 images across 8 categories)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **93.1%**
  - *Sensitivity:* **92.0%**
  - *Specificity:* **93.8%**
  - *AUC:* **0.95**
- **Clinical Utility & Impact:** Directly measures bilateral structural asymmetry, aligning algorithmic scoring with the 'A' (Asymmetry) parameter of standard clinical dermatoscopy.

---

### Paper 24: Improved Segmentation Model for Melanoma Lesion Detection Using Normalized Cross-Correlation-Based k-Means Clustering

- **Authors:** M. I. Faizi; S. M. Adnan
- **Affiliation:** Department of Computer Sciences, University of Engineering and Technology Taxila, Taxila, Pakistan
- **Venue:** IEEE Access (2024) | **DOI:** `10.1109/ACCESS.2024.3360223` | **IEEE Article:** `10416953`
- **PDF File:** `28_M._I._Faizi_2024_Improved_Segmentation_Model_for_Melanoma_Lesion_Detection_Using_Normalized_Cross.pdf`
- **Methodological Category:** Normalized Cross-Correlation & k-Means Segmentation

#### Clinical & Technical Problem
Low contrast, uneven lighting, and vague lesion borders lead to inaccurate boundary segmentation, causing downstream classification models to fail.

#### Primary Research Objective (General Aim)
> **To develop an improved segmentation model for melanoma lesion detection using Normalized Cross-Correlation (NCC) based k-means clustering.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (NCC Distance Metric Formulation):** To formulate a Normalized Cross-Correlation distance metric within the k-means clustering algorithm to replace Euclidean distance for illumination-invariant clustering.
- **RO2 (Adaptive Boundary Partitioning):** To apply the NCC-based clustering algorithm to accurately partition dermoscopic images into distinct lesion and healthy skin clusters.
- **RO3 (Morphological Mask Refinement):** To implement morphological post-processing operations (hole filling, boundary smoothing) to produce finalized binary lesion masks.
- **RO4 (Segmentation Benchmark Evaluation):** To evaluate segmentation accuracy, Dice coefficient, Jaccard index, and boundary error on the PH2 and ISIC 2017 benchmark datasets.
- **RO5 (Automated Clinical Preprocessing Pipeline):** To provide an automated, parameter-free segmentation front-end for computer-aided skin cancer diagnosis workflows.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Normalized Cross-Correlation (NCC) distance metric, modified k-means clustering, morphological post-processing.
- **Evaluated Datasets:** PH2 (200 images), ISIC 2017 segmentation challenge dataset
- **Reported Performance Metrics:**
  - *Segmentation Accuracy:* **96.2%**
  - *Dice Coefficient:* **91.8%**
  - *Jaccard Index:* **85.6%**
  - *Boundary Error:* **Significantly reduced vs standard k-means**
- **Clinical Utility & Impact:** Ensures robust boundary segmentation even in images with vignetting, shadow gradients, and lighting inconsistencies across clinical centers.

---

### Paper 25: Multiple Instance Learning Using 3D Features for Melanoma Detection

- **Authors:** P. M. M. Pereira; L. A. Thomaz; L. M. N. Tavora; P. A. A. Assuncao; R. Fonseca-Pinto; R. P. Paiva; S. M. M. Faria
- **Affiliation:** Instituto de Telecomunicações, Leiria, Portugal; Centre for Informatics and Systems, University of Coimbra, Coimbra, Portugal
- **Venue:** IEEE Access (2022) | **DOI:** `10.1109/ACCESS.2022.3192444` | **IEEE Article:** `9832874`
- **PDF File:** `29_P._M._M._Pereira_2022_Multiple_Instance_Learning_Using_3D_Features_for_Melanoma_Detection.pdf`
- **Methodological Category:** Multiple Instance Learning & 3D Dermoscopy

#### Clinical & Technical Problem
Standard 2D dermoscopic images lack depth and topography information, which are vital clinical indicators (e.g. elevation, nodularity) used by dermatologists to assess melanoma.

#### Primary Research Objective (General Aim)
> **To formulate a Multiple Instance Learning (MIL) framework leveraging 3D surface reconstruction and depth features for enhanced melanoma detection.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (3D Lesion Topography Reconstruction):** To reconstruct 3D surface topography and depth profiles of cutaneous lesions from multi-view or photometric dermoscopic images.
- **RO2 (Volumetric & Curvature Feature Extraction):** To extract volumetric, elevation, and surface curvature descriptors capturing 3D morphological characteristics unavailable in 2D imagery.
- **RO3 (Multiple Instance Learning Formulation):** To formulate a bag-of-instances MIL model that treats 3D lesion patches as instances within a patient bag to accommodate localized malignancy signals.
- **RO4 (Comparative Benchmark Assessment):** To evaluate melanoma detection sensitivity, specificity, and ROC-AUC on a clinical 3D dermoscopy benchmark dataset against 2D baselines.
- **RO5 (Topographical Diagnostic Verification):** To demonstrate that 3D morphological cues significantly improve discrimination between malignant melanoma and flat benign nevi.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** 3D photometric stereo reconstruction, volumetric and elevation feature extraction, Multiple Instance Learning (MIL) bag classification.
- **Evaluated Datasets:** Clinical 3D Dermoscopy Dataset (reconstructed 3D surface models paired with histology)
- **Reported Performance Metrics:**
  - *Melanoma Detection AUC:* **0.894**
  - *Sensitivity Gain over 2D:* **+7.3%**
  - *Specificity:* **88.1%**
- **Clinical Utility & Impact:** Adds the critical clinical dimension of lesion thickness and palpatory elevation to computational dermatoscopy without invasive physical biopsies.

---

### Paper 26: SPCB-Net: A Multi-Scale Skin Cancer Image Identification Network Using Self-Interactive Attention Pyramid and Cross-Layer Bilinear-Trilinear Pooling

- **Authors:** X. Qian; T. Weng; Q. Han; C. Wu; H. Xu; M. Hou; Z. Qiu; B. Zhou; X. Gao
- **Affiliation:** School of Intelligent Technology and Engineering, Chongqing University of Science and Technology, Chongqing, China
- **Venue:** IEEE Access (2024) | **DOI:** `10.1109/ACCESS.2023.3347424` | **IEEE Article:** `10374026`
- **PDF File:** `31_X._Qian_2024_SPCB-Net_A_Multi-Scale_Skin_Cancer_Image_Identification_Network_Using_Self-Inter.pdf`
- **Methodological Category:** Multi-Scale Attention & Bilinear-Trilinear Pooling

#### Clinical & Technical Problem
Skin lesions display immense multi-scale variations in size and shape, while conventional pooling loses fine-grained cross-layer interaction details.

#### Primary Research Objective (General Aim)
> **To develop 'SPCB-Net', a multi-scale skin cancer identification network utilizing a Self-Interactive Attention Pyramid and Cross-Layer Bilinear-Trilinear Pooling.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Self-Interactive Attention Pyramid):** To construct a self-interactive attention pyramid network that recursively captures and correlates multi-scale spatial and semantic representations.
- **RO2 (Cross-Layer Bilinear-Trilinear Pooling):** To formulate a cross-layer bilinear-trilinear pooling module that models complex second- and third-order feature interactions across disparate CNN layers.
- **RO3 (Fine-Grained Lesion Discrimination):** To enhance the network's ability to discriminate fine-grained pigment patterns, regression structures, and irregular border striations.
- **RO4 (Multi-Benchmark Validation):** To validate SPCB-Net on the ISIC 2018 and ISIC 2019 datasets, assessing accuracy, precision, recall, and F1-score across all lesion classes.
- **RO5 (Clinical Diagnostic Advancement):** To outperform existing multi-scale CNN architectures on challenging multi-class skin cancer classification tasks.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** SPCB-Net architecture, self-interactive attention pyramid, cross-layer bilinear-trilinear feature pooling, multi-scale correlation.
- **Evaluated Datasets:** ISIC 2018 (10,015 images), ISIC 2019 (25,331 images)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **95.3%**
  - *Precision:* **94.8%**
  - *Recall/Sensitivity:* **95.1%**
  - *F1-Score:* **94.9%**
- **Clinical Utility & Impact:** Captures multi-scale diagnostic patterns simultaneously, enabling detection of subtle malignant micro-structures within larger benign nevi.

---

### Paper 27: IARS SegNet: Interpretable Attention Residual Skip Connection SegNet for Melanoma Segmentation

- **Authors:** V. S. Narayanan; O. K. Sikha; R. Benitez
- **Affiliation:** Department of Computer Science and Engineering, Amrita School of Computing, Amrita Vishwa Vidyapeetham, Amritapuri, India; Department of Automatic Control, Universitat Politècnica de Catalunya, Barcelona, Spain
- **Venue:** IEEE Access (2024) | **DOI:** `10.1109/ACCESS.2024.3404224` | **IEEE Article:** `10536875`
- **PDF File:** `32_V._S._Narayanan_2024_IARS_SegNet_Interpretable_Attention_Residual_Skip_Connection_SegNet_for_Melanoma.pdf`
- **Methodological Category:** Interpretable Attention & Residual Skip Segmentation

#### Clinical & Technical Problem
Precise delineation of melanoma borders is difficult due to diffuse transitions into normal skin, and black-box segmentation models lack clinical explainability.

#### Primary Research Objective (General Aim)
> **To design and validate 'IARS SegNet', an Interpretable Attention Residual Skip Connection SegNet architecture for automated melanoma segmentation.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Attention Residual Skip Architecture):** To formulate encoder-decoder skip connections embedded with attention gates and residual connections to preserve delicate edge details and spatial resolution.
- **RO2 (Boundary-Refined Segmentation):** To enhance gradient flow and feature propagation to accurately delineate irregular, indistinct melanoma borders from healthy skin.
- **RO3 (Explainable Visual Attention Maps):** To generate interpretable spatial attention maps that visualize the anatomical regions prioritized by the network during boundary delineation.
- **RO4 (Multi-Benchmark Segmentation Assessment):** To rigorously benchmark IARS SegNet against U-Net, SegNet, and state-of-the-art architectures on the ISIC 2017, ISIC 2018, and PH2 datasets.
- **RO5 (Surgical Margin Planning Assistance):** To provide transparent, highly accurate lesion masks to assist surgeons and dermatologists in surgical excision margin planning.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** IARS SegNet architecture, attention gates, residual skip connections, interpretable attention heatmaps, multi-dataset benchmarking.
- **Evaluated Datasets:** ISIC 2017, ISIC 2018, PH2 (200 clinical images)
- **Reported Performance Metrics:**
  - *Dice Coefficient:* **94.5%**
  - *Jaccard Index:* **89.6%**
  - *Boundary Error:* **Significantly lower than baseline SegNet and U-Net**
- **Clinical Utility & Impact:** Provides transparent visual justifications for boundary demarcations, reducing the risk of incomplete surgical excision or excessive healthy tissue removal.

---

### Paper 28: Toward Better Ear Disease Diagnosis: A Multi-Modal Multi-Fusion Model Using Endoscopic Images of the Tympanic Membrane and Pure-Tone Audiometry

- **Authors:** T. Kim; S. Kim; J. Kim; Y. Lee; J. Choi
- **Affiliation:** Department of Applied Artificial Intelligence, Hanyang University, Ansan, South Korea; Department of Otorhinolaryngology-Head and Neck Surgery, Korea University College of Medicine, Seoul, South Korea
- **Venue:** IEEE Access (2023) | **DOI:** `10.1109/ACCESS.2023.3325346` | **IEEE Article:** `10286540`
- **PDF File:** `33_T._Kim_2023_Toward_Better_Ear_Disease_Diagnosis_A_Multi-Modal_Multi-Fusion_Model_Using_Endos.pdf`
- **Methodological Category:** Multimodal Fusion (Endoscopic Imagery + Audiometry)

#### Clinical & Technical Problem
Single-modality diagnostic tools fail to capture the complete clinical picture of ear pathologies, where physical tympanic membrane appearance and functional hearing loss data are complementary.

#### Primary Research Objective (General Aim)
> **To develop a multi-modal multi-fusion deep learning framework combining endoscopic tympanic membrane images and pure-tone audiometry (PTA) numerical data for ear disease diagnosis.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Endoscopic Visual Feature Extraction):** To construct a deep convolutional pipeline to extract visual textural, color, and structural patterns from endoscopic tympanic membrane imagery.
- **RO2 (Audiometric Numerical Data Encoding):** To design a dedicated neural encoder for pure-tone audiometry (PTA) hearing threshold data measured across multiple acoustic frequencies.
- **RO3 (Multi-Modal Multi-Fusion Scheme):** To formulate intermediate and late fusion mechanisms to integrate heterogeneous visual and acoustic representations into a unified diagnostic space.
- **RO4 (Clinical Pathology Assessment):** To evaluate diagnostic accuracy across multiple ear disease categories on a large, curated multi-modal clinical dataset.
- **RO5 (Holistic Multimodal Diagnostic Paradigm):** To demonstrate that fusing physical examination imagery with functional clinical test results significantly outperforms unimodal diagnostic baselines.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Dual-branch multimodal CNN, pure-tone audiometry numerical encoder, intermediate/late multimodal fusion, multi-class ear pathology classification.
- **Evaluated Datasets:** Clinical Multimodal Otology Repository (paired endoscopic tympanic images and pure-tone audiograms)
- **Reported Performance Metrics:**
  - *Multimodal Accuracy:* **91.2%**
  - *Unimodal Image-Only Accuracy:* **84.3%**
  - *Unimodal Audio-Only Accuracy:* **78.6%**
  - *AUC:* **0.95**
- **Clinical Utility & Impact:** Integrates structural otoscopy with functional audiometry, preventing misdiagnoses that arise when visual findings alone are ambiguous.

---

### Paper 29: Classification of Skin Lesion With Features Extraction Using Quantum Chebyshev Polynomials and Autoencoder From Wavelet-Transformed Images

- **Authors:** Farhatullah; X. Chen; D. Zeng; J. Xu; R. Nawaz; R. Ullah
- **Affiliation:** School of Computer Science, China University of Geosciences, Wuhan, China; School of Automation, China University of Geosciences, Wuhan, China
- **Venue:** IEEE Access (2024) | **DOI:** `10.1109/ACCESS.2024.3502513` | **IEEE Article:** `10757392`
- **PDF File:** `34_Farhatullah_2024_Classification_of_Skin_Lesion_With_Features_Extraction_Using_Quantum_Chebyshev_P.pdf`
- **Methodological Category:** Quantum-Inspired Features & Autoencoders

#### Clinical & Technical Problem
High-dimensional dermoscopic images contain redundant background information and subtle frequency-specific textures that standard convolutions fail to extract efficiently.

#### Primary Research Objective (General Aim)
> **To propose a novel feature extraction and classification methodology utilizing Quantum Chebyshev Polynomials and deep autoencoders from 2D wavelet-transformed dermoscopy images.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Wavelet Multi-Resolution Decomposition):** To apply 2D discrete wavelet transforms to decompose dermoscopic images into distinct frequency sub-bands, separating low-frequency morphology from high-frequency textures.
- **RO2 (Quantum Chebyshev Feature Extraction):** To formulate quantum-inspired Chebyshev polynomials to extract compact, orthogonal feature descriptors from multi-scale wavelet sub-bands.
- **RO3 (Deep Autoencoder Latent Compression):** To train a deep autoencoder to compress and reconstruct the quantum polynomial representations into a highly discriminative latent space.
- **RO4 (Diagnostic Classification Benchmarking):** To evaluate classification accuracy, sensitivity, and specificity on the ISIC 2018 and ISIC 2019 datasets using standard machine learning classifiers.
- **RO5 (Computational Complexity Reduction):** To achieve state-of-the-art diagnostic discrimination with a drastically reduced feature dimensionality and lower computational complexity.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** 2D Discrete Wavelet Transform, Quantum Chebyshev Polynomials, deep autoencoder dimensionality reduction, multi-class classification.
- **Evaluated Datasets:** ISIC 2018 (10,015 images), ISIC 2019 (25,331 images)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **94.8%**
  - *Sensitivity:* **93.9%**
  - *Specificity:* **95.4%**
  - *Dimensionality Reduction:* **>70% feature compression**
- **Clinical Utility & Impact:** Captures directional micro-vessel and pigment patterns across frequency bands while requiring minimal computational memory.

---

### Paper 30: Integrating Clinical Knowledge Graphs and Gradient-Based Neural Systems for Enhanced Melanoma Diagnosis via the Seven-Point Checklist

- **Authors:** Y. Wang; T. Yu; J. Cai; S. Kalia; H. Lui; Z. Jane Wang; T. K. Lee
- **Affiliation:** Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC, Canada; Department of Dermatology and Skin Science, University of British Columbia, Vancouver, BC, Canada
- **Venue:** IEEE Transactions on Neural Networks and Learning Systems (2026) | **DOI:** `10.1109/TNNLS.2025.3600443` | **IEEE Article:** `11151232`
- **PDF File:** `35_Y._Wang_2026_Integrating_Clinical_Knowledge_Graphs_and_Gradient-Based_Neural_Systems_for_Enha.pdf`
- **Methodological Category:** Clinical Knowledge Graphs & Rule-Based Neural Integration

#### Clinical & Technical Problem
Disconnect between deep learning 'black boxes' and standard dermatological diagnostic protocols (such as the Seven-Point Checklist) leads to clinician distrust and regulatory hurdles.

#### Primary Research Objective (General Aim)
> **To integrate clinical knowledge graphs with gradient-based neural systems for enhanced, explainable melanoma diagnosis grounded in the dermatoscopic Seven-Point Checklist.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Seven-Point Criteria Graph Formulation):** To construct a formal clinical knowledge graph encoding the Seven-Point Checklist criteria (atypical pigment network, blue-whitish veil, vascular structures, etc.) and their diagnostic weights.
- **RO2 (Gradient-Based Neural-Symbolic Mapping):** To develop a gradient-based neural framework that maps visual dermoscopic features directly to individual checklist criteria nodes within the knowledge graph.
- **RO3 (Explainable Diagnostic Path Reasoning):** To formulate a reasoning engine that generates final malignancy predictions by traversing knowledge graph paths, providing explicit medical explanations.
- **RO4 (Clinical Benchmark Assessment):** To benchmark the system on the ISIC Seven-Point Checklist dataset, evaluating diagnostic accuracy, sensitivity, and criteria attribution fidelity.
- **RO5 (Trustworthy Clinical AI Alignment):** To deliver an auditable, transparent diagnostic tool that aligns directly with dermatologists' cognitive decision-making processes.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Neural-symbolic integration, clinical knowledge graph, gradient-based neural mapping, Seven-Point Checklist criteria attribution.
- **Evaluated Datasets:** ISIC Seven-Point Checklist Benchmark Dataset (2,000 dermoscopy images with expert criteria annotations)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **87.4%**
  - *Checklist Criteria Prediction Accuracy:* **89.1%**
  - *AUC:* **0.93**
  - *Clinician Agreement Rate:* **91.5%**
- **Clinical Utility & Impact:** Produces diagnosis explanations in standard dermatological terminology (e.g., 'Malignancy suspected due to atypical pigment network and blue-whitish veil presence').

---

### Paper 31: A Hybrid Model for Early Melanoma Detection: Integrating YOLOv9 and Faster R-CNN for Enhanced Diagnostic Accuracy

- **Authors:** M. I. Marie; M. S. Elredeny; A. Essayed Yakoub
- **Affiliation:** Department of Information Systems, Faculty of Computers and Artificial Intelligence, Helwan University, Cairo, Egypt
- **Venue:** IEEE Access (2025) | **DOI:** `10.1109/ACCESS.2025.3587625` | **IEEE Article:** `11077147`
- **PDF File:** `36_M._I._Marie_2025_A_Hybrid_Model_for_Early_Melanoma_Detection_Integrating_YOLOv9_and_Faster_R-CNN_.pdf`
- **Methodological Category:** Hybrid Object Detection & Two-Stage Verification

#### Clinical & Technical Problem
High false-positive rates in early melanoma screening due to visual confusion between small early-stage melanomas and atypical dysplastic nevi in wide-field clinical photography.

#### Primary Research Objective (General Aim)
> **To develop a hybrid two-stage detection and verification model integrating YOLOv9 for real-time lesion localization and Faster R-CNN for fine-grained diagnostic verification.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Rapid Lesion Localization via YOLOv9):** To deploy YOLOv9 with Programmable Gradient Information (PGI) to rapidly locate and propose candidate skin lesion bounding boxes in full-field images.
- **RO2 (Deep Diagnostic Verification via Faster R-CNN):** To formulate a second-stage Faster R-CNN model with high-capacity backbone to perform fine-grained classification on candidate lesion crops.
- **RO3 (Joint Confidence Scoring & Decision Fusion):** To design a joint confidence scoring mechanism that balances detection speed with rigorous diagnostic verification.
- **RO4 (Detection Benchmark Assessment):** To evaluate Mean Average Precision (mAP), detection accuracy, sensitivity, and inference latency on ISIC 2019 and ISIC 2020 datasets.
- **RO5 (Wide-Field Early Melanoma Triage):** To achieve high clinical sensitivity for early-stage micro-melanomas in clinical photography, minimizing diagnostic oversight.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Two-stage hybrid detector (YOLOv9 localization + Faster R-CNN classification), Programmable Gradient Information (PGI), confidence thresholding.
- **Evaluated Datasets:** ISIC 2019, ISIC 2020 (annotated bounding box dermoscopy and clinical photography subsets)
- **Reported Performance Metrics:**
  - *Mean Average Precision (mAP@0.5):* **97.1%**
  - *Melanoma Sensitivity:* **96.4%**
  - *Inference Latency:* **38ms per frame**
- **Clinical Utility & Impact:** Allows seamless automated scanning of full-body photographs to detect and triage tiny, evolving dysplastic lesions before they become invasive.

---

### Paper 32: Automated Skin Cancer Report Generation via a Knowledge-Distilled Vision-Language Model

- **Authors:** L. Chakrabarti; B. Zhang; H. Tian; A. Vakanski; M. Xian
- **Affiliation:** Department of Computer Science, University of Idaho, Moscow, ID, USA; Department of Nuclear Engineering and Industrial Management, University of Idaho, Idaho Falls, ID, USA
- **Venue:** IEEE Access (2025) | **DOI:** `10.1109/ACCESS.2025.3591750` | **IEEE Article:** `11091320`
- **PDF File:** `38_L._Chakrabarti_2025_Automated_Skin_Cancer_Report_Generation_via_a_Knowledge-Distilled_Vision-Languag.pdf`
- **Methodological Category:** Vision-Language Models & Knowledge Distillation

#### Clinical & Technical Problem
Generating comprehensive textual dermatological reports is time-consuming for clinicians, and standard VLMs suffer from hallucinations and medical inaccuracy.

#### Primary Research Objective (General Aim)
> **To design and validate an automated skin cancer report generation system using a knowledge-distilled Vision-Language Model (VLM) for dermatoscopy.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Dermatological VLM Architecture):** To construct a vision-language framework combining a dermatoscopic image encoder with an autoregressive medical language decoder.
- **RO2 (Cross-Modal Knowledge Distillation):** To formulate a knowledge distillation strategy to transfer diagnostic domain expertise from large medical foundation models into a compact, lightweight VLM.
- **RO3 (Factual Medical Consistency Enforcement):** To enforce clinical consistency loss functions to eliminate factual hallucinations regarding lesion type, asymmetry, border, color, and diagnostic recommendations.
- **RO4 (Linguistic & Clinical Evaluation):** To evaluate generated reports using natural language generation metrics (BLEU-4, ROUGE-L, CIDEr) and expert clinical factual correctness scores.
- **RO5 (Dermatology Documentation Automation):** To dramatically accelerate clinical documentation workflows by providing structured, pre-filled diagnostic reports for physician review.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Knowledge-distilled Vision-Language Model (VLM), cross-modal projection layer, factual consistency loss, autoregressive text generation.
- **Evaluated Datasets:** Derm-Report Corpus (dermoscopic images paired with verified narrative diagnostic pathology reports)
- **Reported Performance Metrics:**
  - *BLEU-4:* **0.38**
  - *ROUGE-L:* **0.54**
  - *CIDEr:* **1.24**
  - *Clinical Factuality Score:* **94.2%**
- **Clinical Utility & Impact:** Converts complex visual dermatoscopic patterns into fluent, medically accurate clinical narrative summaries, reducing clerical workload for clinicians.

---

### Paper 33: Multi-Scale DCNN with Dynamic Weight and Part Cross-Entropy Loss for Skin Lesion Diagnosis

- **Authors:** G. Wang; L. Liu; F. Lauri; A. H. E. Hassani
- **Affiliation:** Graduate School, Tsinghua University, Shenzhen, China; OPERA, University of Technology of Belfort-Montbéliard, Belfort, France
- **Venue:** Big Data Mining and Analytics (2024) | **DOI:** `10.26599/BDMA.2024.9020038` | **IEEE Article:** `10778156`
- **PDF File:** `39_G._Wang_2024_Multi-Scale_DCNN_with_Dynamic_Weight_and_Part_Cross-Entropy_Loss_for_Skin_Lesion.pdf`
- **Methodological Category:** Multi-Scale DCNN & Dynamic Loss Formulation

#### Clinical & Technical Problem
Large variations in lesion scale and non-uniform distribution of discriminative pathological patterns within lesions cause standard CNNs to miss subtle localized cues.

#### Primary Research Objective (General Aim)
> **To formulate a Multi-Scale Deep Convolutional Neural Network (DCNN) with dynamic weighting and part cross-entropy loss for enhanced skin lesion diagnosis.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Multi-Scale Convolutional Feature Extraction):** To construct a multi-scale DCNN backbone to capture global context and localized lesion sub-structures across diverse receptive fields.
- **RO2 (Part-Based Loss Formulation):** To formulate a part cross-entropy loss function that computes loss over partitioned lesion regions, forcing the network to attend to dispersed localized cues.
- **RO3 (Dynamic Hard Sample Weighting):** To implement a dynamic loss weighting scheme that adaptively adjusts penalties for hard-to-classify and underrepresented lesion samples during training.
- **RO4 (Multi-Class Diagnostic Assessment):** To evaluate classification accuracy, sensitivity, and specificity across the ISIC 2018 and ISIC 2019 benchmark datasets.
- **RO5 (Intra-Class Variance Suppression):** To overcome intra-class morphological heterogeneity and improve discrimination on diffuse, non-homogeneous lesion presentations.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Multi-scale DCNN backbone, part cross-entropy loss function, dynamic sample weighting, spatial region partitioning.
- **Evaluated Datasets:** ISIC 2018, ISIC 2019 (25,331 images across 8 diagnostic classes)
- **Reported Performance Metrics:**
  - *Overall Accuracy:* **92.9%**
  - *Sensitivity:* **91.5%**
  - *Specificity:* **93.8%**
  - *F1-Score:* **92.3%**
- **Clinical Utility & Impact:** Prevents dominant centralized textures from overshadowing critical diagnostic criteria located along peripheral lesion margins.

---

### Paper 34: Skin Lesion Segmentation in Clinical Images Using Nonnegative Matrix Factorization and Mutual Information

- **Authors:** E. Soares Flores; J. Scharcanski
- **Affiliation:** Federal University of Pampa, Alegrete, Brazil; Federal University of Rio Grande do Sul, Porto Alegre, Brazil
- **Venue:** IEEE Access (2025) | **DOI:** `10.1109/ACCESS.2025.3584305` | **IEEE Article:** `11058930`
- **PDF File:** `40_E._Soares_Flores_2025_Skin_Lesion_Segmentation_in_Clinical_Images_Using_Nonnegative_Matrix_Factorizati.pdf`
- **Methodological Category:** Unsupervised Matrix Factorization & Information Theory

#### Clinical & Technical Problem
Supervised segmentation models require vast amounts of expensive, expert-annotated pixel masks and often fail on non-dermoscopic, clinical consumer photography.

#### Primary Research Objective (General Aim)
> **To develop an unsupervised skin lesion segmentation framework for clinical images using Nonnegative Matrix Factorization (NMF) and Mutual Information.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Pigment Spectral Unmixing via NMF):** To apply Nonnegative Matrix Factorization to unmix multi-channel clinical color images into distinct pigment and tissue basis components.
- **RO2 (Mutual Information Basis Optimization):** To utilize mutual information metrics to identify the optimal basis component that maximizes information separation between lesion and background skin.
- **RO3 (Unsupervised Boundary Extraction):** To formulate an automated thresholding and contour refinement pipeline that extracts lesion masks without requiring manual training labels.
- **RO4 (Clinical Image Benchmark Assessment):** To evaluate segmentation accuracy, Jaccard index, and Dice coefficient on the Dermofit and clinical skin lesion benchmarks.
- **RO5 (Annotation-Free Tele-Dermatology Front-End):** To provide an efficient, annotation-free segmentation solution adaptable to diverse camera sensors and non-dermoscopic settings.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Nonnegative Matrix Factorization (NMF), mutual information criterion, unsupervised spectral unmixing, morphological contour refinement.
- **Evaluated Datasets:** Dermofit Image Library (1,300 clinical images across 10 lesion types), ISIC clinical subsets
- **Reported Performance Metrics:**
  - *Jaccard Index:* **88.7%**
  - *Dice Coefficient:* **93.4%**
  - *Supervision Required:* **0% (Fully Unsupervised)**
- **Clinical Utility & Impact:** Enables lesion segmentation directly on standard consumer smartphone images without requiring millions of hand-drawn clinical training masks.

---

### Paper 35: A Transparent Search-Based Framework for Skin and Breast Cancer Diagnosis Using Siamese Networks

- **Authors:** Z. Tabatabaei; A. Colomer; J. O. Moll; V. Naranjo
- **Affiliation:** Department of Computer Science, University of Copenhagen, Copenhagen, Denmark; Instituto de Telecomunicaciones y Aplicaciones Multimedia, Universitat Politècnica de València, Valencia, Spain
- **Venue:** IEEE Access (2025) | **DOI:** `10.1109/ACCESS.2025.3628157` | **IEEE Article:** `11224374`
- **PDF File:** `41_Z._Tabatabaei_2025_A_Transparent_Search-Based_Framework_for_Skin_and_Breast_Cancer_Diagnosis_Using_.pdf`
- **Methodological Category:** Content-Based Image Retrieval & Siamese Deep Metric

#### Clinical & Technical Problem
Deep classifiers output opaque class probabilities without clinical precedents, preventing clinicians from verifying whether a case resembles historically validated diagnoses.

#### Primary Research Objective (General Aim)
> **To establish a transparent, search-based diagnostic framework using Siamese deep metric networks for content-based image retrieval in skin and breast cancer diagnosis.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Siamese Metric Latent Embedding):** To train a Siamese neural network using contrastive/triplet loss to map medical images into an interpretable metric embedding space where clinically similar cases cluster together.
- **RO2 (Content-Based Historical Case Retrieval):** To implement an efficient nearest-neighbor search algorithm to retrieve historically validated reference cases with verified biopsy outcomes.
- **RO3 (Cross-Domain Diagnostic Validation):** To validate the retrieval and classification framework on two distinct clinical domains: dermatoscopic skin lesions (ISIC) and mammographic breast lesions (CBIS-DDSM).
- **RO4 (Diagnostic Relevance Evaluation):** To evaluate classification accuracy, precision-at-k, and retrieval relevance against standalone supervised classification baselines.
- **RO5 (Case-Based Clinical Interpretability):** To empower clinicians to inspect visually and histologically matched historical cases, building diagnostic trust and providing auditability.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** Siamese neural network, deep metric learning, content-based medical image retrieval (CBMIR), k-nearest neighbor case matching.
- **Evaluated Datasets:** ISIC Archive (dermoscopy), CBIS-DDSM (Curated Breast Imaging Subset of DDSM mammography)
- **Reported Performance Metrics:**
  - *Classification Accuracy (Skin):* **93.6%**
  - *Accuracy (Breast):* **91.8%**
  - *Precision@5:* **94.5%**
  - *AUC:* **0.96**
- **Clinical Utility & Impact:** Provides clinicians with immediate access to visually and histopathologically confirmed twin cases from hospital archives to justify decisions.

---

### Paper 36: FoMoSkinNet: A Dual-Stream Deep Learning Model for Early Detection and Classification of Non-Dermoscopic Skin Lesions via Focal Modulation and Local Feature Integration

- **Authors:** F. Bibi; Q. Abbas; S. M. Naqi
- **Affiliation:** Department of Computer Science, Quaid-i-Azam University, Islamabad, Pakistan; College of Computer and Information Sciences, Imam Mohammad Ibn Saud Islamic University, Riyadh, Saudi Arabia
- **Venue:** IEEE Access (2026) | **DOI:** `10.1109/ACCESS.2026.3674219` | **IEEE Article:** `11435372`
- **PDF File:** `42_F._Bibi_2026_FoMoSkinNet_A_Dual-Stream_Deep_Learning_Model_for_Early_Detection_and_Classifica.pdf`
- **Methodological Category:** Focal Modulation & Non-Dermoscopic Clinical Imaging

#### Clinical & Technical Problem
Most deep learning research focuses on dermoscopy; clinical smartphone photography suffers from non-standardized illumination, oblique angles, and complex background skin folds.

#### Primary Research Objective (General Aim)
> **To propose 'FoMoSkinNet', a dual-stream deep learning model utilizing focal modulation and local feature integration for the early detection of non-dermoscopic skin lesions.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Dual-Stream Architectural Design):** To design a dual-stream deep network that separately extracts high-resolution localized textures and broad contextual clinical morphology.
- **RO2 (Focal Modulation Mechanism):** To formulate a focal modulation module that replaces traditional self-attention with lightweight contextual aggregation, capturing multi-scale interactions efficiently.
- **RO3 (Local Feature Integration Block):** To implement a feature integration block that adaptively fuses fine edge details with deep semantic representations.
- **RO4 (Clinical Smartphone Benchmark Assessment):** To evaluate diagnostic accuracy, sensitivity, specificity, and F1-score on the clinical non-dermoscopic PAD-UFES-20 and ISIC datasets.
- **RO5 (Tele-Dermatology Accessibility Enhancement):** To enable accurate, smartphone-based skin cancer screening for community health workers and decentralized tele-dermatology clinics.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** FoMoSkinNet architecture, dual-stream contextual and fine-grained branches, focal modulation mechanism, multi-scale feature integration.
- **Evaluated Datasets:** PAD-UFES-20 (2,298 clinical smartphone images collected from Brazilian patients), ISIC dataset
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **92.6%**
  - *Sensitivity:* **91.9%**
  - *Specificity:* **93.4%**
  - *F1-Score:* **92.3%**
- **Clinical Utility & Impact:** Bridges the clinical divide between costly dermatoscope hardware and ubiquitous consumer smartphones, supporting democratized skin screening.

---

### Paper 37: MSPE-DeiT: A Vision Transformer-Based Multimodal Framework for Skin Cancer Diagnosis

- **Authors:** U. Mittal; S. S. H. Varpe; A. Sharma; T. Sood; P. Khandnor; S. Garg; S. Rani; M. Gupta; L. E. Amraoui; K. Ouni; A. El Amraoui
- **Affiliation:** Department of Computer Science and Engineering, Punjab Engineering College, Chandigarh, India; Department of Computer Science and Information Technology, Chitkara University, Punjab, India
- **Venue:** IEEE Access (2026) | **DOI:** `10.1109/ACCESS.2026.3719871` | **IEEE Article:** `11641552`
- **PDF File:** `43_U._Mittal_2026_MSPE-DeiT_A_Vision_Transformer-Based_Multimodal_Framework_for_Skin_Cancer_Diagno.pdf`
- **Methodological Category:** Vision Transformers & Multimodal Patient Metadata

#### Clinical & Technical Problem
Image-only diagnostic models ignore critical epidemiological risk factors (patient age, sex, lesion anatomical site) that dermatologists always consider in differential diagnosis.

#### Primary Research Objective (General Aim)
> **To develop 'MSPE-DeiT', a Vision Transformer-based multimodal framework integrating dermatoscopic patches and clinical demographic metadata via Multi-Stage Patch Embedding.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Multi-Stage Patch Embedding (MSPE)):** To formulate a Multi-Stage Patch Embedding module that extracts hierarchical multi-scale visual tokens from dermoscopic images.
- **RO2 (Data-Efficient Image Transformer Backbone):** To deploy a Data-Efficient Image Transformer (DeiT) backbone with self-attention mechanisms to model global dependencies with high sample efficiency.
- **RO3 (Multimodal Demographic Feature Fusion):** To construct a multimodal fusion block that seamlessly projects numerical and categorical patient metadata (age, sex, anatomical site) into the visual token stream.
- **RO4 (Comprehensive Multimodal Assessment):** To evaluate diagnostic accuracy, AUC, sensitivity, and specificity on the HAM10000 and ISIC 2020 multimodal datasets.
- **RO5 (Holistic Patient-Centric Clinical Triage):** To provide a clinically realistic diagnostic system that emulates dermatologists by synthesizing visual signs with patient clinical history.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** MSPE-DeiT architecture, Multi-Stage Patch Embedding, Data-Efficient Image Transformer (DeiT), cross-modal demographic token projection.
- **Evaluated Datasets:** HAM10000 (10,015 images with patient metadata), ISIC 2020 (33,126 images with age, sex, and anatomical location)
- **Reported Performance Metrics:**
  - *Classification Accuracy:* **95.8%**
  - *Sensitivity:* **95.1%**
  - *Specificity:* **96.4%**
  - *AUC:* **0.985**
  - *Metadata Fusion Gain:* **+4.1% over Vision-Only DeiT**
- **Clinical Utility & Impact:** Emulates comprehensive clinical consultations by conditioning image classification on vital patient risk factors like age and anatomical location.

---

### Paper 38: MoLE: Mixture-of-LoRA Experts for Parameter-Efficient Dermoscopic Visual Question Answering

- **Authors:** K. Younis; A. M. Muhammad; T. Hussain; M. Asma; A. K. Alzahrani
- **Affiliation:** Centre for AI and Big Data, Namal University, Mianwali, Pakistan; Riphah International University, Islamabad, Pakistan; Department of Computer Science, College of Computer and Information Sciences, King Saud University, Riyadh, Saudi Arabia
- **Venue:** IEEE Access (2026) | **DOI:** `10.1109/ACCESS.2026.3717605` | **IEEE Article:** `11626860`
- **PDF File:** `44_K._Younis_2026_MoLE_Mixture-of-LoRA_Experts_for_Parameter-Efficient_Dermoscopic_Visual_Question.pdf`
- **Methodological Category:** Parameter-Efficient Fine-Tuning & Dermoscopic VQA

#### Clinical & Technical Problem
Adapting large foundation vision-language models for specialized medical visual question answering (VQA) requires prohibitive compute and fine-tuning parameters.

#### Primary Research Objective (General Aim)
> **To construct 'MoLE', a parameter-efficient Mixture-of-LoRA Experts framework for dermoscopic Visual Question Answering (VQA) on edge hardware.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (Mixture-of-LoRA Modular Architecture):** To design a modular Mixture-of-LoRA (Low-Rank Adaptation) architecture where specialized LoRA experts handle distinct clinical inquiry sub-domains (morphology, diagnosis, malignancy risk).
- **RO2 (Dynamic Gating Router Formulation):** To formulate a lightweight gating router that dynamically activates the most relevant LoRA expert based on the input dermoscopic image and clinical question.
- **RO3 (Parameter-Efficient Tuning Optimization):** To restrict trainable parameters to less than 3% of the foundation model, enabling fine-tuning and inference on standard desktop GPUs.
- **RO4 (VQA Clinical Benchmark Assessment):** To evaluate question-answering accuracy, BLEU, and clinical concordance on the Skin-VQA benchmark dataset.
- **RO5 (Interactive Bedside Clinical Dialogue):** To enable interactive, natural-language clinical dialogue systems to support medical students, nurses, and general practitioners during dermatological evaluations.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** MoLE architecture, Mixture-of-LoRA Experts, dynamic routing gating network, parameter-efficient fine-tuning (PEFT), vision-language VQA.
- **Evaluated Datasets:** Skin-VQA Benchmark (thousands of paired dermoscopic images and multi-turn clinical inquiry questions)
- **Reported Performance Metrics:**
  - *VQA Accuracy:* **86.9%**
  - *BLEU-1:* **0.72**
  - *Trainable Parameters:* **2.3M (<3% of backbone)**
  - *Inference Speedup:* **4.5x vs Full Fine-Tuning**
- **Clinical Utility & Impact:** Allows clinicians to ask conversational questions about dermoscopic images ('Is the border regular?', 'What is the risk level?') with low-cost local computing.

---

### Paper 39: SLGAN-EID: Generative Adversarial Network-Based Skin Lesion Image Enhancement With Improved Diagnosis

- **Authors:** M. U. Zafar; M. A. Qureshi; S. K. Noon; K. B. Khan
- **Affiliation:** Department of Electrical Engineering, The Islamia University of Bahawalpur, Bahawalpur, Pakistan; Department of Computer Science, COMSATS University Islamabad, Wah Campus, Wah Cantt, Pakistan
- **Venue:** IEEE Access (2026) | **DOI:** `10.1109/ACCESS.2026.3711048` | **IEEE Article:** `11598907`
- **PDF File:** `45_M._U._Zafar_2026_SLGAN-EID_Generative_Adversarial_Network-Based_Skin_Lesion_Image_Enhancement_Wit.pdf`
- **Methodological Category:** Generative Enhancement & Improved Diagnosis

#### Clinical & Technical Problem
Poor-quality clinical images suffering from low illumination, motion blur, and glare severely degrade the diagnostic sensitivity of deep learning triage models.

#### Primary Research Objective (General Aim)
> **To develop 'SLGAN-EID', a Generative Adversarial Network-based skin lesion image enhancement framework paired with an improved diagnostic classifier.**

#### Specific Research Objectives (Operational & Methodological Goals)

- **RO1 (SLGAN Generator Architecture):** To construct an advanced GAN generator with perceptual and content loss functions to correct uneven illumination, remove specular glare, and enhance micro-textural details.
- **RO2 (Multi-Scale Patch Discriminator):** To formulate a multi-scale patch discriminator to enforce realistic dermoscopic color fidelity and prevent artificial hallucination of false lesion features.
- **RO3 (Downstream Diagnostic Classification Pipeline):** To train a deep convolutional classifier on SLGAN-enhanced dermoscopy images to evaluate diagnostic downstream improvements.
- **RO4 (Image Quality & Diagnostic Benchmarking):** To benchmark image quality metrics (PSNR, SSIM) and diagnostic metrics (accuracy, sensitivity, specificity, AUC) on the ISIC 2018 and ISIC 2020 datasets.
- **RO5 (Pre-Diagnostic Enhancement Front-End):** To establish an automated enhancement pre-processor that elevates low-grade camera images to diagnostic-grade clarity before clinical assessment.

#### Technical Methodology & Benchmark Metrics

- **Key Methodology:** SLGAN-EID framework, perceptual GAN generator, multi-scale patch discriminator, image enhancement (illumination/glare), downstream CNN classification.
- **Evaluated Datasets:** ISIC 2018, ISIC 2020 (degraded low-light and artifact-heavy subsets)
- **Reported Performance Metrics:**
  - *PSNR Gain:* **+6.8 dB**
  - *SSIM:* **0.942**
  - *Enhanced Diagnostic Accuracy:* **96.5%**
  - *Sensitivity Gain:* **+5.8% over degraded raw images**
- **Clinical Utility & Impact:** Restores diagnostically degraded images captured in poorly lit clinics, ensuring that downstream AI and dermatologists see crisp, glare-free lesion details.

---

