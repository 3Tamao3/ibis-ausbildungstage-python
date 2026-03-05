import streamlit as st
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet

col1, col2, col3 = st.columns([1,4,1])

with col2:
    st.title("Ausbildungstagebuch")

col1, col2, col3, col4 = st.columns(4)

with col1:
    lehrlingName = st.text_input("Lehrling: ")

with col2:
    kalenderwoche = st.text_input("Kalenderwoche: ")

with col3:
    vomDatum = st.text_input("Vom: ")

with col4:
    bisDatum = st.text_input("Bis: ")

col1, col2 = st.columns(2)

with col1:
    gruppe = st.text_input("Gruppe: ")

with col2:
    trainer = st.text_input("Trainer/-in: ")

col1, col2, col3, col4 = st.columns([1, 1, 2, 1])

# Tätigkeiten und Bemerkungen #1
with col1:
    datum1 = st.text_input("Datum #1: ")
with col2:
    trainer1 = st.text_input("Trainer/-in #1: ")
with col3:
    tätigkeit1 = st.text_input("Tätigkeit #1: ")
with col4:
    bemerkungen1 = st.text_input("Bemerkungen #1: ")

# Tätigkeiten und Bemerkungen #2
with col1:
    datum2 = st.text_input("Datum #2: ")
with col2:
    trainer2 = st.text_input("Trainer/-in #2: ")
with col3:
    tätigkeit2 = st.text_input("Tätigkeit #2: ")
with col4:
    bemerkungen2 = st.text_input("Bemerkungen #2: ")

# Tätigkeiten und Bemerkungen #3
with col1:
    datum3 = st.text_input("Datum #3: ")
with col2:
    trainer3 = st.text_input("Trainer/-in #3: ")
with col3:
    tätigkeit3 = st.text_input("Tätigkeit #3: ")
with col4:
    bemerkungen3 =  st.text_input("Bemerkungen #3: ")

# Tätigkeiten und Bemerkungen #4
with col1:
    datum4 = st.text_input("Datum #4: ")
with col2:
    trainer4 = st.text_input("Trainer/-in #4: ")
with col3:
    tätigkeit4 = st.text_input("Tätigkeit #4: ")
with col4:
    bemerkungen4 = st.text_input("Bemerkungen #4: ")

# Tätigkeiten und Bemerkungen #5
with col1:
    datum5 = st.text_input("Datum #5: ")
with col2:
    trainer5 = st.text_input("Trainer/-in #5: ")
with col3:
    tätigkeit5 = st.text_input("Tätigkeit #5: ")
with col4:
    bemerkungen5 = st.text_input("Bemerkungen #5: ")

def createPDF(lehrlingName, kalenderwoche, vomDatum, bisDatum, gruppe, trainer, datum1, trainer1, tätigkeit1, bemerkungen1, datum2, trainer2, tätigkeit2, bemerkungen2, datum3, trainer3, tätigkeit3, bemerkungen3, datum4, trainer4, tätigkeit4, bemerkungen4, datum5, trainer5, tätigkeit5, bemerkungen5) -> bytes:
    """Creates a simple PDF in memory and returns its bytes."""
    buffer = BytesIO()

    c = canvas.Canvas(buffer, pagesize=landscape(A4))

    ausbildungstagebuchVorlage = ImageReader("imgs/ausbildungstagebuch_vorlage.png")

    c.drawImage(ausbildungstagebuchVorlage, 0, 0, width=landscape(A4)[0], height=landscape(A4)[1])

    c.setFont("Helvetica", 16)
    c.drawString(200, 800, "Ausbildungstagebuch")

    c.setFont("Helvetica", 12)

    styles = getSampleStyleSheet()
    style = styles["Normal"]

    #Liste(Index) Datum, Trainer, Tätigkeiten und Bemerkungen
    datum_texts = [
        Paragraph(datum1, style),
        Paragraph(datum2, style),
        Paragraph(datum3, style),
        Paragraph(datum4, style),
        Paragraph(datum5, style)
    ]

    trainer_texts = [
        Paragraph(trainer1, style),
        Paragraph(trainer2, style),
        Paragraph(trainer3, style),
        Paragraph(trainer4, style),
        Paragraph(trainer5, style)
    ]

    tätigkeit_texts = [
    Paragraph(tätigkeit1, style),
    Paragraph(tätigkeit2, style),
    Paragraph(tätigkeit3, style),
    Paragraph(tätigkeit4, style),
    Paragraph(tätigkeit5, style)
    ]

    bemerkung_texts = [
    Paragraph(bemerkungen1, style),
    Paragraph(bemerkungen2, style),
    Paragraph(bemerkungen3, style),
    Paragraph(bemerkungen4, style),
    Paragraph(bemerkungen5, style)
    ]

    tätigkeitFrame1 = Frame(
        165, 358,   # x, y position
        327, 62,    # width, height of the box
        showBoundary=1   # shows the box border (good for debugging)
    )

    tätigkeitFrame1.addFromList([tätigkeit_texts[0]], c)
"""
    c.drawString(72, 500, f"{lehrlingName}")
    c.drawString(220, 500, f"{kalenderwoche}")
    c.drawString(350, 500, f"{vomDatum}")
    c.drawString(480, 500, f"{bisDatum}")

    c.drawString(72, 470, f"{gruppe}")
    c.drawString(200, 470, f"{trainer}")

    #info: Datum - 72 und 410, Tätigkeiten - 200 und 410, Bemerkungen - 530 und 410

    c.drawString(72, 380, f"{datum1}")
    c.drawString(200, 380, f"{tätigkeit1}")
    c.drawString(530, 380, f"{bemerkungen1}")
    c.drawString(72, 360, f"{datum2}")
    c.drawString(200, 360, f"{tätigkeit2}")
    c.drawString(530, 360, f"{bemerkungen2}")
    c.drawString(72, 340, f"{datum3}")
    c.drawString(200, 340, f"{tätigkeit3}")
    c.drawString(520, 340, f"{bemerkungen3}")
    c.drawString(72, 320, f"{datum4}")
    c.drawString(200, 320, f"{tätigkeit4}")
    c.drawString(520, 320, f"{bemerkungen4}")
    c.drawString(72, 300, f"{datum5}")
    c.drawString(200, 300, f"{tätigkeit5}")
    c.drawString(520, 300, f"{bemerkungen5}")
"""
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer.read()

if st.button("Create PDF"):
    pdf_bytes = createPDF(lehrlingName, kalenderwoche, vomDatum, bisDatum, gruppe, trainer, datum1, trainer1, tätigkeit1, bemerkungen1, datum2, trainer2, tätigkeit2, bemerkungen2, datum3, trainer3, tätigkeit3, bemerkungen3, datum4, trainer4, tätigkeit4, bemerkungen4, datum5, trainer5, tätigkeit5, bemerkungen5)
    st.success("Successfully created PDF!")
    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name="Ausbildungstagebuch_" + lehrlingName + "_" + kalenderwoche + "_" + vomDatum + "-" + bisDatum + ".pdf",
        mime="application/pdf",
        use_container_width=True
        )