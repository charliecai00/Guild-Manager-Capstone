# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

# AddToParty_TestData = {
#     "HeroIDs": "0,1,2",
#     "PartyID": "0"
# }

# def test_AddToParty():
#     res = TEST_CLIENT.post(ep.ADD_TO_PARTY, json=AddToParty_TestData).get_json()
#     assert res[ep.RESULT] == "Heros added to party."
    
AddToParty_TestData_fail = {
    "HeroIDs": "0",
    "PartyID": "0"
}

def test_AddToParty_fail():
    res = TEST_CLIENT.post(ep.ADD_TO_PARTY, json=AddToParty_TestData_fail).get_json()
    print(res[ep.RESULT])
    assert res[ep.RESULT] == "Some heros were not added. Check input."


# DisbandParty_TestData = {
#     "PartyID": "0"
# }

# def test_DisbandParty():
#     res = TEST_CLIENT.post(ep.DISBAND_PARTY, json=DisbandParty_TestData).get_json()
#     assert res[ep.RESULT] == "{} disbanded.".format(DisbandParty_TestData["PartyID"])
    
DisbandParty_TestData_fail = {
    "PartyID": "0"
}

def test_DisbandParty_fail():
    res = TEST_CLIENT.post(ep.DISBAND_PARTY, json=DisbandParty_TestData_fail).get_json()
    assert res[ep.RESULT] == "Request failed. Check input."
    

# DoQuest_TestData = {
#     "PartyID": "0",
#     "QuestID": "0"
# }

# def test_DoQuest():
#     res = TEST_CLIENT.post(ep.DO_QUEST, json=DoQuest_TestData).get_json()
#     assert res[ep.RESULT] == "{} completed the quest!".format(DoQuest_TestData["PartyID"])
       
DoQuest_TestData_fail = {
    "PartyID": "0",
    "QuestID": "0"
}

def test_DoQuest_fail():
    res = TEST_CLIENT.post(ep.DO_QUEST, json=DoQuest_TestData_fail).get_json()
    assert res[ep.RESULT] == "Request failed. Check input."


GetHeroes_TestData = {
    "Count": 10,
    "Type": "Mage"
}

def test_GetHeroes():
    res = TEST_CLIENT.post(ep.GET_HEROES, json=GetHeroes_TestData).get_json()
    assert res[ep.TITLE] == "Get Heroes"


def test_GET_QUEST():
    res = TEST_CLIENT.get(ep.GET_QUEST).get_json()
    assert res[ep.TITLE] == "Get Quest"


# HireHeroes_TestData = {
#     "Hiree": "0"
# }

# def test_HireHeroes():
#     res = TEST_CLIENT.post(ep.HIRE_HERO, json=HireHeroes_TestData).get_json()
#     assert res[ep.RESULT] == "Hero hired."

HireHeroes_TestData_fail = {
    "Hiree": "DNE"
}

def test_HireHeroes_fail():
    res = TEST_CLIENT.post(ep.HIRE_HERO, json=HireHeroes_TestData_fail).get_json()
    assert res[ep.RESULT] == "Could not hire hero, out of money."


# FireHeroes_TestData = {
#     "Firee": "0"
# }

# def test_FireHeroes():
#     res = TEST_CLIENT.post(ep.FIRE_HERO, json=FireHeroes_TestData).get_json()
#     assert res[ep.RESULT] == "Hero fried."

FireHeroes_TestData_fail = {
    "Firee": "DNE"
}

def test_FireHeroes_fail():
    res = TEST_CLIENT.post(ep.FIRE_HERO, json=FireHeroes_TestData_fail).get_json()
    assert res[ep.RESULT] == "Request failed. Check input."
    
    
def test_List():
    res = TEST_CLIENT.get(ep.LIST).get_json()
    assert res[ep.TITLE] == "List Guild Members"
    