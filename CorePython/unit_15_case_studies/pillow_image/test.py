from PIL import Image
import sys
try:
    image_data = Image.open("112.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)
image_data.show()
