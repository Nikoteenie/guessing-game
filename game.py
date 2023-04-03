
# Put your code here
import random

TOTAL_GUESSES = 10
player_guesses = float("inf")
name = input("What's your name? ")
print("Let's play a guessing game")


def game(high_score):
    low = int(input("Select the lowest number in the range: "))
    high = int(input("Select the highest number in the range: "))

    random_number = random.randint(low, high)

    print(f"Great{name}, I'm thnking of a number between {low} and {high}.")
    print("Try to guess my number.")

    guess = int(input("Your guess? "))
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

game(player_guesses)
