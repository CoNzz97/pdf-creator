from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.set_font(family="Times", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.add_page()
    page_order = row["Order"]
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    for num in range(0, row["Pages"]):
        pdf.add_page()
pdf.output("test.pdf")


