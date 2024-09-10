import requests
from bs4 import BeautifulSoup
import gdown
import os

url = 'https://marathipdf.com/genre/science/'

def download_pdf(pdf_url, output_file):
    if 'drive.google.com' in pdf_url:
        gdown.download(pdf_url, output_file, quiet=False)
    else:
        response = requests.get(pdf_url)
        with open(output_file, 'wb') as file:
            file.write(response.content)

def extract_text_from_pdf(pdf_file, output_file):
    import PyPDF2
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    with open(output_file.txt, 'a', encoding='utf-8') as file:
        file.write(text)

def process_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    books = soup.find_all('div', class_='book-item')
    for book in books:
        title = book.find('h3').text.strip()
        pdf_url = book.find('a')['href']
        output_pdf = f'{title}.pdf'
        output_text = f'{title}.txt'

        download_pdf(pdf_url, output_pdf)
        extract_text_from_pdf(output_pdf, output_text)
        print(f'Downloaded and extracted text from: {title}')

        os.remove(output_pdf)  # Remove the PDF file after extraction

process_page(url)
