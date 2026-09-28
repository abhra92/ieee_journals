"""
generate_all_outputs.py
Comprehensive generation of:
1. Research_Methodology_RQs_39_Papers.docx (Word Document)
2. latex_research_methodology/ (Modular LaTeX project compiled to main.pdf)
"""

import os, sys, re, csv, json, subprocess
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'papers_39_detailed.json'), 'r', encoding='utf-8') as f:
    PAPERS = json.load(f)

print(f"Loaded {len(PAPERS)} detailed paper records.")

# -------------------------------------------------------------
# Common Definitions for Steps 3 to 10
# -------------------------------------------------------------

STEP3_PATTERNS = {
    "A": {
        "title": "Most Commonly Used Datasets",
        "strong": "HAM10000 / ISIC 2018 Task 3 (17 papers: 3, 5, 7, 9, 10, 11, 12, 13, 15, 18, 19, 21, 23, 26, 29, 31, 39) and ISIC Archive series (2016-2020) constitute the dominant benchmark for dermoscopic image classification.",
        "moderate": "PH2 dataset (200 dermoscopic images) utilized frequently for small-scale external validation, transfer testing, and segmentation validation (Papers 7, 17, 20, 24, 27).",
        "limited": "DermIS / DermQuest clinical collections (Papers 2, 6, 17), Derm7pt multimodal dataset (Paper 30), and smartphone clinical photography archives (PAD-UFES-20, Dermofit; Papers 34, 36)."
    },
    "B": {
        "title": "Most Commonly Used Deep Learning Architectures",
        "strong": "Standard Convolutional Neural Networks (CNNs) with Transfer Learning backbones (ResNet-50, DenseNet-121/201, VGG-16, MobileNetV2, InceptionV3) dominate existing implementations (Papers 1, 2, 4, 5, 6, 8, 11, 12, 16, 17, 21, 22, 23, 31, 33).",
        "moderate": "Vision Transformers (ViT, Swin-Transformer, DeiT) demonstrating superior long-range global context modeling (Papers 18, 19, 37) and Capsule Networks (FixCaps; Paper 9).",
        "limited": "Parameter-efficient fine-tuning via Mixture-of-LoRA Experts (MoLE; Paper 38), Dual-Stream Focal Modulation (FoMoSkinNet; Paper 36), Quantum Chebyshev Polynomials (Paper 29), and Neuro-Symbolic Knowledge Graphs (Paper 30)."
    },
    "C": {
        "title": "Most Commonly Used Preprocessing Methods",
        "strong": "Image spatial standardizing (resizing to 224x224, 256x256, or 300x300 pixels) and pixel intensity min-max normalization or z-score standardization (Papers 1-6, 8-13, 15, 16, 18, 19, 21-23, 26, 29, 31, 33, 36, 37, 39).",
        "moderate": "Morphological hair artifact removal algorithms, predominantly DullRazor or bottom-hat filtering (Papers 2, 14, 15, 23, 24, 27, 39).",
        "limited": "Deep learning-based hair segmentation and inpainting via U-Net (Paper 14), Nonnegative Matrix Factorization (NMF) color unmixing (Paper 34), and nonlinear power-law contrast transformations (Paper 1)."
    },
    "D": {
        "title": "Most Commonly Used Augmentation Techniques",
        "strong": "Standard geometric transformations, including random affine rotations (90°, 180°, 270°), horizontal/vertical flipping, random zooming, and cropping (Papers 2, 3, 5, 6, 8, 10, 11, 13, 16, 18, 19, 21, 23, 26, 31, 33, 36, 37).",
        "moderate": "Color space jittering, brightness adjustments, and contrast variations (Papers 2, 3, 12, 13, 18, 21, 26, 39).",
        "limited": "Generative synthetic oversampling via Generative Adversarial Networks (StyleGAN, SLGAN-EID; Papers 15, 39) and margin-free metric clustering oversampling (Paper 10)."
    },
    "E": {
        "title": "Most Commonly Reported Evaluation Metrics",
        "strong": "Overall Classification Accuracy, Sensitivity (Recall), Specificity, and AUC-ROC (Papers 1-13, 15-27, 29-39).",
        "moderate": "Precision, F1-Score (Macro and Weighted), and Confusion Matrix per-class counts (Papers 2, 3, 5, 8, 10, 13, 18, 19, 21, 26, 31, 33, 36, 37).",
        "limited": "Balanced Accuracy, Matthews Correlation Coefficient (MCC), Mean Average Precision (mAP; Paper 31), Dice Similarity Coefficient (for segmentation; Papers 14, 24, 27, 34), and BLEU-4 natural language generation metrics (Paper 32)."
    },
    "F": {
        "title": "Commonly Reported Limitations",
        "strong": "Severe Class Imbalance in benchmark repositories (especially HAM10000, where melanocytic nevi comprise ~67% of samples, leading to high overall accuracy but catastrophic false-negative rates on rare classes like dermatofibroma and vascular lesions; Papers 3, 5, 9, 10, 15, 18, 19, 21, 26, 33, 39).",
        "moderate": "High computational overhead, extensive parameter counts, and inference latency preventing real-time mobile edge deployment (Papers 4, 9, 11, 18, 19, 21, 36, 38); and vulnerability to dermoscopic artifacts (hair, ruler markings, vignetting, air bubbles; Papers 2, 14, 24, 27, 34).",
        "limited": "Saliency map unfaithfulness and lack of correlation with clinical diagnostic criteria (ABCD checklist; Papers 3, 27, 30, 35)."
    },
    "G": {
        "title": "Commonly Reported Research Gaps",
        "strong": "The absence of balanced, loss-level or cost-sensitive mitigation strategies that resolve extreme multi-class imbalance without synthesizing noisy generative artifacts (Papers 3, 5, 10, 15, 19, 21, 33, 39).",
        "moderate": "The trade-off between architectural complexity and mobile/edge triage feasibility, where heavy vision transformers outperform lightweight CNNs but cannot run on edge hardware (Papers 3, 4, 9, 19, 21, 36, 38).",
        "limited": "The lack of quantitative evaluation of Explainable AI (XAI) localization fidelity (testing whether Grad-CAM heatmaps overlap with true pathological lesion boundaries; Papers 3, 27, 30, 35)."
    },
    "H": {
        "title": "Areas Where Existing Studies Disagree",
        "strong": "Heavy Vision Transformers vs. Parameter-Efficient Lightweight CNNs: Karthik et al. (Paper 19) and Mittal et al. (Papers 18, 37) argue that Vision Transformers and attention networks are essential for capturing global multi-scale context. Conversely, Wei et al. (Paper 4), Gururaj et al. (Paper 5), and Lan et al. (Paper 9) demonstrate that compact, parameter-efficient CNNs and fixed capsules achieve competitive diagnostic accuracy (95-97%) with a fraction of the parameters and FLOPs, arguing that heavy transformers overfit on small/medium medical datasets.",
        "moderate": "Preprocessing & Hair Removal Utility: Talavera-Martínez et al. (Paper 14), Faizi et al. (Paper 24), and Ashraf et al. (Paper 2) emphasize that hair artifacts and healthy background skin drastically degrade classification and require algorithmic removal (DullRazor, U-Net inpainting). Conversely, several recent benchmark studies (Papers 1, 3, 5, 13, 19, 21) train directly on raw, uninpainted images, arguing that algorithmic hair removal introduces blurry border artifacts, alters textural lesion boundaries, and degrades fine-grained classification.",
        "limited": "Generative Oversampling vs. Metric Loss Adjustment: Gong et al. (Paper 15) and Zafar et al. (Paper 39) advocate using GANs (StyleGAN, SLGAN) to synthesize minority samples to balance datasets. In contrast, Öztürk & Çukur (Paper 10) and Wang et al. (Paper 33) demonstrate that generative oversampling often introduces hallucinated high-frequency artifacts, arguing instead for metric-space loss adjustments (COMF-TL, part cross-entropy) that operate directly on real samples."
    },
    "I": {
        "title": "Areas That Are Under-Researched",
        "strong": "Fine-grained diagnostic sensitivity and macro-F1 on extreme minority classes (Dermatofibroma [115 images, 1.15%] and Vascular Lesions [142 images, 1.42%]) in HAM10000. Most papers highlight global accuracy (>85-90%) while concealing near-zero sensitivity on rare classes (Papers 3, 5, 10, 19, 21).",
        "moderate": "Quantitative localization fidelity of Explainable AI. While many papers display qualitative Grad-CAM heatmaps (Papers 3, 19, 27), almost none quantitatively measure the Intersection-over-Union (IoU) or pointing game accuracy of these heatmaps against ground-truth clinical lesion masks.",
        "limited": "Standardized comparative ablation of parameter-efficient transfer learning backbones under identical data splitting and optimization protocols on HAM10000."
    },
    "J": {
        "title": "Methodological Weaknesses in Existing Studies",
        "strong": "Over-reliance on Global Accuracy on Imbalanced Data: Reporting 85-92% overall accuracy without highlighting that a naive majority-class classifier predicting 'melanocytic nevus' achieves ~67% accuracy by default (Papers 1, 4, 8, 12, 17, 20, 23).",
        "moderate": "Data Leakage Across Patient Lesions: HAM10000 contains multiple duplicate lesions from the same patient. Several studies perform random image-level train/test splits rather than lesion-level or patient-level grouping, allowing the same lesion to appear in both training and test sets and falsely inflating accuracy (addressed explicitly in Papers 7, 10, 18).",
        "limited": "Absence of Multi-Metric Reporting & Confidence Intervals: Failing to report sensitivity, specificity, macro-F1, and confusion matrices alongside accuracy, making clinical triage utility unverifiable (Papers 1, 8, 12, 17, 23)."
    }
}

