# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:55:53 2019

@author: HP
"""


"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
     
     

"""
http://forsk.in/images/Forsk_logo_bw.png"


Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""


import pandas as pd
from selenium import webdriver
url = "https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome("C:\\users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get(url)    
right_content=driver.find_element_by_class_name('tab-content')
print(right_content)
bid=[]

for item in range(1,11):
    p=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(item)+']/div[1]/p[1]/a').text
    bid.append(p)

quan=[]

for item in range(1,11):
    p=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(item)+']/div[2]/p[2]/span').text
    quan.append(p)

start_date=[]

for item in range(1,11):
    p=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(item)+']/div[4]/p[1]/span').text
    start_date.append(p)

end_date=[]

for item in range(1,11):
    p=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(item)+']/div[4]/p[2]/span').text
    end_date.append(p)

dep_nameadd=[]

for item in range(1,11):
    p=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(item)+']/div[3]/p[2]').text
    dep_nameadd.append(p)


from collections import OrderedDict

col_name = ["bid_no","quantity","startdate","enddate","department"]
col_data = OrderedDict(zip(col_name,[bid,quan,start_date,end_date,dep_nameadd]))
df = pd.DataFrame(col_data) 
df.to_csv("dev.csv")
