# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:35:28 2025

@author: admin
"""

class Sample:
    
    workoutList = {}
    
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        with open(name + ".txt","w") as file:
            file.write("{}'s file\n" .format(name))
        
    def addWorkout(self,work,calories):
        Sample.workoutList[work]=calories
        print("Added workout")
    
    def viewWorkout(self):
        print("{}'s Workout List:" .format(self.name))
        for work, calory in Sample.workoutList.items():
            print("{} : {}" .format(work,calory))
    
    def saveData(self):
        with open(self.name + ".txt","a") as file:
            for work,calory in Sample.workoutList.items():
                file.write("{} : {} calories" .format(work,calory))
            print("Data Saved!")
    
    def loadData(self):
        try:
            with open(self.name + ".txt","r") as file:
                data = file.read()
            print("Data loaded:")
            print(data)
        except FileNotFoundError:
            print("File not found!")
            
            
person = Sample("bzc", 26, 65)
while True:
    print("1.Add Workout\n2.View Workouts\n3.Save Data\n4.Load Data\n5.Exit\nEnter Your Choice:")
    choice = int(input())
    
    if choice == 1:
        name = input("Enter workout name:")
        calory = input("Enter calories burned:")
        person.addWorkout(name, calory)
    elif choice == 2:
        person.viewWorkout()
    elif choice == 3:
        person.saveData()
    elif choice == 4:
        person.loadData()
    elif choice == 5:
        exit(1)
    else:
        break