"""
build_full_39_database.py
Generates the authoritative, evidence-bound 17-field database for all 39 papers in downloaded_journals/
"""
import os, sys, re, csv, json

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load CSV metadata
with open(os.path.join(BASE_DIR, 'papers_metadata_index_39.csv'), 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    csv_rows = [{k.strip(): v.strip() for k, v in r.items() if k and v} for r in reader]

print(f"Loaded {len(csv_rows)} CSV metadata records.")
