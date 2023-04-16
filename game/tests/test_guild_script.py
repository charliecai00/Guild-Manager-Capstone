# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from unittest.mock import patch
import game.guild_script as gs

EX_GUILD_FULL = {
    "ID": 0,
    "Name": "TestFull",
    "HeroIDs": [0, 1, 2, 3, 4],
    "PartyIDs": [0, 1, 2, 3, 4],
    "QuestIDs": [0, 1, 2, 3, 4],
    "Funds": 999,
    "QuestsCompleted": 999
}
EX_GUILD_EMPTY = {
    "ID": 1,
    "Name": "TestEmpty",
    "HeroIDs": [],
    "PartyIDs": [],
    "QuestIDs": [],
    "Funds": 0,
    "QuestsCompleted": 0
}
EX_HERO_UNEMPLOYED = {
    "ID": 0,
    "Name": "String",
    "Health": 0,
    "MaxHealth": 5,
    "Exp": 0,
    "Stats": {
        "STR": 20,
        "CON": 20,
        "DEX": 20,
        "WIS": 20,
        "INT": 20,
        "CHA": 20
    },
    "Hired?": False,
    "InParty?": False,
    "PartyID": 0,
    "Cost": 999
}
EX_HERO_EMPLOYED = {
    "ID": 0,
    "Name": "String",
    "Health": 0,
    "MaxHealth": 5,
    "Exp": 0,
    "Stats": {
        "STR": 20,
        "CON": 20,
        "DEX": 20,
        "WIS": 20,
        "INT": 20,
        "CHA": 20
    },
    "Hired?": True,
    "InParty?": False,
    "PartyID": 0,
    "Cost": 999
}


@patch('guild_script.hero_db.get_hero_details',
       return_value=EX_HERO_UNEMPLOYED.copy())
@patch('guild_script.guild_db.get_guild_details',
       return_value=EX_GUILD_FULL.copy())
@patch('guild_script.guild_db.update_guild')
@patch('guild_script.hero_db.update_hero')
def test_hire_guild_hero_works(get_hero_details_mock,
                               get_guild_details_mock,
                               update_guild_mock,
                               update_hero_mock):
    ret = gs.hire_guild_hero(0, 0)
    assert ret[1] == ""
    assert ret[0] is True


@patch('guild_script.hero_db.get_hero_details',
       return_value=EX_HERO_UNEMPLOYED.copy())
@patch('guild_script.guild_db.get_guild_details',
       return_value=EX_GUILD_EMPTY.copy())
@patch('guild_script.guild_db.update_guild')
@patch('guild_script.hero_db.update_hero')
def test_hire_guild_hero_broke_guild(get_hero_details_mock,
                                     get_guild_details_mock,
                                     update_guild_mock,
                                     update_hero_mock):
    ret = gs.hire_guild_hero(0, 0)
    assert ret[1] == "Guild does not have enough funds"
    assert ret[0] is False


@patch('guild_script.hero_db.get_hero_details',
       return_value=EX_HERO_EMPLOYED.copy())
@patch('guild_script.guild_db.get_guild_details',
       return_value=EX_GUILD_FULL.copy())
@patch('guild_script.guild_db.update_guild')
@patch('guild_script.hero_db.update_hero')
def test_hire_guild_hero_hired_hero(get_hero_details_mock,
                                    get_guild_details_mock,
                                    update_guild_mock,
                                    update_hero_mock):
    ret = gs.hire_guild_hero(0, 0)
    assert ret[1] == "Hero already hired"
    assert ret[0] is False


@patch('guild_script.hero_db.get_hero_details',
       return_value=EX_HERO_EMPLOYED.copy())
@patch('guild_script.guild_db.get_guild_details',
       return_value=None)
@patch('guild_script.guild_db.update_guild')
@patch('guild_script.hero_db.update_hero')
def test_hire_guild_hero_missing_guild(get_hero_details_mock,
                                       get_guild_details_mock,
                                       update_guild_mock,
                                       update_hero_mock):
    ret = gs.hire_guild_hero(0, 0)
    assert ret[1] == "Guild does not exist"
    assert ret[0] is False


@patch('guild_script.hero_db.get_hero_details',
       return_value=None)
@patch('guild_script.guild_db.get_guild_details',
       return_value=EX_GUILD_FULL.copy())
@patch('guild_script.guild_db.update_guild')
@patch('guild_script.hero_db.update_hero')
def test_hire_guild_hero_missing_hero(get_hero_details_mock,
                                      get_guild_details_mock,
                                      update_guild_mock,
                                      update_hero_mock):
    ret = gs.hire_guild_hero(0, 0)
    assert ret[1] == "Hero does not exist"
    assert ret[0] is False
