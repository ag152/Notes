class Item(object):
    def __int__(self, description):
        self.description = description


class Weapon(item):
    def __int__(self, description, damage):
        super(weapon, self).__int__(damage, description)


class Melee(Weapon):
    def __int__(self, description, damage):
        super(melee, self).__int__('Sword of the Great One', 'Saw Clever', 'Brickward', description, damage)


class Ranged(Weapon):
    def __int__(self, description, damage):
        super(ranged, self).__int__('Pistol', description, damage)


class Pistol(Ranged):
    def __int__(self, description, damage):
        super(Pistol, self).__int__(description, damage)
        description = 'It seems it only has 30 bullets'
        damage = 140
        ammo = 30
        if input == shoot:
            ammo = - 1
            print('*gun shot sound*')
        if ammo == 0:
            print('I have no more ammo.')


class Sawclever(Melee):
    def __int__(self, description, damage):
        super(sawclever, self).__int__(description, damage)
        description = 'It has a rigged spikes.'
        damage = 160


class Softgo(Melee):
    def __int__(self, description, damage):
      super(sawclever, self).__int__(description, damage)
      damage = 1000
      description = 'A sword forged by the blood of a great one.'


class Brickward(Melee):
        def __int__(self, description, damage):
            super(sawclever, self).__int__(description, damage)
            damage = 350
            description = ('It is just a giant brick on a titanium rod.')


class Potion(item):
    def __int__(self, description, heal):
        super(heal, self).__int__(description, heal)
        description = 'It is a small teal vial that has a red plus sign'

    def drink(self):
        hp += 100


class Gascan(item):
    def __int__(self, description):
        super(Gascan, self).__int__(description)
        description = 'It is a gas can and there is only bit gas left in it'