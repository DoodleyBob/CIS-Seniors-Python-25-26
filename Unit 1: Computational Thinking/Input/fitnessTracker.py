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

name = input("Your Name: ")
age = int(input("Your Age: "))
weight_in_lbs = float(input("Weight in lbs: "))
height_in_inches = int(input("Height in inches: "))
weekly_exercise_hours = float(input("How many hours do you work out in a week? "))
fitness_goal = str(input("What is your fitness goal? "))

#Calculations

bmi = (weight_in_lbs / (height_in_inches * height_in_inches)) * 703
daily_exercise_minutes = (weekly_exercise_hours * 60) / 7
weekly_calories_burned = weekly_exercise_hours * 300

print("Hello " , name , ", if you are" , age , " years old, weight " , weight_in_lbs, "lbs, are " , height_in_inches , " inches tall, workout for " , weekly_exercise_hours , "and have a fitness goal of, " , fitness_goal , " you will have burned " , weekly_calories_burned , " calories, have a bmi of " , bmi , ", and you would have worked out for " , daily_exercise_minutes , " minutes a day.")
