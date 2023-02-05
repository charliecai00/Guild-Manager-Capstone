# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from random import randrange
from game.object_classes.character import Character
from game.game_math.random import RandomNormalClamped
import game.object_classes.static_consts as sc
import db.hero


class Hero(Character):
    def __init__(self, new_id, type=None) -> None:
        Character.__init__(self)
        self.id = new_id
        self.type = type
        # which party and guild the hero belongs
        self.party_id = None
        self.guild = None
        self.stats = {
            "STR": RandomNormalClamped(20, 10, 5, 95),
            "CON": RandomNormalClamped(20, 10, 5, 95),
            "DEX": RandomNormalClamped(20, 10, 5, 95),
            "WIS": RandomNormalClamped(20, 10, 5, 95),
            "INT": RandomNormalClamped(20, 10, 5, 95),
            "CHA": RandomNormalClamped(20, 10, 5, 95),
        }
        self.items = []
        self.name = str(sc.HERO_ID)
        sc.HERO_ID += 1
        self.health = 2
        self.alive = True
        self.cost = 5
        db.hero.add_hero(self.name, {
            "id": self.id,
            "stats": self.stats,
            "items": self.items,
            "name": self.name,
            "HERO_ID": self.id,
            "health": self.health,
            "alive": self.alive,
            "cost": self.cost
        })

    def __str__(self) -> str:
        s = "Name: {}, Health: {}, Stats: {}, Items: {}, Cost: {}\n".format(
            self.name,
            self.health,
            self.stats,
            self.items,
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
