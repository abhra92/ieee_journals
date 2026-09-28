@echo off
echo ========================================================
echo Compiling Comprehensive Research Questions LaTeX Project
echo ========================================================
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
echo ========================================================
echo Compilation Finished! Check main.pdf.
echo ========================================================
pause
