
# Put your code here
import random

name = input("What's your name? ")
print("Let's play a gessing game")

low = int(input("Select the lowest number in the range: "))
high = int(input("Select the highest number in the range: "))

random_number = random.randint(low, high)

print(f"Great{name}, I'm thnking of a number between {low} and {high}.")
print("Try to guess my number.")

guess = int(input("Your guess? "))
counter = 0
while (random_number != guess):
    counter += 1
    print("Your guess is too low, try again.") if guess < random_number else print("Your guess is too high, try again.")
    guess = int(input("Your guess? "))

print(f"Well done, {name}! You found my number in {counter} tries!")
