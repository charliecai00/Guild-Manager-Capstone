import pytest
import game_object as game_object
from game.object_classes.map import Map

def test_create_map():
    game_map = game_object.Game.Create_Map()
    assert isinstance(game_map, Map)