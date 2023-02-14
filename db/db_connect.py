# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import os
import pymongo as pm

DB = "Guild_Manager"

client = None


def connect_db():
    global client
    if client is None:  # not connected yet!
        print("Connecting to Mongo in the cloud.")
        client = pm.MongoClient("mongodb+srv://db_connect:LVeg9jwn4riFo6vF"
                                + "@guild-manager.kr7jklo.mongodb.net/"
                                + "?retryWrites=true&w=majority")


def insert_one(collection, doc, db=DB):
    """
    Insert a single doc into collection.
    """
    client[db][collection].insert_one(doc)


def fetch_all(collection, db=DB):
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_all_as_dict(key, collection, db=DB):
    ret = {}
    for doc in client[db][collection].find():
        del doc['_id']
        ret[doc[key]] = doc
    return ret


def fetch_field(field, collection, db=DB):
    return client[db][collection].distinct(field)


def fetch_one(collection, filt, db=DB):
    """
    Find a filter and return on the first doc found.
    """
    for doc in client[db][collection].find(filt):
        return doc


def del_one(collection, filt, db=DB):
    """
    Find with a filter and return on the first doc found.
    """
    client[db][collection].delete_one(filt)
