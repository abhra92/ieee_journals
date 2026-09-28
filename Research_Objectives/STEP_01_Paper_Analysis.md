# Comprehensive Research Objectives Analysis - Skin Cancer Detection Using Deep Learning

## Paper 1
**Title:** Skin Lesion Classification Using CNN With Novel Regularizer
**Authors:** M. A. Albahar | **Year:** 2019
1. **Research problem:** Discriminating between benign and malignant skin lesions from dermoscopic imagery where fine-grained morphological differences complicate automated diagnosis
2. **Research aim:** Develop a CNN with novel weight-controlling regularizer for skin lesion classification
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC archive
5. **Dataset size:** 23,906 images (subsets of ~8,000 images)
6. **Skin lesion classes:** Multiple lesion categories (nevus, melanoma, seborrheic keratosis, basal cell carcinoma, solar lentigo)
7. **Deep learning architecture:** Custom CNN with novel regularizer (λ=0.02), 2 conv layers, max pooling, dropout, 128-neuron dense layer
8. **Preprocessing methods:** Resizing to 300×300×3, gamma correction
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** 70/30 train/validation split, 100 epochs
11. **Evaluation metrics:** Accuracy 97.49%, AUC (0.77-0.93 for binary tasks)
12. **Main findings:** High accuracy achieved for binary classification using the novel regularizer
13. **Limitations:** Binary pairwise only, no multi-class, no multi-center validation
14. **Future work:** Unified multi-class classification
15. **Research gaps:** Need for multi-class unified classification rather than pairwise binary
16. **Recommendations for future research:** Not Reported

## Paper 2
**Title:** Region-of-Interest Based Transfer Learning Assisted Framework for Skin Cancer Detection
**Authors:** R. Ashraf et al. | **Year:** 2020
1. **Research problem:** Differentiating malignant melanoma from visually similar benign melanocytic nevi
2. **Research aim:** Develop a transfer learning framework assisted by ROI segmentation
3. **Main objectives:** Not Reported
4. **Dataset used:** DermIS, DermQuest
5. **Dataset size:** 705 images (DermIS), 667 images (DermQuest)
6. **Skin lesion classes:** Malignant melanoma, benign melanocytic nevi
7. **Deep learning architecture:** AlexNet and VGG-16 with transfer learning on segmented ROI patches
8. **Preprocessing methods:** Improved k-means segmentation for ROI isolation
9. **Data augmentation methods:** Random rotations, flipping, zooming, contrast adjustments
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 97.9%, Sensitivity 96.3%, Specificity 98.7%, F1 96.3%, AUC 0.97
12. **Main findings:** ROI segmentation improves classification metrics using standard architectures
13. **Limitations:** Binary classification only, moderate dataset size, k-means segmentation degrades with hair occlusion
14. **Future work:** Not Reported
15. **Research gaps:** Extension to multi-class, handling hair artifacts better
16. **Recommendations for future research:** Not Reported

## Paper 3
**Title:** An Interpretable Skin Cancer Classification Using Optimized CNN for Smart Healthcare
**Authors:** K. Mridha et al. | **Year:** 2023
1. **Research problem:** Need for interpretable skin cancer classification models for healthcare applications
2. **Research aim:** Develop an interpretable and optimized CNN model
3. **Main objectives:** Not Reported
4. **Dataset used:** HAM10000
5. **Dataset size:** 10,015 images
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** Optimized custom CNN with batch norm, max pooling, dropout; Grad-CAM/Grad-CAM++ for interpretability
8. **Preprocessing methods:** Image resizing, pixel normalization
9. **Data augmentation methods:** Random rotations, zooms, shear transformations, flips
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 82.0%, Specificity 94.17%, Sensitivity 82.0%
12. **Main findings:** Model provides visual interpretability for its predictions
13. **Limitations:** Modest multiclass sensitivity on minority classes (dermatofibroma, vascular), needs clinical validation
14. **Future work:** Not Reported
15. **Research gaps:** Class imbalance handling, interpretability improvement
16. **Recommendations for future research:** Not Reported

## Paper 4
**Title:** Automatic Skin Cancer Detection Based on Ensemble Lightweight Deep Learning Network
**Authors:** L. Wei et al. | **Year:** 2020
1. **Research problem:** Accurate yet computationally efficient skin cancer detection
2. **Research aim:** Build an ensemble lightweight deep learning network
3. **Main objectives:** Not Reported
4. **Dataset used:** ISBI 2016, ISBI 2017
5. **Dataset size:** 900+379 images (2016)
6. **Skin lesion classes:** Not Reported explicitly (likely binary melanoma vs. benign)
7. **Deep learning architecture:** Lightweight U-Net segmentation + pair-based feature extraction + ensemble decision fusion
8. **Preprocessing methods:** Transfer learning migration strategy for segmentation
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 87.3%, AUC 0.886, Sensitivity 83.2%, Specificity 89.1%
12. **Main findings:** Achieves competitive accuracy with reduced computational complexity
13. **Limitations:** Sensitivity degradation on indistinct margins, binary classification only
14. **Future work:** Not Reported
15. **Research gaps:** Lightweight models for multi-class
16. **Recommendations for future research:** Not Reported

## Paper 5
**Title:** DeepSkin: A Deep Learning Approach for Skin Cancer Classification
**Authors:** H. L. Gururaj et al. | **Year:** 2023
1. **Research problem:** Discriminating effectively among a large set of skin cancer types
2. **Research aim:** Classify skin lesions using custom and pre-trained CNNs
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2018/HAM10000
5. **Dataset size:** 10,015 images
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** Custom CNN with residual skip connections; VGG-16, ResNet-50, MobileNet for comparison
8. **Preprocessing methods:** Resizing to 224×224, Min-Max scaling
9. **Data augmentation methods:** Random rotations, horizontal flipping, zooming, brightness adjustments
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 88.0%, Sensitivity 86.2%, Specificity 85.0%, Precision 86.4%
12. **Main findings:** Custom architecture with residual skips achieves solid multiclass performance
13. **Limitations:** Confusion between benign keratosis and melanoma, no edge-device profiling, no multi-ethnic clinical evaluation
14. **Future work:** Not Reported
15. **Research gaps:** Better discrimination between visually overlapping classes
16. **Recommendations for future research:** Not Reported

