import PyPDF2  # pip install PyPDF2
import textract # pip install textract
from nltk.tokenize import word_tokenize # pip install nltk
from nltk.corpus import stopwords

filePath = "document_1.pdf"
# Open the pdf file in read binary mode.
fileObject = open(filePath, 'rb')

# Create a pdf reader .
pdfFileReader = PyPDF2.PdfFileReader(fileObject)

# Get total pdf page number.
totalPageNumber = pdfFileReader.numPages

# Print pdf total page number.
print('Pages : ' + str(totalPageNumber))
currentPageNumber = 0
text = ''

# Loop in all the pdf pages.
while (currentPageNumber < totalPageNumber):
    # Get the specified pdf page object.
    pdfPage = pdfFileReader.getPage(currentPageNumber)
    # Get pdf page text.
    text = text + pdfPage.extractText()
    # Process next page.
    currentPageNumber += 1
if (text == ''):
    # If can not extract text then use ocr lib to extract the scanned pdf file.
    text = textract.process(filePath, method='tesseract', encoding='utf-8')
print("Contents : "+text)