class Item(object):
    def __int__(self, description):
        self.description = description


class Weapon(Item):
    def __int__(self, description, damage, name):
        super(Weapon, self).__int__(description, 0, name)
        self.damage = damage
        self.name = name


class Melee(Weapon):
    def __int__(self, description, damage, name):
        super(Melee, self).__int__(description, 0, name)


class Ranged(Weapon):
    def __int__(self, description, damage, name):
        super(Ranged, self).__int__(Pistol, description, 0)
        self.Pistol = Pistol


class Pistol(Ranged):
    def __int__(self, description, damage, name):
        super(Pistol, self).__int__('It is a 1911 pistol from ww2 and it is still in good condition.'
                                    ' and it has 30 bullets per clip.', 140, '1911')

    def shoot(self):
        shoot = input
        ammo = 30
        if input == shoot:
            ammo = - 1
            print('*gun shot sound*')
        if ammo == 0:
            print('I have no more ammo.')


class Sawclever(Melee):
    def __int__(self, description, damage, name):
        super(Sawclever, self).__int__('It is a blade with rigged edges.', 260, 'Sawclever')


class Yeetsword(Melee):
    def __int__(self, description, damage, name):
         super(Yeetsword, self).__int__('It is a long blade made out of some kind of metal.', 1000, 'Yeetsword')


class Brickward(Melee):
        def __int__(self, description, damage, name):
            super(Brickward, self).__int__('It is just a giant brick on a graphene rod', 450, 'Brickward')


class Potion(Item):
    def __int__(self, description, heal):
        super(Potion, self).__int__('It is a small teal vial that has a red plus sign.')
        self.heal = heal

    def drink(self):
        hp += 200


class Gascan(Item):
    def __int__(self, description):
        super(Gascan, self).__int__('It is a gas can and there is only a bit of gas left.')


class Flashlight(Item):
    def __int__(self, description):
        super(Flashlight, self).__int__('It is a flashlight and it seems to run with one battery.')


class Battery(Item):
    def __int__(self, description):
        super(Battery, self).__int__('It is a small battery.')


class Ring(Weapon):
        def __int__(self, description, damage, name):
            super(Ring, self).__int__('It is a custom black ring.', 1000000, 'Ring')