## Paper 6
**Title:** FCN-Based DenseNet Framework for Automated Detection and Classification
**Authors:** A. A. Adegun et al. | **Year:** 2020
1. **Research problem:** Automated segmentation and classification of dermoscopic images
2. **Research aim:** Create a dual-stage framework using FCN and DenseNet
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2017, ISIC 2018, DermQuest
5. **Dataset size:** Not Reported explicitly
6. **Skin lesion classes:** Not Reported explicitly
7. **Deep learning architecture:** FCN segmentation + DenseNet classification
8. **Preprocessing methods:** Dull Razor hair removal, contrast enhancement
9. **Data augmentation methods:** Random rotations, affine scaling
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Classification accuracy 95.0% (ISIC 2017), 98.5% (ISIC 2018), AUC 0.98
12. **Main findings:** FCN coupled with DenseNet significantly improves classification performance
13. **Limitations:** High computational demands, boundary over-segmentation
14. **Future work:** Not Reported
15. **Research gaps:** Reducing computational overhead of dual-stage systems
16. **Recommendations for future research:** Not Reported

## Paper 7
**Title:** Malignant Melanoma Classification Using Deep Learning: Datasets, Performance Measurements, Challenges and Opportunities
**Authors:** A. Naeem et al. | **Year:** 2020
1. **Research problem:** Benchmarking models and understanding challenges in melanoma classification
2. **Research aim:** Systematic benchmark of popular architectures
3. **Main objectives:** Not Reported
4. **Dataset used:** PH2, ISIC 2016, ISIC 2017, ISIC 2018, HAM10000
5. **Dataset size:** Not Reported explicitly
6. **Skin lesion classes:** Malignant melanoma vs other
7. **Deep learning architecture:** ResNet-50, VGG-16, Inception-v3, DenseNet-121
8. **Preprocessing methods:** Aspect-ratio preserving resizing, hair suppression, color normalization
9. **Data augmentation methods:** Horizontal/vertical flipping, zooming
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy up to 93.4%, Sensitivity 91.0%, Specificity 94.2%, AUC 0.95
12. **Main findings:** Demonstrated performance disparities across datasets and architectures
13. **Limitations:** Class imbalance inflates accuracy, no multi-center validation, no clinical metadata integration
14. **Future work:** Not Reported
15. **Research gaps:** Severe class imbalance problem, standardized evaluation protocols needed
16. **Recommendations for future research:** Not Reported

## Paper 8
**Title:** Skin Cancer Detection Using Combined Decision of Deep Learners
**Authors:** A. Imran et al. | **Year:** 2022
1. **Research problem:** Improving binary classification performance by fusing decisions of various models
2. **Research aim:** Use an ensemble of CNNs and CapsNet for skin cancer detection
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC Archive balanced subset
5. **Dataset size:** 2,800 images (1400 benign, 1400 malignant)
6. **Skin lesion classes:** Benign, Malignant
7. **Deep learning architecture:** VGG-16 + ResNet-50 + CapsNet ensemble with soft-voting
8. **Preprocessing methods:** Image normalization, resizing to 224×224
9. **Data augmentation methods:** Random rotations, flips, scaling
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 93.50%, Sensitivity 87.25%, Specificity 94.80%, Precision 94.30%, F1 90.64%
12. **Main findings:** Ensemble soft-voting outperforms single architecture models
13. **Limitations:** Computational overhead of 3 networks, binary dataset only, no multi-class
14. **Future work:** Not Reported
15. **Research gaps:** Extending ensemble approaches to multi-class
16. **Recommendations for future research:** Not Reported

## Paper 9
**Title:** FixCaps: An Improved Capsules Network for Diagnosis of Skin Cancer
**Authors:** Z. Lan et al. | **Year:** 2022
1. **Research problem:** Traditional CNNs lose spatial hierarchical information; need for better feature representation
2. **Research aim:** Develop an improved capsule network for skin cancer diagnosis
3. **Main objectives:** Not Reported
4. **Dataset used:** HAM10000
5. **Dataset size:** 10,015 images
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** FixCaps - improved CapsNet with fixed matrix transformation routing + conv attention
8. **Preprocessing methods:** Color normalization, resizing
9. **Data augmentation methods:** Affine augmentation
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 96.49%, Sensitivity 93.47%, Specificity 98.13%, Precision 93.64%, F1 93.55%, AUC 0.98
12. **Main findings:** Improved routing and attention in capsule networks boosts classification over baseline CNNs
13. **Limitations:** Higher latency than lightweight CNNs, performance drops on minority classes, not tested on clinical photos
14. **Future work:** Not Reported
15. **Research gaps:** Improving minority class performance in capsule networks
16. **Recommendations for future research:** Not Reported

## Paper 10
**Title:** Deep Clustering via Center-Oriented Margin Free-Triplet Loss for Skin Lesion Detection
**Authors:** Ş. Öztürk et al. | **Year:** 2022
1. **Research problem:** Feature separation challenges in multi-class skin lesion datasets
2. **Research aim:** Employ deep metric learning for clustering features
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2018, ISIC 2019
5. **Dataset size:** 10,015 images (2018), 25,331 images (2019)
6. **Skin lesion classes:** 7 classes (2018), 8 classes (2019)
7. **Deep learning architecture:** VGG-16 and ResNet-50 with COMF-TL deep metric clustering
8. **Preprocessing methods:** Color standardization, center-cropping
9. **Data augmentation methods:** Random affine transformations
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Balanced accuracy 83.7%, AUC 0.912, Sensitivity 82.4%, Specificity 92.1%, F1 81.9%
12. **Main findings:** Deep metric clustering improves inter-class margin
13. **Limitations:** High training times, no clinical deployment
14. **Future work:** Not Reported
15. **Research gaps:** Class imbalance in feature space needs better solutions
16. **Recommendations for future research:** Not Reported

