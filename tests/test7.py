from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def create_pdf(heading, image_path, paragraph):
    # Define styles for the heading and paragraph
    styles = getSampleStyleSheet()
    center_alignment = 1  # 1 corresponds to center alignment

    heading_style = ParagraphStyle('h1', parent=styles['Title'], fontSize=20, alignment=center_alignment)
    paragraph_style = ParagraphStyle('CustomParagraphStyle', parent=styles['Normal'], fontSize=12, alignment=center_alignment)

    # Prepare the story (content elements to be included in the PDF)
    story = []

    # Add the heading
    heading_text = f"<b>{heading}</b>"
    heading_paragraph = Paragraph(heading_text, heading_style)
    story.append(heading_paragraph)

    # Add a spacer to center the image vertically
    story.append(Spacer(1, 0.5*inch))

    # Add the image with center alignment
    image = Image(image_path, width=6*inch, height=4*inch, hAlign=center_alignment)
    story.append(image)

    # Add a spacer to center the paragraph vertically
    story.append(Spacer(1, 0.5*inch))

    # Add the paragraph with center alignment
    paragraph_text = "<br/>".join(paragraph.split("\n"))  # Convert newlines to HTML line breaks
    paragraph = Paragraph(paragraph_text, paragraph_style)
    story.append(paragraph)

    return story

def append_to_pdf(input_pdf_path, output_pdf_path, heading, image_path, paragraph):
    # Create content for the new page
    new_page_content = create_pdf(heading, image_path, paragraph)

    # Load existing PDF and create a new PDF
    existing_pdf = PdfReader(input_pdf_path)
    new_pdf = PdfWriter()

    # Append the existing pages to the new PDF
    for page in existing_pdf.pages:
        new_pdf.add_page(page)

    # Create a new page and add the content to it
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    doc.build(new_page_content)

    # Add the new page to the new PDF
    buffer.seek(0)
    new_pdf.addPage(PdfReader(buffer).pages[0])

    # Save the final PDF
    with open(output_pdf_path, "wb") as output_file:
        new_pdf.write(output_file)

if __name__ == "__main__":
    input_pdf_path = "./data/output.pdf"
    output_pdf_path = "C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\ebook\\Mdified_output.pdf"
    heading = "My Heading"
    image_path = "./data/image_1.jpg"
    paragraph = """
        This is a sample paragraph.
        It can have multiple lines and
        will be added to the PDF document.
    """

    append_to_pdf(input_pdf_path, output_pdf_path, heading, image_path, paragraph)
