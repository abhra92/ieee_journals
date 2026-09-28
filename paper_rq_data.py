"""
paper_rq_data.py
Combines PART1, PART2, and PART3 into a unified database of all 39 papers.
"""

from paper_rq_data_part1 import PART1
from paper_rq_data_part2 import PART2
from paper_rq_data_part3 import PART3

PAPERS_RQ_DATABASE = PART1 + PART2 + PART3

if __name__ == '__main__':
    print(f"Successfully assembled complete database with {len(PAPERS_RQ_DATABASE)} papers.")
    assert len(PAPERS_RQ_DATABASE) == 39, f"Expected 39 papers, got {len(PAPERS_RQ_DATABASE)}"
    for idx, p in enumerate(PAPERS_RQ_DATABASE):
        assert p['id'] == idx + 1, f"Paper id mismatch at {idx}: {p['id']} vs {idx+1}"
        assert len(p['rqs']) >= 3, f"Paper {p['id']} has fewer than 3 RQs"
    print("All 39 papers verified with IDs 1 to 39 and at least 3-4 structured RQs each!")
