from fpdf import FPDF
import markdown2

# pip install git+https://github.com/PyFPDF/fpdf2.git@master
# pip install markdown2


# Read the Markdown file
def toPDF(markdown_file):
    # with open("Hackaton-Gent-2025/SpeechToCV/result.md", "r", encoding="utf-8") as md_file:
    #     markdown_content = md_file.read()

    # Convert Markdown to plain text (strip HTML tags)
    plain_text = markdown2.markdown(markdown_file, extras=["strip"])

    # Create a PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.write_html(plain_text)
    pdf.set_font("Arial", size=12)


    # Save the PDF
    pdf.output("Hackaton-Gent-2025/SpeechToCV/response.pdf")

    print("PDF successfully created as 'response.pdf'")
