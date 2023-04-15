# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.game_math.random import RandomRange
from game.game_math.random import RandomNormalClamped
import db.hero as hero_db
import db.guild as guild_db
from pathlib import Path


def generate_hero():
    first_name = get_first_name()
    last_name = get_last_name()
    hero_dict = {
            "ID": hero_db.fetch_curr_id() + 1,
            "Name": first_name + " " + last_name,
            "Health": 5,
            "MaxHealth": RandomNormalClamped(5, 2, 1, 8),
            "Exp": 0,
            "Stats": {
                "STR": RandomNormalClamped(50, 25, 5, 95),
                "CON": RandomNormalClamped(50, 25, 5, 95),
                "DEX": RandomNormalClamped(50, 25, 5, 95),
                "WIS": RandomNormalClamped(50, 25, 5, 95),
                "INT": RandomNormalClamped(50, 25, 5, 95),
                "CHA": RandomNormalClamped(50, 25, 5, 95)
                },
            "Hired?": False,
            "InParty?": False,
            "PartyID": 0,
            "Cost": 5
        }
    # hero cost updating
    for stat in hero_dict["Stats"].values():
        if stat >= 70:
            hero_dict["Cost"] += 1
            if stat >= 80:
                hero_dict["Cost"] += 2
        elif stat <= 30:
            hero_dict["Cost"] -= 1
            if stat <= 20:
                hero_dict["Cost"] -= 2
    hero_dict["Cost"] = max(1, hero_dict["Cost"])
    hero_db.add_hero(hero_dict)


def get_first_name() -> str:
    f_names = []
    data_folder = Path("game/resources/hero_firstname_rsc.txt")
    with open(data_folder, "r") as txtfile:
        for line in txtfile:
            f_names.append(line.strip())
    return f_names[RandomRange(0, len(f_names))]


def get_last_name() -> str:
    l_names = []
    data_folder = Path("game/resources/hero_lastname_rsc.txt")
    with open(data_folder, "r") as txtfile:
        for line in txtfile:
            l_names.append(line.strip())
    return l_names[RandomRange(0, len(l_names))]


def heal_hero(id, guild_id):
    curr_hero = hero_db.get_hero_details(id)
    curr_guild = guild_db.get_guild_details(guild_id)
    if curr_hero["Health"] == curr_hero["MaxHealth"]:
        return False, "Hero already healthy"
    elif curr_hero["Cost"] > curr_guild["Funds"]:
        return False, "Guild does not have enough funds to heal"
    hero_db.update_hero(id, "Health", curr_hero["MaxHealth"])
    return True, "Hero has been healed"


def test_hero(id, stat):
    curr_hero = hero_db.get_hero_details(id)
    roll = RandomRange(0, 99)
    return True, str(roll <= curr_hero["Stats"][stat])
