# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import unittest
import game.game_object as game_object
from game.object_classes.map import Map

class Test(unittest.TestCase):
    def setUp(self):
        self.test_game = game_object.Game()
    
    def tearDown(self):
        self.test_game = None

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
    
    def test_create_map(self):
        #object = game_object.Game()
        self.assertIsInstance(self.test_game.Create_Map(), Map)

if __name__ == '__main__':
    unittest.main()