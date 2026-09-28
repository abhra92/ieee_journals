"""
generate_study_documents.py
Master Python automation script to generate:
1. Research_Methodology_RQs_39_Papers.docx (Executive Word Document)
2. latex_research_methodology/ (Modular LaTeX project compiled to main.pdf)
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

print(f"Loaded {len(PAPERS)} detailed paper records.")

# Helper for docx table cell background
def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

# Helper for docx cell margins/padding
def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

print("Helper functions initialized.")
