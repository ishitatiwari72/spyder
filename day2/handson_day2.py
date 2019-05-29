# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:20:53 2019

@author: HP
"""

list1=list(range(20))


print(list1[::2])
print(list1[1::2])


year=int( input("enter the year"))
if year % 4 == 0 :
    print("leap year")
else:
        print("regular year")
        
        
        
def days_in_month():
    m=int(input("enter the month"))
    y=int(input("enter the year"))
    if(m==2):
        if(y%4==0 ):
            day=29
            return day
        else:
            day=28
            return day
    else:
        if (m%2==0 and m!=8):
            day=31
            return day
        else:
            day=30
        return day
    
        
        