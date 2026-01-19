from PyPDF2 import PdfReader, PdfWriter
import os
import tempfile

def trim_pages_from_end(pdf_path: str, pages_to_remove: int):
    if pages_to_remove <= 0:
        return

    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)

    if pages_to_remove >= total_pages:
        raise ValueError("Cannot remove all pages from the PDF.")

    writer = PdfWriter()

    for i in range(total_pages - pages_to_remove):
        writer.add_page(reader.pages[i])

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        writer.write(tmp)
        temp_path = tmp.name

    os.replace(temp_path, pdf_path)
