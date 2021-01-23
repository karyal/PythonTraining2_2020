# pip install pytesseract
# dowmload and install tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe from https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('image_2.jpeg')
text = pytesseract.image_to_string(img)
print(text)