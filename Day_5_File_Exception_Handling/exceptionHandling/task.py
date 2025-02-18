# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:03:19 2025

@author: admin
"""

def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return "An unknown error occurred: {}" .format(e)

file_path = input("Enter the file path: ")
content = read_file_contents(file_path)
print(content)
