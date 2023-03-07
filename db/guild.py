# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

"""
This module encapsulates details about guilds.
"""

ID = 'ID'
NAME = 'NAME'
HIRED_HERO = 'HIRED_HERO'
PURCHASED_QUEST = 'PURCHASED_QUEST'
CREATED_PARTY = 'CREATED_PARTY'
FUNDS = 'FUNDS'
QUEST_COMPLETED = 'QUEST_COMPLETED'

GUILD_KEY = 'ID'
GUILD_COLLECT = 'Guilds'

TEST_GUILD = 'test_guild'
REQUIRED_FLDS = [ID,
                 NAME,
                 HIRED_HERO,
                 PURCHASED_QUEST,
                 CREATED_PARTY,
                 FUNDS,
                 QUEST_COMPLETED]
dummy_guilds = {TEST_GUILD: {ID: 1,
                             NAME: "Temporary Guild",
                             HIRED_HERO: [1, 2, 3],
                             PURCHASED_QUEST: [1, 2, 3],
                             CREATED_PARTY: ["TempParty1", "TempParty2"],
                             FUNDS: 9999999,
                             QUEST_COMPLETED: 9999999}}


# Create
def add_guild(details):
    dbc.connect_db()
    return dbc.insert_one(GUILD_COLLECT, details)


# Read
def get_field(id, field):
    """
    parameter:  the id of the guild
                takes a field, ex. HERO_ID
    return: a list of values, [1,2,3]
    """
    dbc.connect_db()
    return dbc.fetch_field(GUILD_COLLECT, {GUILD_KEY: id}, field)


def get_guilds():
    """
    return a list of dictionary guilds [{...},{...},{...}]
    """
    dbc.connect_db()
    return dbc.fetch_all(GUILD_COLLECT)


def fetch_curr_id():
    dbc.connect_db()
    return dbc.fetch_curr_id(GUILD_COLLECT)


def get_guild_details(id):
    dbc.connect_db()
    return dbc.fetch_one(GUILD_COLLECT, {GUILD_KEY: id})


def guild_exists(id):
    return get_guild_details(id) is not None


# Update
def update_guild(id, key, value):
    """
    parameter:  id = guild id
                key = column name ex. FUNDS
                value = the value ex. 999999
    """
    dbc.connect_db()
    return dbc.update_one(GUILD_COLLECT, {GUILD_KEY: id}, key, value)


# Delete
def del_guild(ID):
    """
    Please use this method responsiblly
    """
    dbc.connect_db()
    return dbc.del_one(GUILD_COLLECT, {GUILD_KEY: ID})
