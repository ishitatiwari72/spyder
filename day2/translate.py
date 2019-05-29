# -*- coding: utf-8 -*-
"""
Created on Thu May  9 00:42:10 2019

@author: HP
"""
"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""



def translate():
    i = input ("enter the string")
    c="bcdfghjklmnpqrstvwxyzT"
    str=""
    k=0
    while k<len(i):
        for item in i:
            if item in c:
                str=str+item+"o"+item
                k+=1
            else:
                str=str+item
                k+=1
    
    print(str)
    
    
    
    
    
    
    
    
    
    item2=""
    item3=""
    j=0
    for item in i:
        j=0
        flag=0
        for item1 in c:
            while j<=len(c) and flag==0:
                if item1[:]==item[:]:
                   item2=item2+item1*2
                   item2="o".join(item2)
                   flag=1
                   
                elif j==len(c) and  item1[:]!=item[:]:
                   item2=item2+item
                   flag=1
                elif j<len(c) and item1[:]!=item[:]:
                   j=j+1
                   flag=0
      #  item2=item2+item
        
        print(item2)
                

    #print(item2)       