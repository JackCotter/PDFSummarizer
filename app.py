from PIL import Image
import pytesseract
import numpy as np
from pdf2image import convert_from_path
import os
from dotenv import load_dotenv
import sys
from openai import OpenAI
import argparse

load_dotenv()
client = OpenAI()

def convert_pdf_to_text(path_to_pdf):
  pytesseract.pytesseract.tesseract_cmd = os.environ.get('TESSERACT_PATH')
  args = parser.parse_args()

  pdf_start = args.s if args.s else 0
  pdf_finish = args.f if args.f else None

  images = convert_from_path(path_to_pdf, poppler_path=os.environ['POPPLER_PATH'])
  images = images[pdf_start:pdf_finish]

  total_text = ''
  for image in images:
    text = pytesseract.image_to_string(image, lang='eng')
    total_text += text

  # completion = client.chat.completions.create(
  #   model="gpt-3.5-turbo",
  #   messages=[
  #     {"role": "system", "content": "You are a skilled software engineer"},
  #     {"role": "user", "content": "please tell me a joke"}
  #   ]
  # )
  # print(completion.choices[0].text)
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
  parser = argparse.ArgumentParser(description="")

  parser.add_argument('-s', type=int, help="Specify an integer value after -s")
  parser.add_argument('-f', type=int, help="Specify an integer value after -s")

