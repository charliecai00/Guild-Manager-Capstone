# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

PARTY_KEY = 'ID'
PARTY_COLLECT = 'Party'


# Create
def add_party(details):
    """
    Insert a single doc into collection
    """
    dbc.connect_db()
    return dbc.insert_one(PARTY_COLLECT, details)


# Read
def get_party_details(id):
    """
    Use ID as filter and return the row matching the ID
    """
    dbc.connect_db()
    return dbc.fetch_one(PARTY_COLLECT, {PARTY_KEY: id})


def fetch_curr_id():
    """
    Return the last ID of collection
    """
    dbc.connect_db()
    return dbc.fetch_curr_id(PARTY_COLLECT)


# Update
def update_party(id, key, value):
    """
    Using @parameter id as filter, update @parameter key value pair
    """
    dbc.connect_db()
    return dbc.update_one(PARTY_COLLECT, {PARTY_KEY: id}, key, value)


# Delete
def del_party(ID):
    """
    Delete the row matching the ID
    """
    dbc.connect_db()
    return dbc.del_one(PARTY_COLLECT, {PARTY_KEY: ID})
