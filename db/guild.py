# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

GUILD_KEY = 'ID'
GUILD_COLLECT = 'Guild'


# Create
def add_guild(details):
    dbc.connect_db()
    return dbc.insert_one(GUILD_COLLECT, details)


# Read
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
