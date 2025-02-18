# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:16:55 2025

@author: admin
"""

class Exception4:
    
    def typeMethod(self):
        try:
            value = input("Enter a number: ")
            result = 10 + value
            print(result)
        except TypeError:
            print("The type of entered value is not appropriate..")

e = Exception4()
e.typeMethod()