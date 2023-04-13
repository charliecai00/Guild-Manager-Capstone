# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import db.party as db_party

TEST_COLLECT = 'TESTING'
TEST_INPUT = {"ID": 985,
              "Name": "TESTING",
              "HeroIDs": []}


@pytest.fixture(scope='function')
def temp_rec():
    db_party.add_party(TEST_INPUT)
    yield
    db_party.del_party(985)


def test_get_party_details(temp_rec):
    ret = db_party.get_party_details(985)
    assert ret is not None


def test_get_hero_details_not_there(temp_rec):
    ret = db_party.get_party_details(404)
    assert ret is None


def test_fetch_curr_id(temp_rec):
    ret = db_party.fetch_curr_id()
    assert isinstance(ret, int)


def test_update_party(temp_rec):
    ret = db_party.update_party(985, "HeroIDs", [3, 4, 5])
    assert ret is not None
