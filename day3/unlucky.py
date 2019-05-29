# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:33:29 2019

@author: HP
"""
"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""
list1=[]
i=int(input("enter size of list"))
k=0
while k < i:
    j=int(input ("enter the no"))
    list1.append(j)
    k=k+1
p=0
count=0
while p<len(list1):
        if list1[p] is 13:
            p=p+2
        else:
            count=count+list1[p]
            p=p+1






while k<len(list1):
    if list1[k]=='13':
        k=k+2
    else:
        p=list1[k]
        count=count+int(p)
        k=k+1

