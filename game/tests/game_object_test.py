import unittest
import game_object

class Test(unittest.TestCase):
    def test_create_guild(self):
        object = game_object.Game()
        self.assertIsInstance(str(object.Create_Guild()), str)

    def test_get_heros(self):
        object = game_object.Game()
        self.assertIsInstance(object.Get_Heros(), list)

    def test_find_hero(self):
        object = game_object.Game()
        self.assertEqual(object.Find_Hero('Nonexistent'), None)

    def test_hire_hero(self):
        object = game_object.Game()
        # self.assertEqual(object.Hire_Hero('Nonexistent'), None)

    def test_guild_status(self):
        pass

    def test_add_party(self):
        pass
    
    def test_get_quest(self):
        pass

    def test_find_quest(self):
        pass

if __name__ == '__main__':
    unittest.main()