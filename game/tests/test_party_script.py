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


# add_party_hero tests
@patch('db.party.get_party_details',
       return_value=EX_PARTY_HERO_EXCLUDED.copy())
@patch('db.hero.get_hero_details',
       return_value=EX_HERO_NOT_INPARTY.copy())
@patch('db.party.update_party')
@patch('db.hero.update_hero')
def test_add_party_hero_works(get_party_detail_mock,
                              get_hero_details_mock,
                              update_party_mock,
                              update_hero_mock):
    ret = ps.add_party_hero(1, 0)
    assert ret[1] == ""
    assert ret[0] is True


@patch('db.party.get_party_details',
       return_value=EX_PARTY_HERO_EXCLUDED.copy())
@patch('db.hero.get_hero_details',
       return_value=EX_HERO_INPARTY.copy())
@patch('db.party.update_party')
@patch('db.hero.update_hero')
def test_add_party_hero_hero_inparty(get_party_detail_mock,
                                     get_hero_details_mock,
                                     update_party_mock,
                                     update_hero_mock):
    ret = ps.add_party_hero(1, 0)
    assert ret[1] == "Hero already in a party"
    assert ret[0] is False


@patch('db.party.get_party_details',
       return_value=EX_PARTY_HERO_EXCLUDED.copy())
@patch('db.hero.get_hero_details',
       return_value=None)
@patch('db.party.update_party')
@patch('db.hero.update_hero')
def test_add_party_hero_missing_hero(get_party_detail_mock,
                                     get_hero_details_mock,
                                     update_party_mock,
                                     update_hero_mock):
    ret = ps.add_party_hero(1, 0)
    assert ret[1] == "Hero does not exist"
    assert ret[0] is False


@patch('db.party.get_party_details',
       return_value=None)
@patch('db.hero.get_hero_details',
       return_value=EX_HERO_NOT_INPARTY)
@patch('db.party.update_party')
@patch('db.hero.update_hero')
def test_add_party_hero_missing_party(get_party_detail_mock,
                                      get_hero_details_mock,
                                      update_party_mock,
                                      update_hero_mock):
    ret = ps.add_party_hero(1, 0)
    assert ret[1] == "Party does not exist"
    assert ret[0] is False


# remove_party_hero tests
@patch('db.party.get_party_details',
       return_value=EX_PARTY_HERO_INCLUDED)
@patch('db.hero.get_hero_details',
       return_value=EX_HERO_INPARTY)
@patch('db.party.update_party')
@patch('db.hero.update_hero')
def test_remove_party_hero_works(get_party_detail_mock,
                                 get_hero_details_mock,
                                 update_party_mock,
                                 update_hero_mock):
    ret = ps.remove_party_hero(1, 0)
    assert ret[1] == ""
    assert ret[0] is True


@patch('db.party.get_party_details',
       return_value=None)
@patch('db.hero.get_hero_details',
       return_value=EX_HERO_INPARTY)
@patch('db.party.update_party')
@patch('db.hero.update_hero')
def test_remove_party_hero_missing_party(get_party_detail_mock,
                                         get_hero_details_mock,
                                         update_party_mock,
                                         update_hero_mock):
    ret = ps.remove_party_hero(1, 0)
    assert ret[1] == "Party does not exist"
    assert ret[0] is False


@patch('db.party.get_party_details',
       return_value=EX_PARTY_HERO_INCLUDED)
@patch('db.hero.get_hero_details',
       return_value=None)
@patch('db.party.update_party')
@patch('db.hero.update_hero')
def test_remove_party_hero_missing_hero(get_party_detail_mock,
                                        get_hero_details_mock,
                                        update_party_mock,
                                        update_hero_mock):
    ret = ps.remove_party_hero(1, 0)
    assert ret[1] == "Hero does not exist"
    assert ret[0] is False


@patch('db.party.get_party_details',
       return_value=EX_PARTY_HERO_INCLUDED)
@patch('db.hero.get_hero_details',
       return_value=EX_HERO_INPARTY)
def test_test_party_single_works(get_party_details_mock,
                                 get_hero_details_mock):
    ret = ps.test_party_single(1, "STR")
    assert ret[0] is True


@patch('db.party.get_party_details',
       return_value=None)
@patch('db.hero.get_hero_details',
       return_value=EX_HERO_INPARTY)
def test_test_party_single_mising_party(get_party_details_mock,
                                        get_hero_details_mock):
    ret = ps.test_party_single(1, "STR")
    assert ret[1] == "Party does not exist"
    assert ret[0] is False


@patch('db.party.get_party_details',
       return_value=EX_PARTY_HERO_EXCLUDED)
@patch('db.hero.get_hero_details',
       return_value=None)
def test_test_party_single_mising_hero(get_party_details_mock,
                                       get_hero_details_mock):
    ret = ps.test_party_single(1, "STR")
    assert ret[1] == "Hero does not exist"
    assert ret[0] is False
