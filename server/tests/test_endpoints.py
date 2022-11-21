import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

AddToParty_sample = {
    "HeroIDs": "0,1,2",
    "PartyID": "0"
}

def test_AddToParty():
    # res = TEST_CLIENT.post(ep.ADD_TO_PARTY, json=AddToParty_sample).get_json()
    pass

DoQuest_sample_fail = {
    "PartyID": "0",
    "QuestID": "0"
}

def test_DoQuest_fail():
    res = TEST_CLIENT.post(ep.DO_QUEST, json=DoQuest_sample_fail).get_json()
    assert isinstance(res[ep.RESULT], str)

GetHeroes_sample = {
    "Count": 10,
    "Type": "Mage"
}

def test_GetHeroes():
    res = TEST_CLIENT.post(ep.GET_HEROES, json=GetHeroes_sample).get_json()
    assert isinstance(res[ep.TYPE], str)
    assert isinstance(res[ep.TITLE], str)


def test_GET_QUEST():
    res = TEST_CLIENT.get(ep.GET_QUEST).get_json()
    assert isinstance(res[ep.TYPE], str)
    assert isinstance(res[ep.TITLE], str)

HireHeroes_sample_fail = {
    "HireList": "DNE"
}

def test_HireHeroes_error():
    res = TEST_CLIENT.post(ep.HIRE_HEROES, json=HireHeroes_sample_fail).get_json()
    assert isinstance(res[ep.ERROR], str)

def test_List():
    res = TEST_CLIENT.get(ep.LIST).get_json()
    assert isinstance(res[ep.TYPE], str)
    assert isinstance(res[ep.TITLE], str)
    