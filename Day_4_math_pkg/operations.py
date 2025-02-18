# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:34:50 2025

@author: admin
"""

def multiply(a,b):
    return a*b

def division(a,b):
    if a==0 or b==0:
        return ValueError("Can't divide by zero")
    return a//b

class operation:
    def __init__(self,pi):
        self.pi=pi
        
    
