# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:36:45 2025

@author: admin
"""

class Workout:
    
    workoutList = {}
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        with open(name + ".txt", "w") as file:
            file.write("{}'s file\n" .format(name))
    
    def addWorkout(self, work, calories):
        Workout.workoutList[work] = calories
        print("Added workout: {} with {} calories burned" .format(work, calories))
        
    def viewWorkout(self):
        print("\n{}'s Workout List:" .format(self.name))
        for work, calories in Workout.workoutList.items():
            print("{}: {} calories" .format(work,calories))
    
    def saveData(self):
        with open(self.name + ".txt", "a") as file:
            file.write("\nWorkout Data:\n")
            for work, calories in Workout.workoutList.items():
                file.write("{}: {} calories\n" .format(work,calories))
        print("Data saved to file")
    
    def loadData(self):
        try:
            with open(self.name + ".txt", "r") as file:
                data = file.read()
            print("\nLoaded Data:")
            print(data)
        except FileNotFoundError:
            print("File not found")

person = Workout("Virat", 36, 75)
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