# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

NAME = 'Name'
THE_GAME = 'The Game'
GUILD_ID = 'GUILD_ID'
HERO_ID = "HERO_ID"
QUEST_ID = 'QUEST_ID'

GAME_COLLECT = 'Games'

TEST_GAME_NAME1 = 'test_game1'
REQUIRED_FLDS = [HERO_ID, QUEST_ID, GUILD_ID]
dummy_game = {TEST_GAME_NAME1: {NAME: THE_GAME,
                                HERO_ID: [1, 2, 3],
                                QUEST_ID: [1, 2, 3],
                                GUILD_ID: [1, 2, 3]}}

# Create
def initialize_game(details):
    """
    details shoudld be:
    {HERO_ID: [],
    QUEST_ID: [],
    GUILD_ID: []}
    """
    dbc.connect_db()
    return dbc.insert_one(GAME_COLLECT, details)

# Read
def get_field(field):
    """
    parameter: takes a field, ex. HERO_ID
    return: a list of values, [1,2,3]
    """
    dbc.connect_db()
    return dbc.fetch_field(GAME_COLLECT, {}, field)

# Update
def update_game(key, value):
    """
    parameter example: key = HERO_ID, value = integer
    """
    lst = get_field(key)
    lst.append(value)
    dbc.connect_db()
    return dbc.update_one(GAME_COLLECT, {NAME: THE_GAME}, key, lst)


# Delete
def del_game():
    """
    delete all guild
    """
    dbc.connect_db()
    return dbc.del_many(GAME_COLLECT,{})
