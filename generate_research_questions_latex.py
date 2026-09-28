"""
generate_research_questions_latex.py
Generates a complete, modular, publication-quality LaTeX catalog and companion Markdown 
document of Research Questions across all 39 papers in downloaded_journals/.
"""

import os, sys, re, csv

sys.stdout.reconfigure(encoding='utf-8')

BASE_OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'latex_research_questions')
PAPERS_DIR = os.path.join(BASE_OUTPUT_DIR, 'papers')
SECTIONS_DIR = os.path.join(BASE_OUTPUT_DIR, 'sections')

os.makedirs(PAPERS_DIR, exist_ok=True)
os.makedirs(SECTIONS_DIR, exist_ok=True)

# Load CSV metadata
with open('papers_metadata_index_39.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    csv_rows = [{k.strip(): v.strip() for k, v in r.items() if k and v} for r in reader]

# Load complete literature review markdown
with open('complete_literature_review_39_papers.md', 'r', encoding='utf-8') as f:
    lit_text = f.read()

lit_sections = re.split(r'\n###\s+(\d+)\.\s+', lit_text)
lit_data = {}
for i in range(1, len(lit_sections), 2):
    p_num = int(lit_sections[i])
    p_body = lit_sections[i+1].strip()
    lines = p_body.split('\n')
    title = lines[0].strip()
    authors_line = lines[1].replace('**Authors:**', '').strip() if len(lines) > 1 else ''
    affil_line = lines[2].replace('**Affiliation:**', '').strip() if len(lines) > 2 else ''
    citation_line = lines[3].strip() if len(lines) > 3 else ''
    summary = lines[5].strip() if len(lines) > 5 else ''
    lit_data[p_num] = {
        'title': title,
        'authors': authors_line,
        'affiliation': affil_line,
        'citation': citation_line,
        'summary': summary
    }

print(f"Loaded {len(csv_rows)} CSV entries and {len(lit_data)} Literature Review summaries.")
