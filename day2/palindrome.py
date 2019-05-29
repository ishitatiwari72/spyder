# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:35:03 2019

@author: HP
"""
"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""


s=input("enter the items of list")
list1=s.split()
for item in list1:
    if int(item) > 0:
        flag=0
    else:
        flag=1
        print("item is not positive")
        break
n=len(list1)
print(list1)
i=0
while flag==0 and i < n:
    for item in list1:
        if item[:]==item[::-1]:
            palin=0
            break
        else:
            palin=1
            i=i+1
if palin==0:
     print ("list have a palindrome")   
else:
    print ("list dont have a palindrome")
          


