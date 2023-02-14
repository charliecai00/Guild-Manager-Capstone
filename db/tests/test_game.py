# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

# import os
import pytest
import db.game as gm


TEST_DEL_NAME = 'game to be deleted'


def create_game_details():
    details = {}
    for field in gm.REQUIRED_FLDS:
        details[field] = "dummy_data"
    return details


@pytest.fixture(scope='function')
def temp_game():
    gm.add_game(gm.TEST_GAME_NAME1, create_game_details())
    yield
    gm.del_game(gm.TEST_GAME_NAME1)


@pytest.fixture(scope='function')
def new_game():
    return gm.add_game(TEST_DEL_NAME, create_game_details())


def test_del_game(new_game):
    gm.del_game(TEST_DEL_NAME)
    assert not gm.game_exists(TEST_DEL_NAME)


def test_get_games(temp_game):
    gms = gm.get_games()
    assert isinstance(gms, list)
    assert len(gms) > 0  # or 1


def test_get_games_dict(temp_game):
    gms = gm.get_games_dict()
    assert isinstance(gms, dict)
    assert len(gms) > 0  # or 1


def test_get_game_details(temp_game):
    gm_dets = gm.get_game_details(gm.TEST_GAME_NAME1)
    assert isinstance(gm_dets, dict)


def test_game_exists(temp_game):
    assert gm.game_exists(gm.TEST_GAME_NAME1)


def test_game_not_exists(temp_game):
    assert not gm.game_exists('Surely this is not a game name!')


def test_add_game():
    gm.add_game(gm.TEST_GAME_NAME1, create_game_details())
    assert gm.game_exists(gm.TEST_GAME_NAME1)
    gm.del_game(gm.TEST_GAME_NAME1)
