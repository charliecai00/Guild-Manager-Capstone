# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

PARTY_KEY = 'ID'
PARTY_COLLECT = 'Party'


# Create
def add_party(details):
    dbc.connect_db()
    return dbc.insert_one(PARTY_COLLECT, details)


# Read
def get_party():
    """
    return a list of dictionary guilds [{...},{...},{...}]
    """
    dbc.connect_db()
    return dbc.fetch_all(PARTY_COLLECT)


def get_party_details(id):
    dbc.connect_db()
    return dbc.fetch_one(PARTY_COLLECT, {PARTY_KEY: id})


def fetch_curr_id():
    dbc.connect_db()
    return dbc.fetch_curr_id(PARTY_COLLECT)


def party_exists(id):
    return get_party_details(id) is not None


# Update
def update_party(id, key, value):
    dbc.connect_db()
    return dbc.update_one(PARTY_COLLECT, {PARTY_KEY: id}, key, value)


# Delete
def del_party(ID):
    dbc.connect_db()
    return dbc.del_one(PARTY_COLLECT, {PARTY_KEY: ID})
