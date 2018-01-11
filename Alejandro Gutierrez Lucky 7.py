#Make a rigged gambling game so you can lose all your fictional money

#Starts off with $15 use one dollar every game (round)
#2 dice are rolled and if the sum is 7 you get your dollar and an additional $4
#Game ends when you have no more cash.


import random

Dice1 = random.randint(1, 6)
Dice2 = random.randint(1, 6)

money = 15

print("You have $%s and I will roll one dice at a time. Also it is a dollar to play one round." % money)

print("It is %s."% Dice1, "Ok time to roll the second dice." )

print("Annnnd it is %s."% Dice2)

print("In total is %s."% (Dice1 + Dice2))

if (Dice1 + Dice2) < 7:
    print("I guess luck isn't within you, now lets keep playing but first." )
    money -= 1
    print("Now you have $%s" % money)
    print("Thank you, now lets continue")

if (Dice1 + Dice2) > 7:
    print("I guess luck isn't within you, now lets keep playing but first." )
    money -= 1
    print("Now you have $%s" % money)
    print("Thank you, now lets continue")

if (Dice1 + Dice2) == 7:
    print("Would you look at that, you won.")
    money += 4
    print("Now you have $%s" % money)


