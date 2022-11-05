import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

AddToParty_sample = {
    "HeroIDs": "Data ...",
    "PartyID": "Data ..."
}

def test_AddToParty():
    pass

DoQuest_sample = {
    "PartyID": "Data ...",
    "QuestID": "Data ..."
}

def test_DoQuest():
    pass

GetHeroes_sample = {
    "Count": "Data ...",
    "Type": "Data ..."
}

def test_GetHeroes():
    pass

GetHeroes_sample = {
    "Count": "Data ...",
    "Type": "Data ..."
}

def test_GetHeroes():
    pass