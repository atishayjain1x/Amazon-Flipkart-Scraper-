#!/usr/bin/env python
# coding: utf-8

# In[176]:


import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say,What do you want to search ?")
    audio_text = r.listen(source,10,3)
    try:
        searchterm=r.recognize_google(audio_text)
        print("Text: "+ searchterm )
    except:
         print("Sorry, I did not get that")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
d=webdriver.Chrome(executable_path="E:/chromedriver_win32/chromedriver.exe")
d.get("https://www.amazon.in/")
r1=d.find_element_by_id("twotabsearchtextbox")
r1.send_keys(searchterm)
p1=d.find_element_by_class_name("nav-input")
p1.submit()
r=WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='a-price-whole']")))
s=d.find_element_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
amazontitle=s.text
amazonprice=r.text

d.get("https://www.flipkart.com/")
r=d.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']")
r.click()
r=d.find_element_by_name('q')
r.send_keys(searchterm)
p=d.find_element_by_xpath("//button[@class='L0Z3Pu']")
p.submit()
h=WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='_25b18c']")))
#h=d.find_element_by_xpath("//div[@class='_25b18c']")
try:
    s=d.find_element_by_xpath("//div[@class='_4rR01T']")
    flipkarttitle=s.text

except NoSuchElementException:
    flipkarttitle=searchterm
flipkartprice=h.text.split('₹')[1]


az="price of" +amazontitle.partition('(')[0] +"is" + amazonprice+ "on amazon ." +"price of" +flipkarttitle.partition('(')[0] +",is" + flipkartprice + "on flipkart ." 
from gtts import gTTS
import IPython
language = 'en'
myobj = gTTS(text=az, lang=language, slow=False,tld='co.in')
myobj.save("welcome.mp3")
IPython.display.Audio("welcome.mp3")


# In[ ]:




