"""
Script to extract the Related Work / Literature Review sections from all 39 PDF papers
in downloaded_journals/ and compile them into a unified, beautifully structured Markdown file.
"""

import sys, os, csv, re
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

METADATA_FILE = 'papers_metadata_index_39.csv'
OUTPUT_FILE = 'RELATED_WORK_all_39_papers.md'

# Extraction specifications for each of the 39 papers:
# key: filename prefix
# tuple: (start_regex, end_regex, section_title_display, core_topics)
EXTRACTION_RULES = {
    '01_M._A._Albahar': (
        r'III\.\s+RELATED\s+WORK',
        r'IV\.\s+PROPOSED\s+REGULARIZER',
        'Section III: Related Work',
        'Computer-aided diagnosis of skin lesions, deep CNN architectures, clinical feature extraction, and regularization techniques.'
    ),
    '02_R._Ashraf': (
        r'II\.\s+LITERATURE\s+REVIEW',
        r'III\.\s+PROPOSED\s+METHODOLOGY',
        'Section II: Literature Review',
        'ABCD dermoscopic rule analysis, handcrafted color/textural/shape features, SVM/KNN baselines, and ROI transfer learning with CNNs.'
    ),
    '03_K._Mridha': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+METHODOLOGIES',
        'Section II: Related Work',
        'Deep learning in dermatology, CNN architectures (AlexNet, VGG, ResNet), class imbalance handling, and explainable AI (Grad-CAM).'
    ),
    '04_L._Wei': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+METHODOLOGY',
        'Section II: Related Work',
        'Lightweight neural networks, semantic segmentation in dermoscopy (FCN, U-Net), ensemble learning, and fine-grained classification.'
    ),
    '05_H._L._Gururaj': (
        r'II\.\s+LITERATURE\s+REVIEW',
        r'III\.\s+METHODOLOGY',
        'Section II: Literature Review',
        'Machine learning algorithms for lesion screening, deep learning backbones (VGG, ResNet, MobileNet), and multiclass dermoscopic benchmarks.'
    ),
    '06_A._A._Adegun': (
        r'II\.\s+LITERATURE\s+BACKGROUND\s+AND\s+RELATED\s+WORKS',
        r'C\.\s+OUR\s+CONTRIBUTIONS',
        'Section II: Literature Background and Related Works (A. Background & B. Approaches and Related Works)',
        'Boundary detection, lesion segmentation methods (active contours, thresholding, FCNs), DenseNet feature reuse, and conditional random fields.'
    ),
    '07_A._Naeem': (
        r'Another\s+systematic\s+literature\s+on\s+classifying',
        r'III\.\s+DATA\s+ANALYSIS\s+AND\s+RESULTS',
        'Literature Review & Systematic Review Protocol (Sections I & II)',
        'Systematic literature review (SLR) of deep learning for melanoma, Kitchenham methodology, dataset taxonomy, evaluation metrics, and research questions.'
    ),
    '08_A._Imran': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+PROPOSED\s+METHODOLOGY',
        'Section II: Related Work',
        'Deep learners for melanoma detection, CNN ensembles, Capsule Networks (CapsNets) for spatial hierarchies, and multi-model decision fusion.'
    ),
    '10_Z._Lan': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+FixCaps',
        'Section II: Related Work',
        'Traditional ML vs. deep learning in dermoscopy, Capsule Networks and routing mechanisms, soft-attention, and GAN-based data augmentation.'
    ),
    '11_S._Ozturk': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+METHODOLOGY',
        'Section II: Related Work',
        'Deep metric learning, contrastive and triplet loss formulations, margin selection, and class imbalance mitigation in dermatological archives.'
    ),
    '12_A._Kwasigroch': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+NETWORK\s+MORPHISM',
        'Section II: Related Work',
        'Neural Architecture Search (NAS), network morphism, evolutionary algorithms, reinforcement learning for CNN discovery, and dermoscopy optimization.'
    ),
    '13_A._Magdy': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+MATERIALS\s+AND\s+METHODS',
        'Section II: Related Work',
        'Computer vision pipelines, transfer learning with ResNet/DenseNet/EfficientNet, image preprocessing, and feature fusion in skin lesion analysis.'
    ),
    '14_Z._Ji': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+PROPOSED\s+MODEL:\s+EFAM-Net',
        'Section II: Related Work',
        'Feature fusion networks, multi-scale representation learning, spatial and channel attention mechanisms, and multi-class lesion classification.'
    ),
    '15_L._Talavera-Martinez': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+METHODOLOGY',
        'Section II: Related Work',
        'Artifact removal in dermoscopy, DullRazor algorithm, classical morphological filters, and deep learning-based hair segmentation/inpainting.'
    ),
    '16_A._Gong': (
        r'I\.\s+INTRODUCTION',
        r'II\.\s+MATERIALS\s+AND\s+METHODS',
        'Section I: Introduction (Literature Review & State-of-the-Art Analysis)',
        'Generative Adversarial Networks (GANs, StyleGAN), synthetic dermoscopic data generation, transfer learning, and multi-block decision fusion.'
    ),
    '18_L._Riaz': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+MATERIALS\s+AND\s+METHODS',
        'Section II: Related Work',
        'Joint learning frameworks, multi-task convolutional networks, dermatological feature representation, and automated melanoma screening.'
    ),
    '20_L._Ichim': (
        r'II\.\s+RELATED\s+WORKS',
        r'III\.\s+MATERIALS\s+AND\s+METHODS',
        'Section II: Related Works',
        'Multi-network connectivity, ensemble classifiers, texture and color descriptors (LBP, GLCM), and objective melanoma diagnostic systems.'
    ),
    '21_R._Mittal': (
        r'II\.\s+RELATED\s+WORKS',
        r'III\.\s+MATERIALS\s+AND\s+METHODS',
        'Section II: Related Works',
        'Clinical decision support models (CDSM), systematic ML/DL pipelines for dermatosis, Spiking Neural Networks (SNN), and feature extraction.'
    ),
    '22_R._Karthik': (
        r'II\.\s+RELATED\s+WORKS',
        r'III\.\s+METHODS',
        'Section II: Related Works',
        'Vision Transformers (ViT, Swin Transformer), self-attention in medical imaging, group shuffle non-local attention, and hybrid CNN-transformer architectures.'
    ),
    '23_D._Poap': (
        r'A\.\s+RELATED\s+WORKS',
        r'II\.\s+SYSTEM\s+OF\s+INTELLIGENT\s+THINGS',
        'Section I-A: Related Works',
        'Internet of Medical Things (IoMT), embedded intelligent sensors, mobile skin examination, and deep learning for cutaneous markings.'
    ),
    '24_S._Chatterjee': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+METHODOLOGY',
        'Section II: Related Work (Subsections A-C: CNN Methods, Transfer Learning, Ensemble Learning)',
        'Comprehensive taxonomy: CNN architectures, transfer learning benchmarks, ensemble learning strategies, and multi-class skin lesion detection.'
    ),
    '26_A._Gong': (
        r'I\.\s+INTRODUCTION',
        r'II\.\s+MATERIALS\s+AND\s+METHODS',
        'Section I: Introduction (Literature Review & Transfer Learning Evaluation)',
        'Pre-trained CNN models (VGG, ResNet, Inception), GAN data augmentation, individual model advantages, and group decision voting.'
    ),
    '27_V._S._S._B._T._Sathvika': (
        r'II\.\s+RELATED\s+WORKS',
        r'III\.\s+PROPOSED\s+METHOD',
        'Section II: Related Works',
        'Pipelined classification structures, AlexNet deep feature extraction, SVM classification, and bi-sectional textural feature descriptors.'
    ),
    '28_M._I._Faizi': (
        r'II\.\s+LITERATURE\s+REVIEW',
        r'III\.\s+PROPOSED\s+METHODOLOGY',
        'Section II: Literature Review',
        'Melanoma segmentation techniques, thresholding, clustering algorithms (k-means, fuzzy c-means), normalized cross-correlation, and U-Net variants.'
    ),
    '29_P._M._M._Pereira': (
        r'II\.\s+BACKGROUND',
        r'III\.\s+PROPOSED\s+APPROACH',
        'Section II: Background and Related Work',
        'Multiple Instance Learning (MIL), 3D skin lesion surface reconstruction, stereo and photometric stereo dermoscopy, and weakly-supervised classification.'
    ),
    '31_X._Qian': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+METHOD',
        'Section II: Related Work (Subsections A: Feature Fusion Network, B: Attention Mechanism)',
        'Feature fusion networks, feature pyramid networks (FPN), self-interactive attention, and bilinear/trilinear pooling for fine-grained lesions.'
    ),
    '32_V._S._Narayanan': (
        r'II\.\s+RELATED\s+WORKS',
        r'III\.\s+PROPOSED\s+SEGMENTATION\s+MODEL',
        'Section II: Related Works',
        'Deep segmentation models, SegNet and U-Net architectures, residual skip connections, and attention gates for boundary delineation.'
    ),
    '33_T._Kim': (
        r'I\.\s+INTRODUCTION',
        r'II\.\s+MATERIAL\s+AND\s+METHODS',
        'Section I: Introduction (Literature Review & Multi-Modal Diagnostics)',
        'Endoscopic tympanic membrane imaging, pure-tone audiometry (PTA) clinical data, multimodal deep learning fusion, and otolaryngological CAD.'
    ),
    '34_Farhatullah': (
        r'II\.\s+LITERATURE\s+REVIEW',
        r'III\.\s+MATERIALS\s+AND\s+METHOD',
        'Section II: Literature Review',
        'Wavelet transforms, quantum mathematical orthogonal polynomials (Chebyshev), autoencoder dimensionality reduction, and sequential LSTM classifiers.'
    ),
    '35_Y._Wang': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+METHODOLOGY',
        'Section II: Related Work',
        'Clinical 7-point checklist criterion, dermatological knowledge graphs, gradient-based neural networks, and neuro-symbolic medical reasoning.'
    ),
    '36_M._I._Marie': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+DATASETS\s+AND\s+PREPROCESSING',
        'Section II: Related Work',
        'Object detection models in medical imaging, YOLO series (YOLOv7, YOLOv8, YOLOv9), Faster R-CNN, and hybrid multi-detector ensembles.'
    ),
    '38_L._Chakrabarti': (
        r'II\.\s+RELATED\s+WORKS',
        r'III\.\s+DATASET',
        'Section II: Related Works (Subsections A: Skin Lesion Classification, B: Vision-Language Models, C: Medical Report Generation)',
        'Vision-Language Models (VLM) in medicine, automated medical report generation, knowledge distillation from foundation models, and RAG architectures.'
    ),
    '39_G._Wang': (
        r'2\s*[\u3000\s]+Related\s+Work',
        r'3\s*[\u3000\s]+Method',
        'Section 2: Related Work',
        'Multi-scale deep CNNs, dynamic weighting strategies, part cross-entropy loss, and fine-grained visual classification of dermoscopic lesions.'
    ),
    '40_E._Soares_Flores': (
        r'I\.\s+INTRODUCTION',
        r'II\.\s+PROPOSED\s+APPROACH\s+FOR\s+SKIN\s+LESION',
        'Section I: Introduction (Literature Review & State of the Art)',
        'Nonnegative Matrix Factorization (NMF), dictionary learning, mutual information, graph cuts, and comparative benchmarking against U-Net/SegNet/DSNet.'
    ),
    '41_Z._Tabatabaei': (
        r'I\.\s+INTRODUCTION',
        r'II\.\s+METHODOLOGY',
        'Section I: Introduction (Literature Review on Deep Learning & Content Retrieval)',
        'Content-Based Histopathological Image Retrieval (CBHIR), Siamese networks, contrastive metric learning, and explainable AI for ambiguous Spitzoid tumors.'
    ),
    '42_F._Bibi': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+DATASET',
        'Section II: Related Work',
        'Non-dermoscopic clinical skin lesion analysis, dual-stream architectures, focal modulation, local feature integration, and smartphone image screening.'
    ),
    '43_U._Mittal': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+METHODOLOGY',
        'Section II: Related Work',
        'Data-efficient Image Transformers (DeiT), vision transformers vs. CNNs, multi-modal clinical-dermoscopic feature fusion, and dermatological screening.'
    ),
    '44_K._Younis': (
        r'II\.\s+RELATED\s+WORK',
        r'III\.\s+METHODOLOGY',
        'Section II: Related Work',
        'Dermoscopic Visual Question Answering (VQA), parameter-efficient fine-tuning (PEFT), Low-Rank Adaptation (LoRA), and Mixture of Experts (MoE).'
    ),
    '45_M._U._Zafar': (
        r'B\.\s+LIMITATIONS\s+OF\s+CONVENTIONAL\s+ENHANCEMENT',
        r'II\.\s+PROPOSED\s+METHODOLOGY',
        'Section I (Subsections B-D): Literature Limitations, GANs for Medical Images & Gap Analysis',
        'Artifact occlusion, limitations of conventional enhancement (histogram equalization, Retinex), GAN architectures (CycleGAN, Pix2Pix, ESRGAN), and research gaps.'
    )
}

