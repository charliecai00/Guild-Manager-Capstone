# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.game_math.random import RandomRange
from game.game_math.random import RandomNormalClamped
import db.hero as hero_db


def generate_hero(id):
    first_name = get_first_name()
    last_name = get_last_name()
    hero_dict = {
            "ID": id,
            "Name": first_name + " " + last_name,
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

def get_first_name() -> str:
    f_names = []
    with open("game\resources\hero_firstname_rsc.txt", "r") as txtfile:
        for line in txtfile:
            f_names.append(line)
    # print(f_names)
    return f_names[RandomRange(0, len(f_names))]

def get_last_name() -> str:
    l_names = []
    with open("game\resources\hero_firstname_rsc.txt", "r") as txtfile:
        for line in txtfile:
            l_names.append(line)
    # print(l_names)
    return l_names[RandomRange(0, len(l_names))]


def heal_hero(id):
    curr_hero = {}  # hero_db get single
    curr_hero["Health"] = curr_hero["MaxHealth"]
    return True, ""


def test_hero(id, stat):
    curr_hero = {}  # hero_db get single
    roll = RandomRange(0, 99)
    return True, str(roll <= curr_hero["Stats"][stat])
