# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.game_math.random import RandomNormalClamped
import db.hero as db


def generate_hero(id):
    hero_dict = {
            "ID": id,
            "Name": "String",
            "Health": 5,
            "MaxHealth": 5,
            "Exp": 0,
            "Stats": {
                "STR": RandomNormalClamped(20, 10, 5, 95),
                "CON": RandomNormalClamped(20, 10, 5, 95),
                "DEX": RandomNormalClamped(20, 10, 5, 95),
                "WIS": RandomNormalClamped(20, 10, 5, 95),
                "INT": RandomNormalClamped(20, 10, 5, 95),
                "CHA": RandomNormalClamped(20, 10, 5, 95),
            },
            "Hired?": False,
            "InParty?": False,
            "PartyID": 0,
            "Cost": 5
        }
    db.add_hero(hero_dict)


def hire_hero(id, guild_id):
    pass


def fire_hero(id):
    pass


def heal_hero(id):
    pass


def update_hero_party(id, party_id):
    pass


def remove_hero_party(id):
    pass


def test_hero(id, stat):
    pass
