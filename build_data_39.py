"""
build_data_39.py
Extracts and validates the 17 fields for all 39 papers.
"""
import sys, os, re, csv, json
import paper_rq_data

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Load CSV
with open(os.path.join(BASE_DIR, 'papers_metadata_index_39.csv'), 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    csv_rows = [{k.strip(): v.strip() for k, v in r.items() if k and v} for r in reader]

# 2. Load Literature Review Markdown
with open(os.path.join(BASE_DIR, 'complete_literature_review_39_papers.md'), 'r', encoding='utf-8') as f:
    lit_text = f.read()

lit_sections = re.split(r'\n###\s+(\d+)\.\s+', lit_text)
lit_data = {}
for i in range(1, len(lit_sections), 2):
    p_num = int(lit_sections[i])
    p_body = lit_sections[i+1].strip()
    lit_data[p_num] = p_body

print(f"Loaded {len(csv_rows)} CSV rows, {len(lit_data)} lit review entries, {len(paper_rq_data.PAPERS_RQ_DATABASE)} RQ database entries.")

# Let's inspect sample fields
sample = paper_rq_data.PAPERS_RQ_DATABASE[0]
print("Sample RQ database item keys:", sample.keys())
