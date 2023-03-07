# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.game_math.random import RandomRange
from game.game_math.random import RandomNormalClamped
import db.hero as hero_db
import db.guild as guild_db


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
    hero_db.add_hero(hero_dict)


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


def heal_hero(id, guild_id):
    curr_hero = hero_db.get_hero_details(id)
    curr_guild = guild_db.get_guild_details(guild_id)
    if curr_hero["Health"] == curr_hero["MaxHealth"]:
        return False, "Hero already healthy"
    elif curr_hero["Cost"] > curr_guild["Funds"]:
        return False, "Guild does not have enough funds to heal"
    return True, "Hero has been healed"


# possible redundancy with party_script
def update_hero_party(id, party_id):
    curr_hero = hero_db.get_hero_details(id)
    if curr_hero["InParty?"] == True:
        return False, "Hero already in another party"
    elif curr_hero["PartyID"] == party_id:
        return False, "Hero already in this party"
    curr_hero["PartyID"] = party_id
    curr_hero["InParty?"] = True
    return True, "Hero has been added to party"


def heal_hero(id):
    curr_hero = hero_db.get_hero_details(id)
    curr_hero["Health"] = curr_hero["MaxHealth"]
    return True, "Hero has been healed"


def test_hero(id, stat):
    curr_hero = hero_db.get_hero_details(id)
    roll = RandomRange(0, 99)
    return True, str(roll <= curr_hero["Stats"][stat])
