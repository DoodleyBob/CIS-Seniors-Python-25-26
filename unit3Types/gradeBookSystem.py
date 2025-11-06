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
    "name": "Sophia Petel",
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
print()

def print_class_report(students):
    """Prints a formatted report for all students"""
    # Your code here
    print("=" * 30)
    print("CLASS GRADE REPORT")
    print("=" * 30)
    print("\n")

    for student in students:
        print(f"Student: {student['name']}")
        print(f"ID: {student['id']}")
        print(f"Math: {student['math_grade']}")
        print(f"English: {student['english_grade']}")
        print(f"Science: {student['science_grade']}")
        print(f"History: {student['history_grade']}")
        print(f"Average: {student['average']}")
        print("-" * 25)
        
    pass

print("\n")
def find_top_student(students):
    """Returns the student with the highest average"""
    # Your code here
    highest_average = 1
    top_student = None
    for student in students:
        if student["average"] > highest_average:
            top_student = student
            print(f"Top Student: {student["name"]}")
            print(f"Average: {highest_average}")

    pass

def count_honor_students(students):
    """Counts students with average >= 90"""
    # Your code here
    pass

# Test your functions
print_class_report(grade_book)
top_student = find_top_student(grade_book)
honor_count = count_honor_students(grade_book)
    