#from random import function_name

# Put your code here
import random
# or
# from random import function_name

random_number = random.randint(1, 100)

name = input("What's your name? ")
print(f"{name}, I'm thnking of a number between 1 and 100.")
print("Try to guess my number.")

guess = int(input("Your guess? "))
counter = 0
while (random_number != guess):
    counter += 1
    if (guess < random_number): print("Your guess is too low, try again.")
    if (guess > random_number): print("Your guess is too high, try again.")
    guess = int(input("Your guess? "))

print(f"Well done, {name}! You found my number in {counter} tries!")
    # print("Your guess is too low, try again.") if guess < random_number else print("Your guess is too high, try again.")
