'''
File Name: qradeTracker.py
Author: Elijah Snyder
Class: CIS Seniors
Date: 10/1/2025
'''

print("=" * 25)
print("\t\tGRADE TRACKER SYSTEM")
print("=" * 25)
print("Welcome to the Grade Tracker!")
print("This program will help you analyze student grades.")

numStudents = int(input("How many students are in your class? (1-10)"))
if numStudents < 1 or numStudents > 10:
    print("ERROR, number of students must be a number 1 - 10.")

else:
    print("\n\nPlease enter student information:")

print("-" * 20)
student = 0
for student in range(int(numStudents)):
    print("Student #", str(student + 1), ":")
    studentName = input("Enter student name: ")
    score = int(input("Enter student score: "))

print("\n\n")
print("=" * 25)
print("\t\tGRADE ANALYSIS RESULTS")
print("=" * 25)

print("Class Summary:")
print("\tTotal Students: ", numStudents)
totalPoints = 0
for totalPoints in range((score * student) * 10):
    print("Total Points: ", float(totalPoints))
