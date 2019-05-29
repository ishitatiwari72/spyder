# -*- coding: utf-8 -*-
"""
Created on Thu May  9 06:07:26 2019

@author: HP
"""
"""

Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""


def all_():
    list1=[]
    i=int(input("enter the size of list"))
    j=0
    print("enter the item in list")
    while(j<i):
        k=int(input(""))
        list1.append(k)
        j=j+1
    print("MENU:\n1.Add\n2.Multiply\n3.Largest\n4.Smallest\n5.Sorted\n6Without Duplicates\n7 Print")
    l="1234567"
    while True:      
        choice=int(input("enter your choice"))
        if choice==1:
            add=0
            for item in list1:
                add=add+item
            print ("Sum={}".format(add))
         
        elif choice==2:
            mul=1
            for item in list1:
                mul=mul*item
            print ("Multiply={}".format(mul))
        
    
        elif choice==3:
            max1=max(list1)
            print ("Largest={}".format(max1))
        
        
          
        elif choice==4:
            min1=min(list1)
            print ("Smallest={}".format(min1))
        
                
        elif choice==5:
            list1.sort()
            print("Sorted{}".format(list1))
        
        
        
        elif choice==6:
            list(dict.fromkeys(list1))
            list2=[]
            for item in list1:
                if item not in list2:
                    list2.append(item)
            print("Without Duplicates{}".format(list2))
            
            
        
        elif choice==7:
            print ("Sum={}".format(add))
            print ("Multiply={}".format(mul))
            print ("Largest={}".format(max1))
            print ("Smallest={}".format(min1))
            print("Sorted{}".format(list1))
            print("Without Duplicates{}".format(list2))
            
        
        elif choice not in l:
            break
            #print(exit)
            
       