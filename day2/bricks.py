# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:30:58 2019

@author: HP
"""
"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""
list1=[]
def brick_t() :
    s_b=int(input("enter the no of small bricks"))
    l_b=int(input("enter the no of large bricks"))
    t=int(input("enter the target wall"))
    list1.append(s_b)
    list1.append(l_b)
    list1.append(t)

    p=int(t/5)
    q=int(t%5)
    if(p <= l_b) and (q <= s_b):
        print ("true")
    else:
        print ("false")
        
    
