import PyPDF2

fileName = input('Enter PDF file name to make top secret: ')
pdfFile = open(fileName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
firstPage = pdfReader.getPage(0)

pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
firstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(firstPage)

for pageNum in range(1, pdfReader.numPages):
    page = pdfReader.getPage(pageNum)
    pdfWriter.addPage(page)
resultPdfFile = open('Top Secret-' + fileName, 'wb')
pdfWriter.write(resultPdfFile)
pdfFile.close()
resultPdfFile.close()
