from numpy import imag, r_
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
from PIL import Image

img = Image.open('//home/jammin-jiggler/Documents/ocr source files/input images samplr/para.jpg')
text = tess.image_to_string(img)
print(text)