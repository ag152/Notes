# Generate a number
# Ask the user for an input(number)
# Does the guess match the number?
# Add "Higher" and "Lower"
# Add 5 guesses


import random

guessesTaken = 0
number = random.randint(1, 20)

global guess


while guessesTaken < 5:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
     print("Your guess is too low.")

    if guess > number:
     print("Your guess is too high.")

    if guess == number:
     break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good job.")

if guess != number:
    number = str(number)
    print("You lost.")


print("It was %s." % number)


