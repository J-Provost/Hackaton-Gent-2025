from fpdf import FPDF
import markdown2

# pip install git+https://github.com/PyFPDF/fpdf2.git@master
# pip install markdown2


# Read the Markdown file
def toPDF(markdown_file):
    # Convert Markdown to plain text (strip HTML tags)
    html_content = markdown2.markdown(markdown_file)

    # Create a PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write_html(html_content)

    # Save the PDF
    pdf.output("SpeechToCV/response.pdf")

    print("PDF successfully created as 'response.pdf'")