## Paper 11
**Title:** Neural Architecture Search for Skin Lesion Classification
**Authors:** A. Kwasigroch et al. | **Year:** 2020
1. **Research problem:** Manual design of neural architectures is suboptimal for specific domains like dermoscopy
2. **Research aim:** Apply Neural Architecture Search for skin lesion classification
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2018/HAM10000
5. **Dataset size:** 10,015 images
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** DARTS-based Neural Architecture Search
8. **Preprocessing methods:** Resizing, random cropping, color jittering
9. **Data augmentation methods:** Affine transformations
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Balanced accuracy 78.4%, AUC 0.843, Sensitivity 77.2%, Specificity 91.5%, F1 76.8%
12. **Main findings:** Automated search can discover competitive architectures
13. **Limitations:** High GPU search overhead, architectural collapse, minority class bottlenecks
14. **Future work:** Not Reported
15. **Research gaps:** Automated architecture discovery for dermoscopy
16. **Recommendations for future research:** Not Reported

## Paper 12
**Title:** Performance Enhancement of Skin Cancer Classification Using Computer Vision
**Authors:** A. Magdy et al. | **Year:** 2023
1. **Research problem:** Enhancing feature quality before deep learning classification
2. **Research aim:** Combine rigorous computer vision preprocessing with transfer learning
3. **Main objectives:** Not Reported
4. **Dataset used:** HAM10000, ISIC 2019
5. **Dataset size:** 10,015 images (HAM10000)
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** DenseNet-201, ResNet-50, MobileNetV2 with transfer learning
8. **Preprocessing methods:** Dull Razor hair removal, CLAHE contrast enhancement
9. **Data augmentation methods:** Rotations, flipping
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 97.75%, Precision 97.50%, Sensitivity 97.20%, Specificity 98.10%, F1 97.35%, AUC 0.985
12. **Main findings:** Dedicated preprocessing substantially boosts the metrics of standard architectures
13. **Limitations:** Processing latency from multi-step preprocessing, not validated on smartphone images
14. **Future work:** Not Reported
15. **Research gaps:** Synergy between preprocessing and deep learning needs more study
16. **Recommendations for future research:** Not Reported

## Paper 13
**Title:** EFAM-Net: Multi-Class Skin Lesion Classification with Enhanced Feature Fusion and Attention
**Authors:** Z. Ji et al. | **Year:** 2024
1. **Research problem:** Multi-class classification challenges due to subtle feature variations
2. **Research aim:** Develop EFAM-Net combining feature fusion and attention
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2019, HAM10000
5. **Dataset size:** 25,331 images (2019), 10,015 images (HAM10000)
6. **Skin lesion classes:** 8 classes (2019), 7 classes (HAM10000)
7. **Deep learning architecture:** EFAM-Net with Enhanced Feature Fusion Module + Attention Mechanism
8. **Preprocessing methods:** Bicubic resizing to 224×224, standardization
9. **Data augmentation methods:** Random rotations, flips, cropping
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 92.30% (ISIC 2019), 93.85% (HAM10000), AUC 0.960
12. **Main findings:** Attention mechanism focuses on discriminative regions improving fusion
13. **Limitations:** Increased parameter complexity, high GPU memory, sensitivity drops on rare categories
14. **Future work:** Not Reported
15. **Research gaps:** Attention mechanisms for better minority class recognition
16. **Recommendations for future research:** Not Reported

## Paper 14
**Title:** Hair Segmentation and Removal in Dermoscopic Images Using Deep Learning
**Authors:** L. Talavera-Martínez et al. | **Year:** 2021
1. **Research problem:** Hair artifacts obstructing lesion analysis
2. **Research aim:** Develop a U-Net based hair segmentation and inpainting method
3. **Main objectives:** Not Reported
4. **Dataset used:** 196 dermoscopic images with pixel-level hair annotations (ISIC, PH2)
5. **Dataset size:** 196 images
6. **Skin lesion classes:** Not applicable (segmentation focus)
7. **Deep learning architecture:** U-Net FCN for hair segmentation + deep inpainting
8. **Preprocessing methods:** Color space transformations, patch extraction, synthetic hair augmentation
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Pixel accuracy 95.8%, Precision 90.4%, Recall 89.6%, F1 90.0%, IoU 81.8%
12. **Main findings:** Deep learning-based hair removal preserves lesion textures better than traditional methods
13. **Limitations:** Processing latency, texture smoothing on dense hair clusters
14. **Future work:** Not Reported
15. **Research gaps:** Improved artifact removal prior to classification
16. **Recommendations for future research:** Not Reported

## Paper 15
**Title:** Dermoscopy Image Classification Based on StyleGANs and Decision Fusion
**Authors:** A. Gong et al. | **Year:** 2020
1. **Research problem:** Class imbalance and lack of minority class data
2. **Research aim:** Use StyleGANs for synthetic data generation and decision fusion for classification
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2018/HAM10000
5. **Dataset size:** 10,015 images
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** StyleGAN for synthetic data + DenseNet-201, ResNet-50, Inception-v3 ensemble with weighted decision fusion
8. **Preprocessing methods:** Image standardization, resizing
9. **Data augmentation methods:** StyleGAN synthetic generation for minority classes
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 92.83%, AUC 0.965, Precision 89.20%, Sensitivity 88.90%, F1 89.05%
12. **Main findings:** Synthetic augmentation with StyleGAN effectively addresses data scarcity
13. **Limitations:** Heavy GAN computational overhead, potential non-biological artifacts, no multi-device validation
14. **Future work:** Not Reported
15. **Research gaps:** GAN-based augmentation vs. traditional augmentation comparison needed
16. **Recommendations for future research:** Not Reported

