'''
File Name: quizScorer.py
Author: Elijah
Course: CIS Seniors
Date 09/25/25
'''

name = input("Student Name: ")
test = int(input("How many questions are on the quiz? (5-10) "))
print("Scoring quiz for " + name + " has ", test , "questions.")

print("Enter student's aswers (1 for true, 0 for false")
for question in range(test):
    answer = int(input("Question " + str(question + 1) + ": "))
    if answer == 0:
        print("Incorrect ")
    elif answer == 1:
        print("Correct")
    else:
        print("Invalid input, please enter either a 1 or a 0! ")


totalCorrect = 0

print("\n\n")
print("=" * 30)
print("Quiz results: ")
print("=" * 30)

score = totalCorrect / int(test) * 100
print(name + " got ", totalCorrect , "questions correct.")
print(name + " got a score of ", score ,"%")

if score >= 70:
    print("You passed the quiz!")
elif score < 70:
    print("You failed your quiz :(")