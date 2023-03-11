# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.game_math.random import RandomRange
import db.party as party_db
import db.hero as hero_db


def generate_party(name="TestName"):
    party_dict = {
            "ID": 0,
            "Name": name,
            "HeroIDs": []
        }
    party_db.add_party(party_dict)


def add_party_hero(id, hero_id):
    curr_party = party_db.get_party_details(id)
    curr_hero = hero_db.get_hero_details(id)
    if not curr_hero["InParty?"] and hero_id not in curr_party["HeroIDs"]:
        curr_party["HeroIDs"].append(hero_id)
        curr_hero["InParty?"] = True
        curr_hero["PartyID"] = id
        # party_db update party
        party_db.update_party(id, "HeroIDs", curr_party["HeroIDs"])
        # hero_db update hero
        hero_db.update_hero(hero_id, "InParty?", curr_hero["InParty?"])
        hero_db.update_hero(hero_id, "PartyID", curr_hero["PartyID"])
        return True, ""
    elif curr_hero["InParty?"]:
        return False, "Hero already in another party"
    else:
        return False, "Hero already in the party"


def remove_party_hero(id, hero_id):
    curr_party = party_db.get_party_details(id)
    if hero_id in curr_party["HeroIDs"]:
        curr_hero = hero_db.get_hero_details(hero_id)
        curr_party["HeroIDs"].pop(hero_id)
        curr_hero["InParty?"] = False
        curr_hero["PartyID"] = 0
        # party_db update party
        party_db.update_party(id, "HeroIDs", curr_party["HeroIDs"])
        # hero_db update hero
        hero_db.update_hero(hero_id, "InParty?", curr_hero["InParty?"])
        hero_db.update_hero(hero_id, "PartyID", curr_hero["PartyID"])
        return True, ""
    else:
        return False, "Hero not in party"


def test_party_single(id, stat):
    curr_party = party_db.get_party_details(id)
    max_stat = 0
    for hero_id in curr_party["HeroIDs"]:
        curr_hero = hero_db.get_hero_details(hero_id)
        max_stat = max(max_stat, curr_hero["Stats"][stat])
    roll = RandomRange(0, 99)
    return True, str(roll <= max_stat)


def test_party_team(id, stat):
    curr_party = party_db.get_party_details(id)
    avg_stat = 0
    for hero_id in curr_party["HeroIDs"]:
        curr_hero = hero_db.get_hero_details(hero_id)
        avg_stat += curr_hero["Stats"][stat]
    avg_stat /= len(curr_party["HeroIDs"])
    roll = RandomRange(0, 99)
    return True, str(roll <= avg_stat)


def disband_party(id):
    curr_party = party_db.get_party_details(id)
    for hero_id in curr_party["HeroIDs"]:
        curr_hero = hero_db.get_hero_details(hero_id)
        curr_hero["InParty?"] = False
        curr_hero["PartyID"] = 0
        # hero_db update hero
        hero_db.update_hero(hero_id, "InParty?", curr_hero["InParty?"])
        hero_db.update_hero(hero_id, "PartyID", curr_hero["PartyID"])
    curr_party["HeroIDs"].clear()
    # party_db update party
    party_db.update_party(id, "HeroIDs", curr_party["HeroIDs"])
    return True, ""
