# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import server.endpoints as ep
from unittest.mock import patch

TEST_CLIENT = ep.app.test_client()

# Create marco mock data structure
FLAG_MSG = (True, "Success")
LIST = [955, 965, 975]


@patch('game.guild_script.generate_guild')
def test_Create(game_guild_script_generate_guild_mock):
    res = TEST_CLIENT.post(ep.CREATE_PATH, json={'Name': 'Testing'}).get_json()
    assert res[ep.RES] == "Success"


RELOAD_MOCK = [{'ID': 955, 'Name': 'Testing1'},
               {'ID': 965, 'Name': 'Testing2'}]


@patch('db.guild.get_guilds', return_value=RELOAD_MOCK)
def test_Reload(db_guild_get_guilds_mock):
    res = TEST_CLIENT.get(ep.RELOAD_PATH).get_json()
    assert isinstance(res[ep.RES], list)


GUILDDETAIL_MOCK = {"get_guild_details": {"ID": 955,
                                          "Name": "Testing1",
                                          "HeroIDs": [1],
                                          "PartyIDs": [3],
                                          "QuestIDs": [5],
                                          "Funds": 100,
                                          "QuestsCompleted": 100},
                    "get_hero_details": {"ID": 1, "Name": "Testing2"},
                    "get_party_details": {"ID": 3, "Name": "Testing3"},
                    "get_quest_details": {"ID": 5, "Name": "Testing4"}}


@patch('db.guild.get_guild_details',
       return_value=GUILDDETAIL_MOCK["get_guild_details"])
@patch('db.hero.get_hero_details',
       return_value=GUILDDETAIL_MOCK["get_hero_details"])
@patch('db.party.get_party_details',
       return_value=GUILDDETAIL_MOCK["get_party_details"])
@patch('db.quest.get_quest_details',
       return_value=GUILDDETAIL_MOCK["get_quest_details"])
def test_GuildDetail(db_guild_get_guild_details_mock,
                     db_hero_get_hero_details_mock,
                     db_party_get_party_details_mock,
                     db_quest_get_quest_details_mock):
    res = TEST_CLIENT.post(ep.GUILD_DETAIL_PATH,
                           json={'id': 955}).get_json()
    assert isinstance(res[ep.RES], dict)


@patch('db.quest.get_unpurchase_quest', return_value=LIST)
def test_Unsold(db_quest_get_unpurchase_quest_mock):
    res = TEST_CLIENT.get(ep.UNSOLD_QUEST_PATH).get_json()
    assert isinstance(res[ep.RES], list)


@patch('game.quest_script.buy_quest', return_value=FLAG_MSG)
def test_Buy(game_quest_script_buy_quest_mock):
    res = TEST_CLIENT.post(ep.BUY_PATH,
                           json={'id': 955, 'guild_id': 965}).get_json()
    assert isinstance(res[ep.RES], str)


@patch('game.quest_script.sell_quest', return_value=FLAG_MSG)
def test_Sell(game_quest_script_sell_quest_mock):
    res = TEST_CLIENT.post(ep.SELL_PATH,
                           json={'id': 955, 'guild_id': 965}).get_json()
    assert isinstance(res[ep.RES], str)


STARTQUEST_MOCK = {"EventList": "Testing1",
                   "Reward": "Testing2",
                   "PartyStatus": "Testing3"}


@patch('game.quest_script.start_quest', return_value=STARTQUEST_MOCK)
def test_StartQuest(game_quest_script_start_quest_mock):
    res = TEST_CLIENT.post(ep.START_PATH,
                           json={'id': 955, 'party_id': 965}).get_json()
    assert isinstance(res[ep.RES], dict)


QUESTDETAIL_MOCK = {"ID": 955,
                    "Name": "Testing",
                    "Challenges": [1, 2, 3],
                    "ChallengeLevel": 50,
                    "Cost": 50,
                    "Resell": 50,
                    "Purchase": True}


@patch('db.quest.get_quest_details', return_value=QUESTDETAIL_MOCK)
def test_QuestDetail(db_quest_get_quest_details_mock):
    res = TEST_CLIENT.post(ep.QUEST_DETAIL_PATH, json={'id': 955}).get_json()
    assert isinstance(res[ep.RES], dict)


@patch('game.guild_script.hire_guild_hero', return_value=FLAG_MSG)
def test_Hire(game_guild_script_hire_guild_hero_mock):
    res = TEST_CLIENT.post(ep.HIRE_PATH,
                           json={'id': 955, 'guild_id': 965}).get_json()
    assert isinstance(res[ep.RES], str)


@patch('game.guild_script.fire_guild_hero', return_value=FLAG_MSG)
def test_Fire(game_guild_script_fire_guild_hero_mock):
    res = TEST_CLIENT.post(ep.FIRE_PATH,
                           json={'id': 955, 'guild_id': 965}).get_json()
    assert isinstance(res[ep.RES], str)


@patch('db.hero.get_unemploy_hero', return_value=LIST)
def test_Unemployed(db_hero_get_unemploy_hero_mock):
    res = TEST_CLIENT.get(ep.UNEMPLOYED_PATH).get_json()
    assert isinstance(res[ep.RES], list)


@patch('game.hero_script.heal_hero', return_value=FLAG_MSG)
def test_Heal(game_hero_script_heal_hero_mock):
    res = TEST_CLIENT.post(ep.HEAL_PATH,
                           json={'id': 955, 'guild_id': 965}).get_json()
    assert isinstance(res[ep.RES], str)


HERODETAIL_MOCK = {"ID": 955,
                   "Name": "Testing",
                   "Health": 50,
                   "MaxHealth": 50,
                   "Exp": 50,
                   "Stats": {
                       "STR": 50,
                       "CON": 50,
                       "DEX": 50,
                       "WIS": 50,
                       "INT": 50,
                       "CHA": 50},
                   "Hired?": True,
                   "InParty?": False,
                   "PartyID": 50,
                   "Cost": 50}


@patch('db.hero.get_hero_details',
       return_value=HERODETAIL_MOCK)
def test_HeroDetail(db_hero_get_hero_details):
    res = TEST_CLIENT.get(ep.HERO_DETAIL_PATH, json={'id': 955}).get_json()
    assert isinstance(res[ep.RES], dict)


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
