# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:51:35 2019

@author: HP
"""


"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
   Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
      
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""

from functools import reduce
list1=  [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
tot_am=0
list2=[]
list3=[]
for item in list1:
    for item1 in range (1,len(item)):
        order=item[0]
        tot_am = tot_am+item[item1][1]*item[item1][2]
    list2.append((order,tot_am))

s=list(map(lambda x: [x[0]]+list(map(lambda y:y[1]*y[2],x[1:])),list1))
q=list(map(lambda x: [x[0]]+[reduce(lambda a,b:a+b,x[1:])],s))
r=list(map(lambda x: x if x[1]>100 else (x[0],x[1]+10),q ))