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

GUILD_KEY = 'ID'
GUILD_COLLECT = 'Guilds'

TEST_GUILD = 'test_guild'
REQUIRED_FLDS = [ID, NAME, HIRED_HERO, PURCHASED_QUEST, CREATED_PARTY, FUNDS]
dummy_guilds = {TEST_GUILD: {ID: 1,
                             NAME: "Temporary Guild",
                             HIRED_HERO: [1, 2, 3],
                             PURCHASED_QUEST: [1, 2, 3],
                             CREATED_PARTY: ["TempParty1", "TempParty2"],
                             FUNDS: 9999999}}


def add_guild(details):
    dbc.connect_db()
    return dbc.insert_one(GUILD_COLLECT, details)


def get_field(field):
    """
    parameter: takes a field, ex. HERO_ID
    return: a list of values, [1,2,3]
    """
    dbc.connect_db()
    return dbc.fetch_field(field, GUILD_COLLECT)


def get_guilds():
    """
    return a list of dictionary guilds [{...},{...},{...}]
    """
    dbc.connect_db()
    return dbc.fetch_all(GUILD_COLLECT)


# def del_guild(ID):
#     dbc.connect_db()
#     return dbc.del_one(GUILD_COLLECT, {GUILD_KEY: ID})


# def get_guild_details(guild):
#     dbc.connect_db()
#     return dbc.fetch_one(GUILD_COLLECT, {GUILD_KEY: guild})


# def guild_exists(name):
#     return get_guild_details(name) is not None


# def get_guilds_dict():
#     dbc.connect_db()
#     return dbc.fetch_all_as_dict(GUILD_KEY, GUILD_COLLECT)

# def main():
#     print('Adding guilds')
#     add_guild(dummy_guilds[TEST_GUILD])
#     print('Getting games as a list:')
#     guilds = get_guilds()
#     print(f'{guilds=}')


# if __name__ == '__main__':
#     main()
