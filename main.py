import streamlit as st
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape

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

col1, col2, col3 = st.columns([1,2,1])

with col1:
    datum1 = st.text_input("Datum #1: ")

with col2:
    tätigkeit1 = st.text_input("Tätigkeit #1: ")

with col3:
    bemerkungen1 = st.text_input("Bemerkungen #1: ")

with col1:
    datum2 = st.text_input("Datum #2: ")

with col2:
    tätigkeit2 = st.text_input("Tätigkeit #2: ")

with col3:
    bemerkungen2 = st.text_input("Bemerkungen #2: ")

with col1:
    datum3 = st.text_input("Datum #3: ")

with col2:
    tätigkeit3 = st.text_input("Tätigkeit #3: ")

with col3:
    bemerkungen3 =  st.text_input("Bemerkungen #3: ")

with col1:
    datum4 = st.text_input("Datum #4: ")

with col2:
    tätigkeit4 = st.text_input("Tätigkeit #4: ")

with col3:
    bemerkungen4 = st.text_input("Bemerkungen #4: ")

with col1:
    datum5 = st.text_input("Datum #5: ")

with col2:
    tätigkeit5 = st.text_input("Tätigkeit #5: ")

with col3:
    bemerkungen5 = st.text_input("Bemerkungen #5: ")

def createPDF(lehrlingName, kalenderwoche, vomDatum, bisDatum, gruppe, trainer, datum1, tätigkeit1, bemerkungen1, datum2, tätigkeit2, bemerkungen2, datum3, tätigkeit3, bemerkungen3, datum4, tätigkeit4, bemerkungen4, datum5, tätigkeit5, bemerkungen5) -> bytes:
    """Creates a simple PDF in memory and returns its bytes."""
    buffer = BytesIO()

        # Create a PDF canvas that writes into the buffer
    c = canvas.Canvas(buffer, pagesize=landscape(A4))

        # Write some text into the PDF
    c.setFont("Helvetica", 16)
    c.drawString(200, 800, "Ausbildungstagebuch")

    c.setFont("Helvetica", 12)

    c.drawString(72, 500, f"Lehrling: {lehrlingName}")
    c.drawString(220, 500, f"Kalenderwoche: {kalenderwoche}")
    c.drawString(350, 500, f"Vom: {vomDatum}")
    c.drawString(480, 500, f"Bis: {bisDatum}")

    c.drawString(72, 470, f"Gruppe: {gruppe}")
    c.drawString(200, 470, f"Trainer: {trainer}")

    c.drawString(72, 410, "Datum")
    c.drawString(200, 410, "Tätigkeit")
    c.drawString(530, 410, "Bemerkungen")

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

    # Finish the PDF
    c.showPage()
    c.save()

    # Get the bytes from the buffer
    buffer.seek(0)
    return buffer.read()

if st.button("Create PDF"):
    pdf_bytes = createPDF(lehrlingName, kalenderwoche, vomDatum, bisDatum, gruppe, trainer, datum1, tätigkeit1, bemerkungen1, datum2, tätigkeit2, bemerkungen2, datum3, tätigkeit3, bemerkungen3, datum4, tätigkeit4, bemerkungen4, datum5, tätigkeit5, bemerkungen5)
    st.success("Successfully created PDF!")
    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name="Ausbildungstagebuch_" + lehrlingName + "_" + kalenderwoche + "_" + vomDatum + "-" + bisDatum + ".pdf",
        mime="application/pdf",
        use_container_width=True
        )