import random
import string

light = ["clock", "flags", "angle", "packs", "phone", "beats", "seats", "desks", "watch", "glass"]
chances = 10
letters = string.ascii_lowercase
word = random.choice(light)
print("Do you like hangman because guess what we are going to play.")
print(word)
guesses_made = list(string.punctuation + " ")
while chances > 0:

    print("These are your letters, %s" % letters)
    a_letter = input("Put any letter you want.")
    output = []
    for a_letter in word:
        if a_letter in guesses_made:
            output.append(a_letter)
        if a_letter not in word:
            chances -= 1
            print("That's not it, you got this many %s chances left." % chances)
    if chances == 0:
        print("Sorry but you lost.")
print(.join (output))
