# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 01:54:48 2020

@author: Asus
"""

##https://xurorenajori.info/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    file = open('newassamese.txt',"x",encoding="utf8")
except:
    file = open('newassamese.txt',"a",encoding="utf")



n=int(input("number of pages you wanna scrape from xurorenajori: "))

path='C:\Program Files (x86)\chromedriver.exe'



try:
    i=0;
    while(i<n):
        string=''
        link=input("enter the link: ")
        driver = webdriver.Chrome(path)
        driver.get(link)

        main = WebDriverWait(driver,5).until(
                    EC.presence_of_element_located((By.CLASS_NAME,"entry-content"))
                    )
        para = main.find_elements_by_tag_name("p")
        for pin in para:
            print(pin.text)
            string+=pin.text
        file.write(string)
        i+=1
    
finally:
    driver.quit()