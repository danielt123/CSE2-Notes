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



current_node = hdum
directions = ['north', 'south', 'east', 'west']


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
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node['NAME'])  # Change
    print(current_node['DESCRIPTION'])  # Change
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
        # Change
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")

