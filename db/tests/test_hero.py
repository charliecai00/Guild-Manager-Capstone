# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import db.hero as db_hero

TEST_COLLECT = 'TESTING'
TEST_INPUT = {"ID": 975,
              "Name": "TESTING",
              "Health": 100,
              "MaxHealth": 100,
              "Exp": 100,
              "Stats": {
                  "STR": 100,
                  "CON": 100,
                  "DEX": 100,
                  "WIS": 100,
                  "INT": 100,
                  "CHA": 100},
              "Hired?": True,
              "InParty?": True,
              "PartyID": 100,
              "Cost": 100}


@pytest.fixture(scope='function')
def temp_rec():
    db_hero.add_hero(TEST_INPUT)
    yield
    db_hero.del_hero(975)


def test_get_unemploy_hero(temp_rec):
    ret = db_hero.get_unemploy_hero()
    assert isinstance(ret, list)


def test_get_hero_details(temp_rec):
    ret = db_hero.get_hero_details(975)
    assert ret is not None


def test_get_hero_details_not_there(temp_rec):
    ret = db_hero.get_hero_details(976)
    assert ret is None


def test_fetch_curr_id(temp_rec):
    ret = db_hero.fetch_curr_id()
    assert isinstance(ret, int)


def test_update_hero(temp_rec):
    ret = db_hero.update_hero(975, "Exp", 105)
    assert ret is not None
