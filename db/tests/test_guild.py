# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import db.guild as db_guild

TEST_COLLECT = 'TESTING'
TEST_INPUT = {"ID": 965,
              "Name": "TESTING",
              "HeroIDs": [],
              "PartyIDs": [],
              "QuestIDs": [],
              "Funds": 50,
              "QuestsCompleted": 0}


@pytest.fixture(scope='function')
def temp_rec():
    db_guild.add_guild(TEST_INPUT)
    yield
    db_guild.del_guild(965)


def test_get_guilds(temp_rec):
    ret = db_guild.get_guilds()
    assert isinstance(ret, list)


def test_fetch_curr_id(temp_rec):
    ret = db_guild.fetch_curr_id()
    assert isinstance(ret, int)


def test_get_guild_details(temp_rec):
    ret = db_guild.get_guild_details(965)
    assert ret is not None


def test_get_guild_details_not_there(temp_rec):
    ret = db_guild.get_guild_details(404)
    assert ret is None


def test_update_guild(temp_rec):
    ret = db_guild.update_guild(965, "Name", "TESTING_UPDATE")
    assert ret is not None
