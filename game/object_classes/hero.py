
from random import Random
from object_classes.character import Character
from game_math.random import RandomNormalClamped


class Hero(Character):
    def __init__(self) -> None:
        Character.__init__(self)
        self.stats = {
                "STR": RandomNormalClamped(20, 10, 5, 95),
                "CON": RandomNormalClamped(20, 10, 5, 95),
                "DEX": RandomNormalClamped(20, 10, 5, 95),
                "WIS": RandomNormalClamped(20, 10, 5, 95),
                "INT": RandomNormalClamped(20, 10, 5, 95),
                "CHA": RandomNormalClamped(20, 10, 5, 95),
            }
        self.items = []
        self.name = "A new hero"
        self.health = 2
        self.alive = True
        self.cost = 5

    def __str__(self) -> str:
        s = "Name: {}, Health: {}, Stats: {}, Items: {}, Cost: {}\n".format(
            self.name,
            self.health,
            self.stats,
            self.items,
            self.cost
        )
        return s

    def __repr__(self) -> str:
        return str(self)

    def Test_Skill(self, skill):
        roll = Random.randrange(0, 99)
        return roll <= self.stats[skill]

    def Take_Damage(self, dmg):
        self.health -= dmg
