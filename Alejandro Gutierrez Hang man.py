import random
import string

light = ["clock", "flags", "angle", "packs", "phone", "beats", "seats", "desks", "watch", "glass"]
chances = 10
letters = string.ascii_lowercase
word = random.choice(light)
print("Do you like hangman because guess what we are going to play.")
# print(word)

while chances != 0:

    print("These are your letters, %s" % letters)
    a_letter = input("Put any letter you want.")
    if a_letter == word:
        print("Nice.")

    if a_letter != word:
        chances -= 1
        print("Nice try but you got %s chances left."% chances)
    if chances == 0:
        print("Sorry but you lost.")


