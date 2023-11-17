from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.name = input("Name: ")
        self.configure_shirt()

    def configure_shirt(self):
        self.add_page()
        self.set_font("helvetica", "B", 50)
        self.cell(0, 60, "CS50 Shirtificate", align = "c")
        self.image("./shirtificate.png", x = 0, y = 70)
        self.set_font_size(30)
        self.set_text_color(255, 255, 255)
        self.text(x = 47.5, y = 140, txt = f"{self.name} took CS50")


def main():
    pdf = PDF()
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
