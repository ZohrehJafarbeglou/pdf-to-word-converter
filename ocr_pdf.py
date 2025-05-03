# import pytesseract
# from pdf2image import convert_from_path
# import os
# import time
# import threading
# from docx import Document
# from docx.shared import Pt
# from docx.oxml import OxmlElement

# # مسیر فایل PDF
# pdf_path = "C:/Users/TANIN-TCC/Desktop/PhD -tese/data set 3/40/آخرین طناب.pdf"
# pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# # متغیر برای ذخیره متن استخراج شده
# extracted_text = ""

# # تابع برای شمارش زمان
# def timer():
#     elapsed = 0
#     while not stop_timer.is_set():
#         print(f"\rمدت زمان استخراج: {elapsed} ثانیه", end="")
#         time.sleep(1)
#         elapsed += 1

# # شروع تایمر
# stop_timer = threading.Event()
# timer_thread = threading.Thread(target=timer)
# timer_thread.start()

# # شروع زمان استخراج
# start_time = time.time()

# # تبدیل PDF به تصاویر
# images = convert_from_path(pdf_path)

# # پردازش هر تصویر و استخراج متن
# for i, image in enumerate(images):
#     # تنظیمات OCR
#     custom_config = r'--oem 3 --psm 6 -l fas'
#     text = pytesseract.image_to_string(image, config=custom_config)
#     extracted_text += text + "\n"

# # پایان زمان استخراج
# end_time = time.time()
# stop_timer.set()  # توقف شمارشگر
# timer_thread.join()  # انتظار برای پایان شمارشگر

# # ذخیره متن در فایل ورد
# output_path = 'output_text.docx'
# doc = Document()

# # تنظیم جهت متن به راست به چپ
# doc.add_paragraph(extracted_text).paragraph_format.alignment = 2  # راست‌چین کردن پاراگراف

# # ذخیره فایل
# doc.save(output_path)

# # نمایش فایل متنی به کاربر (در ویندوز)
# os.startfile(output_path)

# print("\nمتن استخراج شده در فایل ورد ذخیره شد و باز شد.")
# print(f"مدت زمان کل استخراج: {end_time - start_time:.2f} ثانیه")




import pytesseract
from pdf2image import convert_from_path
import os
import time
import threading
from docx import Document
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# مسیر نصب Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# تابع برای شمارش زمان
def timer():
    elapsed = 0
    while not stop_timer.is_set():
        print(f"\rمدت زمان استخراج: {elapsed} ثانیه", end="")
        time.sleep(1)
        elapsed += 1

# تابع برای تبدیل PDF به DOCX
def convert_pdf_to_docx(pdf_path):
    extracted_text = ""
    stop_timer.clear()  # شروع تایمر

    # شروع تایمر
    timer_thread = threading.Thread(target=timer)
    timer_thread.start()

    # تبدیل PDF به تصاویر
    images = convert_from_path(pdf_path)

    # پردازش هر تصویر و استخراج متن
    for image in images:
        custom_config = r'--oem 3 --psm 6 -l fas'
        text = pytesseract.image_to_string(image, config=custom_config)
        extracted_text += text + "\n"

    # ذخیره متن در فایل ورد
    output_path = pdf_path.replace('.pdf', '.docx')
    doc = Document()
    doc.add_paragraph(extracted_text).paragraph_format.alignment = 2  # راست‌چین کردن پاراگراف
    doc.save(output_path)

    # پایان تایمر
    stop_timer.set()
    timer_thread.join()

    print(f"\nمتن استخراج شده از '{pdf_path}' در '{output_path}' ذخیره شد.")

# مسیر دایرکتوری که فایل‌های PDF در آن قرار دارند
#directory_path = "C:\Users\TANIN-TCC\Desktop\PhD -tese\data set4\NAVID\"
#directory_path = r"C:\Users\TANIN-TCC\Desktop\PhD -tese\data set4\NAVID\"
directory_path = "C:\\Users\\TANIN-TCC\\Desktop\\PhD -tese\\data set 3\\100"


#directory_path = "C:/Users/TANIN-TCC/Desktop/PhD -tese/data set4/NAVID/"
# بررسی و تبدیل همه فایل‌های PDF
stop_timer = threading.Event()

for filename in os.listdir(directory_path):
    if filename.endswith('.pdf'):
        pdf_file_path = os.path.join(directory_path, filename)
        convert_pdf_to_docx(pdf_file_path)

print("تمام فایل‌های PDF تبدیل شدند.")