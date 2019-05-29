# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:36:26 2019

@author: HP
"""


"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""

i= input("enter the name of file")
f1=open(i,'rt')
list1=[]
list2=[]        
c_l=0
w_c=0
word=0
line=0
dic={}
for item in f1:
    c_l=c_l+len(item)
    line=line+1
    list1.append(item.split(" "))
    
    
for item2 in list1:
        word=word+len(item2)

for item in list1:
    for item2 in range(0,len(item)):
        dic[item[item2]]=int(dic.get(item[item2],0))+1
        
for u_item in dic:
    if int(dic[u_item])==1:
        list2.append(u_item)
print(list2)