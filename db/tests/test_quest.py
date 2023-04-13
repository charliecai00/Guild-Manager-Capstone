# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import db.quest as db_quest

TEST_COLLECT = 'TESTING'
TEST_INPUT = {"ID": 995,
              "Name": "TESTING",
              "Challenges": [],
              "ChallengeLevel": 50,
              "Cost": 50,
              "Resell": 50,
              "Purchase": True}


@pytest.fixture(scope='function')
def temp_rec():
    db_quest.add_quest(TEST_INPUT)
    yield
    db_quest.del_quest(995)


def test_get_unpurchase_quest(temp_rec):
    ret = db_quest.get_unpurchase_quest()
    assert isinstance(ret, list)


def test_get_quest_details(temp_rec):
    ret = db_quest.get_quest_details(995)
    assert ret is not None


def test_get_quest_details_not_there(temp_rec):
    ret = db_quest.get_quest_details(404)
    assert ret is None


def test_fetch_curr_id(temp_rec):
    ret = db_quest.fetch_curr_id()
    assert isinstance(ret, int)


def test_update_quest(temp_rec):
    ret = db_quest.update_quest(995, "Purchase", False)
    assert ret is not None
