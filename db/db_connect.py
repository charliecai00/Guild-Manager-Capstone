import os

import pymongo as pm

REMOTE = "0"
LOCAL = "1"
GAME_DB = "gamedb"

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


def fetch_all(collection, db=GAME_DB):
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret
