# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:03:13 2019

@author: HP
"""

"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""

from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

f_l =list(filter(lambda item :'height' in item ,people))
tot_h=list(map(lambda item:item['height'],f_l))
print("total height",reduce(lambda x,y:x+y,tot_h))
tot_c=len(tot_h)


#for item in tot_h:
if tot_c>0:
    average=reduce(lambda x,y: x+y,tot_h)/tot_c
    print("average >>",average)
