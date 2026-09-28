# Research Objectives Repository: 39 Medical Image Analysis Papers

This repository contains the rigorous, academic extraction and formalization of the **Research Objectives** across all 39 peer-reviewed medical computer vision and dermatological deep learning research papers in `downloaded_journals/`.

## Generated Deliverables

| File Name | Format | Description |
|:---|:---:|:---|
| **`Research_Objectives_39_Papers.pdf`** | PDF | Publication-grade compiled document with formal title page, executive taxonomy, master matrix table, and individual paper sections. |
| **`Research_Objectives_39_Papers.docx`** | Microsoft Word | Formatted Word document with custom corporate/academic styles, shaded callout boxes, and structured tables. |
| **`main.tex`** | LaTeX Source | Complete LaTeX source code configured with `tcolorbox`, `tabularx`, `longtable`, and `geometry`. |
| **`research_objectives_all_39_papers.md`** | Markdown | Complete Markdown document for instantaneous viewing and documentation. |
| **`research_objectives_data.py`** | Python | Programmatic Python database export containing all 39 papers with complete metadata and objectives. |

## Structure of Objectives for Each Paper

Each of the 39 papers contains:
1. **Bibliographic Header**: Title, authors, affiliations, journal/venue, year, DOI, IEEE Article Number, and PDF filename.
2. **Clinical & Technical Problem**: The specific healthcare or algorithmic bottleneck addressed by the authors.
3. **Primary Research Objective (General Aim)**: Formal statement of the overarching intent of the study.
4. **Specific Research Objectives (Operational & Methodological Goals)**:
   - **RO1 (Data & Preprocessing):** Hair removal, artifact suppression, gamma contrast correction, synthetic augmentation, or patch extraction.
   - **RO2 (Architectural Formulation):** Custom CNN, Swin Transformer, DenseNet, Capsule networks, FoMoSkinNet, or YOLOv9 + Faster R-CNN.
   - **RO3 (Loss & Optimization):** Weight regularizer, center-oriented margin-free triplet loss, part cross-entropy, or LoRA parameter tuning.
   - **RO4 (Empirical Evaluation):** Validation against international benchmarks (ISIC 2016-2020, HAM10000, DermIS, DermQuest, PH2).
   - **RO5 (Explainability & Deployment):** Grad-CAM attribution, Seven-point checklist graphs, Android edge app, or automated report generation.
5. **Key Methodologies, Evaluated Datasets & Quantitative Metrics**.
6. **Clinical Utility & Real-World Translation**.

## Recompilation Instructions

To recompile the LaTeX document:
```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
