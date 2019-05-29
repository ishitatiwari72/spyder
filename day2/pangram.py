# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:52:55 2019

@author: HP
"""
"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""

str1 = "abcdefghijklmnopqrstuvwxyz"
str2=input("enter the string")
#list1=str2.split()
for item in str1:
    for item2 in str2:
        i=0
        if item[:]==item2[:]:
            flag=1
            break
        elif i < len(str2) and item[:]!=item2[:]:
            flag=0
            i=i+1
            continue
        elif i==len(str2) and item[:]!=item2[:]:
            flag=0
            break
    if flag==0:
        break
    
if(flag==1):
    print("its a pangaram")
else:
    print("its not a pangaram")
        
        
            
    
        