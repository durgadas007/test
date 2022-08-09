#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 00:47:53 2022

@author: dd


Print the below pattern:
    
*
**
***
****
*****    
"""

n=5
for row in range(0,n+1):
    for column in range(0,row):
        print("*", end = "")
    print("\n",end="")
