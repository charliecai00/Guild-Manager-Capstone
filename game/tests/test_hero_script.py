# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from unittest.mock import patch
import game.hero_script as hs

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
EX_HERO_HURT = {
    "ID": 0,
    "Name": "String",
    "Health": 1,
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
EX_HERO_HEALTHY = {
    "ID": 0,
    "Name": "String",
    "Health": 5,
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


# heal_hero tests
@patch('hero_script.hero_db.get_hero_details',
       return_value=EX_HERO_HURT.copy())
@patch('hero_script.guild_db.get_guild_details',
       return_value=EX_GUILD_FULL.copy())
@patch('hero_script.hero_db.update_hero')
def test_heal_hero_works(get_hero_details_mock,
                         get_guild_details_mock,
                         update_hero_mock):
    ret = hs.heal_hero(0, 0)
    assert ret[1] == "Hero has been healed"
    assert ret[0] is True


@patch('hero_script.hero_db.get_hero_details',
       return_value=EX_HERO_HURT.copy())
@patch('hero_script.guild_db.get_guild_details',
       return_value=EX_GUILD_EMPTY.copy())
@patch('hero_script.hero_db.update_hero')
def test_heal_hero_broke(get_hero_details_mock,
                         get_guild_details_mock,
                         update_hero_mock):
    ret = hs.heal_hero(0, 0)
    assert ret[1] == "Guild does not have enough funds to heal"
    assert ret[0] is False


@patch('hero_script.hero_db.get_hero_details',
       return_value=EX_HERO_HEALTHY.copy())
@patch('hero_script.guild_db.get_guild_details',
       return_value=EX_GUILD_FULL.copy())
@patch('hero_script.hero_db.update_hero')
def test_heal_hero_healthy(get_hero_details_mock,
                         get_guild_details_mock,
                         update_hero_mock):
    ret = hs.heal_hero(0, 0)
    assert ret[1] == "Hero already healthy"
    assert ret[0] is False


@patch('hero_script.hero_db.get_hero_details',
       return_value=None)
@patch('hero_script.guild_db.get_guild_details',
       return_value=EX_GUILD_FULL.copy())
@patch('hero_script.hero_db.update_hero')
def test_heal_hero_missing_hero(get_hero_details_mock,
                         get_guild_details_mock,
                         update_hero_mock):
    ret = hs.heal_hero(0, 0)
    assert ret[1] == "Hero does not exist"
    assert ret[0] is False


@patch('hero_script.hero_db.get_hero_details',
       return_value=EX_HERO_HEALTHY)
@patch('hero_script.guild_db.get_guild_details',
       return_value=None)
@patch('hero_script.hero_db.update_hero')
def test_heal_hero_missing_guild(get_hero_details_mock,
                         get_guild_details_mock,
                         update_hero_mock):
    ret = hs.heal_hero(0, 0)
    assert ret[1] == "Guild does not exist"
    assert ret[0] is False


# test_hero tests
@patch('hero_script.hero_db.get_hero_details',
       return_value=EX_HERO_HEALTHY)
def test_test_hero_works(get_hero_details_mock):
    ret = hs.test_hero(0, "STR")
    assert ret[0] is True


@patch('hero_script.hero_db.get_hero_details',
       return_value=None)
def test_test_hero_missing_hero(get_hero_details_mock):
    ret = hs.test_hero(0, "STR")
    assert ret[1] == "Hero does not exist"
    assert ret[0] is False
