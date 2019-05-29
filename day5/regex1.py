# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:45:35 2019

@author: HP
"""

"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""

import re
while True:
        i= input("enter the string")
        if not i:
            break
        elif re.match(r'^[+-]?\d*\.[0-9]+$', i):
            print ("true")
        else:
            print ("false")
