# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import db.db_connect as dbc

TEST_DB = dbc.DB
TEST_COLLECT = 'TESTING'
TEST_INPUT = {"ID": 955,
              "Name": "TESTING",
              "Funds": 50}


@pytest.fixture(scope='function')
def temp_rec():
    dbc.connect_db()
    dbc.client[TEST_DB][TEST_COLLECT].insert_one(TEST_INPUT)
    yield
    dbc.client[TEST_DB][TEST_COLLECT].delete_one({"ID": 955})


def test_fetch_all(temp_rec):
    ret = dbc.fetch_all(TEST_COLLECT)
    assert isinstance(ret, list)


def fetch_all_as_dict(temp_rec):
    ret = dbc.fetch_all_as_dict(TEST_COLLECT)
    assert isinstance(ret, dict)


def test_fetch_one(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {"ID": 955})
    assert ret is not None


def test_fetch_one_not_there(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {"ID": 404})
    assert ret is None


def test_fetch_curr_id(temp_rec):
    ret = dbc.fetch_curr_id(TEST_COLLECT)
    assert isinstance(ret, int)


def test_update_one(temp_rec):
    ret = dbc.update_one(TEST_COLLECT, {"ID": 955}, "Funds", 100)
    assert ret is not None
