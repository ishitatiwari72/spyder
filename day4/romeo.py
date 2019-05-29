# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:56:56 2019

@author: HP
"""


"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

dic={}
list1=[]
with open ('romeo.txt',mode='rt') as file:
    for item1 in file:
        list1.append(item1.split(" "))
    for item1 in list1:
        for item in range(0,len(item1)):
                dic[item1[item]]=int(dic.get(item1[item],0))+1
       
                        
                    
    
            
                     
