from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\\Users\\HP\\PycharmProjects\\web-scraping\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
query="laptop"
file=0
driver.get(f"https://www.amazon.in/s?k={query}&page=2&crid=13EF3JNHQJLSU&qid=1720264360&sprefix=phone%2Caps%2C530&ref=sr_pg_1")
elems=driver.find_elements(By.CLASS_NAME,"puis-card-container")
for elem in elems:
    d=elem.get_attribute("outerHTML")
    with open(f"data/Amazon/{file}.html","w",encoding="utf-8") as f:
        f.write(d)
        file+=1

driver.close()