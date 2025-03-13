import webbrowser
from fpdf import FPDF
from flatmate import Flatmate
from bill import Bill


class PDFReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_one, flatmate_two, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("./assets/house.png", w=30, h=30)

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h= 40, txt='Period', border=1)
        pdf.cell(w=150, h=40, txt="March 2025", border=1, ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt=flatmate_one.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate_one.pays(bill, flatmate_two), 2)), border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate_two.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate_two.pays(bill, flatmate_one), 2)), border=1, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
