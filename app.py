from PIL import Image
import pytesseract
import numpy as np
from pdf2image import convert_from_path
import os
from dotenv import load_dotenv
import sys

def convert_pdf_to_text(path_to_pdf):
  load_dotenv()
  pytesseract.pytesseract.tesseract_cmd = os.environ.get('TESSERACT_PATH')

  images = convert_from_path(path_to_pdf, poppler_path=os.environ['POPPLER_PATH'])
  total_text = ''
  for image in images:
    text = pytesseract.image_to_string(image, lang='eng')
    total_text += text

  print(total_text)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Please provide a path to a PDF file')
    exit(1)

  if not os.path.exists(sys.argv[1]):
    print('File does not exist')
    exit(1)

  if not sys.argv[1].endswith('.pdf'):
    print('File is not a PDF')
    exit(1)

  convert_pdf_to_text(sys.argv[1])
