from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from PyPDF2 import PdfReader, PdfWriter

class Ebook:
    def __init__(self):
        pass

    def create_pdf(self,output_path, heading, image_path, paragraph):
        doc = SimpleDocTemplate(output_path, pagesize=A4)

        # Define styles for the heading and paragraph
        styles = getSampleStyleSheet()
        heading_style = ParagraphStyle('h1', parent=styles['Title'], fontSize=20)
        paragraph_style = ParagraphStyle('CustomParagraphStyle', parent=styles['Normal'], fontSize=16,alignment=1)

        # Prepare the story (content elements to be included in the PDF)
        story = []

        # Add the heading
        heading_text = f"<b>{heading}</b>"
        heading_paragraph = Paragraph(heading_text, heading_style)
        story.append(heading_paragraph)

        # Add the image
        image = Image(image_path, width=6*inch, height=4*inch)
        story.append(image)

        # Add the paragraph
        paragraph_text = "<br/>".join(paragraph.split("\n"))  # Convert newlines to HTML line breaks
        paragraph = Paragraph(paragraph_text, paragraph_style)
        story.append(paragraph)

        # Build the PDF document
        doc.build(story)

    def append_pdf(self,input_pdf_path, output_pdf_path, heading, image_path, paragraph):
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
        # Create content for the new page
        new_page_content = create_pdf(heading, image_path, paragraph)

        # Load existing PDF and create a new PDF
        existing_pdf = PdfReader(input_pdf_path)
        new_pdf = PdfWriter()

        # Append the existing pages to the new PDF
        for page in existing_pdf.pages:
            new_pdf.add_page(page)

        # Create a new page and add the content to it
        new_page = SimpleDocTemplate("./data/temp.pdf", pagesize=A4)
        new_page.build(new_page_content)

        # Append the new page to the new PDF
        with open("./data/temp.pdf", "rb") as temp_file:
            temp_pdf = PdfReader(temp_file)
            for page in temp_pdf.pages:
                new_pdf.add_page(page)

        # Save the final PDF
        with open(output_pdf_path, "wb") as output_file:
            new_pdf.write(output_file)