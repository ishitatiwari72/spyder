# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:44:49 2019

@author: HP
"""



# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com



import json
import requests

Host = "https://requestbin.com"
data = {"firstname":"ishita","language":"English"}
headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}
def post_method():
    response = requests.post(Host,data,headers)
    return response
print (post_method().text )