## Paper 16
**Title:** A Comprehensive Joint Learning System to Detect Skin Cancer
**Authors:** L. Riaz et al. | **Year:** 2023
1. **Research problem:** Improving detection via combination of varied network streams
2. **Research aim:** Develop a joint multi-stream CNN for unified dense classification
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC Archive
5. **Dataset size:** Not Reported explicitly
6. **Skin lesion classes:** Binary (Benign vs Malignant)
7. **Deep learning architecture:** Joint multi-stream CNN (VGG-19 + ResNet-50 + MobileNet) + unified dense classification
8. **Preprocessing methods:** Resizing 224×224, adaptive histogram equalization, Dull Razor
9. **Data augmentation methods:** Random rotations, flips
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 98.60%, Sensitivity 97.80%, Specificity 98.90%, Precision 97.50%, F1 97.65%
12. **Main findings:** Multi-stream approach yields exceptionally high binary metrics
13. **Limitations:** Binary classification only, inflated parameters, no non-dermoscopic testing
14. **Future work:** Not Reported
15. **Research gaps:** Extending joint learning to multi-class
16. **Recommendations for future research:** Not Reported

## Paper 17
**Title:** Melanoma Detection Using Multiple Connected Neural Networks
**Authors:** L. Ichim et al. | **Year:** 2020
1. **Research problem:** Accurately segmenting and detecting melanoma from limited samples
2. **Research aim:** Implement a multiple connected CNN approach using color/texture/spatial features
3. **Main objectives:** Not Reported
4. **Dataset used:** MED-NODE, DermQuest
5. **Dataset size:** 170 images (MED-NODE)
6. **Skin lesion classes:** Melanoma vs other
7. **Deep learning architecture:** U-Net segmentation + parallel CNNs for color/texture/spatial features + decision network
8. **Preprocessing methods:** Color space conversion (HSV, L*a*b*), morphological hair removal, illumination normalization
9. **Data augmentation methods:** Offline augmentation
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 97.50%, Sensitivity 96.80%, Specificity 98.00%, Precision 97.10%, F1 96.95%
12. **Main findings:** Parallel feature extraction aids in robust melanoma detection
13. **Limitations:** Small dataset (170 images), error propagation, binary only
14. **Future work:** Not Reported
15. **Research gaps:** Multi-class extension with larger datasets
16. **Recommendations for future research:** Not Reported

## Paper 18
**Title:** DermCDSM: Clinical Decision Support Model for Dermatosis
**Authors:** R. Mittal et al. | **Year:** 2024
1. **Research problem:** Lack of integrated models for broad clinical dermatosis support
2. **Research aim:** Create a clinical decision support model combining classical ML and DL
3. **Main objectives:** Not Reported
4. **Dataset used:** DermNet + clinical collections
5. **Dataset size:** 5,000+ images
6. **Skin lesion classes:** Multiple dermatosis classes
7. **Deep learning architecture:** Random Forest, SVM + ResNet-50, EfficientNet-B0 comparison
8. **Preprocessing methods:** Median filtering, contrast histogram normalization
9. **Data augmentation methods:** Affine augmentation
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 91.00%, Sensitivity 86.14%, Specificity 87.66%, Precision 86.80%, F1 86.47%, AUC 0.920
12. **Main findings:** Deep learning marginally outperforms classical ML on large clinical sets
13. **Limitations:** Variable lighting/resolution, no clinical trials
14. **Future work:** Not Reported
15. **Research gaps:** ML vs DL systematic comparison for skin conditions
16. **Recommendations for future research:** Not Reported

## Paper 19
**Title:** Hybrid Deep Learning for Skin Cancer Using Swin Transformer and DGS-NLAN
**Authors:** R. Karthik et al. | **Year:** 2024
1. **Research problem:** Capturing both local and global dependencies in skin lesion images
2. **Research aim:** Build a hybrid model fusing a Swin Transformer and CNN-based non-local attention
3. **Main objectives:** Not Reported
4. **Dataset used:** HAM10000, ISIC 2018
5. **Dataset size:** 10,015 images (HAM10000)
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** Swin Transformer + Dense Group Shuffle Non-Local Attention Network (hybrid)
8. **Preprocessing methods:** Resizing 224×224, z-score normalization
9. **Data augmentation methods:** Random rotations, flipping, color jittering
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 94.21%, Sensitivity 93.80%, Specificity 97.10%, Precision 94.00%, F1 96.64%, AUC 0.978
12. **Main findings:** Hybrid architecture is highly effective for global/local feature extraction
13. **Limitations:** High computational overhead, GPU memory demands, performance drops on underrepresented types, no mobile optimization
14. **Future work:** Not Reported
15. **Research gaps:** Transformer-CNN fusion for dermoscopy
16. **Recommendations for future research:** Not Reported

## Paper 20
**Title:** Analysis of Skin Marks Through the Use of Intelligent Things
**Authors:** D. Połap | **Year:** 2019
1. **Research problem:** IoMT-based analysis using heuristic features on constrained devices
2. **Research aim:** Use lightweight NN combined with ABCD rule heuristics for skin mark analysis
3. **Main objectives:** Not Reported
4. **Dataset used:** Clinical archives
5. **Dataset size:** 1,200 skin lesion images
6. **Skin lesion classes:** Not Reported explicitly
7. **Deep learning architecture:** Lightweight NN + ABCD rule heuristic features
8. **Preprocessing methods:** Grayscale, adaptive Gaussian thresholding, edge filtering
9. **Data augmentation methods:** Not Reported
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 91.20%, Sensitivity 89.50%, Specificity 92.40%, Precision 90.10%, F1 89.80%
12. **Main findings:** Provides a feasible pipeline for Internet of Medical Things
13. **Limitations:** Handcrafted heuristics fail on amelanotic lesions, camera noise, small dataset
14. **Future work:** Not Reported
15. **Research gaps:** Deep learning replacing handcrafted features for IoMT
16. **Recommendations for future research:** Not Reported

