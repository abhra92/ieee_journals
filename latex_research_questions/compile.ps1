# PowerShell compilation script for Research Questions LaTeX project
Write-Host "Compiling Comprehensive Research Questions LaTeX Project..." -ForegroundColor Cyan
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
if ($LASTEXITCODE -eq 0) {
    Write-Host "SUCCESS! main.pdf generated successfully." -ForegroundColor Green
} else {
    Write-Host "Compilation completed with warnings or errors. Check main.log." -ForegroundColor Yellow
}
