'''
File Name: fitnessTracker.py
Author: Elijah Snyder
Class: CIS Seniors
Date: 09/23/25

Requirements:
Collects the user's personal fitness information
Stores all data in appropriately named variables
Performs calculations on the collected data
Displays a formatted fitness report
'''

name = input("What is your name? ")
age = int(input("What is your age? "))
weight_in_lbs = float(input("What is your weight in lbs? "))
height_in_inches = int(input("What is your height in inches? "))
weekly_exercise_hours = float(input("How many hours do you work out per week? "))
fitness_goal = str(input("What is your main fitness goal? "))
bmi = (weight_in_lbs / (height_in_inches * height_in_inches)) * 703
daily_exercise_minutes = (weekly_exercise_hours * 60) / 7
weekly_calories_burned = weekly_exercise_hours * 300
print("\n\n")

#Calculations
print("=" * 25)
print("\tFitness report for " , name)
print("=" * 25)
print("\n\n")

print("PERSONAL INFORMATION:")
print("Name: " , name)
print("Age: ", age , " years old")
print("Weight: " , weight_in_lbs , "lbs")
print("Height: " , height_in_inches)
print("\n\n")

print("FITNESS METRICS:")
print("BMI: " , bmi)
print("Weekly Exercise: " , weekly_exercise_hours , " hours")
print("Daily Exercise: " , daily_exercise_minutes , " minutes per day")
print("Estimated Weekly Calories Burned: " , weekly_calories_burned , " calories")
print("\n")
print("Fitness Goal: " , fitness_goal)
print("\n\n")
print("Keep up the great work with your fitness journey!")
print("=" * 25)