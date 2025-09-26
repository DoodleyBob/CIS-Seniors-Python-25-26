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
totalCorrect = 0
for question in range(int(test)):
    answer = int(input("Question " + str(question + 1) + ": "))
    if answer == 0:
        print("Incorrect ")
    elif answer == 1:
        print("Correct")
        totalCorrect += 1
    else:
        print("Invalid input, please enter either a 1 or a 0! ")

print("\n")
print("=" * 25)
print("QUIZ RESULTS FOR ", name)
print("=" * 25)
print("Correct Answers:", totalCorrect, "/",test)
quizPercentage = float((totalCorrect / test) * 100)
print("Quiz Percentage: ",quizPercentage,"%")
if quizPercentage < 70.0:
    print("Final Status: FAIL :(")
elif quizPercentage >= 70.0:
    print("Final Status: PASSED :D")

print("=" * 25)