from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.colors import HexColor
from io import BytesIO
import os
from django.conf import settings

def generate_student_report(student, grades):
    buffer = BytesIO()
    # Create custom styles
    styles = getSampleStyleSheet()
    
    # Custom document with margins matching website padding
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#2c3e50'),
        spaceAfter=30,
        alignment=1  # Center alignment
    )
    
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=HexColor('#2c3e50'),
        spaceAfter=5
    )
    
    info_style = ParagraphStyle(
        'InfoStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#2c3e50'),
        spaceAfter=3
    )
    
    story = []

    # Title
    story.append(Paragraph("Student Report Card", title_style))
    
    # Add student image if available
    if student.Student_image:
        try:
            # For production environment
            if hasattr(student.Student_image, 'url'):
                # Try to get the physical path first
                img_path = student.Student_image.path
                if not os.path.exists(img_path) and hasattr(student.Student_image, 'file'):
                    # If physical path doesn't exist, try to read from storage
                    img_data = BytesIO(student.Student_image.file.read())
                    img = Image(img_data, width=2*inch, height=2*inch)
                else:
                    img = Image(img_path, width=2*inch, height=2*inch)
                img.hAlign = 'CENTER'
                story.append(img)
                story.append(Spacer(1, 20))
        except Exception as e:
            # Silently handle the error and continue without the image
            pass

    # Student Information in a more structured format
    story.append(Paragraph("<b>Student Information</b>", header_style))
    story.append(Paragraph(f"<b>Name:</b> {student.Name}", info_style))
    story.append(Paragraph(f"<b>Student ID:</b> {student.id}", info_style))
    story.append(Paragraph(f"<b>Grade Level:</b> {student.Grade}", info_style))
    story.append(Spacer(1, 20))

    # Academic Performance Header
    story.append(Paragraph("<b>Academic Performance</b>", header_style))
    story.append(Spacer(1, 10))

    # Subject Marks Table with modern styling
    data = [
        ['Subject', 'Marks (/100)', 'Grade'],
        ['Science', str(student.SCI), grades.SCI_GRADE],
        ['Social Studies', str(student.SST), grades.SST_GRADE],
        ['Mathematics', str(student.MTC), grades.MTC_GRADE],
        ['English', str(student.ENG), grades.ENG_GRADE],
        ['Total', str(student.TOTAL), ''],
        ['Aggregates', str(student.AGG), ''],
    ]

    # Calculate column widths based on A4 page size
    available_width = A4[0] - 4*cm  # Total width minus margins
    col_widths = [available_width*0.5, available_width*0.25, available_width*0.25]
    
    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        # Header row styling
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#4a90e2')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        
        # Table body styling
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), HexColor('#2c3e50')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 10),
        
        # Total row styling
        ('BACKGROUND', (0, -1), (-1, -1), HexColor('#f8f9fa')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        
        # Grid styling
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#e1e1e1')),
        ('BOX', (0, 0), (-1, -1), 2, HexColor('#4a90e2')),
        
        # Alternate row colors for better readability
        ('BACKGROUND', (0, 1), (-1, 1), HexColor('#f8f9fa')),
        ('BACKGROUND', (0, 3), (-1, 3), HexColor('#f8f9fa')),
        ('BACKGROUND', (0, 5), (-1, 5), HexColor('#f8f9fa')),
    ]))
    story.append(table)

    # Add footer with date
    story.append(Spacer(1, 30))
    footer_style = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontSize=8,
        textColor=HexColor('#666666'),
        alignment=1  # Center alignment
    )
    from django.utils import timezone
    story.append(Paragraph(f"Generated on {timezone.now().strftime('%B %d, %Y at %I:%M %p')}", footer_style))
    
    # Build PDF with a clean white background
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf