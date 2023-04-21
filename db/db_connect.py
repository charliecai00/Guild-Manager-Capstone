# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pymongo as pm

DB = "Guild_Manager"
client = None


def connect_db():
    """
    Create a database connection
    """
    global client
    if client is None:  # not connected yet!
        print("Connecting to Mongo in the cloud.")
        client = pm.MongoClient("mongodb+srv://db_connect:LVeg9jwn4riFo6vF"
                                + "@guild-manager.kr7jklo.mongodb.net/"
                                + "?retryWrites=true&w=majority")


# Create
def insert_one(collection, doc, db=DB):
    """
    Insert a single doc into collection
    """
    return client[db][collection].insert_one(doc)


# Read
def fetch_all(collection, db=DB):
    """
    Return all rows as a list
    """
    ret = []
    for doc in client[db][collection].find():
        del doc['_id']
        ret.append(doc)
    return ret


# Read
def fetch_all_as_dict(key, collection, db=DB):
    """
    Return all rows as dictionary, use @parameter key as dictionary key
    """
    ret = {}
    for doc in client[db][collection].find():
        del doc['_id']
        ret[doc[key]] = doc
    return ret


def fetch_one(collection, filt, db=DB):
    """
    Use a filter and return on the first doc found.
    """
    for doc in client[db][collection].find(filt):
        del doc['_id']
        return doc


def fetch_curr_id(collection, db=DB):
    """
    Return the last ID of collection
    """
    sort_key = []
    for doc in client[db][collection].find():
        sort_key.append(doc['ID'])
    sort_key.sort()
    if len(sort_key) == 0:
        return 0
    return sort_key[-1]


# Update
def update_one(collection, filt, key, detail, db=DB):
    """
    Using ID as filter, update a value in that row
    """
    return client[db][collection].update_one(filt, {"$set": {key: detail}})


# Delete
def del_one(collection, filt, db=DB):
    """
    Delete one row matching the filter
    """
    return client[db][collection].delete_one(filt)


def del_all(collection, db=DB):
    """
    Delete all rows matching the filter
    """
    connect_db()
    return client[db][collection].delete_many({})
