# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:15:09 2019

@author: HP
"""
"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
i=0
with open('absentee.txt', mode='wt') as file :
    while i<25:
        a=input("enter the name of student")
        file.write(a+"\n")
        i=i+1
        if not a:
            break
with open('absentee.txt', mode='rt') as file :
   file_contents = file.readlines()
   print(file_contents)
        
