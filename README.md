# Overview
Very simple Python program that takes a pdf file as input, analyzes it using Google's Tesseract OCR, then summarizes it using CHAT GPT 3.5 api.

# Use and flags
```
python app.py <flags>
```
```
-i input path for .pdf file. Will not accept any other files. Required.
-s starting page for OCR analysis. Optional.
-f final page for OCR analysis. Optional.
```

# Start Up (Windows)
1. Install Tesseract https://pypi.org/project/pytesseract/, tesseract OCR https://github.com/tesseract-ocr/tesseract and Poppler https://github.com/oschwartz10612/poppler-windows/releases
2. Run ```pip install -r requirements.txt``` from CLI
3. Add TESSERACT_PATH (path to tesseract exe), POPPLER_PATH (poppler exe), and OPENAI_API_KEY from your OPENAI account to a .env file in the base project directory
4. Use PDF Summarizer
