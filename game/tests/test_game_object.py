# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import game_object as go
from game.object_classes.map import Map


@pytest.fixture(scope='class', autouse=True)
def temp_game_object():
    test_game = go.Game()
    yield test_game
    test_game = None


def test_create_guild(temp_game_object):
    assert isinstance(str(temp_game_object.Create_Guild()), str)


def test_get_heros(temp_game_object):
    assert isinstance(temp_game_object.full_hero_dic, dict)


def test_find_hero(temp_game_object):
    assert temp_game_object.Find_Hero('Nonexistent') is None


def test_hire_hero(temp_game_object):
    assert temp_game_object.Hire_Hero('Nonexistent') is False


def test_guild_status(temp_game_object):
    print(temp_game_object.Guild_Status)
    pass
    

def test_get_quest(temp_game_object):
    print(temp_game_object.Get_Quest)
    pass


def test_find_quest(temp_game_object):
    assert temp_game_object.Find_Quest('Nonexistent') is None


def test_create_map(temp_game_object):
    game_map = go.Game.Create_Map()
    assert isinstance(game_map, Map)

# def test_get_map(temp_game_object):
#     assert temp_game_object.Get_Location('0') is str
