#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:58:10 2018

@author: Yunrong
"""

yours = ['Yale','MIT','Berkeley']
mine = ['Yale','Harvard','Princeton']
ours1=  mine + yours 
ours2 = []
ours2.append(mine)
ours2.append(yours)
print(ours1)
print(ours2) 
#Difference: The ours1 is one new list while ours2 are two lists added together

yours[1]='CMU'
print(ours1)
print(ours2)
#our1 didn't change because 