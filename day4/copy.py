# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:45:33 2019

@author: HP
"""

file1 = open("new.txt", "rt")
fp= file1.read()
file2 = open('new1.txt', mode='wt')
file2.write(fp)
file2.close()
file1.close()