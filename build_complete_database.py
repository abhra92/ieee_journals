"""
build_complete_database.py
Compiles the comprehensive 17-field dataset for all 39 papers, ensuring 100% precision.
"""
import os, sys, re, csv, json
import paper_rq_data

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load CSV
with open(os.path.join(BASE_DIR, 'papers_metadata_index_39.csv'), 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    csv_rows = [{k.strip(): v.strip() for k, v in r.items() if k and v} for r in reader]

# Load Literature Review markdown
with open(os.path.join(BASE_DIR, 'complete_literature_review_39_papers.md'), 'r', encoding='utf-8') as f:
    lit_text = f.read()

lit_sections = re.split(r'\n###\s+(\d+)\.\s+', lit_text)
lit_summaries = {}
for i in range(1, len(lit_sections), 2):
    p_num = int(lit_sections[i])
    p_body = lit_sections[i+1].strip()
    lit_summaries[p_num] = p_body

print(f"Loaded {len(csv_rows)} CSV rows and {len(lit_summaries)} summaries.")
