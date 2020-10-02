# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:05:59 2020

@author: Asus
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    file = open('assamese.txt',"x",encoding="utf8")
except:
    file = open('assamese.txt',"a",encoding="utf")
n=int(input('number of pages : '))
for i in range(n):  
    text=input('URL: ')
    path='C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(text)

    try:
        main = WebDriverWait(driver,5).until(
                EC.presence_of_element_located((By.CLASS_NAME,"mw-parser-output"))
                )
        paragraphs = main.find_elements_by_tag_name("p")
        for paragraph in paragraphs:
            file.write(paragraph.text)
        
    finally:
        driver.quit()
file.close()    