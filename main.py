from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


def add_lines():
    y = 21
    for _ in range(0, 26):
        pdf.line(x1=10, y1=y, x2=200, y2=y)
        y = y + 10


is_lined = False
user_input = input("Do you want a lined PDF: y/n ")
if user_input == "y":
    is_lined = True
else:
    is_lined = False

for index, row in df.iterrows():
    pdf.set_font(family="Times", size=12)
    pdf.set_text_color(80, 80, 80)
    pdf.add_page()
    if is_lined:
        add_lines()
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    # Set footer
    pdf.ln(265)
    pdf.set_font(family="Times", size=8)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)
    for num in range(1, row["Pages"]):
        pdf.add_page()
        if is_lined:
            add_lines()
        # Set footer
        pdf.ln(277)
        pdf.set_font(family="Times", size=8)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("test.pdf")
