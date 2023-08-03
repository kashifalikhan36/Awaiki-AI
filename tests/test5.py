# import collections
# import collections.abc
# import pptx

# def create_slide(heading, image_path, paragraph):
#     prs = pptx.Presentation()
#     slide = prs.slides.add_slide(prs.slide_layouts[0])

#     title_shape = slide.shapes.title
#     title_shape.text = heading

#     img_shape = slide.shapes.add_picture(image_path, left=100, top=100)
#     img_shape.height = 5 * pptx.util.Inches(1)

#     paragraph_shape = slide.shapes.placeholders[1]
#     paragraph_shape.text = paragraph

#     prs.save('C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\data\\my_presentation.pptx')

# if __name__ == '__main__':
#     create_slide('My Heading', 'C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\data\\image_1.jpg', 'This is my paragraph. It is 100 words long.')


from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

# def create_pdf(output_path, heading, image_path, paragraph):
#     doc = SimpleDocTemplate(output_path, pagesize=A4)

#     # Define styles for the heading and paragraph
#     styles = getSampleStyleSheet()
#     heading_style = styles['Title']
#     paragraph_style = ParagraphStyle('CustomParagraphStyle', parent=styles['Normal'], spaceAfter=0.3*inch)

#     # Prepare the story (content elements to be included in the PDF)
#     story = []

#     # Add the heading
#     heading_text = f"<b>{heading}</b>"
#     heading_paragraph = Paragraph(heading_text, heading_style)
#     story.append(heading_paragraph)

#     # Add the image
#     image = Image(image_path, width=6*inch, height=4*inch)
#     story.append(image)

#     # Add the paragraph
#     paragraph_text = "<br/>".join(paragraph.split("\n"))  # Convert newlines to HTML line breaks
#     paragraph = Paragraph(paragraph_text, paragraph_style)
#     story.append(paragraph)

#     # Build the PDF document
#     doc.build(story)

# if __name__ == "__main__":
#     output_path = "C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\data\\output.pdf"
#     heading = "My Heading"
#     image_path = "C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\data\\image_1.jpg"
#     paragraph = """
#         This is a sample paragraph.
#         It can have multiple lines and
#         will be added to the PDF document.
#     """
#     create_pdf(output_path, heading, image_path, paragraph)


def create_pdf(output_path, heading, image_path, paragraph):
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

if __name__ == "__main__":
    output_path = "C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\data\\output.pdf"
    heading = "My Heading"
    image_path = "C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\data\\image_1.jpg"
    paragraph = """
        This is a sample paragraph.
        It can have multiple lines and
        will be added to the PDF document.
    """

    create_pdf(output_path, heading, image_path, paragraph)
