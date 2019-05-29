# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:25:28 2019

@author: HP
"""


"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)

As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.


"""



import random
name=['mary','isla','sam']
code_name=['mr.pink','mr.orange','mr blonde']
u=list(map(lambda item: random.choice(code_name),name))
print (u)    
    
