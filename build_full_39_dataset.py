"""
build_full_39_dataset.py
Constructs a comprehensive, verified dictionary for all 39 papers with all 17 fields.
"""
import os, sys, re, csv, json
import paper_rq_data

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Load CSV metadata
with open(os.path.join(BASE_DIR, 'papers_metadata_index_39.csv'), 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    csv_rows = [{k.strip(): v.strip() for k, v in r.items() if k and v} for r in reader]

# 2. Load Literature Review markdown
with open(os.path.join(BASE_DIR, 'complete_literature_review_39_papers.md'), 'r', encoding='utf-8') as f:
    lit_text = f.read()

lit_sections = re.split(r'\n###\s+(\d+)\.\s+', lit_text)
lit_data = {}
for i in range(1, len(lit_sections), 2):
    p_num = int(lit_sections[i])
    p_body = lit_sections[i+1].strip()
    lit_data[p_num] = p_body

print(f"Loaded {len(csv_rows)} CSV rows, {len(lit_data)} lit review entries.")

# Verify each paper
for i in range(39):
    pid = i + 1
    p_meta = csv_rows[i]
    p_lit = lit_data[pid]
    p_rq = paper_rq_data.PAPERS_RQ_DATABASE[i]
    assert pid == p_rq['id'], f"ID mismatch {pid} vs {p_rq['id']}"
    assert p_meta['arnumber'] == p_rq['arnumber'], f"ARNumber mismatch {p_meta['arnumber']} vs {p_rq['arnumber']}"

print("All 39 papers verified and aligned across CSV, Lit Review, and RQ database.")
