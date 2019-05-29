# -*- coding: utf-8 -*-
"""
Created on Fri May 10 06:21:50 2019

@author: HP
"""
"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""
k=int(input("enter the size of list"))
j=0
l=0
u=0
list1=[]
while j<k:
    i=int(input ("enter the no"))
    list1.append(i)
    j=j+1
for item in list1:
    if item==max(list1):
        pass
    elif item==min(list1):
        pass
    else:
        l=l+item
        u=u+1
avg=int(l/u)
print(avg)