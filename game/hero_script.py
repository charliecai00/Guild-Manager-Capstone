# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.game_math.random import RandomNormalClamped
import db.hero as db
# import db.guild as guild_db
# import db.party as party_db


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


def heal_hero(id):
    curr_hero = {} # db get single hero
    curr_guild = {} # guild_db get single guild
    if curr_hero["Health"] == curr_hero["MaxHealth"]:
        return False, "Hero already healthy"
    elif curr_hero["Cost"] > curr_guild["Funds"]:
        return False, "Guild does not have enough funds to heal" 
    return True, "Hero has been healed"


def update_hero_party(id, party_id):
    curr_hero = {} # db get single hero
    curr_party = ()
    if curr_hero["InParty?"] == True:
        return False, "Hero already in another party"
    elif curr_hero["PartyID"] == party_id:
        return False, "Hero already in this party"
    return True, "Hero has been added to party"


def remove_hero_party(id):
    pass


def test_hero(id, stat):
    pass
