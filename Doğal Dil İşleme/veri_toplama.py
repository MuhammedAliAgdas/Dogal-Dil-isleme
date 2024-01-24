import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import numpy as np
import csv

driver = webdriver.Chrome()
url = "https://www.imdb.com/title/tt0111161/reviews?sort=curated&dir=desc&ratingFilter=0"
driver.get(url)
yorumlar=[""]*10500
listIndex = 0
button_xpath = "//button[@id='load-more-trigger']"
wait = WebDriverWait(driver, 10)
try:
    for i in range(420):
        time.sleep(10)
        button = wait.until(EC.presence_of_element_located((By.XPATH, button_xpath)))
        ActionChains(driver).move_to_element(button).click().perform()
        
finally:
    baglanti = BeautifulSoup(driver.page_source,"lxml") 
    contents =baglanti.find_all("div",attrs={"class":"content"})
    for yorum in contents:
        if yorum.find("div", attrs={"class": "text show-more__control"}):
           yorumlar[listIndex]+= yorum.find("div",attrs={"class":"text show-more__control"}).text.lower()
           listIndex+=1
        else:
            yorumlar[listIndex]+= yorum.find("div",attrs={"class":"text show-more__control clickable"}).text.lower()
            listIndex+=1
            
    with open("veriler.csv", mode='w', newline='', encoding='utf-8') as dosya:
         for veri in yorumlar:
             csv.writer(dosya).writerow([veri])

input()







    
