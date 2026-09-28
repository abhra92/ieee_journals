# Research Objectives

### General Objective
To develop and evaluate a deep learning-based multiclass skin lesion classification system using the HAM10000 dermoscopic dataset with optimized image preprocessing, data augmentation, and transfer learning techniques to improve classification performance across seven diagnostic categories.

### Specific Objectives
1. To implement and evaluate image preprocessing techniques—including image resizing, normalization, and artifact suppression—on HAM10000 dermoscopic images and assess their impact on downstream classification accuracy.
2. To investigate the effectiveness of data augmentation strategies—including geometric transformations, color-based augmentation, and class-specific oversampling—in addressing the severe class imbalance present in the HAM10000 dataset.
3. To compare the classification performance of multiple pre-trained CNN architectures—including ResNet-50, DenseNet-201, VGG-16, MobileNetV2, and InceptionV3—fine-tuned via transfer learning on the HAM10000 dataset for seven-class skin lesion classification.
4. To analyze the per-class classification performance across all seven HAM10000 diagnostic categories using comprehensive evaluation metrics including accuracy, precision, recall, F1-score, sensitivity, specificity, AUC-ROC, and confusion matrix analysis.
5. To assess the interpretability of the best-performing deep learning model using Gradient-weighted Class Activation Mapping (Grad-CAM) to visualize and validate the discriminative lesion regions used for classification decisions.

These objectives directly address critical research gaps identified in recent literature surrounding automated skin cancer detection. While several studies have demonstrated that robust preprocessing significantly enhances classification [6], [12], [14], [39], the severe class imbalance inherent to the HAM10000 dataset remains the most frequently cited limitation preventing widespread clinical adoption [3], [7], [9]-[11], [13], [15], [33]. By systematically evaluating class-specific data augmentation alongside a comprehensive comparison of modern pre-trained architectures [2], [5], [7], [12], [16], [18], [21], this research seeks to establish an optimized, reproducible pipeline. Furthermore, this study addresses the notable lack of standardized multi-metric evaluation across all seven diagnostic categories [7] and extends upon preliminary explainability efforts [3], [27], [30] by utilizing Grad-CAM to validate that high-performing models make diagnostic decisions based on clinically relevant morphological features rather than spurious artifacts.

### Research Questions
**RQ1:** How do image preprocessing techniques (resizing, normalization, artifact removal) affect the classification accuracy of deep learning models on HAM10000?
**RQ2:** What data augmentation strategies are most effective in mitigating class imbalance in the HAM10000 dataset for multiclass skin lesion classification?
**RQ3:** Which pre-trained CNN architecture achieves the highest classification performance when fine-tuned via transfer learning on HAM10000 for seven-class skin lesion classification?
**RQ4:** How does classification performance vary across the seven diagnostic categories of HAM10000, and which categories are most frequently misclassified?
**RQ5:** Can Grad-CAM visualizations from the best-performing model produce clinically meaningful activation maps that highlight diagnostically relevant lesion regions?
