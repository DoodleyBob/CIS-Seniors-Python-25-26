'''
Grade Book System

Program: gradeBookSystem.py
Author: Elijah Snyder
Date: 11/04/2025
'''

# Student 1
student1 = {
    "name": "Emma Rodriguez",
    "id": "S12345",
    "math_grade": 95,
    "english_grade": 91,
    "science_grade": 92,
    "history_grade": 89,
    "average": 91.75
}

# Student 2
student2 = {
    "name": "Marcus Chen",
    "id": "S12346",
    "math_grade": 87,
    "english_grade": 90,
    "science_grade": 85,
    "history_grade": 88,
    "average": 87.50
}

# Student 3
student3 = {
    "name": "Emma Rodriguez",
    "id": "S12347",
    "math_grade": 98,
    "english_grade": 96,
    "science_grade": 94,
    "history_grade": 87,
    "average": 96.25
}

grade_book = [
    student1,
    student2,
    student3
]

def print_class_report(students):
    """Prints a formatted report for all students"""
    # Your code here

    pass

def find_top_student(students):
    """Returns the student with the highest average"""
    # Your code here
    pass

def count_honor_students(students):
    """Counts students with average >= 90"""
    # Your code here
    pass

# Test your functions
print_class_report(grade_book)
top_student = find_top_student(grade_book)
honor_count = count_honor_students(grade_book)
    