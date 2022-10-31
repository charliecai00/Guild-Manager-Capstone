"""
This module encapsulates details about heros.
"""


# from telnetlib import TELNET_PORT


TEST_HERO = 'test_hero'
ID = 'id'
HERO_ID = 'HERO_ID'
STATS = 'stats'
ITEMS = 'items'
NAME = 'name'
HEALTH = 'health'
ALIVE = 'alive'
COST = 'cost'


# We expect the hero database to change frequently:
# For now, we will consider ID and hero_ID to be
# our mandatory fields.
REQUIRED_FLDS = [ID, HERO_ID, STATS]

heros = {TEST_HERO: {ID: 4, HERO_ID: 3, STATS: {}, ITEMS: [], NAME: "",
                     HEALTH: 2, ALIVE: True, COST: 5},
         'hero2': {ID: 3, HERO_ID: 9, STATS: {}, ITEMS: [], NAME: "",
                   HEALTH: 2, ALIVE: True, COST: 3},
         'hero3': {ID: 2, HERO_ID: 1, STATS: {}, ITEMS: [], NAME: "",
                   HEALTH: 2, ALIVE: False, COST: 2}}


def hero_exists(name):
    """
    Returns whether or not a hero exists.
    """
    return name in heros


def get_heros_dict():
    return heros


def get_heros():
    return list(heros.keys())


def get_hero_details(hero):
    return heros.get(hero, None)


def add_hero(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    heros[name] = details


def main():
    heros = get_heros()
    print(f'{heros=}')
    print(f'{get_hero_details(TEST_HERO)=}')


if __name__ == '__main__':
    main()
