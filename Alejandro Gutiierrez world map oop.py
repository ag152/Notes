class Room(object):
    def __init__(self, name, description, north, south, west, east, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


northofhouse = Room('North of House',
                    'There nothing to interesting here.',
                    None, None, 'westofhouse', 'garage', None, None)
garage = Room("Garage",
              "there is a car with keys inside. Also there is a a fruit bowl.",
              None, None, 'northofhouse', None, None, None)
westofhouse = Room("West of House",
                   "You are west of the house and there is a chest",
                   None, 'southofhouse', None, 'northofhouse', None, None)
southofhouse = Room("South of House",
                    "There is a window that can be opened and there is a path going south.",
                    'westofhouse', 'paths', 'dinerroom', None, None, None)
dinerroom = Room("Dinning Room",
                   "You are in an old dinning room and there are small piles of dust.",
                 None, None, 'southofhouse', 'kitchen', None, None)
kitchen = Room("Kitchen",
                "There is key a on the counter.",
                'livingroom', None, 'dinerroom', None, None, None)
living_room = Room("Living Room",
                   "There is a note here, a flashlight and six batteries. there seems to be a another door.",
                   'northofhouse', 'kitchen', 'basement', None, None, None)
basement = Room("Basement",
                'There is a bunch of boxes, laundry and dryer machine.',
                None, 'workshop', None, 'livingroom', None, None)
workshop = Room("Work Shop",
                'There is a bunch of power tools and scrap metal, but nothing too important.',
                'Basement', None, 'West Passage', None, None, None)
westpassage2 = Room('West Passage',
                    'Its a narrow passage that keeps going west.',
                    None, None, 'westpassge', 'workshop', None, None)
westpassage = Room('West Passage',
                   'It looks like a different place up ahead.',
                   None, None, 'tunnel2', 'westpassage2', None, None)
tunnel2 = Room('West Tunnel',
               'It look like a old tunnel system',
               None, None, 'westpassage', 'maintunnel', None, None)
maintunnel = Room('Main Tunnel',
                  'There is machete on the old self and there is old rusty tools.',
                  'northtunnel', None, 'westtunnel', 'easttunnel', 'insideofshed', None)
insideofshed = Room('Inside of Shed',
                    'It is a small shed there is not much here.',
                    None, 'shed', None, None, 'maintunnel', None)
shed = Room('Shed',
            'Its a small shed in a forest',
            'insideofshed', 'forest2', None, None, None, None)
forest2 = Room('Forest',
              'It seems a like a forest that leads two ways.',
              'shed', None, 'forest', 'deepforest', None, None)
deepforest = ('Deep Forest',
              'This the deep part of the forest to be a building but blocked by fallen tress.',
              None, None, 'forest2', None, None, None)
forest = Room('Forest',
              'It seems its the beginning of the woods.',
              None, None, 'Paths', 'forest2', None, None)
paths = Room('Paths',
             'It seems there are four rock pathways.',
             'southofhouse', 'mountains', 'river', 'forest', None, None)
mountains = Room('Mountains',
                 'It is a nice view of the city from here.',
                 'paths', None, None, None, None, None)
river = Room('River',
             'Its a that keeps going.',
             None, None, 'river2', 'paths', None, None)
river2 = Room('River',
              'The river keeps getting narrow and there is a cavern',
              'cavern', None, 'endofriver', 'river', None, None)
cavern = Room('Cavern',
              'There a big guy with a medium bolder protecting a chest.',
              None, 'river2', None, None, None, 'Lab')
endofriver = Room('End of the river',
                  'It ends here and I cannot going but there is a beast behind a boulder',
                  None, None, None, 'river2', None, None)
Lab = Room('Lab',
           'There is a panel here with three buttons the first is destroy mobs, the second is teleport to room'
           'and the third one is a nuke.',
           None, None, None, None, 'cavern', None)


current_node = ('northofhouse')
directions = ['North', 'South', 'East', 'West', 'Up', 'Down']
short_directions = ['N', 'S', 'E', 'W', 'U', 'D']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
               print('You cannot go this way.')
    else:
        print('Command not recognized')