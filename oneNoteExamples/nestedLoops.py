"""
Program to print all two-letter domain names.

ord('a') --> take a character and return the ASCII #
chr(97) --> takes an ASCII # and gives you it's character
"""

print("\n\nTwo-letter domain names:")

letter1 = "a"
letter2 = "?"

while letter1 <= "z":   # Outer Loop
    letter2 = "a"
    while letter2 <= "z":   # Inner Loop
        print(f"{letter1}{letter2}.com")
        letter2 = chr(ord(letter2) + 1)    # Protects us from infinite loop
    letter1 = chr(ord(letter1) + 1)     # Protects us from infinite loop