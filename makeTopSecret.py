import PyPDF2

def isVertical(page):
    page = page.mediaBox
    return page.getUpperRight_x() - page.getUpperLeft_x() < page.getUpperRight_y() - page.getLowerRight_y()

fileName = input('Enter PDF file name to make top secret: ')
pdfFile = open(fileName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
firstPage = pdfReader.getPage(0)

if (not isVertical(firstPage)):
    firstPage.rotateCounterClockwise(90)

if (firstPage.get('/Rotate')):
    firstPage.rotateCounterClockwise(firstPage.get('/Rotate'))

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
