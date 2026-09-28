# Step 5: Candidate Research Objectives

Based on the identified research gaps and the literature review of 39 papers, the following 8 candidate research objectives have been formulated. These objectives are specific, measurable, experimentally testable, and feasible for a BCA-level academic prototype using the HAM10000 dataset.

1. **To evaluate** the impact of standardized image preprocessing pipelines (e.g., hair removal via DullRazor and contrast enhancement via CLAHE) on the multi-class classification performance of deep learning models on the HAM10000 dataset.
   - **Supported by:** Papers 6, 12, 14, 39
   - **Gap Addressed:** Insufficient preprocessing pipeline evaluation and limited evaluation of preprocessing impact.

2. **To compare** the efficacy of distinct pre-trained CNN architectures (e.g., ResNet, DenseNet, MobileNet) via transfer learning for categorizing the 7 classes of skin lesions in the HAM10000 dataset.
   - **Supported by:** Papers 2, 5, 7, 12, 16, 18, 21
   - **Gap Addressed:** Limited systematic comparison of transfer learning architectures on HAM10000; multi-class clinical need.

3. **To investigate** the effectiveness of targeted data augmentation strategies (including standard geometric transformations and advanced techniques) in mitigating the severe class imbalance (e.g., 67% nevi dominance) present in the HAM10000 dataset.
   - **Supported by:** Papers 3, 7, 9, 10, 11, 13, 15, 33, 39
   - **Gap Addressed:** Class imbalance inadequately addressed; few studies evaluate augmentation strategies.

4. **To implement** Gradient-weighted Class Activation Mapping (Grad-CAM) to visualize the spatial regions of dermoscopic images that influence the model's predictions, thereby enhancing interpretability.
   - **Supported by:** Papers 3, 27, 30
   - **Gap Addressed:** Most studies lack interpretability/explainability on HAM10000.

5. **To assess** model performance systematically using a comprehensive suite of evaluation metrics (Accuracy, Precision, Recall, F1-Score, Specificity, AUC-ROC, and Confusion Matrix) rather than relying solely on overall accuracy.
   - **Supported by:** Paper 7
   - **Gap Addressed:** Performance metrics often limited to accuracy only; need for comprehensive multi-metric evaluation.

6. **To develop** a simple ensemble model combining the predictions of top-performing individual architectures to ascertain if ensemble techniques yield superior generalizability on the HAM10000 dataset.
   - **Supported by:** Papers 4, 8, 15, 16, 21, 22
   - **Gap Addressed:** Need for robust multi-class classification and improved accuracy beyond individual models.

7. **To analyze** the specific misclassifications and feature confusion between visually similar classes (specifically melanoma and benign keratosis) using confusion matrices and error analysis.
   - **Supported by:** Papers 3, 5
   - **Gap Addressed:** Confusion between melanoma and benign keratosis.

8. **To determine** the optimal hyperparameter configurations (learning rate, batch size, and optimizer choices) for fine-tuning deep neural networks on highly skewed dermatological image datasets.
   - **Supported by:** Papers 7, 12, 13
   - **Gap Addressed:** Limited systematic comparison of training methodologies on HAM10000.