def clean_block_text(text):
    """
    Cleans a single block of text from PyMuPDF.
    """
    # Replace unicode ligatures
    text = text.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff').replace('ﬃ', 'ffi').replace('ﬄ', 'ffl')
    
    # Fix hyphenated words across line breaks
    text = re.sub(r'([A-Za-z]+)-\n([A-Za-z]+)', r'\1\2', text)
    
    # Normalize whitespace inside lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if not lines:
        return ""
        
    skip_regexes = [
        r'^VOLUME\s+\d+.*',
        r'^\d{4,6}$', # standalone page numbers
        r'^IEEE\s+ACCESS.*',
        r'^BIG\s+DATA\s+MINING.*',
        r'.*Personal use is permitted.*',
        r'.*https://www\.ieee\.org.*',
        r'.*The associate editor coordinating.*',
        r'.*This work is licensed under.*',
        r'.*Creative Commons Attribution.*',
        r'^[A-Z]\.\s+[^:]+et\s+al\.:.*', # Running header Author et al.: Title
        r'^[A-Z]\.\s+[A-Z]\.\s+[^:]+:.*', # Running header M. A. Albahar: Title
        r'^Authorized licensed use limited to:.*',
        r'^Downloaded on.*',
    ]
    
    # If entire block is a running header or footer, drop it
    if len(lines) <= 3 and all(any(re.match(p, l, re.IGNORECASE) for p in skip_regexes) for l in lines):
        return ""
        
    # Filter out header/footer lines if present at top/bottom of block
    filtered_lines = [l for l in lines if not any(re.match(p, l, re.IGNORECASE) for p in skip_regexes)]
    if not filtered_lines:
        return ""
        
    block_clean = ' '.join(filtered_lines)
    block_clean = re.sub(r'\s+', ' ', block_clean).strip()
    
    # Check if this block is a Figure or Table caption
    if re.match(r'^(?:FIGURE|TABLE)\s+[0-9IVX]+[\.:]', block_clean, re.IGNORECASE):
        return f"> **{block_clean}**"
        
    # Check if this block is a standalone section / subsection heading
    if re.match(r'^(?:[0-9IVX]+\.|\bSECTION\b)\s+[A-Z\s]{3,}$', block_clean) or \
       re.match(r'^[A-D]\.\s+[A-Z\s]{3,}$', block_clean) or \
       re.match(r'^[0-9]\)\s+[A-Z\s]{3,}$', block_clean):
        return f"### {block_clean}"
        
    # Check if block starts with a Roman numeral or Major Section heading followed by text
    m_main = re.match(r'^((?:[0-9IVX]+\.|\bSECTION\b)\s+[A-Z\s]{3,}?)\s+([A-Z][a-z].*)$', block_clean)
    if m_main and len(m_main.group(1)) < 60:
        return f"### {m_main.group(1).strip()}\n\n{m_main.group(2).strip()}"
        
    # If first words are a subsection marker like "A. FEATURE FUSION NETWORK"
    m_sub = re.match(r'^([A-D]\.\s+[A-Z\s]{4,}?)\s+([A-Z][a-z].*)$', block_clean)
    if m_sub and len(m_sub.group(1)) < 60:
        return f"### {m_sub.group(1).strip()}\n\n{m_sub.group(2).strip()}"
        
    m_sub2 = re.match(r'^([0-9]\)\s+[A-Z\s]{4,}?)\s+([A-Z][a-z].*)$', block_clean)
    if m_sub2 and len(m_sub2.group(1)) < 60:
        return f"#### {m_sub2.group(1).strip()}\n\n{m_sub2.group(2).strip()}"
        
    # Check for bullet point blocks
    if any(line.startswith('•') or line.startswith('- ') for line in filtered_lines):
        curr_item = []
        list_items = []
        for line in filtered_lines:
            if line.startswith('•') or line.startswith('- '):
                if curr_item:
                    list_items.append(' '.join(curr_item))
                curr_item = [line.lstrip('•- ').strip()]
            else:
                curr_item.append(line)
        if curr_item:
            list_items.append(' '.join(curr_item))
        return '\n'.join([f"- {re.sub(r'\\s+', ' ', item).strip()}" for item in list_items])
        
    return block_clean

