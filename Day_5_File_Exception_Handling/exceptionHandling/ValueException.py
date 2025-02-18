# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:11:54 2025

@author: admin
"""

class Exception3:
        
    def checkValue(self):
        try:
            value  = int(input("Enter a value: "))
            result = 10 + value
            print(result)
        except ValueError:
            print("Inappropriate Value Entered")
            
e = Exception3()
e.checkValue()