"""
sanitize_bib.py
Replaces non-ASCII accented characters in references.bib with standard LaTeX macros
so that legacy 8-bit BibTeX does not truncate multibyte sequences.
"""

replacements = {
    'Ş': r'{\c{S}}', 'ş': r'{\c{s}}',
    'Ö': r'{\"O}', 'ö': r'{\"o}',
    'Ç': r'{\c{C}}', 'ç': r'{\c{c}}',
    'ü': r'{\"u}', 'Ü': r'{\"U}',
    'ł': r'{\l}', 'Ł': r'{\L}',
    'ń': r'{\'n}', 'Ń': r'{\'N}',
    'í': r'{\'i}', 'Í': r'{\'I}',
    'á': r'{\'a}', 'Á': r'{\'A}',
    'é': r'{\'e}', 'É': r'{\'E}',
    'ã': r'{\~a}', 'Ã': r'{\~A}',
    'ó': r'{\'o}', 'Ó': r'{\'O}',
    'ú': r'{\'u}', 'Ú': r'{\'U}',
    'à': r'{\`a}', 'è': r'{\`e}',
    '–': '--', '—': '---',
    '“': '``', '”': "''",
}

with open('latex_research_questions/references.bib', 'r', encoding='utf-8') as f:
    text = f.read()

for k, v in replacements.items():
    text = text.replace(k, v)

with open('latex_research_questions/references.bib', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully sanitized references.bib with standard LaTeX diacritics.")