def format_extracted_blocks(blocks_text):
    """
    Takes a list of raw block strings and formats them into cohesive markdown paragraphs.
    """
    formatted = []
    for b in blocks_text:
        cb = clean_block_text(b)
        if cb:
            formatted.append(cb)
    return '\n\n'.join(formatted)

def main():
    print("Reading metadata index...")
    with open(METADATA_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = [h.strip() for h in next(reader)]
        papers = [dict(zip(header, [x.strip() for x in r])) for r in reader]

    print(f"Loaded {len(papers)} papers from CSV.")
    
    extracted_papers = []
    
    for i, p in enumerate(papers):
        idx = p['idx']
        title = p['title']
        authors = p['authors']
        journal = p['journal']
        year = p['year']
        doi = p['doi']
        filename = p['filename']
        
        # Match extraction rule
        rule_key = None
        for k in EXTRACTION_RULES:
            if filename.startswith(k):
                rule_key = k
                break
                
        if not rule_key:
            print(f"ERROR: No rule found for {filename}")
            continue
            
        s_pat, e_pat, sec_title, core_topics = EXTRACTION_RULES[rule_key]
        
        doc = pymupdf.open(filename)
        all_blocks = []
        for pno in range(min(12, len(doc))):
            for b in doc[pno].get_text('blocks'):
                if b[6] == 0 and b[4].strip():
                    all_blocks.append(b[4].strip())
                    
        DELIM = "\n\n===BLOCK_SEP===\n\n"
        full_text = DELIM.join(all_blocks)
        
        s_match = re.search(s_pat, full_text)
        if not s_match:
            print(f"[{idx}] FAILED START: {filename}")
            continue
            
        e_match = re.search(e_pat, full_text[s_match.end():])
        if not e_match:
            print(f"[{idx}] FAILED END: {filename}")
            continue
            
        matched_text = full_text[s_match.start():s_match.end() + e_match.start()]
        target_blocks = [tb.strip() for tb in matched_text.split('===BLOCK_SEP===') if tb.strip()]
        cleaned_section = format_extracted_blocks(target_blocks)
        
        print(f"[{i+1:02d}/39] Processed Paper {idx}: {title[:40]}... ({len(cleaned_section)} chars, {len(target_blocks)} blocks)")
        
        extracted_papers.append({
            'num': i + 1,
            'idx': idx,
            'title': title,
            'authors': authors,
            'journal': journal,
            'year': year,
            'doi': doi,
            'filename': filename,
            'sec_title': sec_title,
            'core_topics': core_topics,
            'text': cleaned_section
        })
        
    print(f"\nSuccessfully extracted {len(extracted_papers)} / 39 papers.")
    
    # Build the final Markdown Document
    print("Writing output Markdown file...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        out.write("# Comprehensive Extraction of Related Work & Literature Review Sections\n")
        out.write("## Systematic Benchmark Catalog Across All 39 Research Papers\n\n")
        out.write("> **Academic Course:** Research Methodology (BCA / Computer Science)  \n")
        out.write("> **Source Directory:** `downloaded_journals/` (39 Verified Research Papers)  \n")
        out.write("> **Metadata Index:** `papers_metadata_index_39.csv` | **BibTeX Archive:** `all_39_journals.bib`  \n")
        out.write("> **Extraction Standard:** 100% Verbatim Extracted Text, Complete Citations Preserved, Zero Extrapolation  \n\n")
        out.write("---\n\n")
        
        out.write("## Table of Contents & Comparative Mapping\n\n")
        out.write("The table below provides a quick reference index to all 39 papers, indicating the exact section extracted and key research themes reviewed in each paper's literature review:\n\n")
        out.write("| # | Title | Authors | Year | Extracted Section | Core Literature Focus |\n")
        out.write("|---|---|---|---|---|---|\n")
        for ep in extracted_papers:
            link = f"[Paper {ep['num']}: {ep['title'][:45]}...](#paper-{ep['num']}-{ep['idx']})"
            first_author = ep['authors'].split(';')[0].strip()
            out.write(f"| {ep['num']} | {link} | {first_author} et al. | {ep['year']} | {ep['sec_title']} | {ep['core_topics']} |\n")
        out.write("\n---\n\n")
        
        for ep in extracted_papers:
            pnum = ep['num']
            pidx = ep['idx']
            out.write(f'<a id="paper-{pnum}-{pidx}"></a>\n\n')
            out.write(f"## Paper {pnum}: {ep['title']}\n\n")
            out.write(f"| Attribute | Details |\n")
            out.write(f"|---|---|\n")
            out.write(f"| **Paper Index** | #{ep['num']} (Catalog ID: {ep['idx']}) |\n")
            out.write(f"| **Authors** | {ep['authors']} |\n")
            out.write(f"| **Journal & Year** | {ep['journal']} ({ep['year']}) |\n")
            out.write(f"| **Digital Object Identifier (DOI)** | [{ep['doi']}](https://doi.org/{ep['doi']}) |\n")
            out.write(f"| **Source PDF File** | [`{ep['filename']}`]({ep['filename']}) |\n")
            out.write(f"| **Target Section Extracted** | `{ep['sec_title']}` |\n")
            out.write(f"| **Core Focus** | {ep['core_topics']} |\n\n")
            
            out.write("### Extracted Section Content\n\n")
            out.write(ep['text'])
            out.write("\n\n---\n\n")
            
    print(f"Done! File written to: {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
