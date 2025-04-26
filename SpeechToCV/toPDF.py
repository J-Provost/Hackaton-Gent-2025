from fpdf import FPDF
import markdown2

# pip install git+https://github.com/PyFPDF/fpdf2.git@master
# pip install markdown2


# Read the Markdown file
def toPDF(markdown_file):
<<<<<<< HEAD
    # with open("Hackaton-Gent-2025/SpeechToCV/result.md", "r", encoding="utf-8") as md_file:
    #     markdown_content = md_file.read()

    # Convert Markdown to plain text (strip HTML tags)
    plain_text = markdown2.markdown(markdown_file, extras=["strip"])
=======
    # Convert Markdown to plain text (strip HTML tags)
    html_content = markdown2.markdown(markdown_file)
>>>>>>> f115d608a9754a8b1d911799ca0f0573be812c94

    # Create a PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
<<<<<<< HEAD
=======
    pdf.write_html(html_content)
>>>>>>> f115d608a9754a8b1d911799ca0f0573be812c94

    # Save the PDF
    pdf.output("SpeechToCV/response.pdf")

    print("PDF successfully created as 'response.pdf'")
