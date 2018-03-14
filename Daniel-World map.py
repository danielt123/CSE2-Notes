world_map = {
    'JUNK JUNCTION': {
        'NAME': 'JUNK JUNCTION',
        'DESCRIPTION': 'Junk Junction is full of metal and on a cliff from the ocean.You can go SOUTHWEST, '
                       'SOUTHEAST, and EAST.',
        'PATHS': {
            'SOUTHWEST':'HAUNTED HILLS',
            'SOUTHEAST':'PLEASANT PARK',
            'EAST':'ANARCHY ACRES'
        }
    },
    'HAUNTED HILLS': {
        'NAME': 'HAUNTED HILLS',
        'DESCRIPTION': 'Haunted Hills id full of old houses with a cemetery next to it.You can go NORTH, EAST,'
                       ' SOUTHEAST'
                       ', and SOUTH.',
        'PATHS': {
            'NORTH':'JUNK JUNCTION',
            'EAST': 'PLEASANT PARK',
            'SOUTHEAST': 'TILTED TOWERS',
            'SOUTH': 'SNOBBY SHORES'
        }
    },
    'PLEASANT PARK': {
        'NAME': 'PLEASANT PARK',
        'DESCRIPTION': 'Pleasant Park has brand new house with basements and a huge soccerfield in the middle of '
                       'the neighborhood.You can go WEST, SOUTHEAST, SOUTHWEST, and NORTHWEST.',
        'PATHS': {
            'WEST':'HAUNTED HILLS',
            'SOUTHEAST':'LOOT LAKE',
            'SOUTHWEST':'SNOBBY SHORES',
            'NORTHWEST':'JUNK JUNCTION'
        }
    },
    'LOOT LAKE': {
        'NAME':'LOOT LAKE',
        'DESCRIPTION': 'Loot lake is full of water surrounded by houses and towers made from wood. You can go SOUTH,'
                       ' NORTHEAST, SOUTHEAST, and NORTHWEST.',
        'PATHS': {
            'SOUTH': 'TILTED TOWERS',
            'NORTHEAST': 'ANARCHY ACRES',
            'SOUTHEAST': 'DUSTY DEPOT',
            'NORTHWEST': 'PLEASANT PARK'
        }
    },
    'TILTED TOWERS': {
        'NAME':'TILTED TOWERS',
        'DESCRIPTION': 'Tilted Towers is full of tall buildings and cars in the underground garages. You can go WEST,'
                       ' SOUTHWEST, SOUTH, and EAST.',
        'PATHS': {
            'WEST': 'SNOBBY SHORES',
            'SOUTHWEST': 'GREASY GROVE',
            'SOUTH': 'SHIFTY SHAFTS',
            'EAST': 'DUSTY DEPOT'
        }
    },
    'SNOBBY SHORES': {
        'NAME': 'SNOBBY SHORES'
    }
}