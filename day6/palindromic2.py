# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:29:28 2019

@author: HP
"""

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
list1=[]
list2=[]
#s = map(int, input("enter the integer >>>").split(' '))
list1= input("enter the integer>>>").split(' ')
print(list1)
for item in list1:
    list2.append(int(item))
k=all (item > 0 for item in list2)

print(list1)
y=any (item==item[::-1] for item in list1)

if(k==y):
    print ("true")
else:
    print ("false")




        