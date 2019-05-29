# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:54:13 2019

@author: HP
"""


"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""


file1=input("enter the name of file")
file2=open(file1,'rt')
p=file2.readlines()[-1]
print(p)
file2.close()