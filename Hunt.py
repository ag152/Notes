# Take damage, status affect, perform action, health, pick u p items, attack, death, move?, descripition, status effect
class Character(object):
    def ___int___(self, hp, attack, status, death, name):
        self.hp = hp
        self.attack = attack
        self.status = status
        self.death = death
        self.name = name

    def name(self):
        name = input('>_')
        print("What is your? Hello %s." % name)

    def hp(self):
        hp = 20000
        if hp == 0:
            print('You died')

    def suicide(self):
        hp =2000
        hp -= 10000000
        print("You turn into a frog and kermit suicide.")


class Item(object):
    def __int__(self, description):
        self.description = description


class Weapon(Item):
    def __int__(self, description, damage, name ):
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
        ammo = 30

    def shoot(self):
        shoot = input
        if input == shoot:
            ammo =- 1
            print('*gun shot sound*')
        if ammo == 0:
            print('I have no more ammo.')


class Sawclever(Melee):
    def __int__(self, description, damage):
        super(Sawclever, self).__int__(description, damage)
        description = 'It has a rigged spikes.'
        damage = 160


class Yeetsword(Melee):
    def __int__(self, description, damage):
       super(Yeetsword, self).__int__(description, damage)
    damage = 1000
    description = 'A sword forged by the blood of a great one.'


class Brickward(Melee):
        def __int__(self, description, damage):
            super(Brickward, self).__int__(description, damage)
            damage = 350
            description = 'It is just a giant brick on a graphene rod.'


class Potion(Item):
    def __int__(self, description, heal):
        super(Potion, self).__int__(description, heal)
        description = 'It is a small teal vial that has a red plus sign'

    def drink(self):
        hp += 100


class Gascan(Item):
    def __int__(self, description):
        super(Gascan, self).__int__(description)
        description = 'It is a gas can and there is only bit gas left in it'


class Flashlight(Item):
    def __int__(self, description):
        super(Flashlight, self).__int__(description)
        description = 'It is a small flashlight that uses one battery.'


class Battery(Item):
    def __int__(self, description):
        super(Battery, self).__int__(description)
        description = 'It is small battery.'


class Ring(Weapon):
        def __int__(self, description, damage):
            super(Ring, self).__int__(description, damage)
            description = 'It seems like a normal ring.'
            damage = 10000000


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
                    'There nothing too interesting here.',
                    None, None, 'westofhouse', 'garage', None, None, None)
garage = Room("Garage",
              "there is a car with keys inside. Also there is a a fruit bowl.",
              None, None, 'northofhouse', None, None, None, None)
westofhouse = Room("West of House",
                   "You are west of the house and there something on the floor",
                   None, 'southofhouse', 'westway', 'northofhouse', None, None, Sawclever)
southofhouse = Room("South of House",
                    "The back door is open but there is another path.",
                    'westofhouse', 'paths', 'dinerroom', None, None, None, None)
dinerroom = Room("Dining Room",
                 "You are in an old dinning room and there are small piles of dust.",
                 None, None, 'southofhouse', 'kitchen', None, None, Potion)
kitchen = Room("Kitchen",
               "There is quite a lot of cooking materials.",
               'livingroom', None, 'dinerroom', None, None, None, Potion)
living_room = Room("Living Room",
                   "There is a note here, a flashlight and six batteries. there seems to be a another door.",
                   'northofhouse', 'kitchen', 'basement', None, None, None, Flashlight)
basement = Room("Basement",
                'There is a bunch of boxes, laundry and dryer machine.',
                None, 'workshop', 'livingroom', None, None, None, Potion)
workshop = Room("Work Shop",
                'There is a bunch of power tools and scrap metal, but nothing too important.',
                'Basement', None, 'eastpassage', None, None, None, Brickward)
westpassage2 = Room('East Passage',
                    'Its a narrow passage.',
                    None, None, 'westpassge', 'westtunnel', None, None, None)
westpassage = Room('East Passage',
                   'Its a narrow passage.',
                   None, None, 'workshop', 'westpassage2', None, None, None)
westtunnel = Room('East Tunnel',
                  'It looks like a old tunnel system',
                  None, None, 'westpassage', 'maintunnel', None, None, None)
maintunnel = Room('Main Tunnel',
                  'There is old rusty tools.',
                  'northtunnel', None, 'westtunnel', 'easttunnel', 'insideofshed', None, None)
insideofshed = Room('Inside of Shed',
                    'It is a small shed there is not much here.',
                    None, 'shed', None, None, None, 'maintunnel', None)
shed = Room('Shed',
            'Its a small shed in a forest',
            'insideofshed', 'forest2', None, None, None, None, None)
forest2 = Room('Forest',
               'It seems a like a forest that leads two ways.',
               'shed', None, 'forest', 'deepforest', None, None, None)
deepforest = Room('Deep Forest',
                  'There is a building but it is completely cut by fallen trees.',
                  None, None, 'forest2', None, None, None, None)
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
           'It looks like they use to do experiments here and there is a sword on a pedestal.',
           None, None, None, None, 'cavern', None, Yeetsword)
northtunnel = Room('North Tunnel',
                   'There something in the corner and I cannot',
                   None, 'maintunnel', None, None, None, None, Potion)
eastpassage2 = Room('East Passage',
                    'Its a narrow passage.',
                    None, None, 'easttunnel', 'eastpassage', None, None, None)
eastpassage = Room('East Passage',
                   'Its a narrow passage.',
                   None, None, 'eastpassage2', 'emptyroom', None, None, None)
easttunnel = Room('East Tunnel',
                  'It looks like a old tunnel system.',
                  None, None, 'maintunnel', 'eastpassage', None, None, None)
emptyroom = Room('Empty Room',
                 'There is just a ladder.',
                 None, None, 'eastpassage', None, 'insideofabandonedwarehouse', None, None)
insideofabandonedwarehouse = Room('Inside of abandoned warehouse',
                                  'This is the warehouse I could not get to.',
                                  None, None, None, None, None, 'emptyroom', Gascan)
livingroom = Room('Living Room',
                  'It is a nice living and there is a opened door.',
                  None, 'kitchen', None, 'basement', None, None, None)
westway = Room('Grass path',
               'It is a small grass path.',
               None, None, 'westway2', 'westofhouse', None, None, None,)
westway2 = Room('Grass Land',
                'It is a nice open field with flowers.',
                None, None, None, 'westway',None, None, Ring)
current_node = northofhouse
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while True:
    # Room information
    print(current_node.name)
    print(current_node.description)

    command = input('>_').lower().strip()

    # Pre-processing
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    elif command == 'quit':
        quit(0)

    # Process Command
    if command in directions:
      try:
        current_node.move(command)
      except KeyError:
        print('You cannot go this way.')
    else:
        print('Command not recognized')