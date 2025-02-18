# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:54:49 2025

@author: admin
"""

class Exception1:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def division(self):
        try:
            result = self.a / self.b
            print("Result: {}" .format(result))
        except ZeroDivisionError:
            print("The value of b should not be zero..")
        else:
            print("When exception doesn't occurs")
        finally:
            print("Finally block executes whether exception occurs or not..")
        
e = Exception1(10,0)
e.division()