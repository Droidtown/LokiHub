#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PyPDF2 import PdfReader
import fitz
import pytesseract
from PIL import ImageOps
from pdf2image import convert_from_path
from concurrent.futures import ThreadPoolExecutor, as_completed
import psutil
import os
import sys

"""
功能：負責處理PDF文件的上傳和轉換，將PDF轉換為文本並傳遞給後續的處理模塊。
主要內容：
1. PDF2Txt腳本的調用與封裝。
2. 處理上傳的PDF文件，將其轉換為純文本格式。
"""

# 特殊符號列表
splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";", "｜", "▸"]

class PDFHandler:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        if not self.pdf_path.endswith(".pdf"):
            print("Unsupported file type!")
            sys.exit()
        self.num_pages = self.get_num_pages()

    def get_num_pages(self):
        reader = PdfReader(self.pdf_path)
        return len(reader.pages)

    def extract_text_with_fitz(self):
        doc = fitz.open(self.pdf_path)
        text_pages = {}
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text = page.get_text()
            if text.strip():  # Check if extracted text is non-empty
                text_pages[page_num] = text
        return text_pages if text_pages else None

    def extract_text_with_ocr(self):
        all_text_pages = {}
        max_workers = os.cpu_count() or 4
        memory = psutil.virtual_memory()

        # Adjust batch_size based on available memory
        batch_size = max(1, int(memory.available / (500 * 1024 * 1024)))  # 500MB per batch

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for start_page in range(1, self.num_pages + 1, batch_size):
                end_page = min(start_page + batch_size - 1, self.num_pages)
                futures.append(executor.submit(self.process_pages_with_ocr, start_page, end_page))

            for future in as_completed(futures):
                try:
                    all_text_pages.update(future.result())
                except Exception as e:
                    print(f"Error in OCR processing: {e}")                

        return all_text_pages

    def process_pages_with_ocr(self, start_page, end_page):
        images = convert_from_path(self.pdf_path, dpi=300, first_page=start_page, last_page=end_page, poppler_path=r'C:\Python312\poppler-24.07.0\Library\bin')
        texts = self.extract_text_from_images(images)
        return {i: text for i, text in enumerate(texts, start=start_page)}

    def extract_text_from_images(self, images):
        res = []
        if images:
            for image in images:
                gray_image = ImageOps.grayscale(image)
                text = pytesseract.image_to_string(gray_image, lang="chi_tra+eng")
                res.append(text)
        return res

    def extract_text(self):
        text_pages = self.extract_text_with_fitz()
        if text_pages:  # If text was successfully extracted using fitz
            all_text = "".join(text_pages[i] for i in sorted(text_pages))
            return self.clean_text(all_text)
        else:  # If fitz extraction failed, fallback to OCR
            print("Text extraction with fitz failed, falling back to OCR.")
            ocr_text_pages = self.extract_text_with_ocr()
            all_text = "".join(ocr_text_pages[i] for i in sorted(ocr_text_pages))
            return self.clean_text(all_text)

    def clean_text(self, text):
        for char in splitLIST:
            text = text.replace(char, '')
        return text

    def save_text_to_file(self, text, output_path='extracted_text.txt'):
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)


if __name__ == "__main__":
    pdf_path = "data/temp.pdf"
    handler = PDFHandler(pdf_path)
    extracted_text = handler.extract_text()
    handler.save_text_to_file(extracted_text)
