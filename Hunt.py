# Take damage, status affect, perform action, health, pick u p items, attack, death, move?, descripition, status effect
class Character(object):
    def ___int___(self, hp, attack, status, death, name):
        self.hp = hp
        self.attack = attack
        self.status = status
        self.death = false
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


class Item(object):
    def __int__(self, description):
        self.description = description


class Weapon(Item):
    def __int__(self, description, damage, ):
        super(weapon, self).__int__(damage, description)


class Melee(Weapon):
    def __int__(self, description, damage):
        super(melee, self).__int__(description, damage, 'Sword of the Great One', 'Saw Clever', 'Brickward',)


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


class Yeetsword(Melee):
    def __int__(self, description, damage):
        super(sawclever, self).__int__(description, damage)
        damage = 1000
        description = 'A sword forged by the blood of a great one.'


class Brickward(Melee):
        def __int__(self, description, damage):
            super(sawclever, self).__int__(description, damage)
            damage = 350
            description = 'It is just a giant brick on a graphene rod.'


class Potion(Item):
    def __int__(self, description, heal):
        super(heal, self).__int__(description, heal)
        description = 'It is a small teal vial that has a red plus sign'

    def drink(self):
        hp += 100


class Gascan(Item):
    def __int__(self, description):
        super(Gascan, self).__int__(description)
        description = 'It is a gas can and there is only bit gas left in it'

class Flashlight(Item):
    def __int__(self, description):
        super(flashlight, self).__int__(description)
        description = 'It is a small flashlight that uses one battery.'

class Battery(Item):
    def __int__(self, description):
        super(Battery, self).__int__(description)
        description = 'It is small battery.'


class Room(object):
    def __init__(self, name, description, north, south, west, east, up, down, item):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.up = up
        self.down = down
        self.item = item

    def move(self, direction):
     global current_node
     current_node = globals()[getattr(self, direction)]



northofhouse = Room('North of House',
                    'There nothing to interesting here.',
                    None, None, 'westofhouse', 'garage', None, None, None)
garage = Room("Garage",
              "there is a car with keys inside. Also there is a a fruit bowl.",
              None, None, 'northofhouse', None, None, None, None)
westofhouse = Room("West of House",
                   "You are west of the house and there something on the floor",
                   None, 'southofhouse', None, 'northofhouse', None, None, Sawclever)
southofhouse = Room("South of House",
                    "There is a window that can be opened and there is a path going south.",
                    'westofhouse', 'paths', 'dinerroom', None, None, None, None)
dinerroom = Room("Dinning Room",
                 "You are in an old dinning room and there are small piles of dust.",
                 None, None, 'southofhouse', 'kitchen', None, None, Potion)
kitchen = Room("Kitchen",
               "There is quite a look of cooking materials.",
               'livingroom', None, 'dinerroom', None, None, None, Potion)
living_room = Room("Living Room",
                   "There is a note here, a flashlight and six batteries. there seems to be a another door.",
                   'northofhouse', 'kitchen', 'basement', None, None, None, Flashlight)
basement = Room("Basement",
                'There is a bunch of boxes, laundry and dryer machine.',
                None, 'workshop', None, 'livingroom', None, None, Potion)
workshop = Room("Work Shop",
                'There is a bunch of power tools and scrap metal, but nothing too important.',
                'Basement', None, 'West Passage', None, None, None, Brickward)
westpassage2 = Room('West Passage',
                    'Its a narrow passage that keeps going west.',
                    None, None, 'westpassge', 'workshop', None, None, None)
westpassage = Room('West Passage',
                   'It looks like a different place up ahead.',
                   None, None, 'tunnel2', 'westpassage2', None, None, None)
tunnel2 = Room('West Tunnel',
               'It look like a old tunnel system',
               None, None, 'westpassage', 'maintunnel', None, None, None)
maintunnel = Room('Main Tunnel',
                  'There is machete on the old self and there is old rusty tools.',
                  'northtunnel', None, 'westtunnel', 'easttunnel', 'insideofshed', None, None)
insideofshed = Room('Inside of Shed',
                    'It is a small shed there is not much here.',
                    None, 'shed', None, None, 'maintunnel', None, None)
shed = Room('Shed',
            'Its a small shed in a forest',
            'insideofshed', 'forest2', None, None, None, None, None)
forest2 = Room('Forest',
               'It seems a like a forest that leads two ways.',
               'shed', None, 'forest', 'deepforest', None, None, None)
deepforest = ('Deep Forest',
              'This the deep part of the forest to be a building but blocked by fallen tress.',
              None, None, 'forest2', None, None, None)
forest = Room('Forest',
              'It seems its the beginning of the woods.',
              None, None, 'paths', 'forest2', None, None, None)
paths = Room('Paths',
             'It seems there are four rock pathways.',
             'southofhouse', 'mountains', 'river', 'forest', None, None, Potion)
mountains = Room('Mountains',
                 'It is a nice view of the city from here.',
                 'paths', None, None, None, None, None, Potion)
river = Room('River',
             'Its a that keeps going.',
             None, None, 'river2', 'paths', None, None, Potion)
river2 = Room('River',
              'The river keeps getting narrow and there is a cavern',
              'cavern', None, 'endofriver', 'river', None, None, Potion)
cavern = Room('Cavern',
              'There a big guy with a medium bolder protecting a chest.',
              None, 'river2', None, None, None, 'Lab', None)
endofriver = Room('End of the river',
                  'It ends here and I cannot going but there is a beast behind a boulder',
                  None, None, None, 'river2', None, None, Battery)
Lab = Room('Lab',
           'There is a panel here with three buttons the first is destroy mobs, the second is teleport to room'
           'and the third one is a nuke.',
           None, None, None, None, 'cavern', None, Yeetsword)


current_node = northofhouse
directions = ['North', 'South', 'East', 'West', 'Up', 'Down']
short_directions = ['N', 'S', 'E', 'W', 'U', 'D']

while True:
    print(current_node.name)
    print(current_node.description)
#print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    elif command in directions:
        try:
            current_node.move(command)
        except KeyError:
             print('You cannot go this way.')
    else:
        print('Command not recognized')