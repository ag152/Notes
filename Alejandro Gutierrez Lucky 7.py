import random

round = 0
money = 15
print("You have $%s and I will roll one dice at a time. Also it is a dollar to play one round." % money)

while money > 0:
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    roll = (Dice1 + Dice2)

    print("Lets start.")
    print("It is %s."% roll)
    if (Dice1 + Dice2) == 7:
        print("Would you look at that, you won.")
        money += 4
        print("Now you have $%s" % money)
        round += 1
    if (Dice1 + Dice2) != 7:
        print("I guess luck isn't within you.")
        money -= 1
        print("Now you have $%s" % money)
        round += 1

print("You played this many %s rounds." % round)



