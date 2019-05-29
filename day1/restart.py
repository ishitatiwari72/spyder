# -*- coding: utf-8 -*-
"""
Created on Wed May  8 05:16:24 2019

@author: HP
"""

"""Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T"""
    
    
i=input ("enter the word")
n=i.find('r')
st1= (i[:n+1])
st2= (i[n+1:])
print (st1)
print (st2)
st4=st2.replace('r','$')
st3=st1+st4
print(st3)