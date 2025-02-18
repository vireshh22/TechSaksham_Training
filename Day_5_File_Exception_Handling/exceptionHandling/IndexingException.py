# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:09:17 2025

@author: admin
"""

class Exception2:
    
    def __init__(self,list1):
        self.list1=list1
        
    def checkValue(self,index):
        try:
            print(self.list1[index])
        except IndexError:
            print("Index out bound!")

e = Exception2([1,2,3,4,5])
e.checkValue(7)