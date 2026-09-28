# Step 7: Scored Candidate Objectives

Each candidate objective is scored from 1 (Lowest) to 5 (Highest) across 7 criteria, for a maximum total of 35.

**Criteria:**
1. Relevance to research topic
2. Connection to literature gap
3. Measurability
4. Experimental feasibility (BCA level)
5. Suitability for HAM10000
6. Academic value
7. Alignment with proposed research questions

| Objective | 1. Relevance | 2. Lit Gap | 3. Measurable | 4. Feasibility | 5. HAM10000 | 6. Academic Value | 7. Alignment | Total | Rank |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Obj 2** (Compare Transfer Learning) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | **35** | **1** |
| **Obj 5** (Multi-metric Evaluation) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | **35** | **1** |
| **Obj 3** (Data Augmentation/Imbalance) | 5 | 5 | 5 | 4 | 5 | 5 | 5 | **34** | **3** |
| **Obj 4** (Grad-CAM Explainability) | 5 | 5 | 5 | 4 | 5 | 5 | 4 | **33** | **4** |
| **Obj 1** (Preprocessing Evaluation) | 4 | 4 | 5 | 4 | 5 | 4 | 4 | **30** | **5** |
| **Obj 7** (Misclassification Analysis) | 4 | 4 | 4 | 5 | 5 | 4 | 4 | **30** | **5** |
| **Obj 6** (Ensemble Methods) | 4 | 3 | 5 | 3 | 4 | 4 | 3 | **26** | **7** |
| **Obj 8** (Hyperparameter Tuning) | 3 | 2 | 5 | 5 | 4 | 2 | 3 | **24** | **8** |

### Justification of Scores:
- **Objectives 2, 3, and 5** score highest because they directly address the most critical literature gaps (class imbalance, multi-class architectures, and metric limitations) while remaining highly feasible and standard for modern CNN research on datasets like HAM10000.
- **Objective 4 (Grad-CAM)** scores very high due to the significant gap in explainability (only Paper 3 utilized it) and high academic value, though it introduces slight complexity for a BCA project (Feasibility: 4).
- **Objectives 1 and 7** are solid analytical objectives that are highly measurable and feasible.
- **Objective 6 (Ensemble)** scores lower on feasibility and gap connection, as it adds significant computational overhead and complexity for a BCA project.
- **Objective 8** is viewed more as standard operating procedure than a distinct, novel research objective.
