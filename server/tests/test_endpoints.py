# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()


AddHeroes_TestData = {
    "Count": 10,
    "Type": "Mage"
}

HireHeroes_TestData = {
    "Hiree": 0
}

HireHeroes_TestData_fail = {
    "Hiree": "DNE"
}

AddPartyWithHeros_TestData = {
    "HeroIDs": "0",
    "PartyName": "test_party_name"
}

AddPartyWithHeros_TestData_fail = {
    "HeroIDs": "1",
    "PartyName": "testPartyName"
}

DisbandParty_TestData = {
    "PartyID": 0
}

DisbandParty_TestData_fail = {
    "PartyID": 1
}

FireHeroes_TestData = {
    "Firee": 0
}

FireHeroes_TestData_fail = {
    "Firee": "DNE"
}
    
    
def test_AddHeroes():
    res = TEST_CLIENT.post(ep.ADD_HEROES, json=AddHeroes_TestData).get_json()
    assert res[ep.TITLE] == "Add Heroes"


def test_HireHeroes():
    TEST_CLIENT.post(ep.ADD_HEROES, json=AddHeroes_TestData).get_json()
    res = TEST_CLIENT.post(ep.HIRE_HEROS, json=HireHeroes_TestData).get_json()
    assert res[ep.RESULT] == "Hero hired."
    res = TEST_CLIENT.post(ep.FIRE_HERO, json=FireHeroes_TestData).get_json()


def test_HireHeroes_fail():
    TEST_CLIENT.post(ep.ADD_HEROES, json=AddHeroes_TestData).get_json()
    res = TEST_CLIENT.post(ep.HIRE_HEROS, json=HireHeroes_TestData_fail).get_json()
    assert res[ep.RESULT] == "Could not hire hero, out of money."


@pytest.fixture(scope='function')
def temp_rec():
    TEST_CLIENT.post(ep.ADD_HEROES, json=AddHeroes_TestData).get_json()
    TEST_CLIENT.post(ep.HIRE_HEROS, json=HireHeroes_TestData).get_json()
    yield
    # TEST_CLIENT.post(ep.FIRE_HERO, json=FireHeroes_TestData).get_json()


def test_AddPartyWithHeros(temp_rec):
    res = TEST_CLIENT.post(ep.ADD_PARTY_WITH_HEROS, json=AddPartyWithHeros_TestData).get_json()
    assert res[ep.RESULT] == "Heros added to a new party."


def test_AddPartyWithHeros_fail(temp_rec):
    res = TEST_CLIENT.post(ep.ADD_PARTY_WITH_HEROS, json=AddPartyWithHeros_TestData_fail).get_json()
    assert res[ep.RESULT] == "Some heros were not hired in the guild. Check input."


def test_FireHero(temp_rec):
    res = TEST_CLIENT.post(ep.FIRE_HERO, json=FireHeroes_TestData).get_json()
    assert res[ep.RESULT] == "Hero Fired."


def test_FireHeroes_fail(temp_rec):
    res = TEST_CLIENT.post(ep.FIRE_HERO, json=FireHeroes_TestData_fail).get_json()
    assert res[ep.RESULT] == "Request failed. Check input."


def test_DisbandParty(temp_rec):
    res = TEST_CLIENT.post(ep.DISBAND_PARTY, json=DisbandParty_TestData).get_json()
    assert res[ep.RESULT] == "{} disbanded.".format(DisbandParty_TestData["PartyID"])


def test_DisbandParty_fail(temp_rec):
    res = TEST_CLIENT.post(ep.DISBAND_PARTY, json=DisbandParty_TestData_fail).get_json()
    assert res[ep.RESULT] == "Request failed. Check input."


# To Be Added Later
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


def test_GET_QUEST():
    res = TEST_CLIENT.get(ep.GET_QUEST).get_json()
    assert res[ep.TITLE] == "Get Quest"


def test_List():
    res = TEST_CLIENT.get(ep.LIST).get_json()
    assert res[ep.TITLE] == "List Guild Members"
