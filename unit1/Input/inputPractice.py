'''
File Name: inputPractice.py
Author: David Wells
Class: CIS Seniors
Date: 09/19/2025

Ask:
First Name
Last Name
Favorite Color
First Number
Second Number 
Favorite TV Show
Favorite Movie
Favorite Song
Favorite Food

- Write out a paragraph outlining the user data using variables. Using the First
 and second numbers, create 3 seperate math equations, and print out the values from the expressionss.
'''

first_name = input("Enter first name: ")
last_name = input("Enter your last name: ")
favorite_color = input("What is your favorite color? ")
first_number = int(input("Enter a number 1 - 1000: "))
second_number = int(input("Enter another number 1 - 1000: "))
favorite_show = input("What is your favorite tv show? ")
favorite_movie = input("What is your favorite movie? ")
favorite_song = input("What is your favorite song? ")
singer = input("Who made your favorite song? ")
favorite_food = input("What is your favorite food? ")
answer_one = first_number + second_number
answer_two = first_number * second_number
answer_three = first_number / second_number

print("Hello my name is " + first_name + " " + last_name + ", my favorite color is " + favorite_color + ". Also my favorite TV show is " + favorite_show + ", and my favorite movie is " + favorite_movie + ". I really like the song " + favorite_song + " made by " + singer + ", and when I am hungry I love to eat " + favorite_food + "!")

print(answer_one)
print(answer_two)
print(answer_three)

