import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
import os

# initialize the WebDriver
driver = webdriver.Chrome()

# open the text file containing the URLs
with open('gavakari_epaper_links.txt', 'r') as f:
    links = f.readlines()
    i=0
    
# iterate over the URLs and download the images
for link in links:
    link = link.split('\n')[0]
    driver.get(link)
    
    driver.implicitly_wait(20)
    try:
        url=  driver.find_element(By.CLASS_NAME, 'epaper-page-viewer').find_element(By.TAG_NAME, 'a').get_attribute('href')
    except:
        print('no image')
        continue
    
    img_data = requests.get(url).content
    if(img_data == None):
        print("no image")
        continue
    
    # save the image to a file
    title = "image"+str(i)+".jpg"   
    with open('gavakari_img/'+title, 'wb') as handler:
        handler.write(img_data)
        i+=1
    print('done')

# close the WebDriver
driver.quit()


# =======================OCR images to get text data=======================


# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Create the output directory if it doesn't exist
if not os.path.exists('gavakari_data'):
    os.mkdir('gavakari_data')

# Get the list of image files
image_files = os.listdir('gavakari_img/')

# Process each image file
for i, image_file in enumerate(image_files):
    # Open the image file
    image_path = os.path.join('gavakari_img', image_file)
    image = Image.open(image_path)
    
    # Custom configuration for Tesseract
    custom_config = r'--oem 3 --psm 6 -l mar+hin'

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image, config=custom_config)
    
    # Save the extracted text to a file
    output_path = os.path.join('gavakari_data', f'image{i}.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f'Processed {image_file} and saved to {output_path}')