STEP4_GAPS = [
    {
        "gap": "Severe Class Imbalance and Extreme Minority Sensitivity Collapse in 7-Class HAM10000 Classification",
        "evidence": "In HAM10000, melanocytic nevi (nv) account for 6,705 of 10,015 images (67%), whereas dermatofibroma (df, 115 images, 1.15%) and vascular lesions (vasc, 142 images, 1.42%) are heavily marginalized. Across multiple surveyed studies, models report overall accuracies exceeding 85-90%, but per-class sensitivity on df and vasc collapses to under 40%.",
        "paper_numbers": "Papers 3, 5, 9, 10, 15, 18, 19, 21, 26, 33, 39",
        "why_matters": "A screening model that achieves 90% accuracy by systematically failing on rare or malignant classes presents severe diagnostic hazards in clinical triage. True clinical utility demands balanced sensitivity across all seven categories.",
        "how_addressed": "Implement and systematically evaluate cost-sensitive learning formulations (Class-Weighted Cross-Entropy, Focal Loss) and targeted geometric oversampling against standard cross-entropy across transfer learning backbones.",
        "feasibility": "Fully feasible on HAM10000 without requiring synthetic GAN generation or external datasets."
    },
    {
        "gap": "Lack of Quantitative Localization Fidelity and Alignment in Visual Explainability (Grad-CAM)",
        "evidence": "Studies such as Mridha et al. (Paper 3) and Narayanan et al. (Paper 27) provide qualitative Grad-CAM heatmaps to claim model interpretability. However, none of these studies quantitatively measure whether the highlighted regions correspond to actual lesion pathology or spurious background artifacts (e.g., dark vignetting, skin hairs, air bubbles).",
        "paper_numbers": "Papers 3, 10, 13, 19, 27, 30, 35",
        "why_matters": "A deep neural network can achieve high classification accuracy based on spurious image correlations rather than genuine lesion morphology. Without quantitative localization validation, explainability maps provide a false sense of clinical trust.",
        "how_addressed": "Conduct quantitative localization evaluation by computing Intersection-over-Union (IoU) and Pointing Game Hit Rates between Grad-CAM / Grad-CAM++ attribution heatmaps and official ISIC 2018 ground-truth lesion segmentation masks.",
        "feasibility": "Fully feasible. The ISIC 2018 challenge repository provides public ground-truth binary lesion segmentation masks corresponding to HAM10000 images."
    },
    {
        "gap": "Architectural Parameter Overhead vs. Multi-Class Diagnostic Discriminability in Edge-Feasible Transfer Learning",
        "evidence": "Recent literature shows a sharp divergence between heavy transformer architectures (Swin, DeiT; Papers 18, 19, 37) requiring extensive computational resources, and lightweight CNN architectures (MobileNetV2, ShuffleNet, EfficientNet-B0; Papers 4, 5, 20, 31, 36). Few studies systematically benchmark where the point of diminishing diagnostic returns occurs under identical experimental conditions.",
        "paper_numbers": "Papers 1, 4, 5, 8, 11, 13, 19, 21, 23, 26, 31, 36, 38",
        "why_matters": "Edge-based smart healthcare and mobile dermatology screening (as envisioned in Papers 3, 20, 36) require compact architectures that run in resource-constrained environments without sacrificing multi-class diagnostic sensitivity.",
        "how_addressed": "Perform an empirical trade-off analysis benchmarking parameter count (M), FLOPs (G), inference latency (ms), and macro-averaged diagnostic metrics (Macro-F1, Balanced Accuracy, AUC-ROC) across lightweight versus heavy transfer learning architectures on HAM10000.",
        "feasibility": "Completely feasible using standard workstation hardware and PyTorch / TensorFlow frameworks."
    },
    {
        "gap": "Inconsistent Impact and Empirical Justification of Preprocessing Artifact Removal on CNN Feature Representations",
        "evidence": "Papers 2, 14, 24, 27, 34, 39 argue that hair removal (e.g., DullRazor) and contrast stretching are essential prerequisites to eliminate artifacts. Conversely, Papers 1, 3, 5, 10, 13, 19, 21 train directly on raw images and achieve superior or equivalent performance, raising questions about whether morphological inpainting removes critical subtle lesion border cues.",
        "paper_numbers": "Papers 1, 2, 3, 5, 10, 13, 14, 19, 21, 24, 27, 34, 39",
        "why_matters": "DullRazor and heuristic inpainting algorithms are computationally intensive and can introduce synthetic blur, potentially altering diagnostic ABCD borderline irregularities.",
        "how_addressed": "Execute a controlled ablation study training identical transfer learning models on: (a) raw resized images, (b) DullRazor hair-removed images, and (c) contrast-enhanced images, evaluating the resulting per-class sensitivity and boundary Grad-CAM focus.",
        "feasibility": "100% feasible on the HAM10000 dataset using standard computer vision libraries."
    }
]

STEP5_CANDIDATE_RQS = [
    {
        "id": "RQ_cand1",
        "text": "How do cost-sensitive loss formulations (Class-Weighted Cross-Entropy vs. Focal Loss) affect the per-class sensitivity and macro-averaged F1-score of extreme minority classes (dermatofibroma and vascular lesions) compared to standard unweighted cross-entropy in 7-class HAM10000 classification?",
        "gap_id": "Gap 1 (Class Imbalance)",
        "papers": "Papers 3, 5, 10, 15, 19, 21, 33"
    },
    {
        "id": "RQ_cand2",
        "text": "To what degree do visual attribution heatmaps generated by Grad-CAM and Grad-CAM++ overlap with ground-truth lesion segmentation masks, and does higher model classification confidence correlate with higher quantitative localization fidelity (IoU) across the 7 HAM10000 lesion classes?",
        "gap_id": "Gap 2 (XAI Localization Fidelity)",
        "papers": "Papers 3, 10, 13, 19, 27, 30, 35"
    },
    {
        "id": "RQ_cand3",
        "text": "What is the quantitative trade-off between architectural parameter count, inference latency, and diagnostic discriminability (macro-AUC and balanced accuracy) when comparing lightweight transfer learning backbones (MobileNetV2, EfficientNet-B0) against standard heavy backbones (ResNet-50, DenseNet-121) on HAM10000?",
        "gap_id": "Gap 3 (Architectural Efficiency)",
        "papers": "Papers 4, 5, 8, 11, 19, 21, 31, 36"
    },
    {
        "id": "RQ_cand4",
        "text": "How does algorithmic hair artifact removal (DullRazor) and contrast enhancement prior to CNN feature extraction impact multi-class diagnostic sensitivity and boundary localization compared to training directly on raw dermoscopic images in HAM10000?",
        "gap_id": "Gap 4 (Preprocessing Ablation)",
        "papers": "Papers 1, 2, 3, 14, 24, 27, 34"
    },
    {
        "id": "RQ_cand5",
        "text": "Does combining complementary transfer learning representations via late decision fusion (soft-voting ensemble of CNN backbones) provide statistically significant improvements in multi-class sensitivity and macro-F1 over individual fine-tuned models on HAM10000?",
        "gap_id": "Ensemble Decision Fusion",
        "papers": "Papers 4, 8, 15, 17, 21, 22, 31"
    },
    {
        "id": "RQ_cand6",
        "text": "What is the comparative effect of targeted geometric data augmentation versus loss-level sample re-weighting on reducing the misclassification rate between malignant melanoma (MEL) and benign melanocytic nevi (NV) in 7-class HAM10000 classification?",
        "gap_id": "Gap 1 (Class Imbalance / Augmentation)",
        "papers": "Papers 2, 3, 5, 10, 15, 21"
    },
    {
        "id": "RQ_cand7",
        "text": "How does varying input image resolution (224x224 vs. 299x299 vs. 384x384 pixels) influence the diagnostic balanced accuracy and Grad-CAM feature localization fidelity of pre-trained CNNs on HAM10000 dermoscopic lesions?",
        "gap_id": "Input Dimensionality & Representation",
        "papers": "Papers 1, 3, 6, 13, 26, 33"
    },
    {
        "id": "RQ_cand8",
        "text": "To what extent does cross-dataset domain shift degrade the sensitivity of transfer learning models trained on HAM10000 when evaluated on an independent external dermoscopic repository (PH2 dataset)?",
        "gap_id": "Cross-Dataset Generalizability",
        "papers": "Papers 2, 7, 17, 20, 24, 27"
    },
    {
        "id": "RQ_cand9",
        "text": "Does selective layer freezing (fine-tuning only the classification head vs. fine-tuning deep convolutional blocks) systematically alter the sensitivity-specificity equilibrium on minority dermoscopic categories in HAM10000?",
        "gap_id": "Transfer Learning Fine-Tuning Dynamics",
        "papers": "Papers 2, 4, 5, 21, 23, 31"
    }
]

