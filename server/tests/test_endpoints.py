# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import server.endpoints as ep
from unittest.mock import patch

TEST_CLIENT = ep.app.test_client()


@patch('guild_script.generate_guild')
def test_Create(create_mock):
    res = TEST_CLIENT.post(ep.CREATE_PATH, json={'Name': 'Testing'}).get_json()
    assert res[ep.RES] == "Success"


# def test_Reload():
#     res = TEST_CLIENT.get(ep.RELOAD_PATH).get_json()
#     assert isinstance(res[ep.RES], list)


# def test_GuildDetail():
#     res = TEST_CLIENT.post(ep.GUILD_DETAIL_PATH,
#                            json={'id': 0}).get_json()
#     assert isinstance(res[ep.RES], dict)


# def test_Unsold():
#     res = TEST_CLIENT.get(ep.UNSOLD_QUEST_PATH).get_json()
#     assert isinstance(res[ep.RES], list)


# def test_Buy():
#     res = TEST_CLIENT.post(ep.BUY_PATH,
#                            json={'id': 9999, 'guild_id': 9999}).get_json()
#     assert isinstance(res[ep.RES], str)


# def test_Sell():
#     res = TEST_CLIENT.post(ep.SELL_PATH,
#                            json={'id': 9999, 'guild_id': 9999}).get_json()
#     assert isinstance(res[ep.RES], str)


# def test_StartQuest():
#     res = TEST_CLIENT.post(ep.START_PATH,
#                            json={'id': 9999, 'party_id': 9999}).get_json()
#     assert isinstance(res[ep.RES], str)


# def test_QuestDetail():
#     res = TEST_CLIENT.post(ep.QUEST_DETAIL_PATH, json={'id': 0}).get_json()
#     assert isinstance(res[ep.RES], dict)


# def test_Hire():
#     res = TEST_CLIENT.post(ep.HIRE_PATH,
#                            json={'id': 9999, 'guild_id': 9999}).get_json()
#     assert isinstance(res[ep.RES], str)


# def test_Fire():
#     res = TEST_CLIENT.post(ep.FIRE_PATH,
#                            json={'id': 9999, 'guild_id': 9999}).get_json()
#     assert isinstance(res[ep.RES], str)


# def test_Unemployed():
#     res = TEST_CLIENT.get(ep.UNEMPLOYED_PATH).get_json()
#     assert isinstance(res[ep.RES], list)


# def test_Heal():
#     res = TEST_CLIENT.post(ep.HEAL_PATH,
#                            json={'id': 9999, 'guild_id': 9999}).get_json()
#     assert isinstance(res[ep.RES], str)


# def test_HeroDetail():
#     res = TEST_CLIENT.get(ep.HERO_DETAIL_PATH, json={'id': 0}).get_json()
#     assert isinstance(res[ep.RES], list)


# def test_HeroNotInParty():
#     res = TEST_CLIENT.get(ep.HERO_NOT_IN_PARTY_PATH).get_json()
#     assert isinstance(res[ep.RES], list)


# def test_DBAddHero():
#     res = TEST_CLIENT.get(ep.DB_ADD_HERO_PATH).get_json()
#     assert res[ep.RES] == "Success"


# def test_AddParty():
#     res = TEST_CLIENT.post(ep.ADD_PARTY_PATH,
#                            json={'Name': 'test_AddParty', 'guild_id': 9999})
#     assert isinstance(res[ep.RES], str)


# def test_DisbandParty():
#     res = TEST_CLIENT.post(ep.DISBAND_PARTY_PATH,
#                            json={'id': 9999, 'party_id': 9999}).get_json()
#     assert isinstance(res[ep.RES], str)


# def test_AddHero():
#     res = TEST_CLIENT.post(ep.ADD_HERO_PATH,
#                            json={'id': 9999, 'party_id': 9999}).get_json()
#     assert isinstance(res[ep.RES], str)


# def test_RemoveHero():
#     res = TEST_CLIENT.post(ep.REMOVE_HERO_PATH,
#                            json={'id': 9999, 'party_id': 9999}).get_json()
#     assert isinstance(res[ep.RES], str)


# def test_GetParty():
#     res = TEST_CLIENT.get(ep.GET_PARTY_PATH).get_json()
#     assert isinstance(res[ep.RES], list)


# def test_PartyDetail():
#     res = TEST_CLIENT.get(ep.PARTY_DETAIL_PATH, json={'id': 0}).get_json()
#     assert isinstance(res[ep.RES], dict)


# RESETDB_MOCK = {"deleted_count": 200}

# @patch('dbc.del_many', return_value=RESETDB_MOCK["deleted_count"])
# @patch('hero_script.generate_hero')
# @patch('quest_script.generate_quest')
# def test_ResetDB(mock_ResetDB):
#     res = TEST_CLIENT.get(ep.RESET_DB_PATH).get_json()
#     assert res is not None