## Paper 21
**Title:** Early Detection of Multiclass Skin Lesions Using Transfer Learning-Based IncepX-Ensemble
**Authors:** S. Chatterjee et al. | **Year:** 2024
1. **Research problem:** Ensuring early detection through multi-class lesion classification
2. **Research aim:** Develop an InceptionV3 and Xception ensemble model
3. **Main objectives:** Not Reported
4. **Dataset used:** HAM10000
5. **Dataset size:** 10,015 images
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** InceptionV3 + Xception ensemble with concatenation fusion
8. **Preprocessing methods:** Resizing, normalization
9. **Data augmentation methods:** Rotation, zooming, shifts, flipping
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 96.87%, Precision 96.90%, Sensitivity 96.85%, Specificity 98.20%, F1 96.87%, AUC 0.982
12. **Main findings:** Ensemble of advanced CNN architectures significantly improves multiclass detection
13. **Limitations:** Large parameter count, inference latency, no external clinical validation
14. **Future work:** Not Reported
15. **Research gaps:** Ensemble efficiency vs. accuracy trade-off
16. **Recommendations for future research:** Not Reported

## Paper 22
**Title:** Classification for Dermoscopy Using CNNs Based on Ensemble of Individual Advantage and Group Decision
**Authors:** A. Gong et al. | **Year:** 2020
1. **Research problem:** Integrating diverse features from multiple CNN models
2. **Research aim:** Build an ensemble exploiting individual advantage and group decision
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2017
5. **Dataset size:** 2,000+150+600 images
6. **Skin lesion classes:** 3 classes
7. **Deep learning architecture:** ResNet-50, DenseNet-121, Inception-v3 with IAN-GDN ensemble
8. **Preprocessing methods:** Standardization, random rotation, cropping, contrast scaling
9. **Data augmentation methods:** Standard geometric augmentation
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 91.50%, AUC 0.942, Sensitivity 88.70%, Specificity 93.10%, Precision 89.20%, F1 88.95%
12. **Main findings:** Strategic ensemble outshines baseline individual CNN models
13. **Limitations:** Complex multi-stage pipeline, increased latency, only 3 diagnostic categories
14. **Future work:** Not Reported
15. **Research gaps:** Extending ensemble advantages to more classes
16. **Recommendations for future research:** Not Reported

## Paper 23
**Title:** Pipelined Structure Based on AlexNet CNN and SVM with Bi-Sectional Texture Features
**Authors:** V. S. S. B. T. Sathvika et al. | **Year:** 2024
1. **Research problem:** Extracting robust texture features to differentiate lesions
2. **Research aim:** Use AlexNet + SVM alongside bi-sectional GLCM/LBP features
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC/HAM10000
5. **Dataset size:** 3,000 images
6. **Skin lesion classes:** Not Reported explicitly
7. **Deep learning architecture:** AlexNet CNN + GLCM/LBP texture features + SVM classifier
8. **Preprocessing methods:** Dull Razor hair removal, median filtering, automated segmentation
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 98.66%, Sensitivity 98.20%, Specificity 99.10%, Precision 98.00%, F1 98.10%, AUC 0.986
12. **Main findings:** Bi-sectional texture features heavily improve the classifier's discriminative ability
13. **Limitations:** AlexNet is outdated, bi-sectional partitioning sensitive to asymmetric lesions, no clinical evaluation
14. **Future work:** Not Reported
15. **Research gaps:** Modern architectures replacing legacy CNNs
16. **Recommendations for future research:** Not Reported

## Paper 24
**Title:** Improved Segmentation Model for Melanoma Using NCC-Based k-Means Clustering
**Authors:** M. I. Faizi et al. | **Year:** 2024
1. **Research problem:** Automating melanoma lesion segmentation robustly
2. **Research aim:** Implement NCC-based k-means clustering for segmentation
3. **Main objectives:** Not Reported
4. **Dataset used:** PH2, ISBI 2016
5. **Dataset size:** 200 images (PH2), 1,279 images (ISBI 2016)
6. **Skin lesion classes:** Melanoma vs other
7. **Deep learning architecture:** NCC + optimized k-means clustering (unsupervised segmentation)
8. **Preprocessing methods:** Grayscale conversion, contrast stretching, template matching
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Unsupervised
11. **Evaluation metrics:** Segmentation accuracy 99.29%, Specificity 97.70%, Sensitivity 94.20%, Dice 93.10%, Jaccard 88.40%
12. **Main findings:** High segmentation overlap without reliance on supervised deep networks
13. **Limitations:** Degrades on diffuse low-contrast margins, no disease classification
14. **Future work:** Not Reported
15. **Research gaps:** Integration of segmentation with classification
16. **Recommendations for future research:** Not Reported

## Paper 25
**Title:** Multiple Instance Learning Using 3D Features for Melanoma Detection
**Authors:** P. M. M. Pereira et al. | **Year:** 2022
1. **Research problem:** Incorporating 3D topographic data into melanoma detection
2. **Research aim:** Extract 3D geometric features combined with MIL attention pooling
3. **Main objectives:** Not Reported
4. **Dataset used:** Biopsy-verified cases (specialized 3D scanning)
5. **Dataset size:** 50 cases
6. **Skin lesion classes:** Melanoma vs benign
7. **Deep learning architecture:** CNN + 3D geometric features + MIL attention pooling
8. **Preprocessing methods:** 3D point cloud reconstruction, surface normal estimation
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 84.00%, Sensitivity 88.89%, Specificity 81.25%, F1 84.21%, AUC 0.880
12. **Main findings:** 3D features provide distinctive cues missed by 2D dermoscopy
13. **Limitations:** Requires specialized 3D equipment, only 50 cases, high computational overhead
14. **Future work:** Not Reported
15. **Research gaps:** 3D features are novel but impractical for standard dermoscopy
16. **Recommendations for future research:** Not Reported

