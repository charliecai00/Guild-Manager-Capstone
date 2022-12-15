# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import db.game as game
import db.hero as hero
import db.quest as hero
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

# AddToParty_TestData = {
#     "HeroIDs": "0,1,2",
#     "PartyID": "0"
# }

# def test_AddToParty():
#     res = TEST_CLIENT.post(ep.ADD_TO_PARTY, json=AddToParty_TestData).get_json()
#     assert res[ep.RESULT] == True
    
AddToParty_TestData_fail = {
    """
    Input cause failure due to `0` is not a valid hero
    """
    
    "HeroIDs": "0",
    "PartyID": "0"
}

def test_AddToParty():
    res = TEST_CLIENT.post(ep.ADD_TO_PARTY, json=AddToParty_TestData_fail).get_json()
    assert res[ep.RESULT] == False


# DisbandParty_TestData = {
#     "PartyID": "0"
# }

# def test_DisbandParty():
#     res = TEST_CLIENT.post(ep.DISBAND_PARTY, json=DisbandParty_TestData).get_json()
#     assert res[ep.RESULT] == True
    
DisbandParty_TestData_fail = {
    """
    Input cause failure due to `0` is not a valid party
    """
    
    "PartyID": "0"
}

def test_DisbandParty_fail():
    res = TEST_CLIENT.post(ep.DISBAND_PARTY, json=DisbandParty_TestData_fail).get_json()
    assert res[ep.RESULT] == False
    

# DoQuest_TestData = {
#     "PartyID": "0",
#     "QuestID": "0"
# }

# def test_DoQuest():
#     res = TEST_CLIENT.post(ep.DO_QUEST, json=DoQuest_TestData).get_json()
#     assert res[ep.RESULT] == True
       
DoQuest_TestData_fail = {
    """
    Input cause failure due to quest does not exist
    """
    
    "PartyID": "0",
    "QuestID": "0"
}

def test_DoQuest_fail():
    res = TEST_CLIENT.post(ep.DO_QUEST, json=DoQuest_TestData_fail).get_json()
    assert res[ep.RESULT] == False


GetHeroes_TestData = {
    "Count": 10,
    "Type": "Mage"
}

def test_GetHeroes():
    res = TEST_CLIENT.post(ep.GET_HEROES, json=GetHeroes_TestData).get_json()
    assert isinstance(res[ep.TYPE], str)
    assert isinstance(res[ep.TITLE], str)


def test_GET_QUEST():
    res = TEST_CLIENT.get(ep.GET_QUEST).get_json()
    assert isinstance(res[ep.TYPE], str)
    assert isinstance(res[ep.TITLE], str)

HireHeroes_TestData_fail = {
    "HireList": "DNE"
}

def test_HireHeroes_error():
    res = TEST_CLIENT.post(ep.HIRE_HEROES, json=HireHeroes_TestData_fail).get_json()
    assert isinstance(res[ep.ERROR], str)

def test_List():
    res = TEST_CLIENT.get(ep.LIST).get_json()
    assert isinstance(res[ep.TYPE], str)
    assert isinstance(res[ep.TITLE], str)
    