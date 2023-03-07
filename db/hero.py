# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

ID = 'ID'
STATS = 'STATS'
NAME = 'NAME'
HEALTH = 'HEALTH'
MAX_HEALTH = 'MAX_HEALTH'
EXP = 'EXP'
ALIVE = 'ALIVE'
COST = 'COST'
HIRE = 'Hired?'
IN_PARTY = 'InParty?'
PARTY_ID = 'PARTY_ID'

HERO_KEY = 'ID'
HERO_COLLECT = 'Hero'

TEST_HERO = 'test_hero'
REQUIRED_FLDS = [ID, STATS, NAME, HEALTH, ALIVE, COST]
dummy_hero = {TEST_HERO: {ID: 1,
                          STATS: {"STR": 999999, "CON": 999999, "DEX": 999999,
                                  "WIS": 999999, "INT": 999999, "CHA": 999999},
                          NAME: "Temporary Hero",
                          HEALTH: 999999,
                          MAX_HEALTH: 999999,
                          EXP: 999999,
                          ALIVE: True,
                          COST: 100,
                          HIRE: True,
                          IN_PARTY: False,
                          PARTY_ID: None}}

# Create
def add_hero(details):
    dbc.connect_db()
    return dbc.insert_one(HERO_COLLECT, details)

# Read
def get_unemploy_hero():
    """
    return: a list of values, [1,2,3]
    """
    dbc.connect_db()
    all_heros = dbc.fetch_all(HERO_COLLECT)

    unemploy = []
    for i in all_heros:
        if i[IN_PARTY] is False:
            del i['_id']
            unemploy.append(i)
    return unemploy


def get_hero_details(id):
    dbc.connect_db()
    return dbc.fetch_one(HERO_COLLECT, {HERO_KEY: id})


def fetch_curr_id():
    dbc.connect_db()
    return dbc.fetch_curr_id(HERO_COLLECT)    


def hero_exists(name):
    return get_hero_details(name) is not None


# Update
def update_hero(previous_id, new_hero):
    """
    1. delete the preivous hero by id
    2. create a new hero, accepting parameter as json
    """
    dbc.connect_db()
    dbc.del_one(HERO_COLLECT, {ID: previous_id})
    return dbc.insert_one(HERO_COLLECT, new_hero)

# Delete
def del_hero(ID):
    """
    Delete all hero
    """
    dbc.connect_db()
    return dbc.del_many(HERO_COLLECT, {})

