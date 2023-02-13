# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

ID = 'ID'
NAME = 'NAME'
HERO_ID = 'HERO_ID'

PARTY_KEY = 'ID'
PARTY_COLLECT = 'Party'

TEST_PARTY = 'TEST_PARTY'
REQUIRED_FLDS = [ID, NAME, HERO_ID]
dummy_party = {TEST_PARTY: {ID: 1,
                            NAME: "Temporary Party",
                            HERO_ID: [1, 2, 3]}}


def add_party(details):
    dbc.connect_db()
    return dbc.insert_one(PARTY_COLLECT, details)


def get_party():
    """
    return a list of dictionary guilds [{...},{...},{...}]
    """
    dbc.connect_db()
    return dbc.fetch_all(PARTY_COLLECT)


def del_party(ID):
    dbc.connect_db()
    return dbc.del_one(PARTY_COLLECT, {PARTY_KEY: ID})
