# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

ID = 'ID'
STATS = 'STATS'
NAME = 'NAME'
HEALTH = 'HEALTH'
ALIVE = 'ALIVE'
COST = 'COST'
HIRE = 'HIRE'

HERO_KEY = 'ID'
HERO_COLLECT = 'Hero'

TEST_HERO = 'test_hero'
REQUIRED_FLDS = [ID, STATS, NAME, HEALTH, ALIVE, COST]
dummy_hero = {TEST_HERO: {ID: 1,
                          STATS: {"STR": 20, "CON": 20, "DEX": 20,
                                  "WIS": 20, "INT": 20, "CHA": 20},
                          NAME: "Temporary Hero",
                          HEALTH: 100,
                          ALIVE: True,
                          HIRE: True,
                          COST: 100}}


def add_hero(details):
    dbc.connect_db()
    return dbc.insert_one(HERO_COLLECT, details)


def get_unemploy_hero():
    """
    return: a list of values, [1,2,3]
    """
    dbc.connect_db()
    all_heros = dbc.fetch_all(HERO_COLLECT)

    unemploy = []
    for i in all_heros:
        if i[HIRE] is False:
            unemploy.append(i)
    return unemploy


# def get_hero_details(name):
#     dbc.connect_db()
#     return dbc.fetch_one(HERO_COLLECT, {HERO_KEY: name})


# def hero_exists(name):
#     return get_hero_details(name) is not None


# def get_heros_dict():
#     dbc.connect_db()
#     return dbc.fetch_all_as_dict(HERO_KEY, HERO_COLLECT)


# def get_heros():
#     dbc.connect_db()
#     return dbc.fetch_all(HERO_COLLECT)


# def del_hero(ID):
#     dbc.connect_db()
#     return dbc.del_one(HERO_COLLECT, {HERO_KEY: ID})


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
