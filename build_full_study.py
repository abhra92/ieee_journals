"""
build_full_study.py
Generates:
1. Research_Methodology_RQs_39_Papers.docx
2. latex_research_methodology/main.tex and compiles it to main.pdf via pdflatex + bibtex
3. Verifies all 39 papers across all 10 steps.
"""
import os, sys, re, csv, json, subprocess
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load papers data
with open(os.path.join(BASE_DIR, 'papers_39_detailed.json'), 'r', encoding='utf-8') as f:
    PAPERS = json.load(f)

print(f"Loaded {len(PAPERS)} detailed papers.")
