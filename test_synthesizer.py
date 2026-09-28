"""
test_synthesizer.py
Tests synthesizing the 17 fields for papers from CSV, Lit Review, and RQ data.
"""
import os, sys, re, csv, json
import paper_rq_data

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'papers_metadata_index_39.csv'), 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    csv_rows = [{k.strip(): v.strip() for k, v in r.items() if k and v} for r in reader]

with open(os.path.join(BASE_DIR, 'complete_literature_review_39_papers.md'), 'r', encoding='utf-8') as f:
    lit_text = f.read()

lit_sections = re.split(r'\n###\s+(\d+)\.\s+', lit_text)
lit_summaries = {}
for i in range(1, len(lit_sections), 2):
    p_num = int(lit_sections[i])
    p_body = lit_sections[i+1].strip()
    lit_summaries[p_num] = p_body

print(f"Total papers in database: {len(paper_rq_data.PAPERS_RQ_DATABASE)}")

# Let's inspect paper 3 (Mridha et al., HAM10000)
p3_meta = csv_rows[2]
p3_lit = lit_summaries[3]
p3_rq = paper_rq_data.PAPERS_RQ_DATABASE[2]

print("Title:", p3_meta['title'])
print("Authors:", p3_meta['authors'])
print("Year:", p3_meta['year'])
print("Datasets:", p3_rq['datasets'])
print("Metrics:", p3_rq['metrics'])
print("Open questions:", p3_rq['open_questions'])
