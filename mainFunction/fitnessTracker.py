"""
Program: fitnessTracker.py
Author: Elijah Snyder
Date: 11/18/2025

# UNSTRUCTURED PROGRAM - Needs fixing!
print("Fitness Tracker")
print("===============")

exercise = input("What exercise did you do? ")
duration_str = input("How many minutes? ")
duration = int(duration_str)

calories_per_minute = 8  # Average
total_calories = duration * calories_per_minute

print("Exercise: " + exercise)
print("Duration: " + str(duration) + " minutes")
print("Calories burned: " + str(total_calories))

if total_calories >= 300:
    print("Great workout!")
else:
    print("Good start! Try for 30+ minutes next time.")
"""

def program_header():
    print("Fitness Tracker")
    print("===============")

def get_exercise():
    exercise = input("What exercise did you do? ")
    duration = int(input("How many minutes? "))
    return exercise, duration

def calories_burned(duration):
    calories_per_minute = 8  # Average
    total_calories = duration * calories_per_minute
    return total_calories

def analyze_calories(total_calories):
    if total_calories >= 300:
        print("Great workout!")
    else:
        print("Good start! Try for 30+ minutes next time.")

def summary_report(exercise, duration, total_calories):
    print("\n=== Fitness Summary ===")
    print("Exercise: " + exercise)
    print("Duration: " + str(duration) + " minutes")
    print("Calories burned: " + str(total_calories))

def main():
    program_header()
    # Collect Information
    exercise, duration = get_exercise()
    calories = calories_burned(duration)
    # Display Results
    summary_report(exercise, duration, calories)


if __name__ == "__main__":
    main()