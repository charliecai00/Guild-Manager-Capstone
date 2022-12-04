# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import os

import pymongo as pm

REMOTE = "0"
LOCAL = "1"
GUILD_DB = "guild_db"

client = None


def connect_db():
    """
    Connect to DB across all uses
    Return a mongo client object
    Set global client variable
    """
    global client
    if client is None:
        print("Setting client because it is None.")
        if os.environ.get("LOCAL_MONGO", LOCAL) == LOCAL:
            print("Connecting to Mongo locally.")
            client = pm.MongoClient()


def insert_one(collection, doc, db=GUILD_DB):
    """
    Insert a single doc into collection.
    """
    client[db][collection].insert_one(doc)


def fetch_one(collection, filt, db=GUILD_DB):
    """
    Find a filter and return on the first foc found.
    """
    for doc in client[db][collection].find(filt):
        return doc


def del_one(collection, filt, db=GUILD_DB):
    """
    Find with a filter and return on the first doc found.
    """
    client[db][collection].delete_one(filt)


def fetch_all(collection, db=GUILD_DB):
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_all_as_dict(key, collection, db=GUILD_DB):
    ret = {}
    for doc in client[db][collection].find():
        del doc['_id']
        ret[doc[key]] = doc
    return ret
