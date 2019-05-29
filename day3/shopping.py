# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:53:01 2019

@author: HP
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""
dir1={}
list1=[]
price=[]
list2=[]
list3=[]
p=int(input("enter the no of items"))
i=0
while(i<p):
    k=input("enter the product with there price")
    k=k.split(" ")
    price.append(int(k[-1]))
    list1.append(" ".join(k[0:-1]))
    i=i+1
list2=(zip(list1,price))
   

for item,val in list2:
    if item in dir1.keys():
        dir1[item]=val+val
    else:
        dir1[item]=val
        
    