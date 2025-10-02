'''
File: luckyNumber.py
Author: Elijah
Class CIS Seniors
Date: 10/2/31
'''

import random

# Game statistics
total_rounds = 0
total_wins = 0
total_guesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

# Main game loop - play multiple rounds
# TODO: Use while True loop with break statement here
while True: 
    break

    # Generate random lucky number
    # TODO: Use random.randint() to generate number between 1 and 50
luckyNum = random.randint(1, 50)
    # Set maximum attempts
    # TODO: Set max_attempts to 7
max_attempts = 7
    # Initialize attempt counter
    # TODO: Create attempts variable starting at 0
attempts = 0

print(f"\nRound {total_rounds + 1}")
print("I'm thinking of a lucky number between 1 and 50...")
print(f"You have {max_attempts} attempts to guess it!")
print()
   
    # Guessing loop - count-controlled while loop
    # TODO: Use while loop that continues while attempts < max_attempts
while attempts < max_attempts:
    
        # Get user's guess
        # TODO: Get input and convert to integer
    user_guess = int(input("Enter a guess: "))
        # Increment attempt counter
        # TODO: Add 1 to attempts
    attempts += 1
        # Check if guess is correct
        # TODO: Compare guess to lucky_number
    if user_guess < lucky_number:
        print("Too low, try again!")
    elif user_guess > lucky_number:
        print("Too high, try again!")
    else:
        print("Congratulations! You managed to guess the number! :)")
            # Player wins!
            # TODO: Display success message
            # TODO: Update statistics
            # TODO: Break out of guessing loop
        total_guesses = attempts
        print("Guesses made: ", total_guesses)   
        total_rounds += 1
        print("Round played: ", total_rounds)
        total_wins += 1
        print("Rounds won: ", total_wins)
        
        break
        # Provide hints
        # TODO: Tell user if guess is too high or too low
       
    # If loop completes without break, player lost
    # TODO: Handle case where player runs out of attempts
    if attempts > max_attempts:
        print("Oh no, you've lost!")
    # Display round statistics
        print("Guesses made: ", total_guesses)
        print("Rounds played: ", total_rounds)
        print("Rounds won: ", total_wins)
    # TODO: Show attempts used, win/loss for this round
    
    # Ask if player wants to play again
    # TODO: Get input and check if user wants to continue
    # TODO: Use break statement to exit main game loop if done

# Display final statistics
# TODO: Show total rounds, wins, and average guesses per round

print("\nThanks for playing! Goodbye!")