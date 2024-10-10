
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Initialize the WebDriver 
driver = webdriver.Chrome()


driver.get('https://www.gavakari.in/sitemaps/epaper-edition_1.xml')

# Wait for the page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Get the page source
page_source = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all the <loc> tags and extract the URLs
urls = [loc_tag.text for loc_tag in soup.find_all('loc')]

# Print the extracted URLs
for url in urls:
    print(url)

# Close the WebDriver
driver.quit()





# save the URLs to a text file
for url in urls:
    with open('gavakari_epaper_links.txt', 'a') as f:
        f.write(url + '\n')