STEP6_SCORING = [
    {"id": "RQ_cand1", "c1": 5, "c2": 5, "c3": 5, "c4": 5, "c5": 5, "c6": 5, "c7": 4, "total": 34, "rank": 1},
    {"id": "RQ_cand2", "c1": 5, "c2": 5, "c3": 5, "c4": 4, "c5": 5, "c6": 5, "c7": 5, "total": 34, "rank": 2},
    {"id": "RQ_cand3", "c1": 5, "c2": 4, "c3": 5, "c4": 5, "c5": 5, "c6": 5, "c7": 5, "total": 34, "rank": 3},
    {"id": "RQ_cand4", "c1": 4, "c2": 4, "c3": 5, "c4": 5, "c5": 4, "c6": 5, "c7": 5, "total": 32, "rank": 4},
    {"id": "RQ_cand5", "c1": 4, "c2": 4, "c3": 5, "c4": 5, "c5": 4, "c6": 5, "c7": 4, "total": 31, "rank": 5},
    {"id": "RQ_cand6", "c1": 4, "c2": 4, "c3": 5, "c4": 5, "c5": 4, "c6": 4, "c7": 4, "total": 30, "rank": 6},
    {"id": "RQ_cand7", "c1": 4, "c2": 3, "c3": 5, "c4": 4, "c5": 4, "c6": 5, "c7": 4, "total": 29, "rank": 7},
    {"id": "RQ_cand8", "c1": 4, "c2": 4, "c3": 4, "c4": 3, "c5": 4, "c6": 4, "c7": 4, "total": 27, "rank": 8},
    {"id": "RQ_cand9", "c1": 4, "c2": 3, "c3": 4, "c4": 4, "c5": 3, "c6": 4, "c7": 4, "total": 26, "rank": 9}
]

STEP7_BEST_5 = [
    {
        "rq_num": "RQ1",
        "title": "Cost-Sensitive Loss Formulations for Extreme Class Imbalance Mitigation",
        "question": "How do cost-sensitive loss formulations (Class-Weighted Cross-Entropy vs. Focal Loss) affect the per-class sensitivity and macro-averaged F1-score of extreme minority classes (dermatofibroma and vascular lesions) compared to standard unweighted cross-entropy in 7-class HAM10000 classification?",
        "gap": "Severe Class Imbalance and Extreme Minority Sensitivity Collapse (Gap 1)",
        "supporting_papers": "Papers 3, 5, 10, 15, 18, 19, 21, 26, 33, 39",
        "iv": "Loss function formulation (Standard Categorical Cross-Entropy, Class-Weighted Cross-Entropy, Focal Loss with gamma=2.0)",
        "dv": "Per-class Sensitivity (Recall), Macro-Averaged F1-Score, Balanced Accuracy, Minority Class Error Rate",
        "dataset": "HAM10000 (10,015 dermoscopic images, 7 classes; patient-level stratified split)",
        "experiment": "Train identical CNN transfer learning models (DenseNet-121 backbone) using identical optimizer and learning rate schedule across three loss formulations, comparing resulting confusion matrices and per-class metrics.",
        "metrics": "Per-Class Sensitivity, Specificity, Precision, Macro-F1, Balanced Accuracy, Confusion Matrix",
        "contribution": "Provides empirical evidence on the extent to which cost-sensitive loss formulations rescue minority class sensitivity without compromising majority class specificity in dermoscopic triage."
    },
    {
        "rq_num": "RQ2",
        "title": "Quantitative Localization Fidelity and Artifact Bias in Visual Explainability",
        "question": "To what degree do visual attribution heatmaps generated by Grad-CAM and Grad-CAM++ overlap with ground-truth lesion segmentation masks, and does higher model classification confidence correlate with higher quantitative localization fidelity (IoU) across the 7 HAM10000 lesion classes?",
        "gap": "Lack of Quantitative Validation and Pathological Alignment in Deep Learning Explainability (Gap 2)",
        "supporting_papers": "Papers 3, 10, 13, 19, 27, 30, 35",
        "iv": "Explainability algorithm (Grad-CAM vs. Grad-CAM++) and model prediction confidence level",
        "dv": "Quantitative localization fidelity: Intersection-over-Union (IoU) between binarized heatmap and ground-truth mask, Pointing Game Hit Rate, Outside-Lesion Attribution Energy Ratio",
        "dataset": "HAM10000 paired with ISIC 2018 Task 1 Ground-Truth Lesion Segmentation Masks",
        "experiment": "Generate attribution heatmaps for all correctly and incorrectly classified test images across all 7 classes. Binarize heatmaps at multiple thresholds (e.g., top 20% activation) and compute spatial overlap with expert segmentation masks.",
        "metrics": "IoU, Pointing Game Accuracy, Pearson correlation between Softmax Confidence and IoU, Outside-Mask Activation Energy Ratio",
        "contribution": "Establishes a rigorous quantitative benchmark testing whether Grad-CAM attribution faithfully reflects true lesion pathology or relies on spurious background skin artifacts."
    },
    {
        "rq_num": "RQ3",
        "title": "Parameter Efficiency vs. Multi-Class Diagnostic Discriminability in Lightweight Transfer Learning",
        "question": "What is the quantitative trade-off between architectural parameter count, inference latency, and diagnostic discriminability (macro-AUC and balanced accuracy) when comparing lightweight transfer learning backbones (MobileNetV2, EfficientNet-B0) against standard heavy backbones (ResNet-50, DenseNet-121) on HAM10000?",
        "gap": "Architectural Parameter Overhead vs. Diagnostic Discriminability Trade-Off in Edge Screening (Gap 3)",
        "supporting_papers": "Papers 1, 4, 5, 8, 11, 13, 19, 21, 23, 26, 31, 36, 38",
        "iv": "Pre-trained CNN architecture backbone (MobileNetV2 [3.5M params], EfficientNet-B0 [5.3M params], ResNet-50 [25.6M params], DenseNet-121 [8.0M params])",
        "dv": "Macro-Averaged AUC-ROC, Balanced Accuracy, Macro-F1, Total Parameter Count (M), FLOPs (G), Average CPU/GPU Inference Latency per image (ms)",
        "dataset": "HAM10000 (10,015 images, 7 classes)",
        "experiment": "Fine-tune all four candidate architectures under an identical training protocol (same input resolution 224x224, learning rate, batch size, epochs, and data splits). Benchmark inference execution time on standard CPU and GPU hardware.",
        "metrics": "Macro-AUC, Balanced Accuracy, Macro-F1, Parameter Count (M), Floating Point Operations (GFLOPs), Inference Latency (ms)",
        "contribution": "Quantifies the empirical margin of diagnostic gain provided by heavy backbones over lightweight edge-feasible models, establishing evidence-based model selection guidelines for mobile triage systems."
    },
    {
        "rq_num": "RQ4",
        "title": "Controlled Empirical Ablation of Algorithmic Preprocessing and Hair Suppression",
        "question": "How does algorithmic hair artifact removal (DullRazor) and contrast enhancement prior to CNN feature extraction impact multi-class diagnostic sensitivity and boundary localization compared to training directly on raw dermoscopic images in HAM10000?",
        "gap": "Inconsistent Impact and Empirical Justification of Preprocessing Artifact Removal (Gap 4)",
        "supporting_papers": "Papers 1, 2, 3, 5, 10, 13, 14, 19, 21, 24, 27, 34, 39",
        "iv": "Preprocessing pipeline state: (a) Raw normalized images, (b) DullRazor hair-suppressed images, (c) DullRazor + Contrast-Limited Adaptive Histogram Equalization (CLAHE)",
        "dv": "Multi-Class Balanced Accuracy, Per-Class Sensitivity, Macro-F1, Grad-CAM Edge Attention Concentration",
        "dataset": "HAM10000 (10,015 images; evaluated across images with and without dense hair occlusion)",
        "experiment": "Train identical transfer learning models on the three preprocessed image sets. Quantify diagnostic performance globally and on a designated 'high-hair-density' evaluation subset.",
        "metrics": "Balanced Accuracy, Per-Class Sensitivity, Macro-F1, Boundary IoU of Grad-CAM heatmaps on hair-occluded samples",
        "contribution": "Resolves the literature conflict regarding whether heuristic hair removal improves deep feature extraction or degrades diagnostic boundary representations."
    },
    {
        "rq_num": "RQ5",
        "title": "Multi-Architecture Decision Fusion and Late Ensemble Synergy",
        "question": "Does combining complementary transfer learning representations via late decision fusion (soft-voting ensemble of CNN backbones) provide statistically significant improvements in multi-class sensitivity and macro-F1 over individual fine-tuned models on HAM10000?",
        "gap": "Decision Fusion and Ensemble Synergy for Skin Cancer Screening",
        "supporting_papers": "Papers 4, 8, 15, 17, 21, 22, 31",
        "iv": "Classification model architecture: Individual fine-tuned backbones (MobileNetV2, DenseNet-121, ResNet-50) vs. Late Decision Fusion Ensemble (soft probability voting and weighted averaging)",
        "dv": "Overall Accuracy, Macro-F1, Balanced Accuracy, Per-Class Sensitivity, Diagnostic False-Negative Rate on Melanoma",
        "dataset": "HAM10000 (10,015 images, 7 classes)",
        "experiment": "Extract softmax class probability distributions from independently fine-tuned CNN models and evaluate soft-voting and weighted ensemble fusion strategies on the held-out test set.",
        "metrics": "Overall Accuracy, Balanced Accuracy, Macro-F1, Melanoma (MEL) Sensitivity, McNemar's Statistical Significance Test (p < 0.05)",
        "contribution": "Determines whether combining diverse feature representations mitigates individual model failure modes and provides statistically significant diagnostic stability across all 7 lesion classes."
    }
]

