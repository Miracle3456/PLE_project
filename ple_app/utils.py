from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from io import BytesIO

def generate_student_report(student, grades):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    normal_style = styles['Normal']

    # Title
    story.append(Paragraph(f"Student Report Card", title_style))
    story.append(Spacer(1, 20))

    # Student Information
    story.append(Paragraph(f"Name: {student.Name}", normal_style))
    story.append(Paragraph(f"Student ID: {student.id}", normal_style))
    story.append(Paragraph(f"Grade: {student.Grade}", normal_style))
    story.append(Spacer(1, 20))

    # Subject Marks Table
    data = [
        ['Subject', 'Marks', 'Grade'],
        ['Science', str(student.SCI), grades.SCI_GRADE],
        ['Social Studies', str(student.SST), grades.SST_GRADE],
        ['Mathematics', str(student.MTC), grades.MTC_GRADE],
        ['English', str(student.ENG), grades.ENG_GRADE],
        ['Total', str(student.TOTAL), ''],
        ['Aggregates', str(student.AGG), ''],
    ]

    table = Table(data, colWidths=[2*inch, inch, inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
    ]))
    story.append(table)

    # Build PDF
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf