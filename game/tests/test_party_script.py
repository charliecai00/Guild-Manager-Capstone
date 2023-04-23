# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from unittest.mock import patch
import game.party_script as ps

EX_HERO_NOT_INPARTY = {
    "ID": 0,
    "Name": "TestSolo",
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
EX_HERO_INPARTY = {
    "ID": 0,
    "Name": "TestParty",
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
    "InParty?": True,
    "PartyID": 1,
    "Cost": 999
}
EX_PARTY_HERO_EXCLUDED = {
            "ID": 1,
            "Name": "TestExcluded",
            "HeroIDs": []
}
EX_PARTY_HERO_INCLUDED = {
            "ID": 1,
            "Name": "TestIncluded",
            "HeroIDs": [0]
}
