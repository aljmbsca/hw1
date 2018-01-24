#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:52:21 2018

@author: Yunrong
"""
#Q3
#Iterative
def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
    
print(sum(100))

#Recursive
def sum_1(n):
    if (n == 1):
        return 1
    else: 
        return n+sum_1(n-1)
print(sum_1(100))