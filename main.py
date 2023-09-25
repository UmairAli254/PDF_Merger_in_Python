# from PyPDF2 import PdfWriter
# import PyPDF2 
import PyPDF2 as pypdf

merger = pypdf.PdfWriter()

all_pdf = ["1.pdf","3.pdf", "2.pdf", ]

for one in all_pdf:
    # It will append all pdf files togethers (but in behind the seen)
    merger.append(one)


# When the loop is ended appending is completed now we can write that appends into a single pdf file using the below method.
merger.write("all in one.pdf")

# Now we have to close it
merger.close()