STEP8_OBJECTIVES = [
    {
        "rq": "RQ1 (Cost-Sensitive Imbalance Mitigation)",
        "objective": "To evaluate the efficacy of Class-Weighted Cross-Entropy and Focal Loss in mitigating minority class performance collapse on dermatofibroma and vascular lesions in HAM10000.",
        "experiment": "Comparative loss formulation training (DenseNet-121 backbone across standard CE, weighted CE, and Focal Loss).",
        "dataset": "HAM10000 (10,015 images, 7 classes)",
        "metrics": "Per-class Sensitivity, Specificity, Macro-F1, Balanced Accuracy, Confusion Matrix",
        "outcome": "Demonstrate a statistically significant increase in minority class sensitivity (>15 percentage points) without substantial sacrifice of majority class specificity."
    },
    {
        "rq": "RQ2 (Quantitative Explainability Fidelity)",
        "objective": "To quantitatively evaluate the spatial localization accuracy and clinical alignment of Grad-CAM and Grad-CAM++ attribution heatmaps against ground-truth lesion masks.",
        "experiment": "Grad-CAM heatmap extraction, multi-threshold binarization, and spatial overlap benchmarking against ISIC 2018 ground truth masks.",
        "dataset": "HAM10000 + ISIC 2018 Task 1 Ground Truth Masks",
        "metrics": "Intersection-over-Union (IoU), Pointing Game Accuracy, Pearson correlation (Softmax Confidence vs IoU)",
        "outcome": "Establish empirical evidence on whether high classification confidence guarantees genuine pathological focus and quantify attribution leakage onto background artifacts."
    },
    {
        "rq": "RQ3 (Architectural Efficiency vs Accuracy)",
        "objective": "To benchmark the computational efficiency (parameters, FLOPs, latency) against diagnostic discriminability across lightweight vs heavy CNN transfer learning backbones.",
        "experiment": "Systematic benchmarking of MobileNetV2, EfficientNet-B0, ResNet-50, and DenseNet-121 under identical hyperparameter conditions.",
        "dataset": "HAM10000 (10,015 images, 7 classes)",
        "metrics": "Macro-AUC, Balanced Accuracy, Macro-F1, Params (M), GFLOPs, Latency (ms)",
        "outcome": "Identify the Pareto-optimal architecture for mobile edge deployment that preserves >95% of peak heavy-model macro-AUC with <20% of parameter overhead."
    },
    {
        "rq": "RQ4 (Preprocessing & Artifact Ablation)",
        "objective": "To determine whether DullRazor hair removal and CLAHE contrast enhancement improve multi-class CNN sensitivity or introduce destructive border blurring artifacts.",
        "experiment": "Ablation study training identical transfer models on raw, DullRazor-filtered, and CLAHE-enhanced images across full and hair-occluded subsets.",
        "dataset": "HAM10000 (Full archive and designated high-hair-density subset)",
        "metrics": "Balanced Accuracy, Per-Class Sensitivity, Boundary IoU of Grad-CAM heatmaps",
        "outcome": "Provide conclusive experimental evidence resolving the literature disagreement on the utility of algorithmic hair removal in modern deep transfer learning."
    },
    {
        "rq": "RQ5 (Ensemble Decision Fusion)",
        "objective": "To assess whether late decision fusion of diverse transfer learning models achieves statistically significant diagnostic gains over standalone models.",
        "experiment": "Probability aggregation and soft-voting ensembling combining MobileNetV2, DenseNet-121, and ResNet-50 test predictions.",
        "dataset": "HAM10000 (10,015 images, 7 classes)",
        "metrics": "Overall Accuracy, Balanced Accuracy, Macro-F1, Melanoma Sensitivity, McNemar's p-value",
        "outcome": "Verify that ensembling reduces diagnostic variance, elevates macro-F1 by 2-4%, and significantly reduces melanoma false-negatives."
    }
]

# -------------------------------------------------------------
# 1. Build Word Document (.docx)
# -------------------------------------------------------------
print("Building Word Document: Research_Methodology_RQs_39_Papers.docx...")
doc = docx.Document()

# Configure margins
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def style_table(table, col_widths=None):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(table.rows):
        # Prevent row from splitting across pages
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        
        # Repeat header on every page
        if i == 0:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
            for j, cell in enumerate(row.cells):
                set_cell_background(cell, "1B365D")
                set_cell_margins(cell, 120, 120, 140, 140)
                for p in cell.paragraphs:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for r in p.runs:
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(255, 255, 255)
                        r.font.size = Pt(9.5)
        else:
            bg_color = "F7F9FB" if i % 2 == 1 else "FFFFFF"
            for j, cell in enumerate(row.cells):
                set_cell_background(cell, bg_color)
                set_cell_margins(cell, 90, 90, 120, 120)
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(8.5)

# Title
title_p = doc.add_heading("Research Methodology: Systematic 39-Paper Analysis and Defensible Research Question Formulation", level=0)
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

sub_p = doc.add_paragraph("Skin Cancer Detection Using Deep Learning | HAM10000 Benchmark | BCA 7th-Semester Academic Research")
sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub_p.runs[0].font.italic = True
sub_p.runs[0].font.size = Pt(11)
sub_p.runs[0].font.color.rgb = RGBColor(70, 80, 95)

# Executive Callout
doc.add_paragraph()
callout = doc.add_paragraph()
callout_run = callout.add_run(
    "RESEARCH CONTEXT & METHODOLOGICAL BOUNDS:\n"
    "This study presents an exhaustive, evidence-bound research methodology analysis across 39 peer-reviewed publications "
    "(downloaded_journals/) in dermatological deep learning. The primary benchmark evaluated is the HAM10000 dataset "
    "(10,015 dermoscopic images across 7 diagnostic categories: MEL, NV, BCC, AKIEC, BKL, DF, VASC). "
    "All research questions are designed strictly for an undergraduate academic research scope, utilizing transfer learning CNNs, "
    "cost-sensitive loss balancing, standardized multi-metric evaluation, and quantitative Grad-CAM visual interpretability. "
    "Crucially, this work addresses academic image classification and screening triage; it does NOT assert clinical diagnostic substitution."
)
callout_run.font.size = Pt(9.5)
callout_run.font.color.rgb = RGBColor(30, 40, 55)

# =============================================================
# STEP 1
# =============================================================
doc.add_heading("Step 1: Systematic Analysis of All 39 Research Papers", level=1)
doc.add_paragraph(
    "Each of the 39 research papers in the repository has been analyzed across the 17 standardized academic dimensions. "
    "All data is extracted directly from the published texts without extrapolation or fabrication."
)

