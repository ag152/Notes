# Take damage, status affect, perform action, health, pick u p items, attack, death, move?, descripition, status effect
inventory = []


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
Enemy3 = (43820, 321, None, False, 'Beter')


class Item(object):
    def __init__(self, name, description):
        self.description = description
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, description):
        super(Weapon, self).__init__(name, description)
        self.damage = damage


class Melee(Weapon):
    def __init__(self, name, damage, description):
        super(Melee, self).__init__(name, damage, description)


class Ranged(Weapon):
    def __init__(self, name, damage, description):
        super(Ranged, self).__init__(name, damage, description)


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
        super(Sawclever, self).__init__('Sawclever', 498, 'It is a blade with rigged edges.')


class Yeetsword(Melee):
    def __init__(self, name, damage, description):
       super(Yeetsword, self).__init__('Yeetsword', 2680, 'It is a long blade made out of some kind of metal.')


class Brickward(Melee):
        def __init__(self, description, damage, name):
            super(Brickward, self).__init__('Brickward', 567, 'It is just a giant brick on a graphene rod')


class Potion(Item):
    def __init__(self, name, description, heal):
        super(Potion, self).__init__('Potion', 'It is a small teal vial that has a red plus sign.')
        self.heal = heal

    def drink(self):
        return 250


class Gascan(Item):
    def __init__(self, name, description):
        super(Gascan, self).__init__('Gascan', 'It is a gas can and there is only a bit of gas left.')

    def use(self):
        print('You poured the gas.')


class Flashlight(Item):
    def __init__(self, name, description):
        super(Flashlight, self).__init__('Flashlight', 'It is a flashlight and it seems to run with one battery.')


class Battery(Item):
    def __init__(self,name,  description):
        super(Battery, self).__init__('Battery', 'It is a small battery.')


class Ring(Weapon):
        def __init__(self, name, damage, description):
            super(Ring, self).__init__('Ring', 100000, 'It is a custom black ring.')


sawclever = Sawclever("sawclever", 498, "It is a blade with rigged edges.")
yeetsword = Yeetsword('Yeetsword', 2680, 'It is a long blade made out of some kind metal.')
ring = Ring('Ring', 100000, 'It is a custom black ring.')
brickward = Brickward('Brickward', 567, 'It is just a giant brick on a graphene rod')
pistol = Pistol('1911', 140, 'It is a 1911 pistol from ww2 and it is still in good condition.'
' and it has 30 bullets per clip.')
battery = Battery('Battery', 'It is a small battery.')
flashlight = Flashlight('Flashlight', 'It is a flashlight and it seems to run with one battery.')
gascan = Gascan('Gascan', 'It is a gas can and there is only a bit of gas left.')
potion = Potion('Potion', 'It is a small teal vial that has a red plus sign.', 250)


class Room(object):
    def __init__(self, name, description, north, south, west, east, up, down, item, characters):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.up = up
        self.down = down
        self.item = item
        self.character = characters

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


northofhouse = Room('North of House',
                    'There nothing too interesting here.',
                    None, None, 'westofhouse', 'garage', 'porchroof', None, None, None)
garage = Room("Garage",
              "there is a car with keys inside. Also there is a a fruit bowl.",
              None, None, 'northofhouse', None, None, None, None, None)
westofhouse = Room("West of House",
                   "You are west of the house and there something on the floor",
                   None, 'southofhouse', 'westway', 'northofhouse', None, None, [sawclever], None)
southofhouse = Room("South of House",
                    "The back door is open but there is another path.",
                    'westofhouse', 'paths', 'dinerroom', None, None, None, None, None)
dinerroom = Room("Dining Room",
                 "You are in an old dinning room and there are small piles of dust.",
                 None, None, 'southofhouse', 'kitchen', None, None, [potion], [Enemy])
kitchen = Room("Kitchen",
               "There is quite a lot of cooking materials.",
               'livingroom', None, 'dinerroom', None, None, None, [potion], [Enemy])
living_room = Room("Living Room",
                   "There is a note here, a flashlight and six batteries. there seems to be a another door.",
                   'northofhouse', 'kitchen', 'basement', None, None, None, [flashlight], None)
basement = Room("Basement",
                'There is a bunch of boxes, laundry and dryer machine.',
                None, 'workshop', 'livingroom', None, None, None, [potion], [Enemy2])
workshop = Room("Work Shop",
                'There is a bunch of power tools and scrap metal, but nothing too important.',
                'Basement', None, 'westpassage', None, None, None, [brickward], None)
westpassage2 = Room('West Passage',
                    'Its a narrow passage.',
                    None, None, 'westpassge', 'westtunnel', None, None, None, None)
