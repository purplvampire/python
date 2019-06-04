#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):    # list files in directory.
    if filename.endswith('.pdf'):   # flitering PDF file.
        pdfFiles.append(filename)   # Append PDF file in list.
print(pdfFiles)

# Sorting filename by A to Z
pdfFiles.sort(key=str.lower)

# Create a New PDF Object
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages (except the first page) and add them.
    for pageNum in range(1, pdfReader.numPages): 
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()