## Paper 26
**Title:** SPCB-Net: Multi-Scale Skin Cancer Identification Using Self-Interactive Attention Pyramid
**Authors:** X. Qian et al. | **Year:** 2024
1. **Research problem:** Analyzing fine-grained lesion details across multiple scales
2. **Research aim:** Develop SPCB-Net with Self-Interactive Attention Pyramid for identification
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2018/HAM10000, ISIC 2019
5. **Dataset size:** 10,015 images (2018), 25,331 images (2019)
6. **Skin lesion classes:** 7 classes (2018), 8 classes (2019)
7. **Deep learning architecture:** SPCB-Net with SIAP + Cross-Layer Bilinear-Trilinear Pooling
8. **Preprocessing methods:** Bicubic resizing 224×224, z-score normalization
9. **Data augmentation methods:** Random rotations, flipping, affine scaling
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 93.60%, Precision 92.80%, Sensitivity 92.40%, Specificity 96.50%, F1 92.60%, AUC 0.975
12. **Main findings:** Multi-scale feature modeling captures intricate morphological details efficiently
13. **Limitations:** High tensor complexity, elevated GPU memory, latency for mobile
14. **Future work:** Not Reported
15. **Research gaps:** Multi-scale feature modeling for fine-grained lesion analysis
16. **Recommendations for future research:** Not Reported

## Paper 27
**Title:** IARS SegNet: Interpretable Attention Residual Skip SegNet for Melanoma Segmentation
**Authors:** V. S. Narayanan et al. | **Year:** 2024
1. **Research problem:** Accurate boundary delineation with interpretable mechanisms
2. **Research aim:** Propose IARS SegNet for interpretable melanoma segmentation
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2017, ISIC 2018
5. **Dataset size:** 2,000 images (2017), 2,594 images (2018)
6. **Skin lesion classes:** Melanoma (segmentation focus)
7. **Deep learning architecture:** SegNet with attention-guided residual skip connections
8. **Preprocessing methods:** Resizing, contrast enhancement, Dull Razor hair removal
9. **Data augmentation methods:** Geometric transformations
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Segmentation accuracy 96.80%, Dice 92.40%, Jaccard 86.10%, Sensitivity 93.10%, Specificity 97.50%
12. **Main findings:** Highly accurate and interpretable boundary segmentation
13. **Limitations:** Segmentation only (no classification), degrades on amelanotic lesions
14. **Future work:** Not Reported
15. **Research gaps:** Integrating interpretable segmentation with classification
16. **Recommendations for future research:** Not Reported

## Paper 28
**Title:** Toward Better Ear Disease Diagnosis: Multi-Modal Multi-Fusion Model
**Authors:** T. Kim et al. | **Year:** 2023
1. **Research problem:** Fusing multimodal clinical data for disease diagnosis (otology use case)
2. **Research aim:** Implement a cross-attention fusion model for multi-modal data
3. **Main objectives:** Not Reported
4. **Dataset used:** Endoscopic tympanic membrane images + PTA records
5. **Dataset size:** 2,416 records
6. **Skin lesion classes:** Not applicable (otology - 6 categories)
7. **Deep learning architecture:** ResNet-50 + 1D CNN for audiograms + cross-attention fusion
8. **Preprocessing methods:** Resizing 224×224, contrast normalization, PTA scaling
9. **Data augmentation methods:** Affine augmentations
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 94.90%, Sensitivity 93.20%, Specificity 96.10%, Precision 93.50%, F1 93.35%, AUC 0.970
12. **Main findings:** Demonstrated that multimodal fusion outpaces unimodal data
13. **Limitations:** Application is otology (not dermatology), requires synchronized multimodal data
14. **Future work:** Not Reported
15. **Research gaps:** Multi-modal fusion approach applicable to skin cancer if metadata available
16. **Recommendations for future research:** Not Reported

## Paper 29
**Title:** Classification of Skin Lesion Using Quantum Chebyshev Polynomials and Autoencoder
**Authors:** Farhatullah et al. | **Year:** 2024
1. **Research problem:** Seeking novel mathematical feature extractors to improve lesion discrimination
2. **Research aim:** Use Quantum Chebyshev Polynomials coupled with deep autoencoders
3. **Main objectives:** Not Reported
4. **Dataset used:** HAM10000, ISIC 2019
5. **Dataset size:** 10,015 images (HAM10000)
6. **Skin lesion classes:** 7 classes (HAM10000)
7. **Deep learning architecture:** DWT + Quantum Chebyshev Polynomial features + deep autoencoder + ensemble classifier
8. **Preprocessing methods:** 2D Discrete Wavelet Transform decomposition, contrast scaling
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 98.23%, Precision 98.26%, Sensitivity 98.21%, Specificity 99.12%, F1 98.24%, AUC 0.991
12. **Main findings:** Extremely high accuracy using this quantum-inspired feature approach
13. **Limitations:** Computational overhead of quantum polynomials, no end-to-end backpropagation, no embedded device testing
14. **Future work:** Not Reported
15. **Research gaps:** Novel feature extraction methods for dermoscopy
16. **Recommendations for future research:** Not Reported

## Paper 30
**Title:** Integrating Clinical Knowledge Graphs and Gradient-Based Neural Systems for Melanoma Diagnosis
**Authors:** Y. Wang et al. | **Year:** 2026
1. **Research problem:** Aligning neural representations with clinical diagnostic rules (7-point checklist)
2. **Research aim:** Fuse CNNs with Clinical Knowledge Graphs using regularization
3. **Main objectives:** Not Reported
4. **Dataset used:** Derm7pt, HAM10000
5. **Dataset size:** 1,011 pairs (Derm7pt)
6. **Skin lesion classes:** Melanoma vs other
7. **Deep learning architecture:** CNN + Clinical Knowledge Graph with 7-point checklist regularization
8. **Preprocessing methods:** Image standardization, clinical pair alignment
9. **Data augmentation methods:** Data augmentation (unspecified details)
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** AUC 88.60%, Accuracy 83.40%, Sensitivity 82.10%, Specificity 87.20%, F1 82.70%
12. **Main findings:** Imparts clinical rationale directly into network optimization
13. **Limitations:** Manual ontology curation, small dataset (1,011), complex co-optimization
14. **Future work:** Not Reported
15. **Research gaps:** Neuro-symbolic approaches bridging clinical knowledge with deep learning
16. **Recommendations for future research:** Not Reported

