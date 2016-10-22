#! bin/bash script
python mass_damper.py
pdflatex mass_damper.tex
bibtex mass_damper
pdflatex mass_damper.tex
pdflatex mass_damper.tex
rm *.aux *.bbl *.blg *.log
mv mass_damper.pdf ../output/153010009.pdf
evince ../output/mass_damper.pdf
