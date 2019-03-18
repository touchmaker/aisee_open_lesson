import cv2
import pytesseract
from PIL import Image
import os

text = pytesseract.image_to_string(Image.open("testocr.jpg"))
print(text)