
from art import logo
import random


def play_game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")

    difficulty = input("Type a difficulty level, type 'easy' or 'hard' \n : ")

    no_of_attempts = 5
    if difficulty == 'easy' or difficulty == 'e':
        no_of_attempts += 5
    correct_number = random.randint(1, 100)

    while no_of_attempts > 0:
        print("You have {0} attempts to guess the number".format(no_of_attempts))
        response = int(input("Make a guess : "))

        if response in range(1, 101):
            if response == correct_number:
                print("You guessed it right, you win!")
                no_of_attempts = 0
            elif response < correct_number:
                print("Too low, guess again : ")
            elif response > correct_number:
                print("Too high, guess again : ")
        else:
            print("Please enter a valid input, any number from 1 to 100")

        no_of_attempts -= 1
        if no_of_attempts == 0:
            print("You did not guess it right, you lose the game 😱")


while input("Do you wish to play the game? Type 'y' or 'n'. \n :  ") == 'y':
    play_game()