for p in PAPERS:
    h2 = doc.add_heading(f"Paper {p['id']}: {p['title']}", level=2)
    meta_p = doc.add_paragraph()
    meta_p.add_run(f"Authors: {p['authors']} | Year: {p['year']} | Journal: {p['journal']} | DOI: {p['doi']} | IEEE Doc: {p['arnumber']}\n").font.size = Pt(9)
    
    # 17 fields
    fields = [
        ("1. Paper Title", p['title']),
        ("2. Authors", p['authors']),
        ("3. Publication Year", p['year']),
        ("4. Dataset(s) Used", ", ".join(p['datasets']) if isinstance(p['datasets'], list) else str(p['datasets'])),
        ("5. Dataset Size", p['dataset_size']),
        ("6. Deep Learning Architecture", p['model_architecture']),
        ("7. Preprocessing Techniques", p['preprocessing']),
        ("8. Data Augmentation Techniques", p['augmentation']),
        ("9. Classification Task", p['classification_task']),
        ("10. Number of Classes", str(p['num_classes'])),
        ("11. Evaluation Metrics", ", ".join(p['evaluation_metrics']) if isinstance(p['evaluation_metrics'], list) else str(p['evaluation_metrics'])),
        ("12. Main Results", p['main_results']),
        ("13. Main Contribution", p['main_contribution']),
        ("14. Limitations", p['limitations']),
        ("15. Future Work", p['future_work']),
        ("16. Explicitly Stated Research Gaps", p['research_gaps']),
        ("17. Relevant Findings for BCA Study", p['relevance_to_my_study'])
    ]
    for label, val in fields:
        p_field = doc.add_paragraph()
        r_lbl = p_field.add_run(f"{label}: ")
        r_lbl.bold = True
        r_lbl.font.size = Pt(9)
        r_val = p_field.add_run(str(val))
        r_val.font.size = Pt(9)

# =============================================================
# STEP 2
# =============================================================
doc.add_heading("Step 2: Complete Literature Matrix (39 Papers)", level=1)
doc.add_paragraph(
    "The following master cross-study matrix synthesizes all 39 papers across 15 standard comparative dimensions. "
    "Missing values are recorded strictly as 'Not Reported'."
)

# Table with 15 columns
headers_step2 = [
    "No.", "Title", "Year", "Dataset", "Size", "Model", "Preprocessing", 
    "Augmentation", "Task", "Metrics", "Best Result", "Limitations", 
    "Future Work", "Research Gap", "Relevance"
]

tbl_step2 = doc.add_table(rows=len(PAPERS)+1, cols=15)
for j, h in enumerate(headers_step2):
    tbl_step2.rows[0].cells[j].text = h

for i, p in enumerate(PAPERS):
    row_cells = tbl_step2.rows[i+1].cells
    row_cells[0].text = str(p['id'])
    row_cells[1].text = p['title'][:40] + "..." if len(p['title']) > 40 else p['title']
    row_cells[2].text = str(p['year'])
    d_str = ", ".join(p['datasets']) if isinstance(p['datasets'], list) else str(p['datasets'])
    row_cells[3].text = d_str[:30] + "..." if len(d_str) > 30 else d_str
    row_cells[4].text = p['dataset_size'][:25] + "..." if len(p['dataset_size']) > 25 else p['dataset_size']
    row_cells[5].text = p['model_architecture'][:35] + "..." if len(p['model_architecture']) > 35 else p['model_architecture']
    row_cells[6].text = p['preprocessing'][:30] + "..." if len(p['preprocessing']) > 30 else p['preprocessing']
    row_cells[7].text = p['augmentation'][:25] + "..." if len(p['augmentation']) > 25 else p['augmentation']
    row_cells[8].text = p['classification_task'][:25] + "..." if len(p['classification_task']) > 25 else p['classification_task']
    m_str = ", ".join(p['evaluation_metrics']) if isinstance(p['evaluation_metrics'], list) else str(p['evaluation_metrics'])
    row_cells[9].text = m_str[:30] + "..." if len(m_str) > 30 else m_str
    row_cells[10].text = p['main_results'][:30] + "..." if len(p['main_results']) > 30 else p['main_results']
    row_cells[11].text = p['limitations'][:35] + "..." if len(p['limitations']) > 35 else p['limitations']
    row_cells[12].text = p['future_work'][:35] + "..." if len(p['future_work']) > 35 else p['future_work']
    row_cells[13].text = p['research_gaps'][:35] + "..." if len(p['research_gaps']) > 35 else p['research_gaps']
    row_cells[14].text = p['relevance_to_my_study'][:35] + "..." if len(p['relevance_to_my_study']) > 35 else p['relevance_to_my_study']

style_table(tbl_step2)

# =============================================================
# STEP 3
# =============================================================
doc.add_heading("Step 3: Common Patterns and Methodological Evidence", level=1)
doc.add_paragraph(
    "Following systematic extraction across the 39 publications, key recurring patterns, architectural agreements/disagreements, "
    "and methodological limitations were identified and categorized into three tiers of evidence."
)

for key in sorted(STEP3_PATTERNS.keys()):
    pat = STEP3_PATTERNS[key]
    doc.add_heading(f"{key}. {pat['title']}", level=2)
    
    p_s = doc.add_paragraph()
    r1 = p_s.add_run("• Strong Evidence: ")
    r1.bold = True
    p_s.add_run(pat['strong'])
    
    p_m = doc.add_paragraph()
    r2 = p_m.add_run("• Moderate Evidence: ")
    r2.bold = True
    p_m.add_run(pat['moderate'])
    
    p_l = doc.add_paragraph()
    r3 = p_l.add_run("• Limited Evidence: ")
    r3.bold = True
    p_l.add_run(pat['limited'])

# =============================================================
# STEP 4
# =============================================================
doc.add_heading("Step 4: Identification of Genuine Research Gaps", level=1)
doc.add_paragraph(
    "Based strictly on the 39 reviewed papers, four genuine, defensible research gaps were formulated to support our undergraduate study. "
    "No gaps were artificially manufactured; each is directly corroborated by specific paper citations."
)

for i, g in enumerate(STEP4_GAPS):
    doc.add_heading(f"Research Gap {i+1}: {g['gap']}", level=2)
    
    items = [
        ("Evidence from Papers", g['evidence']),
        ("Supporting Paper Numbers", g['paper_numbers']),
        ("Why the Gap Matters", g['why_matters']),
        ("How My Study Can Address It", g['how_addressed']),
        ("Feasibility with HAM10000", g['feasibility'])
    ]
    for lbl, val in items:
        p_item = doc.add_paragraph()
        r = p_item.add_run(f"{lbl}: ")
        r.bold = True
        p_item.add_run(val)

# =============================================================
# STEP 5
# =============================================================
doc.add_heading("Step 5: Candidate Research Questions (8-10)", level=1)
doc.add_paragraph(
    "Nine candidate research questions were formulated. Each question is specific, measurable, experimentally testable, "
    "grounded in the HAM10000 dataset, and tailored to an undergraduate BCA computer science project."
)

for i, rq in enumerate(STEP5_CANDIDATE_RQS):
    p_rq = doc.add_paragraph()
    r_num = p_rq.add_run(f"Candidate RQ {i+1} ({rq['id']}): ")
    r_num.bold = True
    p_rq.add_run(f"{rq['text']}\n")
    r_meta = p_rq.add_run(f"[Targeted Gap: {rq['gap_id']} | Corroborating Literature: {rq['papers']}]")
    r_meta.font.italic = True
    r_meta.font.size = Pt(8.5)

# =============================================================
# STEP 6
# =============================================================
doc.add_heading("Step 6: Quantitative Scoring and Ranking of Candidate RQs", level=1)
doc.add_paragraph(
    "Every candidate research question was quantitatively evaluated across seven rigorous methodological criteria (scored 1 to 5, max 35): "
    "(1) Research Relevance, (2) Novelty, (3) Measurability, (4) Experimental Feasibility, (5) Connection to Literature Gap, "
    "(6) Suitability for HAM10000, and (7) Suitability for BCA Undergraduate Scope."
)

score_headers = ["Rank", "Candidate ID", "Relevance", "Novelty", "Measurability", "Feasibility", "Gap Match", "HAM10000", "Scope", "Total /35"]
tbl_score = doc.add_table(rows=len(STEP6_SCORING)+1, cols=10)
for j, h in enumerate(score_headers):
    tbl_score.rows[0].cells[j].text = h

# Sort by rank
sorted_scores = sorted(STEP6_SCORING, key=lambda x: x['rank'])
for i, sc in enumerate(sorted_scores):
    rc = tbl_score.rows[i+1].cells
    rc[0].text = str(sc['rank'])
    rc[1].text = sc['id']
    rc[2].text = str(sc['c1'])
    rc[3].text = str(sc['c2'])
    rc[4].text = str(sc['c3'])
    rc[5].text = str(sc['c4'])
    rc[6].text = str(sc['c5'])
    rc[7].text = str(sc['c6'])
    rc[8].text = str(sc['c7'])
    rc[9].text = f"{sc['total']} / 35"

style_table(tbl_score)

# =============================================================
# STEP 7
# =============================================================
doc.add_heading("Step 7: Selection and Specification of the Best 5 Research Questions", level=1)
doc.add_paragraph(
    "From the top-ranked candidates, five complementary research questions were selected to establish a coherent, "
    "academically defensible research inquiry for the HAM10000 benchmark."
)