## Paper 31
**Title:** Hybrid Model for Early Melanoma Detection: YOLOv9 + Faster R-CNN
**Authors:** M. I. Marie et al. | **Year:** 2025
1. **Research problem:** Simultaneous localization and classification of melanoma
2. **Research aim:** Combine state-of-the-art object detection frameworks YOLOv9 and Faster R-CNN
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2020, ISIC 2019
5. **Dataset size:** 33,126 images (2020)
6. **Skin lesion classes:** Melanoma vs other
7. **Deep learning architecture:** YOLOv9 (PGI + GELAN) + Faster R-CNN (ResNet-101)
8. **Preprocessing methods:** Bounding-box formatting, color constancy normalization
9. **Data augmentation methods:** Mosaic augmentation
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 95.80%, Precision 95.20%, Sensitivity 95.60%, Specificity 96.80%, F1 95.40%, mAP 94.70%
12. **Main findings:** High mAP confirms strong localization alongside accurate classification
13. **Limitations:** Two-stage latency, high memory consumption, requires bounding box annotations
14. **Future work:** Not Reported
15. **Research gaps:** Object detection for lesion localization and classification
16. **Recommendations for future research:** Not Reported

## Paper 32
**Title:** Automated Skin Cancer Report Generation via Knowledge-Distilled Vision-Language Model
**Authors:** L. Chakrabarti et al. | **Year:** 2025
1. **Research problem:** Bridging the gap between raw classification and natural language clinical reports
2. **Research aim:** Distill a VLM to automatically generate descriptive text reports
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC archives (paired images and reports)
5. **Dataset size:** 4,000+ paired images
6. **Skin lesion classes:** Not Reported explicitly
7. **Deep learning architecture:** ViT encoder + distilled language decoder (knowledge distilled from large VLM)
8. **Preprocessing methods:** Image normalization, text cleaning, BPE tokenization
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** F1 90.25%, BLEU-4 0.428, CIDEr 1.15, Accuracy 92.10%, Sensitivity 90.50%, Specificity 93.40%
12. **Main findings:** Capable of outputting coherent text reports with diagnostic relevance
13. **Limitations:** Language hallucination risk, requires expert-annotated text, training overhead
14. **Future work:** Not Reported
15. **Research gaps:** VLM for medical report generation in dermoscopy
16. **Recommendations for future research:** Not Reported

## Paper 33
**Title:** Multi-Scale DCNN with Dynamic Weight and Part Cross-Entropy Loss
**Authors:** G. Wang et al. | **Year:** 2024
1. **Research problem:** Mitigating data imbalance while focusing on distinct parts of the lesion
2. **Research aim:** Employ dynamic weighting and Part Cross-Entropy loss in a multi-scale DCNN
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2018/HAM10000, ISIC 2017
5. **Dataset size:** 10,015 images (2018)
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** Multi-branch DCNN + Part Cross-Entropy loss + dynamic weighting
8. **Preprocessing methods:** Aspect-ratio preserving resizing, multi-scale pyramid, color standardization
9. **Data augmentation methods:** Geometric augmentations
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 91.80%, AUC 0.952, Sensitivity 87.60%, Specificity 93.80%, F1 88.20%
12. **Main findings:** Dynamic loss function effectively handles class imbalance in training
13. **Limitations:** Multi-branch latency, PCE loss sensitive to hyperparameters, no clinical photo testing
14. **Future work:** Not Reported
15. **Research gaps:** Dynamic loss functions for class-imbalanced dermoscopy
16. **Recommendations for future research:** Not Reported

## Paper 34
**Title:** Skin Lesion Segmentation in Clinical Images Using NMF and Mutual Information
**Authors:** E. Soares Flores et al. | **Year:** 2025
1. **Research problem:** Difficulties in segmenting uncontrolled clinical (non-dermoscopic) images
2. **Research aim:** Utilize NMF and Mutual Information thresholding for unsupervised segmentation
3. **Main objectives:** Not Reported
4. **Dataset used:** Dermofit Image Library
5. **Dataset size:** 1,300 clinical images
6. **Skin lesion classes:** 10 classes
7. **Deep learning architecture:** NMF-based patch decomposition + Mutual Information thresholding (unsupervised)
8. **Preprocessing methods:** Patch decomposition, color space transformation, illumination normalization
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Unsupervised
11. **Evaluation metrics:** Segmentation accuracy 93.80%, Dice 84.50%, Jaccard 74.20%, Sensitivity 86.10%, Specificity 94.70%
12. **Main findings:** Adaptable unsupervised segmentation for challenging clinical photography
13. **Limitations:** Lower boundary overlap than supervised methods, high per-image latency, no classification
14. **Future work:** Not Reported
15. **Research gaps:** Unsupervised segmentation for clinical photography
16. **Recommendations for future research:** Not Reported

## Paper 35
**Title:** Transparent Search-Based Framework for Skin and Breast Cancer Using Siamese Networks
**Authors:** Z. Tabatabaei et al. | **Year:** 2025
1. **Research problem:** Need for transparent decision support via Content-Based Health Image Retrieval
2. **Research aim:** Develop a Siamese network framework with contrastive/triplet loss
3. **Main objectives:** Not Reported
4. **Dataset used:** Skin cancer histopathology patches, BreakHis
5. **Dataset size:** 9,109 microscopic images
6. **Skin lesion classes:** Various histopathology classes
7. **Deep learning architecture:** Siamese Network with contrastive/triplet loss for CBHIR
8. **Preprocessing methods:** Macenko stain normalization, patch extraction
9. **Data augmentation methods:** Rotations, elastic deformations
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Top-1 accuracy 88.50%, Top-5 94.20%, Precision 89.10%, Recall 87.80%, F1 88.40%
12. **Main findings:** Enables diagnosis by searching for similar verified cases, boosting interpretability
13. **Limitations:** Memory/indexing latency, relies on biopsy tissue, retrieval quality depends on archive
14. **Future work:** Not Reported
15. **Research gaps:** Content-based retrieval for interpretable decision support
16. **Recommendations for future research:** Not Reported

