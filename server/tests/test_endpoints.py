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

def test_GET_QUEST():
    res = TEST_CLIENT.get(ep.GET_QUEST).get_json()
    assert isinstance(res[ep.TYPE], str)
    assert isinstance(res[ep.TITLE], str)

HireHeroes_sample = {
    "HireList": "Data ..."
}

def test_HireHeroes():
    pass

HireHeroes_error_sample = {
    "HireList": "DNE"
}

def test_HireHeroes_error():
    # res = TEST_CLIENT.get(ep.HIRE_HEROES).get_json()
    # assert isinstance(res[ep.ERROR], str)
    pass

def test_List():
    res = TEST_CLIENT.get(ep.LIST).get_json()
    assert isinstance(res[ep.TYPE], str)
    assert isinstance(res[ep.TITLE], str)
    