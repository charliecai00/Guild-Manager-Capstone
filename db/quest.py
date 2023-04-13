# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

QUEST_KEY = 'ID'
QUEST_COLLECT = 'Quest'


# Create
def add_quest(details):
    dbc.connect_db()
    return dbc.insert_one(QUEST_COLLECT, details)


# Read
def get_unpurchase_quest():
    """
    return: a list of values, [1,2,3]
    """
    dbc.connect_db()
    all_quest = dbc.fetch_all(QUEST_COLLECT)

    unpurchase = []
    for i in all_quest:
        if i["Purchase"] is False:
            unpurchase.append(i)
    return unpurchase


def get_quest_details(id):
    dbc.connect_db()
    return dbc.fetch_one(QUEST_COLLECT, {QUEST_KEY: id})


def fetch_curr_id():
    dbc.connect_db()
    return dbc.fetch_curr_id(QUEST_COLLECT)


# Update
def update_quest(id, key, value):
    dbc.connect_db()
    return dbc.update_one(QUEST_COLLECT, {QUEST_KEY: id}, key, value)


# Delete
def del_quest(ID):
    """
    Delete one quest
    """
    dbc.connect_db()
    return dbc.del_one(QUEST_COLLECT, {QUEST_KEY: ID})
