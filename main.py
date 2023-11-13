from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("Text+Files/*.txt")

pdf = FPDF(orientation='P',unit='mm',format='A4')

for filepath in filepaths:
    filename = Path(filepath).stem
    pdf.add_page()

    pdf.set_font('Times', style='B', size=18)
    pdf.cell(w=50,h=10,txt=filename.title(),align='l',ln=1)

    with open(filepath,'r') as file:
        content = file.read()

    pdf.set_font('Times', size=12)
    pdf.multi_cell(w=0,h=8,txt=content)

pdf.output("output.pdf")