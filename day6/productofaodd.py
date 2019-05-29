# -*- coding: utf-8 -*-
"""
Created on Tue May 14 04:41:28 2019

@author: HP
"""




"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""
from functools import reduce

list1=list(map(int,input("enter the value>>>").split(',')))
def pod(x):
    r=1
    if x%2==1:
        r=r*x
        return r

q=  list(filter(pod,list1))
s=reduce(lambda x,y:x+y,list(filter(pod,list1)))
print (s)