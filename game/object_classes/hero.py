# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from random import randrange
from game.object_classes.character import Character
from game.game_math.random import RandomNormalClamped
import db.hero


class Hero(Character):
    def __init__(self, new_id) -> None:
        Character.__init__(self)
        self.id = new_id
        self.is_hired = False
        self.is_in_party = False
        self.party_id = None
        self.stats = {
            "STR": RandomNormalClamped(20, 10, 5, 95),
            "CON": RandomNormalClamped(20, 10, 5, 95),
            "DEX": RandomNormalClamped(20, 10, 5, 95),
            "WIS": RandomNormalClamped(20, 10, 5, 95),
            "INT": RandomNormalClamped(20, 10, 5, 95),
            "CHA": RandomNormalClamped(20, 10, 5, 95),
        }
        self.name = str(new_id)     # TODO: name generation
        self.health = 3
        self.alive = True
        self.cost = 5
        db.hero.add_hero(self.id, self.as_dict())

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "stats": self.stats,
            "health": self.health,
            "alive": self.alive,
            "cost": self.cost,
            "hired": self.is_hired,
            "in_party": self.is_in_party,
            "pary_id": self.party_id
        }

    def __str__(self) -> str:
        s = "Name: {}, Health: {}, Stats: {}, Cost: {}\n".format(
            self.name,
            self.health,
            self.stats,
            self.cost
        )
        return s

    def __repr__(self):
        return str(self)

    def __eq__(self, __o: object) -> bool:
        return __o.id == self.id

    def Test_Skill(self, skill):
        roll = randrange(99)
        return roll <= self.stats[skill]

    def Take_Damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.alive = False
