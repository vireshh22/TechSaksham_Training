# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:34:02 2025

@author: admin
"""

class One:
    
    def __init__(self,name):
        self.name=name
    
    def getName(self):
        return self.name

o2 = One("abc")
print(o2.getName())