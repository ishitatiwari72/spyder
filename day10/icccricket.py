# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:19:41 2019

@author: HP
"""



"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
from bs4 import BeautifulSoup

import requests

source=requests.get(" https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text
print(source)
soup=BeautifulSoup(source,"lxml")
req_table=soup.find('table',class_='table')
print(req_table)
a=[]
b=[]
c=[]
d=[]
e=[]
for row in req_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==5:
        a.append(cells[0].text.strip())
        b.append(cells[1].text.strip())
        c.append(cells[2].text.strip())
        d.append(cells[3].text.strip())
        e.append(cells[4].text.strip())
        
import pandas as pd
from collections import OrderedDict


col_name = ["Pos","team","weightmatches","point","rating"]
col_data = OrderedDict(zip(col_name,[a,b,c,d,e]))

df = pd.DataFrame(col_data) 
df.to_csv("former.csv")

        
    