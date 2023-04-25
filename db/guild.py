# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

GUILD_KEY = 'ID'
GUILD_COLLECT = 'Guild'


# Create
def add_guild(details):
    """
    Insert a single doc into collection
    """
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
    """
    Return the last ID of collection
    """
    dbc.connect_db()
    return dbc.fetch_curr_id(GUILD_COLLECT)


def get_guild_details(id):
    """
    Use ID as filter and return the row matching the ID
    """
    dbc.connect_db()
    return dbc.fetch_one(GUILD_COLLECT, {GUILD_KEY: id})


# Update
def update_guild(id, key, value):
    """
    Parameter:  id = guild id
                key = column name ex. Funds
                value = the value ex. 999999
    """
    dbc.connect_db()
    return dbc.update_one(GUILD_COLLECT, {GUILD_KEY: id}, key, value)


# Delete
def del_guild(ID):
    """
    Delete one row using ID
    """
    dbc.connect_db()
    return dbc.del_one(GUILD_COLLECT, {GUILD_KEY: ID})
