# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 02:47:22 2020

@author: Asus
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    file = open('newwwassamese.txt',"x",encoding="utf8")
except:
    file = open('newwwassamese.txt',"a",encoding="utf")



n=int(input("number of pages you wanna scrape: "))

path='C:\Program Files (x86)\chromedriver.exe'



try:
    i=0;
    
    string=''
    link=input("enter the link: ")
    driver = webdriver.Chrome(path)
    driver.get(link)
    while(i<n):
        print(i)
        main = WebDriverWait(driver,5).until(
                    EC.presence_of_element_located((By.CLASS_NAME,"single-container"))
                    )
        para = main.find_elements_by_tag_name("p")
        for pin in para:
            print(pin.text)
            string+=pin.text
        file.write(string)
        mainone = WebDriverWait(driver,5).until(
                    EC.presence_of_element_located((By.CLASS_NAME,"prev-post"))
                    )
        a=mainone.find_element_by_tag_name("a")
        a.click()
        i+=1
finally:
    driver.quit()