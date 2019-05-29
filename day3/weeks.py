# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:25:57 2019

@author: HP
"""

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""

dict1={'sunday','monday','tuesday','wednesday','thurusday','friday','saturday'}
tup=(input("enter the days"))
tup=set(tup.split(','))
s1=dict1.difference(tup)
print(s1)



list3=zip[s1]



l1 = "a b c d e".split()
l2 = list(range(6))
print(list(zip(l1,l2)))