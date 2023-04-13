# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

HERO_KEY = 'ID'
HERO_COLLECT = 'Hero'


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
        if i["Hired?"] is False and len(unemploy) <= 10:
            unemploy.append(i)

    return unemploy


def get_hero_details(id):
    dbc.connect_db()
    return dbc.fetch_one(HERO_COLLECT, {HERO_KEY: id})


def fetch_curr_id():
    dbc.connect_db()
    return dbc.fetch_curr_id(HERO_COLLECT)


# Update
def update_hero(id, key, value):
    dbc.connect_db()
    return dbc.update_one(HERO_COLLECT, {HERO_KEY: id}, key, value)


# Delete
def del_hero(ID):
    """
    Delete one hero
    """
    dbc.connect_db()
    return dbc.del_one(HERO_COLLECT, {HERO_KEY: ID})
