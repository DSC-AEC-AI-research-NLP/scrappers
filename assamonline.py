# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 00:07:32 2020

@author: Asus
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

try:
    file = open('assamese.txt',"x",encoding="utf8")
except:
    file = open('assamese.txt',"a",encoding="utf")
n=int(input('number of pages : '))

path='C:\Program Files (x86)\chromedriver.exe'



try:
    i=0;
    while(i<n):
        string=''
        link=input("enter the link: ")
        driver = webdriver.Chrome(path)
        driver.get(link)
        sleep(3)
        para =driver.find_elements_by_tag_name("p")
        sleep(1)
        for pin in para:
            print(pin.text)
            string+=pin.text
        file.write(string)
        i+=1
    
finally:
    driver.quit()