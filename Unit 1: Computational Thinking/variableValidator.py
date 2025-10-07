# Python Variable Name Validator
# Student Name: Elijah Snyder
# Date: 10/07/2025

# List of Python keywords
python_keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield'
]

invalid_char = [
    '@', '#', '!', '-'
]

# Display welcome message
print("=== PYTHON VARIABLE NAME VALIDATOR ===")
print("This program checks if your variable name is valid in Python.")
print()


# Get user input
variable_name = input("Enter a variable name to validate: ")
first_char = variable_name[0]
last_char = variable_name[-1]

if variable_name == " ":
    print("Invalid variable name, reason: variable contains nothing.")

elif variable_name == python_keywords:
    print("Invalid variable name, reason: Is a python keyword.")

elif variable_name.isdigit(first_char) == True:
    print("Invalid variable name, reason: The first character in a variable CANNOT be a digit.")

elif variable_name.isdigit(first_char) == False:
    for char in variable_name:
        if char == invalid_char:
            print("Invalid variable name, reason: Contains invalid character.")
        
else:
    print("VALID, you have entered a valid variable name!")


# Your validation code goes here
# Check each rule and provide appropriate feedback