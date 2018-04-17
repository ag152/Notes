import random
import string

word_list = ["clock", "flags", "angle", "packs", "phone", "beats", "seats", "desks", "watch", "glass"]
chances = 10
word = random.choice(word_list)
print("Do you like hangman because guess what we are going to play.")
print(word)
guesses_made = []

while chances > 0:
    output = []
    for a_letter in word:
        if a_letter in guesses_made:  # guesses made = guesses previously made
            output.append(a_letter)
        else:
            output.append("*")

    print("".join(output))

    if "*" not in output:
        print('Winner')
        quit(0)

    if a_letter not in word:
        chances -= 1
        print("That is not a letter in the word.")

    if chances == 0:
        print("Too bad")