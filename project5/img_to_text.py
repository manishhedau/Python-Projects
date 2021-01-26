import pytesseract
import os
from PIL import Image

# First of all to run this program you need to do two things
# 1. install pytesseract module - pip install pytesseract
# 2. you need to download the tesseract exe file from google using github link
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract.OCR\tesseract.exe'

def Image_to_Text():
    img = Image.op('image.jpg') # here just need to pass the image name whatever you want to give

    # this function text of img into string form
    text = pytesseract.image_to_string(img)
    print(text)


Image_to_Text()