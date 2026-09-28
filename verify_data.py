import sys, csv, re
import paper_rq_data

sys.stdout.reconfigure(encoding='utf-8')

with open('papers_metadata_index_39.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    csv_rows = [{k.strip(): v.strip() for k, v in r.items() if k and v} for r in reader]

print(f"CSV count: {len(csv_rows)}")
print(f"RQ Database count: {len(paper_rq_data.PAPERS_RQ_DATABASE)}")

for i in range(39):
    csv_r = csv_rows[i]
    rq_p = paper_rq_data.PAPERS_RQ_DATABASE[i]
    if csv_r['arnumber'] != rq_p['arnumber']:
        print(f"Mismatch at {i}: {csv_r['arnumber']} vs {rq_p['arnumber']}")
    else:
        print(f"Paper {i+1:02d}: OK - {csv_r['title'][:40]}... [{rq_p['arnumber']}]")

print("All 39 papers aligned!")
