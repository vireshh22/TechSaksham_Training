# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:37:56 2025

@author: admin
"""

def readFile(fileName):
    with open(fileName,'r') as file:
        content = file.read()
        print(content)
        
def writeFile(fileName):
    with open(fileName,'w') as file:
        file.write("abcdefghijklmnopqrstuvwxyz")
        
def appendInFile(fileName):
    with open(fileName,'a') as file:
        file.write("1234567890")

PLACEHOLDER = "[name]"

# Reading names from the file
with open("sample.txt", 'r') as names_list:
    names = names_list.readlines()

# Reading the letter template
with open("starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()

# Generating personalized letters
for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

    # Writing the personalized letter to a new file
    with open(f"letter_for_{stripped_name}.docx", 'w+') as completed_letter:
        completed_letter.write(new_letter)