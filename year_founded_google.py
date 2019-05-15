import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(chrome_options=options)

text="Johnson Financial Group year founded"
text.replace(" ", "+")

driver.get('https://www.google.com/search?q=' + text)
time.sleep(10)
copiedText = wait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gsfi"))).text
print(copiedText)
soup = BeautifulSoup(driver.page_source, "html.parser")
answer = soup.find(class_="Z0LcW")
print(answer.get_text())
driver.quit()