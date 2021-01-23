import PyPDF2
pdfFileObject = open(r"document_1.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
print("Pages :", pdfReader.numPages)
if pdfReader.numPages>0:
    current_page=0
    while current_page<pdfReader.numPages:
        pageObject = pdfReader.getPage(0)
        print("Content of Page "+str(current_page+1)+" -----------------------------------------")
        print(pageObject.extractText())
        current_page=current_page+1
pdfFileObject.close()