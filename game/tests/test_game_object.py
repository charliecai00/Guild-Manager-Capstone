import pytest
import game_object as game_object
from game.object_classes.map import Map

def test_create_guild(self):
    #object = game_object.Game()
    self.assertIsInstance(str(self.test_game.Create_Guild()), str)

def test_get_heros(self):
    #object = game_object.Game()
    self.assertIsInstance(self.test_game.Get_Heros(), list)

def test_find_hero(self):
    #object = game_object.Game()
    self.assertEqual(self.test_game.Find_Hero('Nonexistent'), None)

def test_hire_hero(self):
    #object = game_object.Game()
    self.assertEqual(self.test_game.Hire_Hero('Nonexistent'), False)

def test_guild_status(self):
    #object = game_object.Game()
    print(self.test_game.Guild_Status)
    pass
    
def test_get_quest(self):
    #object = game_object.Game()
    print(self.test_game.Get_Quest)
    pass

def test_find_quest(self):
    #object = game_object.Game()
    self.assertEqual(self.test_game.Find_Quest('Nonexistent'), None)

def test_create_map():
    game_map = game_object.Game.Create_Map()
    assert isinstance(game_map, Map)