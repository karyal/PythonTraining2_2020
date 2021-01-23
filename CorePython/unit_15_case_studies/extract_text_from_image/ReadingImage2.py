# pip install Wand
import cv2
import pytesseract
import warped as warped

from  PIL import Image
import PIL.Image
from pytesseract import image_to_string

def image_resize():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img1 = cv2.imread('image_2.jpeg', cv2.IMREAD_UNCHANGED)
    print(img1.shape)
    dim=(1350, 1150)
    img2 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("output", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()