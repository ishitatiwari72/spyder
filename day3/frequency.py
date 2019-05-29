# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:45:07 2019

@author: HP
"""
"""
 Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
dic={}
value=0
i=(input("enter the string"))
j=set(i)
print (j)
for item in j:
    for item1 in i:
        if item==item1:
            dic[item]=int(dic.get(item,0))+1
        
            
        
    
    