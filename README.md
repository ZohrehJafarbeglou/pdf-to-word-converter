# 📝 PDF to Word (Farsi OCR)

This script converts scanned Persian (Farsi) PDF files into editable Word documents using Tesseract OCR and Python.

## 🚀 Features
- Batch converts multiple PDFs from a folder
- Extracts Persian text (OCR) using Tesseract
- Saves output as `.docx` files with right-to-left formatting
- Shows extraction time for each document

## 📁 Folder Structure
project/
├── your_script.py
└── dataset/
├── file1.pdf
├── file2.pdf
└── ...

## ⚙️ Requirements

Install these before running the script:

### 📦 Python Libraries
```bash
pip install pytesseract pdf2image python-docx pillow
📄 Tesseract OCR
Download and install Tesseract: https://github.com/tesseract-ocr/tesseract

Make sure the Farsi language pack is installed:

On Windows:
It usually comes with Farsi (fas). If not, install it manually.

On Linux:
sudo apt install tesseract-ocr-fas
🧠 How It Works
The script scans a specified folder (e.g., data set 3/100) for .pdf files.

It converts each PDF page to an image.

OCR is applied using Tesseract to extract Persian text.

The text is saved in a .docx file with proper right-to-left alignment.

A timer prints how long each extraction takes.

🏁 How to Run
Change this line in the script to point to your PDF folder:
directory_path = "C:\\Path\\To\\Your\\Folder"
python your_script.py
Each .docx file will be saved in the same folder as the original PDF.

📝 Sample Output
Input: myfile.pdf

Output: myfile.docx (same location)

📃 License
This project is licensed under the MIT License.
