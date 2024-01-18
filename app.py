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

def convert_pdf_to_text(args):
  pytesseract.pytesseract.tesseract_cmd = os.environ.get('TESSERACT_PATH')

  pdf_start = args.s if args.s else 0
  pdf_finish = args.f if args.f else None

  images = convert_from_path(args.i, poppler_path=os.environ['POPPLER_PATH'])
  images = images[pdf_start:pdf_finish]
  print(images.__len__())

  total_text = ''
  for image in images:
    text = pytesseract.image_to_string(image, lang='eng')
    total_text += text

  print(len(total_text))

  prompt_messages = [
      {"role": "system", "content": "You are a skilled software engineer"},
      {"role": "user", "content": "please summarize the following text in few short bullet points. Please ignore sentences that don't make sense."},
  ]
  last_index = 0
  total_resonse_text = ''
  for new_index in range(3000, len(total_text) + 3000, 3000):
    if new_index >= len(total_text):
      new_index = len(total_text)
    current_messages = prompt_messages.copy()
    current_messages.append({"role": "user", "content": total_text[last_index:new_index]},)
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=current_messages,
    )
    print(completion.choices[0].message.content)
    total_resonse_text += completion.choices[0].message.content
    last_index = new_index
    
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a skilled software engineer"},
      {"role": "user", "content": "Please summarize the following bullet points to be more concise, without losing any information."},
      {"role": "user", "content": total_resonse_text},
],
  )
  print("======== overall summary ========" + "\n" + completion.choices[0].message.content)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="")

  parser.add_argument('-i', type=str, help="Specify an integer value after -s")
  parser.add_argument('-s', type=int, help="Specify an integer value after -s")
  parser.add_argument('-f', type=int, help="Specify an integer value after -f")
  args = parser.parse_args()

  if args.s and args.f and args.s > args.f:
    print('Start page must be less than finish page')
    exit(1)

  if args.s and args.s < 0:
    print('Start page must be greater than 0')
    exit(1)

  if args.f and args.f < 0:
    print('Finish page must be greater than 0')
    exit(1)

  if args.i is None:
    print('Please provide a path to a PDF file')
    exit(1)

  if not os.path.exists(args.i):
    print('File does not exist')
    exit(1)

  if not args.i.endswith('.pdf'):
    print('File is not a PDF')
    exit(1)

  convert_pdf_to_text(args)
