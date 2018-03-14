world_map = {
    'WESTHOUSE': {
        'NAME': 'WEST OF HOUSE',
        'DESCRIPTION': 'You are west of a white house.',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'SOUTHHOUSE':{
        'NAME': 'South of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            "WEST": 'WESTHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'North of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    }
}

current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']


class Room(object):
    def __init__(self, name, north, south, east, west):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


hdum = Room()

current_node = hdum
directions = ['north', 'south', 'east', 'west']

while True:
    print(current_node['NAME'])  # Change
    print(current_node['DESCRIPTION'])  # Change
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:

            except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
