# Take damage, status affect, perform action, health, pick u p items, attack, death, move?, descripition, status effect
class Character(object):
    def ___int___(self, hp, attack, status, death, name ):
        self.hp = hp
        self.attack = attack
        self.status = status
        self.death = False
        self.name = name

    def name(self):
        name = input('>_')
        print("What is your? Hello %s." % name)


    def hp(self):
        hp = 2000
        if hp == 0:
            print('You died')

    def suicide(self):
        hp -= 100000000
        print("%s committed suicide.")