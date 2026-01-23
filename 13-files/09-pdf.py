from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", size = 14)

pdf.cell(200, 10, txt="Hello world in PDF", ln=True, align='C')
pdf.cell(200, 10, txt="Python Generated PDF!", ln=True, align='C')

pdf.output('pdf_file.pdf')