westpassage = Room('West Passage',
                   'Its a narrow passage.',
                   None, None, 'workshop', 'westpassage2', None, None, None, None)
westtunnel = Room('West Tunnel',
                  'It looks like a old tunnel system',
                  None, None, 'westpassage', 'maintunnel', None, None, None, None)
maintunnel = Room('Main Tunnel',
                  'There is old rusty tools.',
                  'northtunnel', None, 'westtunnel', 'easttunnel', 'insideofshed', None, [potion], [Enemy3])
insideofshed = Room('Inside of Shed',
                    'It is a small shed there is not much here.',
                    None, 'shed', None, None, None, 'maintunnel', None, None)
shed = Room('Shed',
            'Its a small shed in a forest',
            'insideofshed', 'forest2', None, None, None, None, None, None)
forest2 = Room('Forest',
               'It seems a like a forest that leads two ways.',
               'shed', None, 'forest', 'deepforest', None, None, None, None)
deepforest = Room('Deep Forest',
                  'There is a building but it is completely cut by fallen trees.',
                  None, None, 'forest2', None, None, None, None, [Enemy2])
forest = Room('Forest',
              'It seems its the beginning of the woods.',
              None, None, 'paths', 'forest2', None, None, None, None)
paths = Room('Paths',
             'It seems there are four rock pathways.',
             'southofhouse', 'mountains', 'river', 'forest', None, None, [potion], None)
mountains = Room('Mountains',
                 'It is a nice view of the city from here.',
                 'paths', None, None, None, None, None, [potion], None)
river = Room('River',
             'Its a that keeps going.',
             None, None, 'river2', 'paths', None, None, [potion], None)
river2 = Room('River',
              'The river keeps getting narrow and there is a cavern',
              'cavern', None, 'endofriver', 'river', None, None, [potion], None)
cavern = Room('Cavern',
              'Its a cavern with a Fiend and there is ladder down next to me.',
              None, 'river2', None, None, None, 'Lab', None, [Enemy2])
endofriver = Room('End of the river',
                  'It ends here and I cannot going but there is a beast behind a boulder',
                  None, None, None, 'river2', None, None, [Battery], [Enemy])
Lab = Room('Lab',
           'It looks like they use to do experiments here and there is a sword on a pedestal, but it is impossible'
           ' to get.',
           None, None, None, None, 'cavern', None, [yeetsword], None)
northtunnel = Room('North Tunnel',
                   'There something in the corner and I cannot',
                   None, 'maintunnel', None, None, None, None, [potion], None)
eastpassage2 = Room('East Passage',
                    'Its a narrow passage.',
                    None, None, 'easttunnel', 'eastpassage', None, None, None, None)
eastpassage = Room('East Passage',
                   'Its a narrow passage.',
                   None, None, 'eastpassage2', 'emptyroom', None, None, [battery], None)
easttunnel = Room('East Tunnel',
                  'It looks like a old tunnel system.',
                  None, None, 'maintunnel', 'eastpassage', None, None, [battery], None)
emptyroom = Room('Empty Room',
                 'There is just a ladder.',
                 None, None, 'eastpassage', None, 'insideofabandonedwarehouse', None, None, None)
insideofabandonedwarehouse = Room('Inside of abandoned warehouse',
                                  'This is the warehouse I could not get to also there is a fiend here.',
                                  None, None, None, None, None, 'emptyroom', [Gascan], [Enemy2])
livingroom = Room('Living Room',
                  'It is a nice living, but there isnt anything interesting.',
                  None, 'kitchen', None, 'basement', None, None, None, None)
westway = Room('Grass path',
               'It is a small grass path.',
               None, None, 'westway2', 'westofhouse', None, None, None, None)
westway2 = Room('Grass Land',
                'It is a nice open field with flowers and there is a goblin.',
                None, None, None, 'westway', None, None, None, [Enemy])
porchroof = Room('Porch Roof',
                 'I can see some other homes and barns when I am up here.',
                 None, None, None, None, None, 'northofhouse', [ring], None)
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
        for item in current_node.item:
            inventory.append(item)
        current_node.item = None
        print('Taken')
    elif 'buddy' in command:
        print('(*-*)\n'
              ' /|\ \n'
              '  |\n'
              ' / \   ')
    elif 'konami code' in command:
        print('You summoned Exodia the Forbidden One'
              ' and won the game.')
        quit(0)
  #  elif command in ['i, inv', 'inventory']:
   #     for item in Player.inventory:
    #        print(item.name)

    elif "attack" in command:
        ['Brickward', 'Yeetsword', 'Ring', 'Sawclever']



    else:
        print('Command not recognized')
