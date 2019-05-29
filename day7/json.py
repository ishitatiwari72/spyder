# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:23:47 2019

@author: HP
"""



"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""




import json
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1 + url2 + url3
print (url)


response = requests.get(url)
response.content
print (type(response.content))
data=response.json()

print ("Status code: " + str(response.status_code))
print ("Headers : " + str(response.headers))
print ("Data : " + response.text)



print (data["coord"])
print (data["weather"])
print (data["wind"])
data["sys"]["sunrise"]
data["sys"]["sunset"]
  