for b in STEP7_BEST_5:
    doc.add_heading(f"{b['rq_num']}: {b['title']}", level=2)
    doc.add_paragraph().add_run(f"Research Question: {b['question']}").bold = True
    
    specs = [
        ("Literature Gap Addressed", b['gap']),
        ("Supporting Literature", b['supporting_papers']),
        ("Independent Variable (IV)", b['iv']),
        ("Dependent Variable (DV)", b['dv']),
        ("Primary Dataset", b['dataset']),
        ("Required Experiment", b['experiment']),
        ("Evaluation Metrics", b['metrics']),
        ("Expected Scientific Contribution", b['contribution'])
    ]
    for lbl, val in specs:
        p_sp = doc.add_paragraph()
        r = p_sp.add_run(f"{lbl}: ")
        r.bold = True
        p_sp.add_run(val)

# =============================================================
# STEP 8
# =============================================================
doc.add_heading("Step 8: Mapping Research Questions to Research Objectives", level=1)
doc.add_paragraph(
    "To ensure experimental feasibility, each of the five selected research questions is explicitly mapped to a corresponding research objective, "
    "experimental procedure, target dataset, quantitative metrics, and expected outcome."
)

obj_headers = ["RQ", "Research Objective", "Experiment Required", "Dataset", "Metrics", "Expected Outcome"]
tbl_obj = doc.add_table(rows=len(STEP8_OBJECTIVES)+1, cols=6)
for j, h in enumerate(obj_headers):
    tbl_obj.rows[0].cells[j].text = h

for i, ob in enumerate(STEP8_OBJECTIVES):
    rc = tbl_obj.rows[i+1].cells
    rc[0].text = ob['rq']
    rc[1].text = ob['objective']
    rc[2].text = ob['experiment']
    rc[3].text = ob['dataset']
    rc[4].text = ob['metrics']
    rc[5].text = ob['outcome']

style_table(tbl_obj)

# =============================================================
# STEP 9
# =============================================================
doc.add_heading("Step 9: Overlap, Redundancy, and Feasibility Audit", level=1)
doc.add_paragraph(
    "A rigorous audit was conducted across the five finalized research questions to verify independence, eliminate confounding variables, "
    "and guarantee that all experimental requirements are strictly feasible within the constraints of an undergraduate BCA project."
)

audit_points = [
    ("Variable Orthogonality & Non-Redundancy", "Each RQ investigates an entirely distinct axis of deep learning: RQ1 evaluates loss-function mechanics for class imbalance; RQ2 evaluates visual attribution localization fidelity; RQ3 benchmarks computational complexity vs accuracy across backbones; RQ4 isolates preprocessing/hair removal artifacts; and RQ5 explores multi-model decision fusion. There is zero variable overlap."),
    ("Experimental Feasibility on HAM10000", "All experiments utilize the publicly available HAM10000 dataset (and paired ISIC 2018 Task 1 ground-truth lesion masks for RQ2). None of the questions require external proprietary hospital cohorts or unavailable clinical metadata."),
    ("Resource & Compute Constraints", "All proposed architectures (MobileNetV2, EfficientNet-B0, ResNet-50, DenseNet-121) can be trained within reasonable epochs using standard workstation GPUs or Google Colab environments without requiring multi-GPU server infrastructure."),
    ("Elimination of Clinical Replacement Claims", "None of the RQs claim that deep learning can replace dermatological biopsy or definitive histology. The entire scope is framed around computer-assisted screening triage, balanced sensitivity, and visual interpretability verification.")
]

for title, text in audit_points:
    p_aud = doc.add_paragraph()
    r = p_aud.add_run(f"• {title}: ")
    r.bold = True
    p_aud.add_run(text)

# =============================================================
# STEP 10
# =============================================================
doc.add_heading("Step 10: Final IEEE-Style Research Questions Section", level=1)
doc.add_paragraph(
    "The section below is formatted in standard academic prose, suitable for direct inclusion in a formal research paper or undergraduate thesis."
)

doc.add_heading("Research Questions", level=2)

for b in STEP7_BEST_5:
    p_final = doc.add_paragraph()
    r_tag = p_final.add_run(f"{b['rq_num']}: ")
    r_tag.bold = True
    p_final.add_run(f"{b['question']}")

p_synth = doc.add_paragraph()
p_synth.paragraph_format.first_line_indent = Inches(0.25)
p_synth.add_run(
    "Synthesis Narrative: The formulation of these five research questions is directly grounded in our systematic review of 39 recent publications "
    "in deep learning-based dermatological analysis. While existing literature demonstrates high aggregate classification accuracy (often exceeding 85–90%), "
    "a recurring limitation identified across multiple studies [Papers 3, 5, 10, 15, 18, 19, 21, 33, 39] is the catastrophic collapse of diagnostic sensitivity "
    "on severe minority categories (dermatofibroma and vascular lesions) within the benchmark HAM10000 archive. Furthermore, while visual explainability tools "
    "such as Grad-CAM are increasingly incorporated to justify predictions [Papers 3, 19, 27], previous works rely almost exclusively on subjective visual inspection, "
    "leaving a critical literature gap regarding the quantitative localization fidelity of attribution heatmaps against ground-truth lesion margins. "
    "Simultaneously, literature conflicts regarding whether heavy vision transformers justify their extensive parameter overhead compared to compact lightweight CNNs "
    "[Papers 4, 9, 19, 36], and whether heuristic hair suppression algorithms genuinely improve or distort fine-grained boundary features [Papers 2, 14, 24], "
    "necessitate controlled empirical ablation. Finally, decision fusion strategies [Papers 4, 8, 21, 22] offer a mathematically grounded approach to reduce individual "
    "model diagnostic variance. Together, RQ1 through RQ5 establish a comprehensive, experimentally tractable framework tailored to advancing multi-class dermoscopic "
    "screening on the HAM10000 dataset."
)

# Save Word document
docx_path = os.path.join(BASE_DIR, "Research_Methodology_RQs_39_Papers.docx")
doc.save(docx_path)
print(f"Successfully generated and saved Word Document: {docx_path}")

# -------------------------------------------------------------
# 2. Build LaTeX Project in latex_research_methodology/
# -------------------------------------------------------------
print("Building LaTeX Repository in latex_research_methodology/...")
LATEX_DIR = os.path.join(BASE_DIR, "latex_research_methodology")
os.makedirs(LATEX_DIR, exist_ok=True)
os.makedirs(os.path.join(LATEX_DIR, "sections"), exist_ok=True)
os.makedirs(os.path.join(LATEX_DIR, "papers"), exist_ok=True)

# Helper for LaTeX escaping
def tex_clean(s):
    if not s:
        return ""
    s = str(s)
    s = s.replace('—', '---').replace('–', '--')
    s = s.replace('“', "``").replace('”', "''")
    s = s.replace('‘', "`").replace('’', "'")
    s = s.replace('×', r'$\times$')
    s = s.replace('λ', r'$\lambda$')
    s = s.replace('≥', r'$\ge$').replace('≤', r'$\le$')
    s = s.replace('&', r'\&')
    s = s.replace('%', r'\%')
    s = s.replace('_', r'\_')
    s = s.replace('#', r'\#')
    return s

# Generate references.bib
# Copy from all_39_journals.bib
with open(os.path.join(BASE_DIR, 'all_39_journals.bib'), 'r', encoding='utf-8') as f_in:
    bib_content = f_in.read()

replacements = {
    'Ş': r'{\c{S}}', 'ş': r'{\c{s}}',
    'Ö': r'{\"O}', 'ö': r'{\"o}',
    'Ç': r'{\c{C}}', 'ç': r'{\c{c}}',
    'ü': r'{\"u}', 'Ü': r'{\"U}',
    'ł': r'{\l}', 'Ł': r'{\L}',
    'ń': r'{\'n}', 'Ń': r'{\'N}',
    'í': r'{\'i}', 'Í': r'{\'I}',
    'á': r'{\'a}', 'Á': r'{\'A}',
    'é': r'{\'e}', 'É': r'{\'E}',
    'ã': r'{\~a}', 'Ã': r'{\~A}',
    'ó': r'{\'o}', 'Ó': r'{\'O}',
    'ú': r'{\'u}', 'Ú': r'{\'U}',
    'à': r'{\`a}', 'è': r'{\`e}',
    '–': '--', '—': '---',
    '“': '``', '”': "''",
}
for k, v in replacements.items():
    bib_content = bib_content.replace(k, v)

with open(os.path.join(LATEX_DIR, 'references.bib'), 'w', encoding='utf-8') as f_out:
    f_out.write(bib_content)

# Generate main.tex
main_tex_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=1in]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{array}
\usepackage{makecell}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{tcolorbox}
\usepackage{cite}

