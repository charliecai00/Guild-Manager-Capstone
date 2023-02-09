# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

"""
This module encapsulates details about guilds.
"""


TEST_GUILD = 'test_guild'
ID = 'id'
GUILD_ID = 'PART_ID'
HIRED_HEROS = 'hired_heros_list'
GROUPS = 'groups_list'
QUESTS = 'quest_list'
QUEST_HISTORY = 'quest_history'
PARTIES = 'party_list'
FUNDS = 'funds'

GUILD_KEY = 'name'
GUILD_COLLECT = 'Guilds'

REQUIRED_FLDS = [ID, GUILD_ID, HIRED_HEROS]

guilds = {TEST_GUILD: {ID: 9, GUILD_ID: 9, HIRED_HEROS: 2, GROUPS: [],
                       QUESTS: [], QUEST_HISTORY: [], PARTIES: [], FUNDS: 0},
          'guild2': {ID: 9, GUILD_ID: 9, HIRED_HEROS: 2, GROUPS: [],
                     QUESTS: [], QUEST_HISTORY: [], PARTIES: [], FUNDS: 0},
          'guild3': {ID: 6, GUILD_ID: 1, HIRED_HEROS: 2, GROUPS: [],
                     QUESTS: [], QUEST_HISTORY: [], PARTIES: [], FUNDS: 0}}


def get_guild_details(guild):
    dbc.connect_db()
    return dbc.fetch_one(GUILD_COLLECT, {GUILD_KEY: guild})


def guild_exists(name):
    return get_guild_details(name) is not None


def get_guilds_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(GUILD_KEY, GUILD_COLLECT)


def get_guilds():
    dbc.connect_db()
    return dbc.fetch_all(GUILD_COLLECT)


def add_guild(name, details):
    doc = details
    dbc.connect_db()
    doc[GUILD_KEY] = name
    return dbc.insert_one(GUILD_COLLECT, doc)


def del_guild(name):
    dbc.connect_db()
    return dbc.del_one(GUILD_COLLECT, {GUILD_KEY: name})
