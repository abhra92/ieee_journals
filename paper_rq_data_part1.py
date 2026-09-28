"""
paper_rq_data_part1.py: Papers 1 to 13
"""

PART1 = [
    # -------------------------------------------------------------
    # Paper 1: Albahar (2019)
    # -------------------------------------------------------------
    {
        "id": 1,
        "csv_idx": 1,
        "arnumber": "8669763",
        "category": "Regularized & Lightweight CNNs",
        "primary_problem": "Fine-grained morphological overlaps between benign and malignant skin lesions cause catastrophic overfitting in traditional unregularized deep CNNs.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Architectural Innovation",
                "question": "Can a lightweight custom Convolutional Neural Network with an embedded novel weight-controlling regularizer prevent weight explosion and mitigate overfitting in binary skin lesion classification without requiring multi-million parameter backbones?",
                "methodology": "Constructed a 2-layer convolutional network embedded with a novel weight regularizer (penalty hyperparameter lambda = 0.02), coupled with max pooling, dropout, a 128-neuron dense layer, and softmax output.",
                "answer": "Yes. The novel regularizer successfully stabilized weight trajectories during 100 training epochs, achieving an average validation weighted accuracy of 97.49% and preventing divergence on fine-grained lesion classes."
            },
            {
                "num": "RQ2",
                "dim": "Preprocessing & Data Transformation",
                "question": "How does nonlinear power-law transformation (gamma correction) affect image contrast and convergence speed in automated dermoscopic image classification?",
                "methodology": "Applied power-law transformation to standardize 300x300x3 dermoscopic images, balancing illumination differences and highlighting subtle boundary gradations prior to convolution.",
                "answer": "Power-law transformation accelerated gradient descent convergence and reduced training loss fluctuations across varying lighting conditions across the ISIC dataset."
            },
            {
                "num": "RQ3",
                "dim": "Clinical Diagnostic Performance",
                "question": "What diagnostic discrimination capability (ROC-AUC) does the regularized model achieve across specific pairwise benign versus malignant lesion types?",
                "methodology": "Partitioned 23,906 ISIC archive images into ~8,000 image subsets (70% train, 30% val) across binary clinical pairings.",
                "answer": "Achieved ROC-AUC of 0.77 for nevus vs. melanoma, 0.93 for seborrheic keratosis vs. basal cell carcinoma, 0.85 for seborrheic keratosis vs. melanoma, and 0.86 for solar lentigo vs. melanoma."
            },
            {
                "num": "RQ4",
                "dim": "Clinical Translation & Scalability",
                "question": "What are the structural constraints of pairwise binary classification when translating computer-aided diagnostic systems to multi-class clinical triage?",
                "methodology": "Analyzed model inference across disparate clinical presentations against practical dermatologist triage needs.",
                "answer": "The binary pairwise formulation cannot holistically evaluate complex multi-class differential diagnoses, and the lack of external prospective multi-center testing limits generalizability."
            }
        ],
        "datasets": ["ISIC Archive (23,906 images; 8,000 subset, 70/30 split)"],
        "metrics": {"Accuracy": "97.49%", "AUC (Nevus vs Mel)": "0.77", "AUC (SK vs BCC)": "0.93", "AUC (SK vs Mel)": "0.85"},
        "open_questions": [
            "How can the weight regularizer be generalized to unified multi-class differential diagnosis without loss of per-class sensitivity?",
            "How does the model perform prospectively across diverse patient phototypes in multi-center clinical trials?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 2: Ashraf et al. (2020)
    # -------------------------------------------------------------
    {
        "id": 2,
        "csv_idx": 2,
        "arnumber": "9160933",
        "category": "ROI Localization & Transfer Learning",
        "primary_problem": "Surrounding healthy skin, lighting variations, and hair artifacts introduce confounding background noise when deep networks process full unsegmented dermoscopic images.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Preprocessing & ROI Segmentation",
                "question": "Does isolating the lesion Region of Interest (ROI) via an improved k-means clustering segmentation algorithm improve transfer learning feature discrimination over using full unsegmented images?",
                "methodology": "Implemented improved k-means clustering to segment lesion borders, followed by ROI cropping and offline data augmentation (rotations, flips, zooming, contrast adjustments).",
                "answer": "Yes. Eliminating healthy skin artifacts allowed feature extraction networks to focus exclusively on lesion texture, boosting accuracy to 97.9% on DermIS and 97.4% on DermQuest."
            },
            {
                "num": "RQ2",
                "dim": "Architectural Backbone Evaluation",
                "question": "How do deep pre-trained CNN backbones (AlexNet vs. VGG-16) compare in feature transferability when fine-tuned strictly on segmented dermatoscopic lesion ROIs?",
                "methodology": "Fine-tuned pre-trained AlexNet and VGG-16 architectures on isolated lesion patches across two clinical benchmark datasets under identical training protocols.",
                "answer": "Both architectures demonstrated strong transferability; VGG-16 captured finer textural details, yielding 96.3% sensitivity and 98.7% specificity on DermIS and 95.8% sensitivity and 98.1% specificity on DermQuest."
            },
            {
                "num": "RQ3",
                "dim": "Benchmark Generalization",
                "question": "Can an ROI-based transfer learning framework achieve robust, consistent diagnostic performance across independent clinical benchmark datasets?",
                "methodology": "Evaluated the pipeline on DermIS (705 images: 448 benign, 257 melanoma) and DermQuest (667 images: 434 nevus, 233 melanoma) using AUC, precision, and F1-score.",
                "answer": "Demonstrated exceptional consistency across datasets: AUC reached 0.97 on DermIS and 0.96 on DermQuest, with F1-scores of 96.3% and 95.8% respectively."
            },
            {
                "num": "RQ4",
                "dim": "Methodological Limitations",
                "question": "Under what clinical conditions does k-means ROI segmentation fail, and how does this affect downstream melanoma detection?",
                "methodology": "Error analysis of segmentation failures on difficult border topologies and dense hair artifacts.",
                "answer": "k-means clustering degrades in the presence of severe hair occlusion and diffuse, poorly demarcated lesion margins, leading to border over-clipping or under-segmentation."
            }
        ],
        "datasets": ["DermIS (705 images)", "DermQuest (667 images)"],
        "metrics": {"Accuracy (DermIS)": "97.9%", "Sensitivity": "96.3%", "Specificity": "98.7%", "AUC (DermIS)": "0.97", "Accuracy (DermQuest)": "97.4%", "AUC (DermQuest)": "0.96"},
        "open_questions": [
            "Can automated deep semantic segmentation replace k-means to eliminate manual tuning in the presence of dense hair?",
            "Can the framework scale to multi-class classification beyond binary melanoma vs. nevus distinction?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 3: Mridha et al. (2023)
    # -------------------------------------------------------------
    {
        "id": 3,
        "csv_idx": 3,
        "arnumber": "10107401",
        "category": "Explainable AI (XAI) & Mobile Healthcare",
        "primary_problem": "Deep learning CAD systems act as 'black boxes', lacking visual transparency and suffering from severe performance drops on underrepresented minority classes in multi-class dermatological screening.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Optimization & Activation Engineering",
                "question": "What combination of optimization algorithms (Adam vs. RMSprop) and activation functions (ReLU, Swish, Tanh) maximizes multi-class lesion classification accuracy on HAM10000?",
                "methodology": "Trained a custom CNN with batch normalization, max pooling, and dropout across systematic combinations of optimizers and activation functions.",
                "answer": "The custom CNN achieved peak overall accuracy of 82.0% and specificity of 94.17% with Adam optimizer and Swish/ReLU activations, with a loss accuracy of 0.47%."
            },
            {
                "num": "RQ2",
                "dim": "Explainable AI & Visual Attribution",
                "question": "Can post-hoc visual attribution maps (Grad-CAM and Grad-CAM++) accurately highlight clinically relevant lesion structures to build clinician trust?",
                "methodology": "Generated localized gradient attribution heatmaps at the final convolutional layer to visualize discriminative regions for each of the 7 diagnostic classes.",
                "answer": "Grad-CAM and Grad-CAM++ successfully localized pigmented network patterns and atypical margins matching dermatologist inspection criteria."
            },
            {
                "num": "RQ3",
                "dim": "Class Imbalance Impact",
                "question": "How significantly does class imbalance affect per-class sensitivity across common (melanocytic nevi) versus rare (dermatofibroma, vascular) skin lesions?",
                "methodology": "Analyzed confusion matrices across all 7 classes of HAM10000 (10,015 images) following geometric data augmentation.",
                "answer": "Sensitivity remained high for dominant classes but dropped on minority classes (df and vasc), demonstrating that geometric augmentation alone is insufficient to resolve extreme skew."
            },
            {
                "num": "RQ4",
                "dim": "Point-of-Care Mobile Feasibility",
                "question": "Can an explainable deep CNN be integrated into an Android smart healthcare application for real-time mobile clinical triage?",
                "methodology": "Exported the optimized lightweight CNN model and embedded it within an end-to-end Android mobile screening application.",
                "answer": "Successfully validated end-to-end mobile execution with near real-time inference latency suitable for decentralized point-of-care screening."
            }
        ],
        "datasets": ["HAM10000 (10,015 images across 7 classes)"],
        "metrics": {"Accuracy": "82.0%", "Specificity": "94.17%", "Sensitivity": "82.0%", "Loss Accuracy": "0.47%"},
        "open_questions": [
            "How can synthetic metric oversampling or cost-sensitive losses improve minority class sensitivity in mobile models?",
            "What is the diagnostic accuracy of the Android application when tested prospectively in multi-ethnic outpatient clinics?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 4: Wei et al. (2020)
    # -------------------------------------------------------------
    {
        "id": 4,
        "csv_idx": 4,
        "arnumber": "9099799",
        "category": "Lightweight Networks & Ensemble Learning",
        "primary_problem": "High computational complexity and massive parameter counts prevent deployment of state-of-the-art deep networks on resource-constrained clinical workstations and edge devices.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Lightweight Architecture Efficiency",
                "question": "Can a lightweight ensemble deep learning framework drastically reduce model parameters while maintaining state-of-the-art diagnostic accuracy on benchmark dermoscopic challenges?",
                "methodology": "Designed a parameter-efficient ensemble using lightweight CNN feature extractors, a lightweight U-Net segmentation module, and a fine-grained discrimination network.",
                "answer": "Yes. The framework achieved an accuracy of 87.3% and an AUC of 0.886 on ISBI 2016 with orders-of-magnitude fewer parameters than standard heavyweight baselines."
            },
            {
                "num": "RQ2",
                "dim": "Pair-Based Feature Discrimination",
                "question": "How does pair-based feature extraction and fine-grained metric learning improve discrimination between visually ambiguous benign nevi and malignant melanoma?",
                "methodology": "Trained a feature discrimination network on positive and negative sample pairs using fine-grained classification principles to learn subtle boundary differences.",
                "answer": "Pair-based learning effectively separated subtle boundary patterns, yielding a test sensitivity of 83.2%, specificity of 89.1%, and average precision of 0.732 on ISBI 2016."
            },
            {
                "num": "RQ3",
                "dim": "Integrated Semantic Segmentation",
                "question": "Does integrating a lightweight U-Net trained via transfer learning eliminate the need for manual hair and artifact preprocessing?",
                "methodology": "Trained an end-to-end lightweight U-Net to isolate lesion contours directly from raw dermoscopic imagery without heuristic artifact filtering.",
                "answer": "Automated segmentation successfully isolated lesion contours end-to-end, providing clean input patches to downstream pair-based classification networks."
            },
            {
                "num": "RQ4",
                "dim": "Boundary Sensitivity & Complexity",
                "question": "What are the diagnostic failure modes on lesions with highly indistinct, diffuse boundaries, and what is the training overhead of ensemble decision fusion?",
                "methodology": "Evaluated ensemble convergence, training memory footprint, and false-negative edge cases on ISBI 2016 and ISBI 2017.",
                "answer": "Performance modestly degraded on lesions with fuzzy, diffuse boundaries, and training multiple lightweight networks sequentially introduced non-negligible training time overhead."
            }
        ],
        "datasets": ["ISBI 2016 (900 train, 379 test)", "ISBI 2017 Challenge Dataset"],
        "metrics": {"Accuracy": "87.3%", "AUC": "0.886", "Sensitivity": "83.2%", "Specificity": "89.1%", "Average Precision": "0.732"},
        "open_questions": [
            "Can pair-based lightweight feature discrimination scale effectively to 8-class multi-category classification?",
            "Can knowledge distillation compress the lightweight ensemble into a single ultra-compact inference model?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 5: Gururaj et al. (2023)
    # -------------------------------------------------------------
    {
        "id": 5,
        "csv_idx": 5,
        "arnumber": "10122533",
        "category": "Residual Custom Architectures & Multi-Class Screening",
        "primary_problem": "Existing CAD systems suffer from accuracy degradation in multi-class classification and require heavy pre-trained backbones that struggle with class-imbalanced dermoscopic archives.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Architectural Design",
                "question": "Can a tailored custom CNN with residual skip connections ('DeepSkin') match or surpass standard transfer learning models (VGG-16, ResNet-50, MobileNet) on multi-class dermoscopic screening?",
                "methodology": "Architected DeepSkin with residual skip connections to preserve low-level textural gradients, benchmarked comparatively against VGG-16, ResNet-50, and MobileNet.",
                "answer": "DeepSkin achieved 88.0% overall accuracy, outperforming several heavier pre-trained models while maintaining architectural simplicity and compact parameterization."
            },
            {
                "num": "RQ2",
                "dim": "Multiclass Performance & Imbalance",
                "question": "How effectively does DeepSkin handle the 7 diagnostic classes of HAM10000 under Min-Max scaling and geometric data augmentation?",
                "methodology": "Preprocessed 10,015 images with Min-Max intensity scaling, 224x224 resizing, and spatial augmentations (rotations, flips, zooms, brightness adjustments).",
                "answer": "Achieved overall sensitivity of 86.2%, specificity of 85.0%, and precision of 86.4% across all 7 pathological categories."
            },
            {
                "num": "RQ3",
                "dim": "Diagnostic Confusion Patterns",
                "question": "Which pathological categories exhibit the highest cross-class confusion within the DeepSkin architecture?",
                "methodology": "Evaluated class-wise confusion matrices and classification errors across benign keratosis, melanocytic nevi, and malignant melanoma.",
                "answer": "The primary clinical confusion occurred between benign keratosis and melanoma due to morphological and chromatic overlaps in early-stage lesions."
            },
            {
                "num": "RQ4",
                "dim": "Edge Profiling & Clinical Readiness",
                "question": "What deployment barriers remain before DeepSkin can be integrated into resource-constrained point-of-care settings?",
                "methodology": "Assessed deployment requirements, edge hardware profiling, and demographic population diversity.",
                "answer": "Identified lack of hardware edge-profiling (FPS, RAM consumption) and absence of multi-ethnic clinical validation cohorts as critical deployment gaps."
            }
        ],
        "datasets": ["ISIC 2018 / HAM10000 (10,015 images, 7 classes)"],
        "metrics": {"Accuracy": "88.0%", "Sensitivity": "86.2%", "Specificity": "85.0%", "Precision": "86.4%"},
        "open_questions": [
            "How can attention gates be added to DeepSkin to resolve confusion between benign keratosis and melanoma?",
            "What is the inference latency of DeepSkin on embedded microcontroller and edge-TPU hardware?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 6: Adegun & Viriri (2020)
    # -------------------------------------------------------------
    {
        "id": 6,
        "csv_idx": 6,
        "arnumber": "9167192",
        "category": "Integrated Segmentation & Dense Feature Reuse",
        "primary_problem": "Fuzzy lesion margins, irregular pigment borders, and occluding hair shafts degrade end-to-end classifiers that lack prior semantic lesion localization.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Integrated Two-Stage Pipeline",
                "question": "Does cascading a Fully Convolutional Network (FCN) segmentation model with a DenseNet classification network improve multi-class skin lesion recognition over single-stage models?",
                "methodology": "Built an integrated pipeline where an FCN with encoder-decoder residual skips segments the lesion mask to crop input patches for a DenseNet classifier.",
                "answer": "Yes. The pipeline achieved state-of-the-art classification accuracy of 95.0% on ISIC 2017 and 98.5% on ISIC 2018, with 96.0% sensitivity and 0.98 AUC."
            },
            {
                "num": "RQ2",
                "dim": "Dense Connectivity & Feature Reuse",
                "question": "What is the architectural advantage of DenseNet's dense connectivity and feature reuse in capturing subtle dermoscopic biomarkers?",
                "methodology": "Leveraged dense connectivity blocks to concatenate feature maps from all preceding layers, maximizing gradient flow and feature reuse.",
                "answer": "Dense feature reuse preserved fine textural and micro-vascular details, leading to 97.0% specificity and 95.0% F1-score across 3-class lesion classification."
            },
            {
                "num": "RQ3",
                "dim": "Artifact Suppression Preprocessing",
                "question": "Does DullRazor morphological hair artifact suppression improve FCN segmentation accuracy and boundary delineation?",
                "methodology": "Applied DullRazor morphological filtering followed by contrast enhancement and affine augmentations before feeding images to the FCN.",
                "answer": "DullRazor artifact removal significantly boosted segmentation quality, yielding a 98.5% segmentation accuracy, 92.5% Dice coefficient, and 86.8% Jaccard index."
            },
            {
                "num": "RQ4",
                "dim": "Computational Complexity",
                "question": "What is the computational overhead of two-stage FCN + DenseNet training, and how does it handle diffuse, poorly demarcated lesion boundaries?",
                "methodology": "Benchmarked training memory requirements, inference latency, and segmentation error on ambiguous lesion margins.",
                "answer": "The two-stage framework demands substantial GPU memory during sequential training, and exhibits slight boundary over-segmentation on lesions with faint, diffuse margins."
            }
        ],
        "datasets": ["ISIC 2017 (2,750 images)", "ISIC 2018 (3,694 images)", "DermQuest"],
        "metrics": {"Segmentation Accuracy": "98.5%", "Dice Coefficient": "92.5%", "Jaccard Index": "86.8%", "Classification Accuracy (2018)": "98.5%", "Classification Accuracy (2017)": "95.0%", "AUC": "0.98"},
        "open_questions": [
            "Can the FCN and DenseNet stages be trained end-to-end with joint loss backpropagation to reduce training time?",
            "How robust is the FCN segmentation when tested on low-contrast, non-dermoscopic smartphone images?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 7: Naeem et al. (2020) - Systematic Literature Review (SLR)
    # -------------------------------------------------------------
    {
        "id": 7,
        "csv_idx": 7,
        "arnumber": "9113301",
        "category": "Systematic Literature Review (Kitchenham SLR)",
        "primary_problem": "Lack of standardized evaluation protocols, heterogeneous dataset partitions, and unaddressed class imbalance prevent objective comparison of deep learning melanoma diagnostic algorithms.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "SLR Explicit RQ1: Model Taxonomy",
                "question": "What type of deep learning based classifiers are used for diagnosing melanoma disease?",
                "methodology": "Conducted a systematic literature review following the Kitchenham protocol across IEEE, Springer, Elsevier, ACM, ScienceDirect, and Medline from 2014 to 2020.",
                "answer": "Pre-trained CNN architectures dominate the literature (ResNet-50, VGG-16, Inception-v3, and DenseNet-121), with transfer learning being the preferred strategy to overcome medical image scarcity."
            },
            {
                "num": "RQ2",
                "dim": "SLR Explicit RQ2: Performance Measurement",
                "question": "What is the performance measurement used for the evaluation of deep learning models in melanoma diagnosis?",
                "methodology": "Analyzed performance metric reporting standards across 52 finalized peer-reviewed publications.",
                "answer": "Accuracy, Sensitivity (Recall), Specificity, and ROC-AUC are the primary metrics; best models achieve ~93.4% accuracy and 0.95 AUC, but precision and F1 are inconsistently reported."
            },
            {
                "num": "RQ3",
                "dim": "SLR Explicit RQ3: Dataset Taxonomy",
                "question": "What type of datasets are used for melanoma diagnosis in existing literature?",
                "methodology": "Categorized benchmark repositories, sample sizes, class distributions, and data accessibility across published studies.",
                "answer": "Public benchmarks dominate: ISIC Challenge archives (2016-2018), HAM10000, and PH2 are universally used, but severe class imbalance (benign nevi >> melanoma) universally distorts accuracy."
            },
            {
                "num": "RQ4",
                "dim": "SLR Research Gaps & Opportunities",
                "question": "What are the critical open challenges and future research opportunities identified in deep learning melanoma diagnosis?",
                "methodology": "Synthesized unresolved methodological and clinical gaps across the systematic review corpus.",
                "answer": "Identified 3 major gaps: (1) lack of prospective multi-center clinical validation, (2) failure to integrate clinical demographic metadata, and (3) vulnerability to adversarial artifacts and hair occlusions."
            }
        ],
        "datasets": ["PH2 (200 images)", "ISIC 2016 (1,279 images)", "ISIC 2017 (2,000 images)", "ISIC 2018 (10,015 images)", "HAM10000"],
        "metrics": {"Highest Benchmark Accuracy": "93.4%", "Average Sensitivity": "91.0%", "Average Specificity": "94.2%", "Peak AUC": "0.95"},
        "open_questions": [
            "How can standardized cross-validation benchmarks be enforced across IEEE and medical AI publications?",
            "What multimodal architectures best fuse clinical patient metadata with deep dermoscopic visual embeddings?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 8: Imran et al. (2022)
    # -------------------------------------------------------------
    {
        "id": 8,
        "csv_idx": 8,
        "arnumber": "9940917",
        "category": "Ensemble Fusion & Capsule Networks",
        "primary_problem": "Subtle chromatic and textural similarities between benign and malignant lesions yield high false-positive rates in single-model CAD systems.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Architectural Heterogeneity",
                "question": "Can combining heterogeneous deep learning architectures (custom VGG-16, residual ResNet-50, and Capsule Network) outperform individual standalone classifiers in melanoma detection?",
                "methodology": "Trained three distinct models capturing spatial textures (CNNs) and spatial-relational hierarchies (CapsNet) on a curated balanced dataset.",
                "answer": "Yes. Fusing CNN feature representations with Capsule Network spatial equivariance achieved superior discriminative reliability, boosting accuracy to 93.50%."
            },
            {
                "num": "RQ2",
                "dim": "Ensemble Decision Mechanics",
                "question": "How does an ensemble soft-voting decision mechanism reconcile divergent predictions between conventional CNNs and Capsule Networks?",
                "methodology": "Aggregated output probability vectors from VGG-16, ResNet-50, and CapsNet using weighted soft-voting to produce final class labels.",
                "answer": "Soft-voting reduced individual model variance and eliminated single-model outlier misclassifications, yielding 94.80% specificity and 94.30% precision."
            },
            {
                "num": "RQ3",
                "dim": "Diagnostic Balance & Sensitivity",
                "question": "What sensitivity and F1-score are achieved on a balanced dermoscopic benchmark of 2,800 images?",
                "methodology": "Evaluated the combined system on a balanced subset of 1,400 benign and 1,400 malignant ISIC images with extensive geometric augmentations.",
                "answer": "Achieved a sensitivity of 87.25%, an F1-score of 90.64%, and an overall classification accuracy of 93.50%."
            },
            {
                "num": "RQ4",
                "dim": "Computational Latency Trade-Offs",
                "question": "What is the inference latency overhead of concurrently executing three deep networks during clinical point-of-care screening?",
                "methodology": "Analyzed GPU runtime, model parameter scaling, and memory footprint of concurrent inference across the three learners.",
                "answer": "Concurrent execution of three deep networks triples memory consumption and increases inference latency, requiring high-end GPUs that may restrict point-of-care mobile deployment."
            }
        ],
        "datasets": ["ISIC Archive Curated Balanced Dataset (2,800 images: 1,400 benign, 1,400 malignant)"],
        "metrics": {"Accuracy": "93.50%", "Sensitivity": "87.25%", "Specificity": "94.80%", "Precision": "94.30%", "F1-Score": "90.64%"},
        "open_questions": [
            "Can model pruning or knowledge distillation distill the three-model ensemble into a single fast inference network?",
            "How does the combined decision framework perform when deployed on imbalanced multi-class benchmarks?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 9: Lan et al. (2022) - FixCaps (CSV idx 10)
    # -------------------------------------------------------------
    {
        "id": 9,
        "csv_idx": 10,
        "arnumber": "9791221",
        "category": "Capsule Networks & Attention Routing",
        "primary_problem": "Standard CNN pooling layers discard critical spatial part-whole relationships, while traditional Capsule Networks suffer from slow convergence and high compute latency due to iterative dynamic routing.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Routing Algorithm Innovation",
                "question": "Can replacing iterative dynamic routing with a fixed matrix transformation routing mechanism ('FixCaps') eliminate the computational bottleneck of Capsule Networks in dermoscopy?",
                "methodology": "Replaced dynamic routing with fixed matrix transformation and incorporated convolutional attention modules to maintain transformation equivariance without routing iterations.",
                "answer": "Yes. FixCaps dramatically accelerated training convergence while retaining vector capsule representations, achieving an extraordinary peak accuracy of 96.49% on HAM10000."
            },
            {
                "num": "RQ2",
                "dim": "Spatial Hierarchy & Equivariance",
                "question": "How does vector capsule representation enhance feature discrimination across multi-class skin lesions with complex spatial sub-structures?",
                "methodology": "Evaluated vector activation norms for encoding lesion pose, orientation, and subtle textural patterns across 7 diagnostic categories.",
                "answer": "Vector capsules effectively captured spatial part-whole relationships (pigment network to border), yielding 93.47% sensitivity, 98.13% specificity, and 0.98 AUC."
            },
            {
                "num": "RQ3",
                "dim": "Diagnostic Precision & F1",
                "question": "What precision and F1-score are attained by FixCaps across the 10,015 images of the HAM10000 benchmark?",
                "methodology": "Benchmarked FixCaps using 5-fold cross-validation on color-normalized and augmented HAM10000 images.",
                "answer": "FixCaps achieved 93.64% precision and 93.55% F1-score, establishing state-of-the-art capsule performance in dermatological CAD."
            },
            {
                "num": "RQ4",
                "dim": "Minority Class Robustness",
                "question": "What are the performance limitations of FixCaps on severely underrepresented minority classes such as dermatofibroma?",
                "methodology": "Class-wise sensitivity breakdown and evaluation on out-of-distribution clinical photography.",
                "answer": "Minor sensitivity degradation was observed on rare classes (dermatofibroma), and the architecture was not validated on clinical (non-dermoscopic) photographs."
            }
        ],
        "datasets": ["HAM10000 (10,015 images across 7 classes)"],
        "metrics": {"Accuracy": "96.49%", "Sensitivity": "93.47%", "Specificity": "98.13%", "Precision": "93.64%", "F1-Score": "93.55%", "AUC": "0.98"},
        "open_questions": [
            "Can FixCaps be adapted to segment lesion boundaries directly from capsule activation lengths?",
            "How does FixCaps perform on non-dermoscopic smartphone images taken under variable clinical lighting?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 10: Öztürk & Çukur (2022) (CSV idx 11)
    # -------------------------------------------------------------
    {
        "id": 10,
        "csv_idx": 11,
        "arnumber": "9810181",
        "category": "Deep Metric Learning & Imbalance Mitigation",
        "primary_problem": "Extreme sample imbalance between common benign lesions and rare malignant melanoma severely biases deep classifiers toward majority classes under standard cross-entropy loss.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Loss Function Innovation",
                "question": "How does a Center-Oriented Margin-Free Triplet Loss (COMF-TL) overcome the hyperparameter tuning instability and gradient saturation of standard triplet losses in skewed dermatological datasets?",
                "methodology": "Formulated COMF-TL to adaptively pull feature embeddings toward dynamically updated class centers while repelling negative clusters without requiring a manually tuned fixed margin.",
                "answer": "COMF-TL eliminated the sensitivity to margin selection and stabilized embedding clustering, yielding a 4.58% AUC improvement over standard cross-entropy baselines."
            },
            {
                "num": "RQ2",
                "dim": "Metric Space Clustering",
                "question": "Can deep metric clustering separate minority cancer classes without requiring synthetic oversampling techniques (SMOTE, GANs) that risk introducing artifacts?",
                "methodology": "Trained ResNet-50 and VGG-16 backbones using COMF-TL to learn discriminative metric spaces directly from unaugmented, imbalanced feature distributions.",
                "answer": "Yes. Deep clustering achieved robust boundary separation, attaining a balanced multi-class accuracy of 83.7%, sensitivity of 82.4%, and specificity of 92.1% on ISIC 2018."
            },
            {
                "num": "RQ3",
                "dim": "Large-Scale Scaling",
                "question": "Does COMF-TL scale effectively when tested on the massive 8-class ISIC 2019 benchmark (25,331 images)?",
                "methodology": "Evaluated the framework on ISIC 2019 across ResNet-50 and VGG-16 backbones using mean AUC and macro-averaged F1-score.",
                "answer": "Demonstrated strong scalability, achieving an overall AUC of 0.912 and an F1-score of 81.9% on ISIC 2019, consistently outperforming standard cross-entropy baselines."
            },
            {
                "num": "RQ4",
                "dim": "Computational Overhead",
                "question": "What is the training latency and memory overhead introduced by continuous cluster center recalculation and online triplet mining?",
                "methodology": "Profiled epoch training times, triplet mining complexity, and cluster center synchronization during backpropagation.",
                "answer": "Dynamic cluster center recalculation and online semi-hard triplet mining increased per-epoch training time by ~30% compared to standard cross-entropy."
            }
        ],
        "datasets": ["ISIC 2018 (10,015 images, 7 classes)", "ISIC 2019 (25,331 images, 8 classes)"],
        "metrics": {"Balanced Accuracy": "83.7%", "AUC": "0.912", "AUC Improvement": "+4.58%", "Sensitivity": "82.4%", "Specificity": "92.1%", "F1-Score": "81.9%"},
        "open_questions": [
            "Can COMF-TL be integrated with Vision Transformers to cluster patch tokens directly in self-attention layers?",
            "How does COMF-TL perform under open-set conditions where unseen skin disease classes are encountered during inference?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 11: Kwasigroch et al. (2020) (CSV idx 12)
    # -------------------------------------------------------------
    {
        "id": 11,
        "csv_idx": 12,
        "arnumber": "8950333",
        "category": "Neural Architecture Search (NAS)",
        "primary_problem": "Manual trial-and-error design of deep CNN architectures for dermatological diagnosis is computationally inefficient, subjective, and sub-optimal for complex multi-class benchmarks.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Automated Architecture Discovery",
                "question": "Can Neural Architecture Search (NAS) using network morphism automatically discover optimal CNN topologies tailored for skin lesion classification that outperform hand-crafted networks?",
                "methodology": "Applied network morphism operations (inserting layers, widening channels) guided by hill-climbing search optimization on the ISIC 2018 benchmark.",
                "answer": "Yes. The morphologically discovered CNN achieved 82.8% multiclass accuracy and 81.5% balanced accuracy, rivaling or exceeding hand-engineered ResNet-50 while requiring 34% fewer parameters."
            },
            {
                "num": "RQ2",
                "dim": "Search Efficiency & Network Morphism",
                "question": "How does network morphism preserve learned model knowledge during architectural mutations to reduce search compute costs?",
                "methodology": "Inherited weights from parent architectures during layer insertions and dimensional expansions, training mutant models incrementally.",
                "answer": "Knowledge inheritance prevented re-training from scratch, enabling search convergence in orders of magnitude fewer GPU hours than standard reinforcement-learning NAS."
            },
            {
                "num": "RQ3",
                "dim": "AUC & Diagnostic Generalization",
                "question": "What mean ROC-AUC across the 7 classes of ISIC 2018 is attained by the NAS-derived architecture?",
                "methodology": "Evaluated the final searched architecture across 10,015 images using macro-averaged ROC-AUC and balanced accuracy metrics.",
                "answer": "Achieved a mean ROC-AUC of 0.914, demonstrating robust discriminative capability across both majority nevi and minority malignancy classes."
            },
            {
                "num": "RQ4",
                "dim": "Search Space Constraints",
                "question": "What are the computational limitations and search space sensitivity issues encountered during dermatological NAS?",
                "methodology": "Analyzed GPU day resource consumption and search trajectory dependence on initial seed architecture.",
                "answer": "The search process required multiple dedicated GPU days and exhibited sensitivity to seed model selection, with the search space restricted to feedforward convolutional operations."
            }
        ],
        "datasets": ["ISIC 2018 Challenge Task 3 (10,015 images, 7 classes)"],
        "metrics": {"Multiclass Accuracy": "82.8%", "Balanced Accuracy": "81.5%", "Mean AUC": "0.914", "Parameter Reduction": "34%"},
        "open_questions": [
            "Can NAS search spaces be expanded to discover hybrid attention blocks and vision transformer tokens automatically?",
            "Can multi-objective NAS optimize simultaneously for diagnostic accuracy and mobile inference latency?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 12: Magdy et al. (2023) (CSV idx 13)
    # -------------------------------------------------------------
    {
        "id": 12,
        "csv_idx": 13,
        "arnumber": "10181245",
        "category": "Computer Vision Enhancement & Multi-Model Transfer",
        "primary_problem": "Poor image contrast, irregular illumination, and skin artifacts degrade deep feature representations in transfer learning models.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Preprocessing & Contrast Enhancement",
                "question": "Does integrating Contrast Limited Adaptive Histogram Equalization (CLAHE) and color constancy improve deep transfer learning accuracy on dermoscopic images?",
                "methodology": "Implemented a computer vision pipeline incorporating Gray World color constancy and CLAHE contrast enhancement prior to transfer learning classification.",
                "answer": "Yes. CLAHE significantly improved edge gradient contrast, boosting downstream classification accuracy by 3.8% across pre-trained backbones."
            },
            {
                "num": "RQ2",
                "dim": "Comparative Backbone Benchmarking",
                "question": "How do modern CNN architectures (ResNet-50, DenseNet-201, EfficientNet-B0) compare when processing contrast-enhanced dermoscopic lesions?",
                "methodology": "Fine-tuned ResNet-50, DenseNet-201, and EfficientNet-B0 on enhanced ISIC 2019 and HAM10000 images under standardized hyperparameter protocols.",
                "answer": "EfficientNet-B0 achieved the superior trade-off of accuracy and parameter efficiency, reaching 94.6% accuracy, 93.2% sensitivity, 95.8% specificity, and 0.965 AUC."
            },
            {
                "num": "RQ3",
                "dim": "Precision & F1 Verification",
                "question": "What precision and F1-score are delivered by the optimized EfficientNet pipeline across dermoscopic benchmarks?",
                "methodology": "Measured precision and macro-averaged F1-scores across 5-fold cross-validation runs on benchmark datasets.",
                "answer": "EfficientNet-B0 with CLAHE delivered an F1-score of 94.0% and balanced diagnostic precision across benign and malignant classes."
            },
            {
                "num": "RQ4",
                "dim": "Preprocessing Latency & Artifacts",
                "question": "What are the computational trade-offs of multi-stage contrast enhancement pipelines during high-throughput clinical screening?",
                "methodology": "Profiled preprocessing execution time per image and analyzed false-positive edge artifacts generated by aggressive local histogram equalization.",
                "answer": "CLAHE can amplify high-frequency background noise (skin pores, hair stubble) in low-contrast images, requiring careful clipping limit tuning that increases per-image preprocessing time."
            }
        ],
        "datasets": ["ISIC 2019", "HAM10000"],
        "metrics": {"Accuracy (EfficientNet-B0)": "94.6%", "Sensitivity": "93.2%", "Specificity": "95.8%", "F1-Score": "94.0%", "AUC": "0.965"},
        "open_questions": [
            "Can contrast enhancement parameters be learned end-to-end via a differentiable image processing layer?",
            "How does the CLAHE-enhanced pipeline perform on non-dermoscopic smartphone camera images?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 13: Ji et al. (2024) - EFAM-Net (CSV idx 14)
    # -------------------------------------------------------------
    {
        "id": 13,
        "csv_idx": 14,
        "arnumber": "10695064",
        "category": "Multi-Scale Attention & Feature Fusion",
        "primary_problem": "Single-scale deep networks fail to capture both macroscopic lesion contour geometry and microscopic pigment network textures simultaneously.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Dual-Branch Attention Innovation",
                "question": "Can combining Enhanced Feature Fusion with Spatial and Channel Attention Mechanisms ('EFAM-Net') simultaneously capture global lesion boundaries and fine-grained dermoscopic textures?",
                "methodology": "Designed EFAM-Net featuring a multi-scale feature pyramid, a channel attention module (CAM) for inter-channel dependencies, and a spatial attention module (SAM) for lesion localization.",
                "answer": "Yes. EFAM-Net achieved a top-tier multi-class classification accuracy of 94.28% on HAM10000, significantly outperforming single-scale CNN baselines."
            },
            {
                "num": "RQ2",
                "dim": "Attention-Driven Feature Separation",
                "question": "How do spatial and channel attention mechanisms suppress irrelevant peripheral healthy skin artifacts while accentuating subtle atypical pigment networks?",
                "methodology": "Visualized attention weight maps across intermediate stages of the multi-scale pyramid on ambiguous lesion boundaries.",
                "answer": "Channel attention dynamically weighted discriminative pigment feature maps, while spatial attention effectively masked surrounding healthy tissue and vignetting artifacts."
            },
            {
                "num": "RQ3",
                "dim": "Multiclass Diagnostic Performance",
                "question": "What mean sensitivity, specificity, and AUC are attained by EFAM-Net across the 7 diagnostic classes of ISIC 2018 / HAM10000?",
                "methodology": "Evaluated EFAM-Net across 10,015 images using aspect-ratio preserving resizing, affine augmentations, and cross-entropy loss.",
                "answer": "Achieved mean sensitivity of 91.85%, mean specificity of 95.40%, F1-score of 93.12%, and an impressive ROC-AUC of 0.973."
            },
            {
                "num": "RQ4",
                "dim": "Computational Complexity",
                "question": "What is the memory and FLOP overhead of dual-branch multi-scale attention modules during model training and inference?",
                "methodology": "Benchmarked FLOP count, parameter scaling, and GPU inference latency against standard ResNet and MobileNet architectures.",
                "answer": "Dual attention branches increase computational complexity and training GPU memory requirements, demanding optimization before deployment on embedded medical devices."
            }
        ],
        "datasets": ["ISIC 2018 / HAM10000 (10,015 images across 7 classes)"],
        "metrics": {"Accuracy": "94.28%", "Mean Sensitivity": "91.85%", "Mean Specificity": "95.40%", "F1-Score": "93.12%", "AUC": "0.973"},
        "open_questions": [
            "Can EFAM-Net's multi-scale attention modules be distilled into a lightweight backbone for real-time mobile triage?",
            "How does EFAM-Net perform on clinical photography with heavy shadow occlusions?"
        ]
    }
]

print(f"Loaded PART1 with {len(PART1)} papers.")
