# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:29:11 2019

@author: HP
"""
"""

Code Challenge 5

Fortune Teller (Horoscope)

A program that checks your horoscope on various astrology sites and puts them 
together for you each day. The code should share the Horoscope on Tweeter account
 of the user.
"""

from  selenium import webdriver
from time import sleep
url="https://www.clickastro.com/free-daily-horoscope"
driver=webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver")
driver.get(url)
sleep(2)
#email 
print ("ASTROLOGY:-------\nSelect your zoidac sign:-\n1.Aries\n2.Tarus\n3.Gemini\n4.Cancer\n5.Leo\n6.Virgo\n7.Libra\n8.Scorpio\n9.Sagitarus\n10..Capricon\n11.Aquarus\n12.Pisces")
i = input ("Select your Zoidac sign : ")
if i==1:
      x=driver.find_element_by_xpath("/html/body/section[1]/div[3]/a[1]")
      x.click()
      horoscope=driver.find_element_by_xpath("/html/body/section/section[1]/div[2]/main/p[2]")  
      print('hello')
      print(horoscope)
elif i==2:
    x=driver.find_element_by_xpath("/html/body/section[1]/div[3]/a[2]")
    x.click()
    horoscope=driver.find_element_by_xpath("/html/body/section/section[1]/div[2]/main/p[2]")
    print(horoscope)
elif i==3:
    x=driver.find_element_by_xpath("/html/body/section[1]/div[3]/a[3]")
    x.click()
    horoscope=driver.find_element_by_xpath("/html/body/section/section[1]/div[2]/main/p[2]")
    print(horoscope)
elif i==4:
    x=driver.find_element_by_xpath("/html/body/section[1]/div[3]/a[4]")
    x.click()
    horoscope=driver.find_element_by_xpath("/html/body/section/section[1]/div[2]/main/p[2]")
    print(horoscope)
elif i==5:
    x=driver.find_element_by_xpath("/html/body/section[1]/div[3]/a[5]")
    x.click()
    horoscope=driver.find_element_xpath("/html/body/section/section[1]/div[2]/main/p[2]")
    print(horoscope)
sleep(2)
