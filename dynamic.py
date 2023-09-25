# Get all in pdfs dynamically in a folder and merger all of them

import PyPDF2
import os

merger = PyPDF2.PdfWriter()


for one in os.listdir():
    if ".pdf" in one:
        merger.append(one)


merger.write("new one.pdf")

merger.close()
