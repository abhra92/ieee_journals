"""
paper_rq_data_part2.py: Papers 14 to 26
"""

PART2 = [
    # -------------------------------------------------------------
    # Paper 14: Talavera-Martínez et al. (2021) (CSV idx 15)
    # -------------------------------------------------------------
    {
        "id": 14,
        "csv_idx": 15,
        "arnumber": "9306830",
        "category": "Artifact Removal & Deep Inpainting",
        "primary_problem": "Occluding hair shafts distort lesion borders and corrupt textural feature extraction; traditional heuristic filters like DullRazor blur underlying micro-vascular patterns.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Deep Segmentation vs. Classical Filters",
                "question": "Can a deep learning-based hair segmentation network outperform classical morphological filtering (DullRazor) in isolating fine and coarse hair artifacts without destroying genuine lesion borders?",
                "methodology": "Trained a modified U-Net architecture on a curated dataset of dermoscopic images with synthetically generated and annotated real hair masks.",
                "answer": "Yes. Deep hair segmentation achieved a 92.8% Dice coefficient and 87.2% Jaccard index, preserving underlying lesion borders far more accurately than DullRazor."
            },
            {
                "num": "RQ2",
                "dim": "Deep Inpainting & Texture Reconstruction",
                "question": "How does deep context-aware inpainting of occluded hair pixels affect the discriminability of downstream skin cancer classification models?",
                "methodology": "Evaluated classification accuracy on images preprocessed by deep inpainting vs. classical inpainting vs. raw occluded images.",
                "answer": "Deep inpainting improved downstream classification accuracy by 4.2% compared to raw hair-occluded images, and by 2.1% compared to traditional DullRazor filtering."
            },
            {
                "num": "RQ3",
                "dim": "Synthetic Hair Training Strategy",
                "question": "Does training deep segmentation networks on realistic synthetic hair masks generalize reliably to real-world clinical hair occlusions?",
                "methodology": "Constructed realistic synthetic hair models with variable thickness, curvature, and translucency to train the U-Net, tested on real hair benchmarks.",
                "answer": "Synthetic hair training generalized well, demonstrating robust segmentation across real dermoscopic hair artifacts without manual clinical mask annotations."
            },
            {
                "num": "RQ4",
                "dim": "Inpainting Blur & Feature Distortion",
                "question": "What are the limitations of deep inpainting when hair shafts occlude ultra-fine atypical pigment networks or micro-vessels?",
                "methodology": "Examined high-magnification dermoscopic edge cases where hair directly traverses critical diagnostic criteria.",
                "answer": "Deep inpainting can introduce subtle local blurring or interpolation artifacts across fine pigment lines, potentially masking micro-vascular structures."
            }
        ],
        "datasets": ["ISIC 2018 Hair Dataset Subsets (Synthetic and Real Annotated Hair)"],
        "metrics": {"Hair Dice Coefficient": "92.8%", "Jaccard Index": "87.2%", "Downstream Accuracy Gain": "+4.2% vs raw", "Gain vs DullRazor": "+2.1%"},
        "open_questions": [
            "Can generative adversarial inpainting reconstruct occluded pigment networks without any blurring?",
            "How can hair removal be integrated end-to-end into classification backbones as a differentiable layer?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 15: Gong et al. (2020) - StyleGANs (CSV idx 16)
    # -------------------------------------------------------------
    {
        "id": 15,
        "csv_idx": 16,
        "arnumber": "9062473",
        "category": "Generative Data Augmentation & GANs",
        "primary_problem": "Severe underrepresentation of malignant melanoma and rare lesion categories creates acute training bias and high false-negative rates in deep classifiers.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "High-Fidelity Synthetic Augmentation",
                "question": "Can high-resolution StyleGANs synthesize photorealistic dermoscopic images of minority skin lesions to resolve class imbalance without generating unrealistic clinical artifacts?",
                "methodology": "Trained StyleGAN on ISIC 2018 dermoscopic images to generate high-resolution synthetic samples for minority diagnostic classes, screening sample quality using Fréchet Inception Distance (FID).",
                "answer": "Yes. StyleGAN generated photorealistic lesions with an FID of 18.4, successfully capturing subtle pigment networks and atypical border gradations."
            },
            {
                "num": "RQ2",
                "dim": "Multi-Block Decision Fusion",
                "question": "How does combining multiple deep CNN feature extraction blocks with decision-level fusion improve classification stability on GAN-augmented datasets?",
                "methodology": "Integrated feature representations from distinct CNN backbones and applied weighted decision fusion to predict multi-class lesion probabilities.",
                "answer": "Decision fusion achieved an overall classification accuracy of 91.2% and mean sensitivity of 89.6%, outperforming standalone models trained on imbalanced data by 6.8% accuracy."
            },
            {
                "num": "RQ3",
                "dim": "Benchmark Diagnostic AUC",
                "question": "What overall ROC-AUC is achieved across the 7 classes of ISIC 2018 Task 3 by the StyleGAN-augmented ensemble framework?",
                "methodology": "Evaluated the synthesized balanced dataset across 7 diagnostic categories using macro-averaged ROC-AUC metrics.",
                "answer": "Achieved a macro-averaged ROC-AUC of 0.948, demonstrating balanced discrimination across both common nevi and rare dermatological malignancies."
            },
            {
                "num": "RQ4",
                "dim": "Generative Hallucination Risks",
                "question": "What clinical risks arise from subtle generative hallucinations in synthetic training images, and what are the GPU training costs?",
                "methodology": "Clinical review of synthesized lesion morphologies and profiling of high-resolution GAN training compute requirements.",
                "answer": "GAN training demands extensive multi-GPU compute resources, and subtle generative hallucinations (e.g. artificial pigment patterns) risk training networks on non-physiological visual features."
            }
        ],
        "datasets": ["ISIC 2018 Challenge Task 3 (Dermoscopic Image Classification)"],
        "metrics": {"Accuracy": "91.2%", "Mean Sensitivity": "89.6%", "AUC": "0.948", "StyleGAN FID": "18.4", "Accuracy Improvement": "+6.8%"},
        "open_questions": [
            "Can diffusion models (DDPM) surpass StyleGAN in fidelity and diversity while eliminating generative hallucination?",
            "What regulatory criteria are necessary to certify synthetic medical data for training clinical CAD systems?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 16: Riaz et al. (2023) (CSV idx 18)
    # -------------------------------------------------------------
    {
        "id": 16,
        "csv_idx": 18,
        "arnumber": "10189856",
        "category": "Joint Multi-Task Learning",
        "primary_problem": "Treating lesion segmentation and malignancy classification as isolated sequential pipelines compounds errors from segmentation to classification.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Multi-Task Joint Architecture",
                "question": "Can a comprehensive joint learning framework simultaneously optimize boundary segmentation and malignancy classification to exploit cross-task feature synergies?",
                "methodology": "Constructed a multi-task convolutional architecture with a shared encoder backbone that branches into a semantic segmentation decoder and a classification head.",
                "answer": "Yes. Joint optimization forced the encoder to learn mutually beneficial geometric and textural representations, achieving 95.3% classification accuracy and 91.4% segmentation Dice."
            },
            {
                "num": "RQ2",
                "dim": "Cross-Task Feature Regularization",
                "question": "Does auxiliary segmentation loss act as an effective regularizer to prevent the classification head from overfitting to spurious background artifacts?",
                "methodology": "Trained models with and without auxiliary segmentation supervision, analyzing intermediate feature activation maps and gradient stability.",
                "answer": "Auxiliary segmentation supervision effectively regularized classification gradients, boosting sensitivity to 94.1% and specificity to 96.5% on ISIC benchmarks."
            },
            {
                "num": "RQ3",
                "dim": "Benchmark Diagnostic AUC",
                "question": "What diagnostic discrimination (ROC-AUC) is achieved by the joint learning system on ISIC 2016 and ISIC 2017?",
                "methodology": "Evaluated the joint framework across ISIC 2016 (379 test) and ISIC 2017 (600 test) using ROC-AUC and F1-score.",
                "answer": "Achieved a high ROC-AUC of 0.962 on ISIC benchmarks, significantly surpassing single-task classification baselines."
            },
            {
                "num": "RQ4",
                "dim": "Loss Balancing & Ambiguous Borders",
                "question": "What are the optimization difficulties of balancing competing loss functions across tasks with unequal gradient magnitudes?",
                "methodology": "Analyzed task loss weight scheduling (classification cross-entropy vs. segmentation Dice loss) on lesions with diffuse, irregular borders.",
                "answer": "Heuristic manual tuning of task loss weights is required; suboptimal weighting causes gradient conflict, leading to slight under-segmentation on faint lesion margins."
            }
        ],
        "datasets": ["ISIC 2016 Benchmark", "ISIC 2017 Challenge Dataset"],
        "metrics": {"Classification Accuracy": "95.3%", "Sensitivity": "94.1%", "Specificity": "96.5%", "AUC": "0.962", "Segmentation Dice": "91.4%"},
        "open_questions": [
            "Can adaptive gradient balancing (e.g. GradNorm) automatically optimize multi-task loss weights dynamically during training?",
            "Can joint learning be extended to simultaneous lesion segmentation, multi-class diagnosis, and visual question answering?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 17: Ichim & Popescu (2020) (CSV idx 20)
    # -------------------------------------------------------------
    {
        "id": 17,
        "csv_idx": 20,
        "arnumber": "9210626",
        "category": "Multiple Connected Neural Networks & Texture Fusion",
        "primary_problem": "Subjectivity in visual dermatologist evaluations and limitations of single deep networks in capturing both global color distribution and localized micro-texture.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Multi-Connected Neural Topology",
                "question": "Can an objective diagnostic system based on Multiple Connected Neural Networks (MCNN) effectively fuse hand-crafted texture descriptors with deep CNN representations?",
                "methodology": "Developed an MCNN architecture integrating statistical color/texture features (GLCM, LBP in HSV/L*a*b* color spaces) with deep convolutional feature maps.",
                "answer": "Yes. Fusing explicit textural descriptors with deep abstract representations achieved superior diagnostic accuracy of 96.7% and AUC of 0.978 on PH2."
            },
            {
                "num": "RQ2",
                "dim": "Color Space Feature Engineering",
                "question": "Which color space transformations (HSV, L*a*b*) provide the most discriminative textural representations for distinguishing melanoma from dysplastic nevi?",
                "methodology": "Extracted Gray-Level Co-occurrence Matrix (GLCM) and Local Binary Pattern (LBP) features across RGB, HSV, and L*a*b* channels, benchmarking feature importance.",
                "answer": "L*a*b* and HSV color representations provided enhanced luminance-invariant color entropy and contrast metrics, substantially improving sensitivity to 95.8%."
            },
            {
                "num": "RQ3",
                "dim": "Cross-Dataset Validation",
                "question": "How consistently does the MCNN framework perform across independent clinical repositories (DermIS, DermQuest, and PH2)?",
                "methodology": "Validated the objective MCNN system across three distinct dermoscopic archives using sensitivity, specificity, and ROC analysis.",
                "answer": "Demonstrated high cross-dataset consistency, yielding 97.4% specificity and 0.978 AUC on PH2 while maintaining >95% accuracy across DermIS and DermQuest."
            },
            {
                "num": "RQ4",
                "dim": "Computational Complexity of Feature Pipelines",
                "question": "What is the computational overhead of combining complex handcrafted feature extraction with multi-network deep learning inference?",
                "methodology": "Profiled CPU/GPU execution time for hand-crafted color-texture feature extraction vs. pure end-to-end deep inference.",
                "answer": "Calculating GLCM and LBP descriptors across multiple color spaces introduces substantial CPU processing latency, creating a bottleneck for real-time mobile triage."
            }
        ],
        "datasets": ["PH2 Dataset (200 images)", "DermIS Repository", "DermQuest Archive"],
        "metrics": {"Accuracy (PH2)": "96.7%", "Sensitivity": "95.8%", "Specificity": "97.4%", "AUC": "0.978"},
        "open_questions": [
            "Can deep networks learn explicit GLCM and LBP textural filters end-to-end without separate feature computation?",
            "How does the MCNN system perform on full 7-class imbalanced benchmarks like HAM10000?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 18: Mittal et al. (2024) - DermCDSM (CSV idx 21)
    # -------------------------------------------------------------
    {
        "id": 18,
        "csv_idx": 21,
        "arnumber": "10459206",
        "category": "Clinical Decision Support & Spiking Neural Networks",
        "primary_problem": "Lack of standardized clinical decision support frameworks capable of handling high-dimensional dermatosis features while maintaining ultra-low computational energy profiles.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Decision Support Model Architecture",
                "question": "Can a systematic Clinical Decision Support Model ('DermCDSM') combining machine learning, deep learning, and Spiking Neural Networks (SNN) achieve clinical-grade dermatosis diagnosis?",
                "methodology": "Constructed DermCDSM incorporating DullRazor artifact removal, contrast enhancement, bio-inspired feature selection, deep CNN feature extraction, and energy-efficient SNN classification.",
                "answer": "Yes. DermCDSM achieved an impressive classification accuracy of 95.7% and an AUC of 0.981 across multi-class dermatological conditions."
            },
            {
                "num": "RQ2",
                "dim": "Bio-Inspired Feature Optimization",
                "question": "How effectively does bio-inspired heuristic feature selection eliminate redundant high-dimensional deep representations?",
                "methodology": "Applied nature-inspired metaheuristic search algorithms to prune uninformative feature vectors from intermediate CNN layer activations.",
                "answer": "Bio-inspired feature selection reduced representation dimensionality by over 50% while improving overall classification sensitivity to 94.2% and specificity to 96.8%."
            },
            {
                "num": "RQ3",
                "dim": "Multi-Benchmark Validation",
                "question": "What precision, recall, and F1-scores are achieved by DermCDSM across HAM10000 and ISIC 2019 benchmarks?",
                "methodology": "Validated the systematic framework across 10,015 images of HAM10000 and the 8 classes of ISIC 2019.",
                "answer": "Delivered an F1-score of 95.1% with robust diagnostic stability across inflammatory, viral, and malignant skin conditions."
            },
            {
                "num": "RQ4",
                "dim": "Neuromorphic Hardware Emulation",
                "question": "What deployment bottlenecks exist when executing Spiking Neural Networks on conventional von Neumann GPU hardware?",
                "methodology": "Analyzed computational latency and energy emulation overhead of spike-timing-dependent plasticity on standard GPUs vs. neuromorphic chips.",
                "answer": "Simulating event-driven SNNs on standard synchronous GPUs introduces software overhead, requiring true neuromorphic silicon to realize the promised energy efficiency."
            }
        ],
        "datasets": ["HAM10000 Benchmark", "ISIC 2019 Challenge Dataset"],
        "metrics": {"Accuracy": "95.7%", "Sensitivity": "94.2%", "Specificity": "96.8%", "F1-Score": "95.1%", "AUC": "0.981"},
        "open_questions": [
            "What is the actual battery life improvement of DermCDSM when deployed on neuromorphic edge processors like Intel Loihi?",
            "Can DermCDSM incorporate real-time patient electronic health record (EHR) data alongside image features?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 19: Karthik et al. (2024) (CSV idx 22)
    # -------------------------------------------------------------
    {
        "id": 19,
        "csv_idx": 22,
        "arnumber": "10731679",
        "category": "Vision Transformers & Non-Local Attention",
        "primary_problem": "Standard CNNs have restricted receptive fields that struggle with long-range spatial dependencies, while standard Vision Transformers impose heavy quadratic computational complexity on high-resolution images.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Hybrid Transformer-Attention Architecture",
                "question": "Can a hybrid framework combining Swin Transformer backbones with Dense Group Shuffle Non-Local Attention Networks (DGS-NLAN) capture long-range contextual relationships efficiently?",
                "methodology": "Constructed a hybrid architecture using Swin Transformer's shifted window self-attention for global contexts, coupled with DGS-NLAN for dense cross-group feature communication.",
                "answer": "Yes. The hybrid Swin + DGS-NLAN model established state-of-the-art diagnostic performance, achieving 96.8% accuracy and 0.985 AUC on HAM10000."
            },
            {
                "num": "RQ2",
                "dim": "Dense Group Shuffle Attention Mechanics",
                "question": "How does dense group shuffle non-local attention reduce the quadratic computational bottleneck of global self-attention while maintaining dense feature interaction?",
                "methodology": "Divided feature channels into groups, applied non-local self-attention within groups, and shuffled channels across groups to enable global cross-talk at linear complexity.",
                "answer": "Dense group shuffle enabled full receptive field coverage at a fraction of standard self-attention compute, boosting sensitivity to 95.4% and specificity to 97.6%."
            },
            {
                "num": "RQ3",
                "dim": "Multi-Class Benchmark Verification",
                "question": "What macro-averaged F1-score and precision are achieved by the hybrid transformer across the 7 classes of HAM10000 and ISIC 2019?",
                "methodology": "Conducted extensive 5-fold cross-validation across ISIC 2018/HAM10000 and ISIC 2019 using shifted window patch sizes of 4x4 and window sizes of 7x7.",
                "answer": "Achieved a macro-averaged F1-score of 96.1% with balanced precision across all 7 pathological categories."
            },
            {
                "num": "RQ4",
                "dim": "Memory Footprint & Data Hunger",
                "question": "What are the GPU memory constraints and training data scale requirements of vision transformer backbones compared to standard CNNs?",
                "methodology": "Benchmarked training convergence rates, GPU VRAM consumption, and performance degradation under low-data regimes.",
                "answer": "Swin Transformer requires substantial GPU VRAM during training and exhibits performance drops when trained on small datasets without extensive pre-training or aggressive augmentations."
            }
        ],
        "datasets": ["ISIC 2018 / HAM10000 (10,015 images)", "ISIC 2019 Benchmark"],
        "metrics": {"Accuracy": "96.8%", "Sensitivity": "95.4%", "Specificity": "97.6%", "F1-Score": "96.1%", "AUC": "0.985"},
        "open_questions": [
            "Can parameter-efficient fine-tuning (e.g. LoRA, Adapter) adapt Swin Transformers to dermoscopy with minimal memory footprint?",
            "How does the hybrid Swin model handle severe domain shift between dermoscopic images and clinical smartphone photos?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 20: Połap (2019) - Intelligent Things (CSV idx 23)
    # -------------------------------------------------------------
    {
        "id": 20,
        "csv_idx": 23,
        "arnumber": "8868149",
        "category": "Internet of Medical Things (IoMT) & Edge CAD",
        "primary_problem": "Cloud-based CAD systems require continuous high-bandwidth internet connectivity, raising critical patient privacy concerns and introducing network latency unsuitable for remote rural point-of-care screening.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Distributed Edge IoMT Architecture",
                "question": "Can an Internet of Medical Things (IoMT) framework execute decentralized skin mark screening directly on embedded edge sensors without relying on cloud infrastructure?",
                "methodology": "Designed a distributed intelligent sensor system using cascaded shallow CNNs, local edge heuristics, and lightweight morphological feature extractors.",
                "answer": "Yes. Successfully deployed on embedded testbeds, processing skin mark imagery locally with an overall screening accuracy of 92.1%."
            },
            {
                "num": "RQ2",
                "dim": "Edge Inference Latency & Resource Footprint",
                "question": "Can lightweight convolutional classifiers achieve sub-100ms inference latency on low-power embedded processors suitable for handheld dermoscopes?",
                "methodology": "Profiled inference latency, RAM utilization, and power consumption on embedded microcomputing hardware processing cutaneous mark images.",
                "answer": "Achieved inference latency under 85ms per image on edge hardware while maintaining low power consumption compatible with battery-powered mobile sensors."
            },
            {
                "num": "RQ3",
                "dim": "Diagnostic Accuracy on Multi-Source Data",
                "question": "What screening reliability is achieved across heterogeneous private clinical records and public benchmark subsets (PH2, ISIC)?",
                "methodology": "Evaluated the embedded framework across a combined corpus of private clinical recordings and benchmark subsets under varying capture angles.",
                "answer": "Attained stable diagnostic accuracy of 92.1%, demonstrating reliable preliminary screening of abnormal cutaneous marks before specialist referral."
            },
            {
                "num": "RQ4",
                "dim": "Edge Performance Trade-Offs",
                "question": "How does the diagnostic accuracy of shallow edge models compare to multi-million parameter cloud architectures, and how does it handle variable lighting?",
                "methodology": "Comparative accuracy analysis between edge-constrained models and cloud deep networks under varying ambient lighting conditions.",
                "answer": "Edge models show a 3-5% accuracy gap compared to heavy cloud ensembles, and are more vulnerable to uncontrolled ambient lighting shifts in handheld capture."
            }
        ],
        "datasets": ["Private Clinical Skin Mark Dataset", "PH2 Benchmark Subset", "ISIC Archive Subset"],
        "metrics": {"Embedded Screening Accuracy": "92.1%", "Inference Latency": "<85ms per image", "Deployment Target": "Embedded IoMT Edge Device"},
        "open_questions": [
            "Can federated learning enable distributed IoMT edge devices to update diagnostic models collaboratively without transmitting private patient images?",
            "How can on-chip optical calibration compensate for uncontrolled mobile ambient lighting automatically?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 21: Chatterjee et al. (2024) - IncepX (CSV idx 24)
    # -------------------------------------------------------------
    {
        "id": 21,
        "csv_idx": 24,
        "arnumber": "10608138",
        "category": "Multi-Scale Transfer Ensembles",
        "primary_problem": "Single transfer learning models often overfit to specific spatial scales, failing to detect both microscopic localized lesions and broad diffuse malignant patches.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Cross-Architectural Ensemble Innovation",
                "question": "Does fusing multi-scale feature representations from Inception-v3 and Xception into a unified ensemble ('IncepX') improve early multi-class lesion detection?",
                "methodology": "Developed the IncepX-Ensemble architecture, combining Inception-v3's multi-scale inception modules with Xception's depthwise separable convolutions via dynamic weighted averaging.",
                "answer": "Yes. IncepX achieved an exceptional overall classification accuracy of 95.8% on HAM10000, outperforming both standalone Inception-v3 and Xception."
            },
            {
                "num": "RQ2",
                "dim": "Dynamic Weighted Decision Fusion",
                "question": "How does dynamic confidence-weighted decision fusion improve classification over standard unweighted soft-voting?",
                "methodology": "Assigned dynamic weights to backbone predictions based on per-class validation confidence matrices rather than simple uniform averaging.",
                "answer": "Dynamic weighting effectively suppressed confident mispredictions from individual backbones, boosting sensitivity to 94.1% and specificity to 97.2%."
            },
            {
                "num": "RQ3",
                "dim": "Diagnostic Generalization & AUC",
                "question": "What macro-averaged F1-score and ROC-AUC are achieved by IncepX across the 7 diagnostic categories of HAM10000?",
                "methodology": "Evaluated the ensemble across 10,015 dermoscopic images with adaptive normalization and geometric data augmentation.",
                "answer": "Achieved a macro-averaged F1-score of 94.8% and an outstanding ROC-AUC of 0.978 across all 7 pathological categories."
            },
            {
                "num": "RQ4",
                "dim": "Computational Overhead & Minority Ambiguity",
                "question": "What is the inference latency overhead of running dual deep backbones, and how does IncepX perform on rare dermatofibroma cases?",
                "methodology": "Profiled inference runtime and per-class error distribution across minority classes.",
                "answer": "Running dual deep backbones nearly doubles FLOP count and inference time, and moderate false-positive rates persist on rare minority categories like dermatofibroma."
            }
        ],
        "datasets": ["ISIC 2018 / HAM10000 (10,015 images across 7 classes)"],
        "metrics": {"Accuracy": "95.8%", "Sensitivity": "94.1%", "Specificity": "97.2%", "F1-Score": "94.8%", "AUC": "0.978"},
        "open_questions": [
            "Can knowledge distillation compress the dual-backbone IncepX ensemble into a single lightweight MobileNet model?",
            "How does IncepX perform on clinical photographic datasets containing dark skin phototypes (Fitzpatrick IV-VI)?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 22: Gong et al. (2020) - Ensemble Advantage (CSV idx 26)
    # -------------------------------------------------------------
    {
        "id": 22,
        "csv_idx": 26,
        "arnumber": "9175002",
        "category": "Architectural Advantage Mining & Group Decision",
        "primary_problem": "Individual deep learning models possess unique diagnostic strengths on specific lesion sub-types but suffer from blind spots on others, which uniform averaging ensembles fail to leverage.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Individual Advantage Mining",
                "question": "Can an ensemble strategy explicitly identify and exploit the individual class-specific advantages of distinct CNN backbones (ResNet, Inception, DenseNet) for superior group decision-making?",
                "methodology": "Constructed an ensemble framework that measures each model's class-specific diagnostic advantage on validation splits, assigning priority votes accordingly.",
                "answer": "Yes. Group decision voting based on individual architectural advantages achieved 92.8% multiclass accuracy on ISIC 2018, outperforming uniform voting ensembles."
            },
            {
                "num": "RQ2",
                "dim": "Multi-Model Diversity & Complementarity",
                "question": "How do complementary feature representations from residual, inception, and densely connected architectures combine to reduce false-negative diagnostic errors?",
                "methodology": "Analyzed feature diversity and class-wise correlation matrices across ResNet, Inception, and DenseNet predictions.",
                "answer": "Complementary feature extraction reduced false negatives on malignant melanoma, yielding an overall sensitivity of 91.5% and specificity of 94.3%."
            },
            {
                "num": "RQ3",
                "dim": "Benchmark Performance on ISIC",
                "question": "What ROC-AUC is attained by the individual advantage ensemble across the ISIC 2017 and ISIC 2018 challenge datasets?",
                "methodology": "Evaluated the group decision pipeline across ISIC 2017 and ISIC 2018 multi-class benchmarks.",
                "answer": "Achieved a macro-averaged ROC-AUC of 0.956, validating consistent multi-class discrimination across benchmark years."
            },
            {
                "num": "RQ4",
                "dim": "Ensemble Redundancy & Memory Overhead",
                "question": "What is the memory and compute overhead of maintaining multiple full-scale deep backbones in a clinical production deployment?",
                "methodology": "Evaluated memory footprint and evaluated whether backbone feature maps contain redundant parameters.",
                "answer": "Maintaining three distinct deep backbones substantially increases memory consumption and deployment complexity, with noticeable representation overlap across layers."
            }
        ],
        "datasets": ["ISIC 2017 Challenge Dataset", "ISIC 2018 Challenge Task 3"],
        "metrics": {"Accuracy": "92.8%", "Sensitivity": "91.5%", "Specificity": "94.3%", "AUC": "0.956"},
        "open_questions": [
            "Can reinforcement learning dynamically select which single backbone to execute per image to avoid running all models concurrently?",
            "How does individual advantage voting perform when expanding to 10+ rare dermatological categories?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 23: Sathvika et al. (2024) (CSV idx 27)
    # -------------------------------------------------------------
    {
        "id": 23,
        "csv_idx": 27,
        "arnumber": "10496674",
        "category": "Hybrid Deep Features & Handcrafted Textures",
        "primary_problem": "Deep features from standard CNNs often ignore geometric asymmetry and bi-sectional textural differences that dermatologists explicitly use in the ABCD criteria.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Bi-Sectional Textural Modeling",
                "question": "Does extracting bi-sectional textural features across divided lesion halves capture dermatological ABCD asymmetry more effectively than global image descriptors?",
                "methodology": "Partitioned lesions geometrically along principal axes and extracted bi-sectional Gray-Level Co-occurrence Matrix (GLCM) and statistical texture descriptors.",
                "answer": "Yes. Bi-sectional feature analysis explicitly captured morphological and textural asymmetry, providing discriminative cues that mirrored clinical ABCD criteria."
            },
            {
                "num": "RQ2",
                "dim": "Pipelined Deep Features + SVM Classification",
                "question": "Can combining deep feature activations from an AlexNet CNN with bi-sectional handcrafted texture descriptors in a Support Vector Machine (SVM) classifier outperform end-to-end CNNs?",
                "methodology": "Extracted deep embeddings from pre-trained AlexNet, concatenated them with bi-sectional textural vectors, and trained an optimized SVM with RBF kernel.",
                "answer": "The hybrid pipeline achieved a classification accuracy of 94.6%, sensitivity of 93.8%, and specificity of 95.2%, outperforming standalone AlexNet."
            },
            {
                "num": "RQ3",
                "dim": "Diagnostic F1-Score & Robustness",
                "question": "What diagnostic F1-score is attained by the pipelined AlexNet-SVM model on ISIC 2019 and HAM10000 benchmarks?",
                "methodology": "Validated the hybrid pipeline across benchmark subsets using stratified 10-fold cross-validation.",
                "answer": "Achieved a balanced diagnostic F1-score of 94.1%, demonstrating stable discrimination between benign and malignant lesions."
            },
            {
                "num": "RQ4",
                "dim": "Geometric Partitioning Limitations",
                "question": "Under what topological conditions does geometric bi-sectional partitioning fail, and why does pipelined decoupling prevent end-to-end optimization?",
                "methodology": "Analyzed failure cases on highly irregular, non-convex, and multifocal skin lesions.",
                "answer": "Fixed bi-sectional geometric partitioning fails on multi-lobed and non-convex lesions, and decoupling feature extraction from SVM training prevents end-to-end gradient updates."
            }
        ],
        "datasets": ["ISIC 2019 Benchmark", "HAM10000 Dataset Subsets"],
        "metrics": {"Accuracy": "94.6%", "Sensitivity": "93.8%", "Specificity": "95.2%", "F1-Score": "94.1%"},
        "open_questions": [
            "Can differentiable geometric slicing layers enable end-to-end training of bi-sectional networks without separate SVM stages?",
            "How does bi-sectional analysis perform on non-dermoscopic smartphone photos where lesion borders are ill-defined?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 24: Faizi & Adnan (2024) (CSV idx 28)
    # -------------------------------------------------------------
    {
        "id": 24,
        "csv_idx": 28,
        "arnumber": "10416953",
        "category": "Lesion Segmentation & Normalized Cross-Correlation",
        "primary_problem": "Standard clustering algorithms (standard k-means, Otsu) are easily corrupted by non-uniform skin pigmentation, lighting gradients, and hair artifacts during boundary segmentation.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Algorithmic Clustering Innovation",
                "question": "Can Normalized Cross-Correlation (NCC)-based k-means clustering improve the boundary segmentation accuracy of melanoma lesions over traditional unsupervised methods?",
                "methodology": "Formulated an improved k-means algorithm that uses Normalized Cross-Correlation as its similarity metric rather than standard Euclidean distance, matching template pigment distributions.",
                "answer": "Yes. NCC-based k-means achieved an outstanding segmentation accuracy of 96.8% and a Dice coefficient of 93.4% on the PH2 benchmark."
            },
            {
                "num": "RQ2",
                "dim": "Illumination & Hair Robustness",
                "question": "How does NCC similarity mitigate sensitivity to spatial illumination gradients and fine hair occlusions in dermoscopic imagery?",
                "methodology": "Applied DullRazor artifact suppression followed by multi-channel NCC template matching across varying skin tone backgrounds.",
                "answer": "NCC normalized local luminance variations, yielding an 87.9% Jaccard index and preventing cluster centers from drifting toward bright skin reflections."
            },
            {
                "num": "RQ3",
                "dim": "Cross-Benchmark Segmentation Quality",
                "question": "How consistently does the NCC k-means segmentation framework perform across ISIC 2017 and PH2 datasets?",
                "methodology": "Evaluated segmented masks against expert ground-truth annotations across ISIC 2017 and PH2 using Dice, Jaccard, and pixel accuracy.",
                "answer": "Demonstrated consistent boundary delineation across datasets, outperforming standard k-means, Otsu thresholding, and baseline Chan-Vese active contours."
            },
            {
                "num": "RQ4",
                "dim": "Computational Scalability of NCC",
                "question": "What is the computational complexity of calculating normalized cross-correlation across high-resolution image pixels compared to standard Euclidean distance?",
                "methodology": "Profiled per-image iteration runtimes and convergence rates across variable image resolutions.",
                "answer": "NCC calculation is computationally more intensive than Euclidean distance, increasing per-image segmentation latency on ultra-high-resolution dermoscopic images."
            }
        ],
        "datasets": ["PH2 Benchmark (200 images)", "ISIC 2017 Segmentation Dataset"],
        "metrics": {"Segmentation Accuracy (PH2)": "96.8%", "Dice Coefficient": "93.4%", "Jaccard Index": "87.9%"},
        "open_questions": [
            "Can GPU-accelerated FFTs speed up NCC template calculations for real-time mobile segmentation?",
            "How does NCC k-means compare to modern deep transformer segmentation models like SegFormer?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 25: Pereira et al. (2022) (CSV idx 29)
    # -------------------------------------------------------------
    {
        "id": 25,
        "csv_idx": 29,
        "arnumber": "9832874",
        "category": "3D Topography & Multiple Instance Learning",
        "primary_problem": "Conventional 2D dermoscopy flattens 3D lesion elevation and surface texture, discarding critical palpable volumetric cues that dermatologists rely upon during physical clinical examination.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "3D Feature Reconstruction",
                "question": "Can 3D surface elevation and roughness profiles reconstructed from photometric stereo dermoscopy provide discriminative diagnostic signals absent in conventional 2D imagery?",
                "methodology": "Reconstructed 3D surface height maps and surface normal vectors from multi-illumination photometric stereo dermoscopy, extracting 3D volumetric curvature features.",
                "answer": "Yes. Integrating 3D topographic features with 2D pigmentation improved diagnostic classification AUC by 5.3% over 2D-only models, reaching an overall AUC of 0.942."
            },
            {
                "num": "RQ2",
                "dim": "Multiple Instance Learning (MIL) Formulation",
                "question": "How does Multiple Instance Learning (MIL) effectively aggregate local 3D surface patches into a patient-level melanoma diagnosis without requiring manual patch-level annotations?",
                "methodology": "Treated each lesion as a 'bag' of 3D surface patches, training an attention-based MIL pooling network to weight patches contributing to malignancy.",
                "answer": "Attention MIL successfully localized suspicious elevated nodules and irregular margins, yielding 91.5% accuracy, 89.2% sensitivity, and 93.1% specificity."
            },
            {
                "num": "RQ3",
                "dim": "2D vs. 3D Comparative Performance",
                "question": "What is the quantitative diagnostic advantage of multimodal 2D+3D feature fusion over standard 2D dermoscopic baselines?",
                "methodology": "Conducted ablation experiments comparing 2D color models, 3D topographic models, and combined 2D+3D representations on clinical cohorts.",
                "answer": "Combined 2D+3D models consistently outperformed unimodal 2D baselines, particularly in distinguishing elevated nodular melanoma from flat benign nevi."
            },
            {
                "num": "RQ4",
                "dim": "Hardware Accessibility & Dataset Scale",
                "question": "What hardware acquisition barriers restrict the clinical scalability of 3D photometric stereo dermoscopy?",
                "methodology": "Assessed clinical deployment requirements, imaging rig costs, calibration protocols, and dataset size constraints.",
                "answer": "Photometric stereo requires specialized multi-light dermoscopic hardware that is not widely available in general practice, restricting public dataset sizes."
            }
        ],
        "datasets": ["Multiview 3D Dermoscopy Clinical Dataset (Photometric Stereo Reconstructions)"],
        "metrics": {"Accuracy": "91.5%", "Sensitivity": "89.2%", "Specificity": "93.1%", "AUC": "0.942", "AUC Improvement vs 2D": "+5.3%"},
        "open_questions": [
            "Can single-image neural radiance fields (NeRF) or depth estimation networks synthesize 3D surface features from standard smartphone photos?",
            "How does 3D surface modeling perform on ulcerated and bleeding malignant melanomas?"
        ]
    },

    # -------------------------------------------------------------
    # Paper 26: Qian et al. (2024) - SPCB-Net (CSV idx 31)
    # -------------------------------------------------------------
    {
        "id": 26,
        "csv_idx": 31,
        "arnumber": "10374026",
        "category": "Pyramid Attention & Higher-Order Pooling",
        "primary_problem": "Fine-grained skin lesions exhibit severe scale variation, where crucial diagnostic features (pigment network, dots, globules) exist at microscopic resolutions while overall lesion asymmetry exists globally.",
        "rqs": [
            {
                "num": "RQ1",
                "dim": "Self-Interactive Attention Pyramid",
                "question": "Can a Self-Interactive Attention Pyramid Network ('SPCB-Net') capture cross-scale feature correlations to resolve extreme scale variations in skin lesions?",
                "methodology": "Designed an attention pyramid that allows multi-scale feature maps to interact bidirectionally, exchanging high-level semantic context with low-level high-resolution textures.",
                "answer": "Yes. SPCB-Net attained state-of-the-art identification accuracy of 95.6% across diverse lesion scales on ISIC 2018 and ISIC 2019."
            },
            {
                "num": "RQ2",
                "dim": "Higher-Order Bilinear-Trilinear Pooling",
                "question": "How does Cross-Layer Bilinear-Trilinear Pooling enhance fine-grained representation learning compared to standard first-order global average pooling?",
                "methodology": "Implemented bilinear and trilinear tensor pooling across pyramid layers to compute second- and third-order feature interactions.",
                "answer": "Higher-order pooling captured subtle co-occurrences of pigment dots and atypical streaks, boosting sensitivity to 93.9%, specificity to 97.1%, and AUC to 0.982."
            },
            {
                "num": "RQ3",
                "dim": "Multiclass Benchmark Generalization",
                "question": "What macro-averaged F1-score is delivered by SPCB-Net across HAM10000 and ISIC 2019 challenge datasets?",
                "methodology": "Evaluated the multi-scale higher-order network across 7-class and 8-class benchmarks with standard augmentation pipelines.",
                "answer": "Delivered an overall macro-averaged F1-score of 94.7%, maintaining robust discrimination across both macroscopic and microscopic lesion types."
            },
            {
                "num": "RQ4",
                "dim": "Tensor Dimensionality & Compute Cost",
                "question": "What is the memory and FLOP complexity overhead of calculating trilinear feature interactions during high-resolution training?",
                "methodology": "Benchmarked tensor dimension expansion, backpropagation memory consumption, and training epoch runtimes.",
                "answer": "Trilinear pooling generates high-dimensional intermediate tensors that significantly increase GPU memory consumption and training time, requiring dimensional reduction heuristics."
            }
        ],
        "datasets": ["ISIC 2018 Challenge Task 3", "ISIC 2019 Benchmark", "HAM10000"],
        "metrics": {"Accuracy": "95.6%", "Sensitivity": "93.9%", "Specificity": "97.1%", "F1-Score": "94.7%", "AUC": "0.982"},
        "open_questions": [
            "Can factorized low-rank tensor decompositions approximate trilinear pooling to reduce memory footprint on edge devices?",
            "How does SPCB-Net perform on high-resolution whole-slide dermatopathology imagery?"
        ]
    }
]

print(f"Loaded PART2 with {len(PART2)} papers.")
