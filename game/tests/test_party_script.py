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

@patch('party_script.party_db.get_party_details',
       return_value=EX_PARTY_HERO_EXCLUDED.copy())
@patch('party_script.hero_db.get_hero_details',
       return_value=EX_HERO_NOT_INPARTY.copy())
@patch('party_script.party_db.update_party')
@patch('party_script.hero_db.update_hero')
def test_add_party_hero_works(get_party_detail_mock,
                              get_hero_details_mock,
                              update_party_mock,
                              update_hero_mock):
    ret = ps.add_party_hero(1, 0)
    assert ret[1] == ""
    assert ret[0] is True