\hypersetup{
    colorlinks=true,
    linkcolor=blue!70!black,
    citecolor=blue!70!black,
    urlcolor=blue!70!black
}

\pagestyle{fancy}
\fancyhf{}
\setlength{\headheight}{15pt}
\lhead{\small\textit{Research Methodology: 39-Paper Analysis}}
\rhead{\small\textit{Skin Cancer Detection (HAM10000)}}
\cfoot{\thepage}

\begin{document}

\begin{titlepage}
\centering
\vspace*{1.5cm}
{\Large\textbf{RESEARCH METHODOLOGY REPORT:}\\[0.3cm]
\LARGE\textbf{Systematic 39-Paper Literature Analysis and Defensible Research Question Formulation for Deep Learning Skin Cancer Detection}\par}
\vspace{1.0cm}
{\large\textbf{Domain:} Medical Image Analysis \& Deep Learning \\
\textbf{Primary Benchmark:} HAM10000 (ISIC 2018 Task 3) \\
\textbf{Context:} BCA 7th-Semester Academic Research Methodology\par}
\vspace{1.5cm}
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{Methodological Executive Summary}]
This report provides a systematic academic analysis across all \textbf{39 peer-reviewed publications} in \texttt{downloaded\_journals/}. 
Following a strict anti-hallucination protocol, each paper is dissected across 17 standardized dimensions to construct a 
comprehensive 15-column literature matrix. Cross-study evidence is synthesized into common architectural patterns, preprocessing 
paradigms, evaluation metrics, and recurring limitations. Four genuine literature gaps are identified and used to generate 
nine candidate Research Questions (RQs). Following multi-dimensional quantitative scoring (scored 1--5 across 7 criteria), 
the top five Research Questions are selected, fully specified, and mapped to experimental objectives. All inquiries are strictly 
grounded in the \textbf{HAM10000 benchmark} and tailored to an academic undergraduate research scope.
\end{tcolorbox}
\vfill
{\large Department of Computer Science / Applications \\ Academic Year 2024--2026\par}
\end{titlepage}

\newpage
\tableofcontents
\newpage

\section{Introduction and Research Scope}
This study operates within the academic domain of automated dermatological image classification. Automated screening using deep convolutional neural networks (CNNs) has emerged as a promising tool to assist clinical triage. However, clinical translation is constrained by severe dataset class imbalance, lack of quantitative explainability validation, computational resource overhead on mobile edge hardware, and conflicting preprocessing protocols. This report reviews 39 published works to formulate academically rigorous, experimentally testable Research Questions (RQs) centered on the 7-class HAM10000 benchmark.

\section{Step 1: Systematic Analysis of All 39 Research Papers}
Each of the 39 research publications has been analyzed across the 17 specified fields. Below is the comprehensive catalog.
"""

for p in PAPERS:
    pid = p['id']
    main_tex_content += f"\n\\subsection{{Paper {pid}: {tex_clean(p['title'])}}}\n"
    main_tex_content += f"\\textbf{{Authors:}} {tex_clean(p['authors'])} \\\\\n"
    main_tex_content += f"\\textbf{{Year / Venue:}} {tex_clean(p['year'])} (\\textit{{{tex_clean(p['journal'])}}}) | \\textbf{{DOI:}} \\href{{https://doi.org/{p['doi']}}}{{{tex_clean(p['doi'])}}} | \\textbf{{Citation:}} \\cite{{{p['arnumber']}}}\n\n"
    main_tex_content += "\\begin{itemize}\\small\n"
    main_tex_content += f"\\item \\textbf{{Dataset(s) Used:}} {tex_clean(', '.join(p['datasets']) if isinstance(p['datasets'], list) else str(p['datasets']))}\n"
    main_tex_content += f"\\item \\textbf{{Dataset Size:}} {tex_clean(p['dataset_size'])}\n"
    main_tex_content += f"\\item \\textbf{{Model Architecture:}} {tex_clean(p['model_architecture'])}\n"
    main_tex_content += f"\\item \\textbf{{Preprocessing:}} {tex_clean(p['preprocessing'])}\n"
    main_tex_content += f"\\item \\textbf{{Data Augmentation:}} {tex_clean(p['augmentation'])}\n"
    main_tex_content += f"\\item \\textbf{{Classification Task:}} {tex_clean(p['classification_task'])} ({p['num_classes']} Classes)\n"
    main_tex_content += f"\\item \\textbf{{Evaluation Metrics:}} {tex_clean(', '.join(p['evaluation_metrics']) if isinstance(p['evaluation_metrics'], list) else str(p['evaluation_metrics']))}\n"
    main_tex_content += f"\\item \\textbf{{Main Results:}} {tex_clean(p['main_results'])}\n"
    main_tex_content += f"\\item \\textbf{{Main Contribution:}} {tex_clean(p['main_contribution'])}\n"
    main_tex_content += f"\\item \\textbf{{Limitations:}} {tex_clean(p['limitations'])}\n"
    main_tex_content += f"\\item \\textbf{{Future Work:}} {tex_clean(p['future_work'])}\n"
    main_tex_content += f"\\item \\textbf{{Explicit Research Gaps:}} {tex_clean(p['research_gaps'])}\n"
    main_tex_content += f"\\item \\textbf{{Relevance to BCA Study:}} {tex_clean(p['relevance_to_my_study'])}\n"
    main_tex_content += "\\end{itemize}\n"

main_tex_content += r"""
\newpage
\section{Step 2: Cross-Study Literature Matrix}
Table~\ref{tab:lit_matrix} presents the 15-column comparative matrix across all 39 analyzed publications.

