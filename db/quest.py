# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

ID = 'ID'
NAME = 'Name'
CHALLENGE = 'Challenge'
DIFFICULTY = 'Difficulty'
COST = 'Cost'
RESELL = 'Resell'
PURCHASE = 'Purchase'

QUEST_KEY = 'ID'
QUEST_COLLECT = 'Quest'

TEST_QUEST = 'TEST_QUEST'
REQUIRED_FLDS = [ID, NAME, CHALLENGE, DIFFICULTY, COST, RESELL]
dummy_quest = {TEST_QUEST: {ID: 1,
                            NAME: "Temporary Quest",
                            CHALLENGE: [1, 2, 3],
                            DIFFICULTY: 5,
                            COST: 999999,
                            RESELL: 999999,
                            PURCHASE: False}}


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
        if i[PURCHASE] is False:
            unpurchase.append(i)
    return unpurchase


def get_quest_details(id):
    dbc.connect_db()
    return dbc.fetch_one(QUEST_COLLECT, {QUEST_KEY: id})


def fetch_curr_id():
    dbc.connect_db()
    return dbc.fetch_curr_id(QUEST_COLLECT)


def quest_exists(id):
    return get_quest_details(id) is not None


# Update
def update_quest(id, key, value):
    dbc.connect_db()
    return dbc.update_one(QUEST_COLLECT, {QUEST_KEY: id}, key, value)


# Delete
def del_quest(name):
    """
    Delete all quest
    """
    dbc.connect_db()
    return dbc.del_many(QUEST_COLLECT, {})
