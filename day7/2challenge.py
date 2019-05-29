# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:05:37 2019

@author: HP
"""



"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""



import requests

#url1 = "//api.fixer.io/latest?base=USD&symbol=EUR"    
#url3 =  "http://api.fixer.io/latest?base=USD&symbol=EUR
url="http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y"       
url = url+"&apiKey=5f67dcfc33f131a3eb24"
print (url)
response = requests.get(url)
data=response.json()

#by post method
Host = "http://httpbin.org/post"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}
