from fpdf import FPDF;
import fpdf;

class PDF(FPDF):
    def header(self):
        self.set_font("Times", "B", 24); #bolded and size 24
        self.set_auto_page_break(False);
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.set_text_color(0,0,0); #black
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)

def main():
    name=input("Name: ");
    pdf=PDF(orientation="P", format="A4");
    pdf.add_page();
    pdf.image("shirtificate.png", x=fpdf.Align.C, w=150, h=200); #w is x and h is y
    pdf.set_text_color(255,255,255); #white
    pdf.cell(text=name+" took CS50", w=175, h=-300, align=fpdf.Align.C);
    pdf.output("shirtificate.pdf");

if __name__ == "__main__":
    main();
