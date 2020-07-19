import PyPDF2
import sys
import os

#module that i used here was PyPDF2
# Merge input pdf files into singel file
merger = PyPDF2.PdfFileMerger()
for infile in sys.argv[1:]:
    merger.append(infile)
merger.write('super.pdf')


# Created a function to merge all the files into one single file
def pdf_combiner(li, outfile_Name):
    output_file = os.getcwd() + outfile_Name + ".pdf"
    merger = PyPDF2.PdfFileMerger()
    for file in li:
        merger.append(file)
    merger.write(output_file)


# code to mergepages so that water mark file will merge into other file pages
file_reader = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
wtr_reader = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

writer = PyPDF2.PdfFileWriter()

for pageNo in range(file_reader.getNumPages()):
    file_page = file_reader.getPage(pageNo)
    wtr_page = wtr_reader.getPage(0)
    file_page.mergePage(wtr_page)
    writer.addPage(file_page)

with open('super-wtr.pd', 'wb') as out_file:
    writer.write(out_file)

# print(type(os.getcwd()))

# How to read file
with open('dummy.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file)

    page = reader.getPage(0)
    page.rotateClockwise(90)
    # print(page.rotateClockwise(90))
    # How to write to a PDF file
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('dummy-rotate.pdf', 'wb') as file:
        writer.write(file)

    # Print some information from file
    print(reader.documentInfo)
    print(reader.numPages)
    print(dir(reader))
