# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:29:30 2020

@author: Asus
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
try:
    file = open('newwwassamese.txt',"x",encoding="utf8")
except:
    file = open('newwwassamese.txt',"a",encoding="utf")



n=int(input("number of pages you wanna scrape: "))

path='C:\Program Files (x86)\chromedriver.exe'



try:
    i=0;
    link=input("enter the link: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    while(i<n):
        string=''
        print(i)
        time.sleep(2)
        main = WebDriverWait(driver,5).until(
                    EC.presence_of_element_located((By.TAG_NAME,"article"))
                    )
        para = main.find_elements_by_tag_name("span")
        for pin in para:
            string+=pin.text
        print(string)
        file.write(string)
            
        mainone = WebDriverWait(driver,5).until(
                    EC.presence_of_element_located((By.ID,"blog-pager-older-link"))
                    )
        a=mainone.find_element_by_tag_name("a")
        a.click()
        i+=1
finally:
    driver.quit()