world_map = {
    'WESTOFHOUSE': {
        'NAME': 'West of House',
        'DESCRIPTION': 'You are west of a white house. There is also a chest.',
        'PATHS': {
            'NORTH': 'NORTHOFHOUSE',
            'SOUTH': 'SOUTHOFHOUSE'
        }
    },
    'SOUTHOFHOUSE': {
        'NAME': ' South of House',
        'DESCRIPTION': 'You are south of a white house.',
        'PATHS': {
            'WEST': 'WESTHOUSE',
            'SOUTH': 'PATHS',
            'NORTH': 'WINDOW'
             }
    },
    'DINERROOM': {
       'NAME': 'Diner Room',
       'DESCRIPTION': 'It appears that no one lived here for a couple of years and there is two weird teal potions.',
       'PATHWAYS': {
            'EAST': 'KITCHEN',
            'NORTH': 'LIVINGROOM',
            'SOUTH': 'SOUTHOFHOUSE'
        }
    },
    'KITCHEN': {
        'NAME': 'Livinig Room',
        'DESCRIPTION': 'There is the front door of house and there is a another room.',
        'PATHWAYS': {
            'NORTH': 'LIVINGROOM',
            'EAST': 'BASEMENT'
        }
    },
    'BASEMENT': {
        'NAME': 'Basement',
        'DESCRIPTION': 'There piles of old clothes and hole.',
        'PATHWAYS': {
            'SOUTH': 'WORKSHOP',
            'WEST': 'KITCHEN'
        }
    },
    'WORKSHOP': {
        'NAME': 'Workshop',
        'DESCRIPTION': 'It seems to be a old work shop, there is a small hole in the wall. Also there is a chest',
        'PATHWAYS': {
            'NORTH': 'BASEMENT',
            'SOUTH': 'ARTROOM'
        }
    },
    'ARTROOM': {
        'NAME': 'Art Studio',
        'DESCRIPTION': 'There is a note on the wall.',
        'PATHWAYS': {
            'WEST': 'WESTPASSAGE',
            'NORTH': 'WORKSHOP'
        }
    },
    'NORTHOFHOUSE': {
        'NAME': ' North of House',
        'DESCRIPTION': 'You are north of a white house; there seems to be a note on the door.',
        'PATHS': {
            'WEST': 'WESTOFHOUSE',
            'EAST': 'PARKEDCAR'
        }
    },
    'PATHS': {
        'NAME': 'Paths',
        'DESCRIPTION': 'You have three pathways East,West, and North',
        'PATHS': {
            'EAST': 'FOREST',
            'WEST': 'RIVER',
            'NORTH': 'MOUNTAINS',
            'SOUTH': ' SOUTHOFHOUSE'
        }
    },
    'PARKEDCAR': {
        'NAME': 'Garage',
        'DESCRIPTION': 'There is a parked car with keys inside; the gas tank is empty.',
        'PATHWAYS': {
            'WEST': 'NORTHOFHOUSE'
        }
    },
    'RIVER': {
        'NAME': 'River',
        'DESCRIPITION': 'The river starts from here and ends somewhere down south.',
        'PATHWAY': {
            'NORTH': 'CAVERN',
            'WEST': 'WALKWAY',
            'EAST': 'PATHS'
        }
    },
    'MOUNTAINS': {
        'NAME': 'Mountians',
        'DESCRIPTION': 'There is a small path but its to trenches to go.',
        'PATHWAYS': {
            'SOUTH': 'PATHS'
        }
    },
    'CAVERN': {
        'NAME': 'Cavern',
        'DESCRIPTION': 'There is a large sack before a small rock and there is another generator here.',
        'PATHWAYS': {
            'SOUTH': 'RIVER'
        }
    },
    'WALKWAY': {
        'NAME': 'Walkway',
        'DESCRIPTION': 'It is a long walkway that only goes up north.',
        'PATHWAYS': {
            'NORTH': 'STREET'
        }
    },
    'FOREST': {
        'NAME': 'Forest',
        'DESCRIPTION': 'There is a sign that says "DANGER: NO ENTRY"',
        'PATHWAYS': {
            'SOUTH': 'MOUNTAINVIEW',
            'EAST': 'FOREST2'
        }
    },
    'FOREST2': {
        'NAME': 'Forest',
        'DESCRIPTION': 'There a pathway and a small hole.',
        'PATHWAYS': {
            'EAST': 'DEEPFOREST',
            'NORTH': 'SMALL SHED'
        }
    },
    'DEEPFOREST': {
        'NAME': 'Deep Forest',
        'DESCRIPTION': 'There something up east but cannot make it out.',
        'PATHWAYS': {
            'EAST': 'ABANDONEDWAREHOUSE',
            'WEST': 'FOREST2'
        }
    },
    'ABANDONEDWAREHOUSE': {
        'NAME': 'Abandoned Warehouse',
        'DESCRIPTION': 'I can not enter because there are vines in the way.',
        'PATHWAYS': {
            'WEST': 'DEEPFOREST'
        }

    },
    'INSIDEOFABANDONEDWAREHOUSE': {
        'NAME': 'Inside of Abandoned Warehouse',
        'DESCRIPTION': 'There seems to be a gas tank here.',
        'PATHWAYS': {
            'DOWN': 'EMPTYROOM'
        }
    },
    'SHED': {
        'NAME': 'Small Shed',
        'DESCRIPTION': 'It is a small shed; it appears to have no lock.,',
        'PATHWAYS': {
            'SOUTH': 'FOREST2',
            'NORTH': 'INSIDEOFSHED'
        }
    },
    'INSIDEOFSHED': {
        'NAME': 'Inside Of Shed',
        'DESCRIPTION': 'It goes down and there is a small wooden crate.',
        'PATHWAYS': {
            'DOWN': 'TUNNEL',
            'SOUTH': 'SHED'
        }
    },
    'TUNNEL': {
        'NAME': 'Tunnel',
        'DESCRIPTION': 'It is going north still.',
        'PATHWAYS': {
            'UP': 'INSIDEOFHED',
            'NORTH': 'TUNNEL2'
        }
    },
    'TUNNEL2': {
        'NAME': 'Tunnel',
        'DESCRIPTION': 'It goes three different ways to go.',
        'PATHWAYS': {
            'WEST': 'WESTPASSAGE',
            'EAST': 'EASTPASSAGE',
            'SOUTH': 'TUNNEL',
            'NORTH': 'TUNNEL3'
        }
    },
    'TUNNEL3': {
        'NAME': 'Tunnel',
        'DESCRIPTION': 'It seems to end here and there is a machete next to some rocks.',
        'PATHWAYS': {
            'SOUTH': 'TUNNEL2'
        }
    },
    'WESTPASSAGE': {
        'NAME': 'West Passage',
        'DESCRIPTION': 'It seems to only go one way.',
        'PATHWAYS': {
            'EAST': 'TUNNEL2',
            'WEST': 'WESTPASSAGE2'
        }
    },
    'WESTPASSAGE2': {
        'NAME': 'West Passage',
        'DESCRIPTION': 'It is a long way until reach the end.',
        'PATHWAYS': {
            'EAST': 'WESTPASSAGE',
            'WEST': 'ARTROOM'
        }
    },
    'EASTPASSAGE': {
        'NAME': 'East Passage',
        'DESCRIPTION': 'Only goes East.',
        'PATHWAYS': {
            'WEST': 'TUNNEL2',
            'EAST': 'EASTPASSAGE2'
        }
    },
    'EASTPASSAGE2': {
        'NAME': 'East Passage',
        'DESCRIPTION': 'Looks like this might be the end of this boring hallway.',
        'PATHWAYS': {
            'EAST': 'EMPTYROOM',
            'WEST': 'EASTPASSAGE'
        }
    },
    'EMPTYROOM': {
        'NAME': 'Empty Room',
        'DESCRIPTION': 'There is a ladder in the middle of the room.',
        'PATHWAYS': {
            'UP': 'INSIDEOFABADONEDWAREHOUSE',
            'WEST': 'EASTPASSAGE2'
        }
    },
    'INSIDEOFABADONEDWAREHOUSE': {
        'NAME': 'Abandon Warehouse',
        'DESCRIPTION':'There is a troll holding a brick guarding a gas can and a sword',
        'PATHWAYS':{
            'DOWN': None
        }
    }
}


current_node = world_map['NORTHOFHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
       try:
        name_of_code = current_node['PATHS'][command]
        print(name_of_code)
       except KeyError:
        print('You can not go this way.')
    else:
        print('Command not recognized')
