import streamlit as st
from io import BytesIO
from reportlab.pdfgen import canvas

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

def createPDF(lehrlingName, kalenderwoche, vomDatum, bisDatum, gruppe, trainer) -> bytes:
    """Creates a simple PDF in memory and returns its bytes."""
    buffer = BytesIO()

        # Create a PDF canvas that writes into the buffer
    c = canvas.Canvas(buffer)

        # Write some text into the PDF
    c.setFont("Helvetica", 16)
    c.drawString(200, 800, "Ausbildungstagebuch")

    c.setFont("Helvetica", 12)

    c.drawString(72, 760, f"Lehrling: {lehrlingName}")
    c.drawString(72, 740, f"Kalenderwoche: {kalenderwoche}")
    c.drawString(72, 720, f"Vom: {vomDatum}")
    c.drawString(200, 720, f"Bis: {bisDatum}")

    c.drawString(72, 700, f"Gruppe: {gruppe}")
    c.drawString(200, 700, f"Trainer: {trainer}")

    # Finish the PDF
    c.showPage()
    c.save()

    # Get the bytes from the buffer
    buffer.seek(0)
    return buffer.read()

if st.button("Create PDF"):
    pdf_bytes = createPDF(lehrlingName, kalenderwoche, vomDatum, bisDatum, gruppe, trainer)
    st.success("Successfully created PDF!")
    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name="Ausbildungstagebuch_" + lehrlingName + "_" + kalenderwoche + "_" + vomDatum + "-" + bisDatum + ".pdf",
        mime="application/pdf",
        use_container_width=True
        )