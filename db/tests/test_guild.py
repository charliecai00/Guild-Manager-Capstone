# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import db.guild as gu


TEST_DEL_NAME = 'guild to be deleted'


def create_guild_details():
    details = {}
    for field in gu.REQUIRED_FLDS:
        details[field] = "dummy_data"
    return details


@pytest.fixture(scope='function')
def temp_guild():
    gu.add_guild(gu.TEST_GUILD, create_guild_details())
    yield
    gu.del_guild(gu.TEST_GUILD)


@pytest.fixture(scope='function')
def new_guild():
    return gu.add_guild(TEST_DEL_NAME, create_guild_details())


def test_del_guild(new_guild):
    gu.del_guild(TEST_DEL_NAME)
    assert not gu.guild_exists(TEST_DEL_NAME)


def test_get_guilds(temp_guild):
    chs = gu.get_guilds()
    assert isinstance(chs, list)
    assert len(chs) > 0  # or 1


def test_get_guilds_dict(temp_guild):
    chs = gu.get_guilds_dict()
    assert isinstance(chs, dict)
    assert len(chs) > 0  # or 1


def test_get_guild_details(temp_guild):
    ch_dets = gu.get_guild_details(gu.TEST_GUILD)
    assert isinstance(ch_dets, dict)


def TEST_GUILD_exists(temp_guild):
    assert gu.guild_exists(gu.TEST_GUILD)


def TEST_GUILD_not_exists(temp_guild):
    assert not gu.guild_exists('Surely this is not a guild name!')


def test_add_guild():
    gu.add_guild(gu.TEST_GUILD, create_guild_details())
    assert gu.guild_exists(gu.TEST_GUILD)
    gu.del_guild(gu.TEST_GUILD)
