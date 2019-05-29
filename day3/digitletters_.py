# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:42:05 2019
ode Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_lette
    r_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
@author: HP
"""
dict1={'digit':0,'letters':0}

i=list(input("enter the string"))
for item in i:
    if(item.isalpha()):
        dict1['letters']=int(dict1.get('letters')) + 1
    elif(item.isdigit()):
        dict1['digit']=int(dict1.get('digit')) + 1
    else:
        continue
 
        

