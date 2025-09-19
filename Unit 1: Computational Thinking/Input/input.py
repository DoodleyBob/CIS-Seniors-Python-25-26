'''
File Name: input.py
Author Elijah Snyder
Class: CIS Seniors
Date: 09/19/2025
'''

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("How old are you? ")
math = input("What is Pi? ")
favorite_class = input("Is this your favorite class? ")

print("Your name is " + first_name + " " + last_name + ".")
print("You are " + age + " years old.")

if favorite_class == "yes": 
    favorite_class = "True"
    print("I am happy to hear this is your favorite class!")
else:
    favorite_class = "False"
    print("GET OUT!")