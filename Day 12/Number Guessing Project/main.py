from random import randint
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

"""Computer chooses a number"""
chosen_number = randint(1, 100)
#print(f"The number to guess is {chosen_number}.")

game = True
attempts = 0

"""Player chooses difficulty, which sets the number of attempts given."""
while True:
    difficulty = input("Choose a difficulty: easy or hard ").lower()
    if difficulty == "easy":
        attempts = 10
        break
    elif difficulty == "hard":
        attempts = 5
        break
    else:
        print("You did not pick a valid difficulty. Type 'easy' or 'hard'.")

print(f"You have {attempts} attempts to guess the number.")

"""Function for if a player doesn't pick the chosen number."""
def incorrect_guess():
    global attempts
    global game
    attempts -= 1
    if attempts != 0:
        print(f"You have {attempts} attempt(s) remaining to guess the number.")
    else:
        print(f"You've run out of guesses. The correct number was {chosen_number}. Refresh the page to run again.")
        game = False

"""Keeps the player guessing until the pick the number or run out of attempts."""
while game is True:
    while True:
        try:
            player_guess = int(input("Make a guess: "))
            break
        except ValueError:
            print("Invalid guess. Please enter a number between 1 and 100.")
    if player_guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
        game = False
    elif player_guess > chosen_number:
        print("Too high. \nGuess again.")
        incorrect_guess()
    elif player_guess < chosen_number:
        print("Too low. \nGuess again.")
        incorrect_guess()