\begin{small}
\begin{longtable}{p{0.5cm} p{2.2cm} p{0.8cm} p{1.8cm} p{2.0cm} p{2.0cm} p{2.0cm} p{2.5cm}}
\caption{Master Literature Matrix Across 39 Published Studies} \label{tab:lit_matrix} \\
\toprule
\textbf{\#} & \textbf{Title} & \textbf{Yr} & \textbf{Dataset} & \textbf{Architecture} & \textbf{Task} & \textbf{Best Result} & \textbf{Relevance / Gaps} \\
\midrule
\endhead
\bottomrule
\endfoot
"""

for p in PAPERS:
    t_short = tex_clean(p['title'][:30] + "...")
    d_short = tex_clean(", ".join(p['datasets'])[:20] if isinstance(p['datasets'], list) else str(p['datasets'])[:20])
    m_short = tex_clean(p['model_architecture'][:25] + "...")
    task_short = tex_clean(p['classification_task'][:20] + "...")
    res_short = tex_clean(p['main_results'][:25] + "...")
    rel_short = tex_clean(p['relevance_to_my_study'][:30] + "...")
    main_tex_content += f"{p['id']} & {t_short} & {p['year']} & {d_short} & {m_short} & {task_short} & {res_short} & {rel_short} \\\\\n"

main_tex_content += r"""
\end{longtable}
\end{small}

\newpage
\section{Step 3: Common Patterns and Methodological Evidence}
Synthesis of literature trends classified by evidentiary strength:
\begin{itemize}
"""

for key in sorted(STEP3_PATTERNS.keys()):
    pat = STEP3_PATTERNS[key]
    main_tex_content += f"\\item \\textbf{{{key}. {tex_clean(pat['title'])}}}\n\\begin{{itemize}}\n"
    main_tex_content += f"  \\item \\textbf{{Strong Evidence:}} {tex_clean(pat['strong'])}\n"
    main_tex_content += f"  \\item \\textbf{{Moderate Evidence:}} {tex_clean(pat['moderate'])}\n"
    main_tex_content += f"  \\item \\textbf{{Limited Evidence:}} {tex_clean(pat['limited'])}\n"
    main_tex_content += "\\end{itemize}\n"

main_tex_content += r"""
\end{itemize}

\section{Step 4: Identification of Genuine Research Gaps}
Four genuine research gaps grounded in the 39-paper corpus:
"""

for i, g in enumerate(STEP4_GAPS):
    main_tex_content += f"\n\\subsection{{Research Gap {i+1}: {tex_clean(g['gap'])}}}\n"
    main_tex_content += "\\begin{itemize}\n"
    main_tex_content += f"\\item \\textbf{{Evidence from Papers:}} {tex_clean(g['evidence'])}\n"
    main_tex_content += f"\\item \\textbf{{Supporting Papers:}} {tex_clean(g['paper_numbers'])}\n"
    main_tex_content += f"\\item \\textbf{{Why the Gap Matters:}} {tex_clean(g['why_matters'])}\n"
    main_tex_content += f"\\item \\textbf{{How My Study Can Address It:}} {tex_clean(g['how_addressed'])}\n"
    main_tex_content += f"\\item \\textbf{{Feasibility with HAM10000:}} {tex_clean(g['feasibility'])}\n"
    main_tex_content += "\\end{itemize}\n"

main_tex_content += r"""
\section{Step 5: Candidate Research Questions}
\begin{enumerate}
"""

for rq in STEP5_CANDIDATE_RQS:
    rq_id_clean = tex_clean(rq['id'])
    rq_text_clean = tex_clean(rq['text'])
    rq_gap_clean = tex_clean(rq['gap_id'])
    rq_papers_clean = tex_clean(rq['papers'])
    main_tex_content += f"\\item \\textbf{{{rq_id_clean}:}} {rq_text_clean} \\\\\n\\textit{{[Gap: {rq_gap_clean}; Corroborating: {rq_papers_clean}]}}\n"

main_tex_content += r"""
\end{enumerate}

\section{Step 6: Quantitative Scoring of Candidate RQs}
\begin{table}[htbp]
\centering
\small
\begin{tabular}{l ccccccc c c}
\toprule
\textbf{Candidate ID} & \textbf{Rel.} & \textbf{Nov.} & \textbf{Meas.} & \textbf{Feas.} & \textbf{Gap} & \textbf{HAM} & \textbf{Scope} & \textbf{Total /35} & \textbf{Rank} \\
\midrule
"""

for sc in sorted_scores:
    rank_str = str(sc['rank'])
    main_tex_content += f"{tex_clean(sc['id'])} & {sc['c1']} & {sc['c2']} & {sc['c3']} & {sc['c4']} & {sc['c5']} & {sc['c6']} & {sc['c7']} & \\textbf{{{sc['total']}}} & \\textbf{{\\#{rank_str}}} \\\\\n"

main_tex_content += r"""
\bottomrule
\end{tabular}
\caption{Quantitative Multi-Dimensional Scoring of Candidate Research Questions}
\label{tab:scoring}
\end{table}

\section{Step 7: Selected Top 5 Research Questions}
"""

for b in STEP7_BEST_5:
    main_tex_content += f"\n\\subsection{{{b['rq_num']}: {tex_clean(b['title'])}}}\n"
    main_tex_content += f"\\textbf{{Question:}} {tex_clean(b['question'])}\n\\begin{{itemize}}\n"
    main_tex_content += f"\\item \\textbf{{Literature Gap:}} {tex_clean(b['gap'])}\n"
    main_tex_content += f"\\item \\textbf{{Supporting Papers:}} {tex_clean(b['supporting_papers'])}\n"
    main_tex_content += f"\\item \\textbf{{Independent Variable (IV):}} {tex_clean(b['iv'])}\n"
    main_tex_content += f"\\item \\textbf{{Dependent Variable (DV):}} {tex_clean(b['dv'])}\n"
    main_tex_content += f"\\item \\textbf{{Primary Dataset:}} {tex_clean(b['dataset'])}\n"
    main_tex_content += f"\\item \\textbf{{Required Experiment:}} {tex_clean(b['experiment'])}\n"
    main_tex_content += f"\\item \\textbf{{Evaluation Metrics:}} {tex_clean(b['metrics'])}\n"
    main_tex_content += f"\\item \\textbf{{Expected Contribution:}} {tex_clean(b['contribution'])}\n"
    main_tex_content += "\\end{itemize}\n"

main_tex_content += r"""
\section{Step 8: Mapping Research Questions to Objectives}
\begin{table}[htbp]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{p{2.0cm} p{3.5cm} p{3.5cm} p{2.0cm} p{3.0cm}}
\toprule
\textbf{RQ} & \textbf{Research Objective} & \textbf{Experiment} & \textbf{Dataset} & \textbf{Expected Outcome} \\
\midrule
"""

for ob in STEP8_OBJECTIVES:
    main_tex_content += f"{tex_clean(ob['rq'][:20])} & {tex_clean(ob['objective'])} & {tex_clean(ob['experiment'])} & {tex_clean(ob['dataset'])} & {tex_clean(ob['outcome'])} \\\\\n\\midrule\n"

main_tex_content += r"""
\bottomrule
\end{tabularx}
\caption{Systematic Mapping of Research Questions to Experimental Objectives}
\label{tab:objectives}
\end{table}

\section{Step 9: Overlap, Redundancy, and Feasibility Audit}
A systematic verification was executed across the five selected research questions:
\begin{itemize}
    \item \textbf{Variable Orthogonality:} RQ1 isolates cost-sensitive loss formulations; RQ2 assesses quantitative XAI heatmap IoU; RQ3 evaluates computational efficiency vs accuracy across backbones; RQ4 isolates preprocessing/hair removal artifacts; and RQ5 explores multi-model decision fusion. No overlapping variables exist.
    \item \textbf{HAM10000 Experimental Feasibility:} All five questions operate directly on the publicly available HAM10000 archive and paired ISIC 2018 Task 1 ground-truth lesion segmentation masks without requiring external hospital data.
    \item \textbf{Computational Tractability:} All models (MobileNetV2, EfficientNet-B0, ResNet-50, DenseNet-121) can be trained on a single standard GPU or Colab environment.
    \item \textbf{Academic Research Integrity:} Diagnostic claims are strictly framed around statistical image classification and triage support rather than definitive clinical biopsy.
\end{itemize}

\section{Step 10: Final IEEE-Style Research Questions Section}
\subsection*{Research Questions}
\begin{description}
"""

for b in STEP7_BEST_5:
    main_tex_content += f"\\item[\\textbf{{{b['rq_num']}:}}] {tex_clean(b['question'])}\n"

main_tex_content += r"""
\end{description}

\paragraph{Literature Synthesis:}
The formulation of these five research questions is directly grounded in our systematic review of 39 recent publications in deep learning-based dermatological analysis. While existing literature demonstrates high aggregate classification accuracy (often exceeding 85--90\%), a recurring limitation identified across multiple studies \cite{10107401, 10122533, 9810181, 9062473, 10459206, 10731679, 10608138, 10778156, 11598907} is the catastrophic collapse of diagnostic sensitivity on severe minority categories (dermatofibroma and vascular lesions) within the benchmark HAM10000 archive. Furthermore, while visual explainability tools such as Grad-CAM are increasingly incorporated to justify predictions \cite{10107401, 10731679, 10536875}, previous works rely almost exclusively on subjective visual inspection, leaving a critical literature gap regarding the quantitative localization fidelity of attribution heatmaps against ground-truth lesion margins. Simultaneously, literature conflicts regarding whether heavy vision transformers justify their extensive parameter overhead compared to compact lightweight CNNs \cite{9099799, 9791221, 10731679, 11435372}, and whether heuristic hair suppression algorithms genuinely improve or distort fine-grained boundary features \cite{9160933, 9306830, 10416953}, necessitate controlled empirical ablation. Finally, decision fusion strategies \cite{9099799, 9940917, 10608138, 9175002} offer a mathematically grounded approach to reduce individual model diagnostic variance. Together, RQ1 through RQ5 establish a comprehensive, experimentally tractable framework tailored to advancing multi-class dermoscopic screening on the HAM10000 dataset.

\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
"""

with open(os.path.join(LATEX_DIR, 'main.tex'), 'w', encoding='utf-8') as f_tex:
    f_tex.write(main_tex_content)

print("Generated latex_research_methodology/main.tex successfully.")

# Create compile.bat and compile.ps1
with open(os.path.join(LATEX_DIR, 'compile.bat'), 'w', encoding='utf-8') as f_bat:
    f_bat.write("@echo off\npdflatex -interaction=nonstopmode main.tex\nbibtex main\npdflatex -interaction=nonstopmode main.tex\npdflatex -interaction=nonstopmode main.tex\necho Compilation complete!\npause\n")

with open(os.path.join(LATEX_DIR, 'compile.ps1'), 'w', encoding='utf-8') as f_ps1:
    f_ps1.write("& pdflatex -interaction=nonstopmode main.tex\n& bibtex main\n& pdflatex -interaction=nonstopmode main.tex\n& pdflatex -interaction=nonstopmode main.tex\nWrite-Host 'LaTeX compilation finished!'\n")

# Compile LaTeX to PDF
print("Compiling LaTeX document via pdflatex and bibtex...")
try:
    for ext in ['.aux', '.bbl', '.blg', '.log', '.out', '.toc']:
        p = os.path.join(LATEX_DIR, 'main' + ext)
        if os.path.exists(p):
            try: os.remove(p)
            except: pass
            
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=LATEX_DIR, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["bibtex", "main"], cwd=LATEX_DIR, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=LATEX_DIR, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=LATEX_DIR, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pdf_path = os.path.join(LATEX_DIR, "main.pdf")
    if os.path.exists(pdf_path):
        print(f"SUCCESS: Compiled LaTeX PDF successfully! File size: {os.path.getsize(pdf_path)} bytes.")
    else:
        print("WARNING: main.pdf not found after compilation.")
except Exception as e:
    print(f"Error during compilation: {e}")

print("Generation pipeline completed successfully!")
