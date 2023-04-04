# Put your code here
import random

TOTAL_GUESSES = 10
player_guesses = float("inf")

type_of_game = input("Let's play a guessing game! Do you want to play or do you want the computer to play? ")

# User Guess Helper
def valid_input(string, message):
    guess_again = string

    while (not guess_again.isnumeric()):
        print("You did not enter a valid number")
        guess_again= input(message)

    guess_again = int(guess_again)
    return guess_again


def game(high_score):
    name = input("What's your name? ")
    low = input("Select the lowest number in the range: ")
    low = valid_input(low, "Select the lowest number in the range: ")
    high = input("Select the highest number in the range: ")
    high = valid_input(high, "Select the highest number in the range: ")

    random_number = random.randint(low, high)

    print(f"Great {name}, I'm thnking of a number between {low} and {high}.")
    print("Try to guess my number.")

    guess = input("Your guess? ")
    guess = valid_input(guess,"Your guess? ")

    counter = 1

    while (random_number != guess):
        counter += 1
        if (counter >= TOTAL_GUESSES):
            print("Too many tries")
            break
        print("Your guess is too low, try again.") if guess < random_number else print("Your guess is too high, try again.")
        guess = int(input("Your guess? "))

    if (counter < high_score):
        high_score = counter

    if (random_number == guess):
        print(f"Well done, {name}! You found my number in {counter} tries!")

    print(f"Your high score is {high_score} guesses.")

    play_again = input("Would you like to play again? ")
    if (play_again.lower() == "yes"): game(high_score)
    else: return

def computer_turn():
    low = int(input("Select the lowest number in the range: "))
    high = int(input("Select the highest number in the range: "))

    response = None
    while (response != "c"):
        guess = round((low + high) / 2)
        response = input(f"Here's my guess: {guess}. Is it too high or too low? ")

        if (response.lower() == "h"):
            high = guess
        elif (response.lower() == "l"):
            low = guess
        elif (response.lower() == "c"):
            break


if (type_of_game.lower() == "c"):
    computer_turn()
else:
    game(player_guesses)
