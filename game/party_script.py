# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from random import randrange
import db.party as party_db
# import db.hero as hero_db


def generate_party(id, name="TestName"):
    party_dict = {
            "ID": 0,
            "Name": name,
            "HeroIDs": []
        }
    party_db.add_party(party_dict)


def add_party_hero(id, hero_id):
    curr_party = {}     # party_db get single party
    curr_hero = {}      # hero_db get single hero
    if not curr_hero["InParty?"] and hero_id not in curr_party["HeroIDs"]:
        curr_party["HeroIDs"].append(hero_id)
        curr_hero["InParty?"] = True
        curr_hero["PartyID"] = id
        # party_db update party
        # hero_db update hero
        return True, ""
    elif curr_hero["InParty?"]:
        return False, "Hero already in another party"
    else:
        return False, "Hero already in the party"


def remove_party_hero(id, hero_id):
    curr_party = {}     # party_db get single party
    if hero_id in curr_party["HeroIDs"]:
        curr_hero = {}  # hero_db get single hero
        curr_party["HeroIDs"].pop(hero_id)
        curr_hero["InParty?"] = False
        curr_hero["PartyID"] = 0
        # party_db update party
        # hero_db update hero
        return True, ""
    else:
        return False, "Hero not in party"


def test_party_single(id, stat):
    curr_party = {}     # party_db get single party
    max_stat = 0
    for id in curr_party["HeroIDs"]:
        curr_hero = {}  # hero_db get single hero
        max_stat = max(max_stat, curr_hero["Stats"][stat])
    roll = randrange(99)
    return True, str(roll <= max_stat)


def test_party_team(id, stat):
    curr_party = {}     # party_db get single party
    avg_stat = 0
    for id in curr_party["HeroIDs"]:
        curr_hero = {}  # hero_db get single hero
        avg_stat += curr_hero["Stats"][stat]
    avg_stat /= len(curr_party["HeroIDs"])
    roll = randrange(99)
    return True, str(roll <= avg_stat)


def disband_party(id):
    curr_party = {}     # party_db get single party
    for id in curr_party["HeroIDs"]:
        curr_hero = {}  # hero_db get single hero
        curr_hero["InParty?"] = False
        curr_hero["PartyID"] = 0
        # hero_db update hero
    curr_party["HeroIDs"].clear()
    # party_db update party
    return True, ""
