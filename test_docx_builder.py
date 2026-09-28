"""
test_docx_builder.py
Tests creating the docx structure with python-docx.
"""
import os, sys, json
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# Set standard 1 inch margins
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Add title
title = doc.add_heading("Research Methodology: Systematic Analysis & Research Question Formulation from 39 Papers", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph("Domain: Skin Cancer Detection Using Deep Learning | Dataset: HAM10000 | BCA 7th-Semester")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.save("test_out.docx")
print("Saved test_out.docx successfully!")
