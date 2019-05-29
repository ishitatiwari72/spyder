# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:43:27 2019

@author: HP
"""
"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""

import csv
water=0
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # row has the list of all columns
    for row in csv_reader:
        if row[0]=='lion':
            water+=int(row[2])
            print(water)
list1=[]        
def group(csv_file):
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            if row[0] in list1:
                continue
            else:
                list1.append(row[0])

dic={}
def totwaterneed(csv_file):
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            if  row[0] in dic:
                dic[row[0]]=int(dic[row[0]]) + int(row[2])
            else:
                dic[row[0]]=int(row[2])
for item in dic:
    print(item,dic[item])
    

def total_w(dic):
    tot=sum(dic.values())
    return tot
""" total=0
    for item in dic:
    total=total+dic[item]
"""
        
