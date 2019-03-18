#coding=utf-8
#coding=utf-8import cv2
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
#coding=utf-8
text = pytesseract.image_to_string(Image.open("testocr.tif"),lang='chi_sim')

print(text)