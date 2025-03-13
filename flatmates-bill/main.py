from bill import Bill
from flatmate import Flatmate
from pdf_report import PDFReport

if __name__ == '__main__':
    bill = Bill(amount=1200, period="March 2025")
    john = Flatmate(name="John", days_in_house=20)
    marry = Flatmate(name="Marry", days_in_house=25)

    print(john.pays(bill, marry))
    print(marry.pays(bill, john))

    pdf_report = PDFReport(filename="Report.pdf")
    pdf_report.generate(flatmate_one=john, flatmate_two=marry, bill=bill)

