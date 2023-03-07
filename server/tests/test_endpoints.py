# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

# import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()


def test_Create():
    res = TEST_CLIENT.post(ep.CREATE_PATH, json={'Name': 'test'}).get_json()
    assert res[ep.RES] == "Success"


def test_Reload():
    res = TEST_CLIENT.get(ep.RELOAD_PATH).get_json()
    assert res[ep.RES] == "Success"


def test_Unsold():
    res = TEST_CLIENT.get(ep.UNSOLD_QUEST_PATH).get_json()
    assert res[ep.RES] == "Success"


def test_Buy():
    res = TEST_CLIENT.post(ep.BUY_PATH, json={'id': 1}).get_json()
    assert res[ep.RES] == "Success"


def test_Sell():
    res = TEST_CLIENT.post(ep.SELL_PATH, json={'id': 1}).get_json()
    assert res[ep.RES] == "Success"


def test_StartQuest():
    res = TEST_CLIENT.post(ep.START_PATH, json={'id': 1,
                                                'party_id': 1}).get_json()
    assert res[ep.RES] == "Success"


def test_Hire():
    res = TEST_CLIENT.post(ep.HIRE_PATH, json={'id': 1,
                                               'guild_id': 1}).get_json()
    assert res[ep.RES] == "Success"


def test_Fire():
    res = TEST_CLIENT.post(ep.FIRE_PATH, json={'id': 1}).get_json()
    assert res[ep.RES] == "Success"


def test_Unemployed():
    res = TEST_CLIENT.get(ep.UNEMPLOYED_PATH).get_json()
    assert res[ep.RES] == "Success"


def test_Heal():
    res = TEST_CLIENT.post(ep.HEAL_PATH, json={'id': 1})
    assert res[ep.RES] == "Success"


def test_AddParty():
    res = TEST_CLIENT.post(ep.ADD_PARTY_PATH, json={'Name': 'test'})
    assert res[ep.RES] == "Success"


def test_DisbandParty():
    res = TEST_CLIENT.post(ep.DISBAND_PARTY_PATH, json={'id': 1})
    assert res[ep.RES] == "Success"


def test_AddHero():
    res = TEST_CLIENT.post(ep.ADD_HERO_PATH, json={'id': 1, 'party_id': 1})
    assert res[ep.RES] == "Success"


def test_RemoveHero():
    res = TEST_CLIENT.post(ep.REMOVE_HERO_PATH, json={'id': 1, 'party_id': 1})
    assert res[ep.RES] == "Success"


def test_GetParty():
    res = TEST_CLIENT.get(ep.GET_PARTY_PATH).get_json()
    assert res[ep.RES] == "Success"
