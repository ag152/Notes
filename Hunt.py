# Take damage, status affect, perform action, health, pick u p items, attack, death, move?, descripition, status effect
class Character(object):
    def ___int___(self, hp, attack, status, death, name):
        self.hp = hp
        self.attack = attack
        self.status = status
        self.death = death
        self.name = name


Player = (15000, 0, None, False, 'Bames Bond')
Enemy = (27835, 265, None, False, 'Fiend')
Enemy2 = (24654, 193, None, False, 'Goblin')
Enemy3 = (43820, 321, None, False, '')


class Item(object):
    def __init__(self, description):
        self.description = description


class Weapon(Item):
    def __init__(self, name, damage, description):
        super(Weapon, self).__init__(description)
        self.damage = damage
        self.name = name


class Melee(Weapon):
    def __init__(self, description, damage, name):
        super(Melee, self).__init__(description, damage, name)


class Ranged(Weapon):
    def __init__(self, name, damage, description):
        super(Ranged, self).__init__("Pistol", damage, description)


class Pistol(Ranged):
    def __init__(self, name, damage, description):
        super(Pistol, self).__init__('1911', 140, 'It is a 1911 pistol from ww2 and it is still in good condition.'
                                    ' and it has 30 bullets per clip.')
        self.ammo = 30

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print('*gun shot sound*')
        else:
            print('I have no more ammo.')


class Sawclever(Melee):
    def __init__(self, name, damage, description):
        super(Sawclever, self).__init__('Sawclever', 260, 'It is a blade with rigged edges.')


class Yeetsword(Melee):
    def __init__(self, name, damage, description):
       super(Yeetsword, self).__init__('Yeetsword', 1000, 'It is a long blade made out of some kind of metal.')


class Brickward(Melee):
        def __init__(self, description, damage, name):
            super(Brickward, self).__init__('Brickward', 450, 'It is just a giant brick on a graphene rod')


class Potion(Item):
    def __init__(self, description, heal):
        super(Potion, self).__init__('It is a small teal vial that has a red plus sign.')
        self.heal = heal

    def drink(self):
        return 200


class Gascan(Item):
    def __init__(self, description):
        super(Gascan, self).__init__('It is a gas can and there is only a bit of gas left.')


class Flashlight(Item):
    def __init__(self, description):
        super(Flashlight, self).__init__('It is a flashlight and it seems to run with one battery.')


class Battery(Item):
    def __init__(self, description):
        super(Battery, self).__init__('It is a small battery.')


class Ring(Weapon):
        def __init__(self, name, damage, description):
            super(Ring, self).__init__('Ring', 100000, 'It is a custom black ring.')


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
                   None, 'southofhouse', 'westway', 'northofhouse', None, None, [Sawclever])
southofhouse = Room("South of House",
                    "The back door is open but there is another path.",
                    'westofhouse', 'paths', 'dinerroom', None, None, None, None)
dinerroom = Room("Dining Room",
                 "You are in an old dinning room and there are small piles of dust.",
                 None, None, 'southofhouse', 'kitchen', None, None, [Potion])
kitchen = Room("Kitchen",
               "There is quite a lot of cooking materials.",
               'livingroom', None, 'dinerroom', None, None, None, [Potion])
living_room = Room("Living Room",
                   "There is a note here, a flashlight and six batteries. there seems to be a another door.",
                   'northofhouse', 'kitchen', 'basement', None, None, None, Flashlight)
basement = Room("Basement",
                'There is a bunch of boxes, laundry and dryer machine.',
                None, 'workshop', 'livingroom', None, None, None, Potion)
workshop = Room("Work Shop",
                'There is a bunch of power tools and scrap metal, but nothing too important.',
                'Basement', None, 'westpassage', None, None, None, Brickward)
westpassage2 = Room('West Passage',
                    'Its a narrow passage.',
                    None, None, 'westpassge', 'westtunnel', None, None, None)
westpassage = Room('West Passage',
                   'Its a narrow passage.',
                   None, None, 'workshop', 'westpassage2', None, None, None)
westtunnel = Room('West Tunnel',
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
              'There a goblin guarding a chest.',
              None, 'river2', None, None, None, 'Lab', None)
endofriver = Room('End of the river',
                  'It ends here and I cannot going but there is a beast behind a boulder',
                  None, None, None, 'river2', None, None, Battery)
Lab = Room('Lab',
           'It looks like they use to do experiments here and there is a sword on a pedestal, but it is impos.',
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
                                  'This is the warehouse I could not get to also there is a fiend here.',
                                  None, None, None, None, None, 'emptyroom', Gascan)
livingroom = Room('Living Room',
                  'It is a nice living and there is a opened door.',
                  None, 'kitchen', None, 'basement', None, None, None)
westway = Room('Grass path',
               'It is a small grass path.',
               None, None, 'westway2', 'westofhouse', None, None, None,)
westway2 = Room('Grass Land',
                'It is a nice open field with flowers.',
                None, None, None, 'westway', None, None, Ring)
current_node = northofhouse
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while True:
    # Room information
    print(current_node.name)
    print(current_node.description)
    if current_node.item is not None:
        for item in current_node.item:
            print(item.name)
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
    elif 'suicide' in command:
        print('You turned into a frog and kermit suicide.')
        quit(0)
    elif 'take' in command:
        Player.inventory.append(current_node.item)
        current_node.item = None
        print('Taken')
    else:
        print('Command not recognized')

