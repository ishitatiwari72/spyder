# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:00:23 2019

@author: HP
"""

 
"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement: (simpsons_phone_book.txt)
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
"""



import re
list1=[]
f1=open('simpsons_phone_book.txt','rt')
f2=open('s_p_b.txt','wt')
for item in f1:
    if re.findall(r'^J[a-zA-Z]*\sNeu',item):
        list1.append(item)
    else:
        continue
result= 
if result:
      f2.write(str(result))
f1.close()
f2.close()
    

