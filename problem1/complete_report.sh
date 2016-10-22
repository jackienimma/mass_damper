#! bin/bash script
python mass_damper.py
pdflatex mass_damper.tex
bibtex mass_damper
pdflatex mass_damper.tex
pdflatex mass_damper.tex
evince mass_damper.pdf
