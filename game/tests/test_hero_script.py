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
