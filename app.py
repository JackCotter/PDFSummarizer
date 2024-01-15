from PIL import Image
import pytesseract
import numpy as np
from pdf2image import convert_from_path
import os
from dotenv import load_dotenv

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = os.environ.get('TESSERACT_PATH')

images = convert_from_path('', poppler_path=os.environ['POPPLER_PATH'])
total_text = ""
for image in images:
  text = pytesseract.image_to_string(images[1], lang='eng')
  total_text += text
  break

print(total_text)