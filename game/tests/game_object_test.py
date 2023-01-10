# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import unittest
import game.game_object as game_object
# from game.object_classes.map import Map
from game.object_classes.hero import Hero


class Test(unittest.TestCase):
    def setUp(self):
        self.test_game = game_object.Game()
    
    def tearDown(self):
        self.test_game = None
        
    def addHeroes(self, num=10):
        last_hero_id = self.test_game.Add_Heros(num, "mage")
        return last_hero_id

    def test_AddHeroes(self):
        last_hero_id = self.addHeroes()
        print("last hero id is ", last_hero_id)
        self.assertIsInstance(self.test_game.full_hero_dic[last_hero_id - 1], Hero)

    def hireHeroes(self, id=0):
        is_hired = self.test_game.Hire_Hero(id)
        return is_hired

    def test_HireHeroes(self):
        self.addHeroes()
        is_hired = self.hireHeroes(0)
        self.assertEqual(is_hired, True)
        self.assertEqual(self.test_game.full_hero_dic[0], "hiredByGuild")

    def test_HireHeroes_fail(self):
        self.addHeroes()
        self.hireHeroes(0)
        hero_already_hired_by_guild = self.hireHeroes(0)
        hero_not_in_game = self.hireHeroes(10)
        self.assertEqual(hero_already_hired_by_guild, False)
        self.assertEqual(hero_not_in_game, False)

    def test_AddPartyWithHeros(self):
        self.addHeroes()
        self.hireHeroes(0)
        self.hireHeroes(1)
        res = self.test_game.Add_Party_With_Heros([0, 1], "test_party")
        self.assertEqual(res, True)

    def test_AddPartyWithHeros_fail(self):
        self.addHeroes()
        self.hireHeroes(0)
        self.hireHeroes(1)
        hero_not_hired_by_guild = self.test_game.Add_Party_With_Heros([0, 2], "test_party")
        self.assertEqual(hero_not_hired_by_guild, False)

    def test_FireHero(self):
        self.addHeroes()
        self.hireHeroes(0)
        fired = self.test_game.Fire_Hero(0)
        self.assertEqual(fired, True)

    def test_FireHeroes_fail(self):
        self.addHeroes()
        self.hireHeroes(0)
        fired = self.test_game.Fire_Hero(1)
        self.assertEqual(fired, False)

    def test_DisbandParty(self):
        self.addHeroes()
        self.hireHeroes(0)
        self.test_game.Add_Party_With_Heros([0])
        res = self.test_game.Disband_Party(0)
        self.assertEqual(res, True)

    def test_DisbandParty_fail(self):
        self.addHeroes()
        self.hireHeroes(0)
        self.test_game.Add_Party_With_Heros([0])
        res = self.test_game.Disband_Party(1)
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()