## Paper 36
**Title:** FoMoSkinNet: Dual-Stream Model for Non-Dermoscopic Skin Lesions
**Authors:** F. Bibi et al. | **Year:** 2026
1. **Research problem:** Analyzing skin lesions from standard macroscopic cameras rather than dermatoscopes
2. **Research aim:** Propose a dual-stream model combining Focal Modulation and CNN
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2024, clinical photographic repos
5. **Dataset size:** 12,000+ non-dermoscopic images
6. **Skin lesion classes:** Multiple
7. **Deep learning architecture:** Focal Modulation stream + CNN stream with cross-attention gate fusion
8. **Preprocessing methods:** Bilinear resizing 224×224, color constancy
9. **Data augmentation methods:** Flipping, scaling, rotation
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 99.46%, Precision 98.23%, Sensitivity 98.40%, Specificity 99.50%, F1 99.47%, AUC 0.995
12. **Main findings:** Extremely robust performance on lower-quality non-dermoscopic imagery
13. **Limitations:** Dual-stream parameter footprint, needs clinical trials across Fitzpatrick skin types
14. **Future work:** Not Reported
15. **Research gaps:** Non-dermoscopic image analysis, diversity in skin phototypes
16. **Recommendations for future research:** Not Reported

## Paper 37
**Title:** MSPE-DeiT: Vision Transformer-Based Multimodal Framework for Skin Cancer Diagnosis
**Authors:** U. Mittal et al. | **Year:** 2026
1. **Research problem:** Integrating patient metadata with visual cues for accurate diagnosis
2. **Research aim:** Create a DeiT architecture incorporating multimodal cross-attention
3. **Main objectives:** Not Reported
4. **Dataset used:** HAM10000, ISIC 2019
5. **Dataset size:** 10,015 images + metadata (age, sex, site)
6. **Skin lesion classes:** 7 classes
7. **Deep learning architecture:** DeiT + Multi-Scale Positional Encoding + MLP metadata branch + cross-modal attention
8. **Preprocessing methods:** Patch tokenization, metadata one-hot encoding, feature standardization
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Accuracy 91.76% (up to 94.59% multimodal), Sensitivity 84.81%, Specificity 91.77%, Precision 85.20%, F1 85.00%, AUC 0.935
12. **Main findings:** Adding clinical metadata substantially boosts classification over images alone
13. **Limitations:** High transformer complexity, performance degrades with missing metadata, no multi-center validation
14. **Future work:** Not Reported
15. **Research gaps:** Multimodal fusion of metadata with images for skin cancer
16. **Recommendations for future research:** Not Reported

## Paper 38
**Title:** MoLE: Mixture-of-LoRA Experts for Dermoscopic Visual Question Answering
**Authors:** K. Younis et al. | **Year:** 2026
1. **Research problem:** Creating interactive diagnostic tools for querying dermoscopic features
2. **Research aim:** Use Mixture-of-LoRA Experts applied to Visual Question Answering
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC images + Q&A pairs (tested on HAM10000)
5. **Dataset size:** ~1,200 ISIC images + 24,000 Q&A pairs
6. **Skin lesion classes:** Not Reported explicitly
7. **Deep learning architecture:** LLaVA-1.5-7B + 3 LoRA expert modules with routing gate
8. **Preprocessing methods:** Patch embedding, prompt tokenization
9. **Data augmentation methods:** Not Reported explicitly
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** VQA accuracy 79.40%, METEOR +16.9%, CIDEr +19.1% vs single-LoRA
12. **Main findings:** Experts specialize in different diagnostic domains, improving natural language answers
13. **Limitations:** Research prototype only, requires dermatologist oversight, GPU hardware needed
14. **Future work:** Not Reported
15. **Research gaps:** VQA and interactive clinical consultation in dermoscopy
16. **Recommendations for future research:** Not Reported

## Paper 39
**Title:** SLGAN-EID: GAN-Based Skin Lesion Image Enhancement With Improved Diagnosis
**Authors:** M. U. Zafar et al. | **Year:** 2026
1. **Research problem:** Artifacts and poor illumination hinder standard diagnostic models
2. **Research aim:** Design a GAN that cleans and enhances images while preserving disease features
3. **Main objectives:** Not Reported
4. **Dataset used:** ISIC 2019, HAM10000
5. **Dataset size:** 25,331 images (2019), 10,015 images (HAM10000)
6. **Skin lesion classes:** 8 classes (2019), 7 classes (HAM10000)
7. **Deep learning architecture:** Dual-discriminator GAN (quality D1 + diagnostic D2) with multi-scale attention U-Net generator
8. **Preprocessing methods:** Dull Razor filtering, patch cropping
9. **Data augmentation methods:** Adversarial augmentation
10. **Training methodology:** Not Reported explicitly
11. **Evaluation metrics:** Classification accuracy 94.30%, F1 92.30%, PSNR improved to 32.87 dB, SSIM 0.863, Sensitivity 93.10%, Specificity 95.20%, AUC 0.965
12. **Main findings:** Dual discriminator setup prevents GAN from hallucinating spurious textures
13. **Limitations:** High training complexity of dual-discriminator, mode collapse risk, needs multi-center validation
14. **Future work:** Not Reported
15. **Research gaps:** Feature-preserving image enhancement for dermoscopy
16. **Recommendations for future research:** Not Reported
