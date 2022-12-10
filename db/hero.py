# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc


ID = 'id'
STATS = 'stats'
ITEMS = 'items'
NAME = 'name'
HERO_ID = 'HERO_ID'
HEALTH = 'health'
ALIVE = 'alive'
COST = 'cost'

HERO_KEY = 'name'
HERO_COLLECT = 'Heros'

TEST_HERO = 'test_hero'
REQUIRED_FLDS = [ID, STATS, ITEMS, NAME, HERO_ID, HEALTH, ALIVE, COST]
dummy_hero = {TEST_HERO: {ID: 1,
                          STATS: {"STR": 20, "CON": 20, "DEX": 20, "WIS": 20, "INT": 20, "CHA": 20},
                          ITEMS: [],
                          NAME: "1",
                          HERO_ID: 1,
                          HEALTH: 2,
                          ALIVE: True,
                          COST: 5
                          }}


def get_hero_details(name):
    dbc.connect_db()
    return dbc.fetch_one(HERO_COLLECT, {HERO_KEY: name})


def hero_exists(name):
    return get_hero_details(name) is not None


def get_heros_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(HERO_KEY, HERO_COLLECT)


def get_heros():
    dbc.connect_db()
    return dbc.fetch_all(HERO_COLLECT)


def add_hero(name, details):
    doc = details
    dbc.connect_db()
    doc[HERO_KEY] = name
    return dbc.insert_one(HERO_COLLECT, doc)


def del_hero(name):
    dbc.connect_db()
    return dbc.del_one(HERO_COLLECT, {HERO_KEY: name})


# def main():
#     print('Adding a hero')
#     add_hero(TEST_HERO, dummy_hero[TEST_HERO])
#     print('Getting heros as a list:')
#     heros = get_heros()
#     print(f'{heros=}')
#     print('Getting heros as a dict:')
#     games = get_heros_dict()
#     print(f'{games=}')
#     print(f'{get_hero_details(TEST_HERO)=}')


# if __name__ == '__main__':
#     main()
