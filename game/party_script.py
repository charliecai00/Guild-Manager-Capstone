# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

from game.game_math.random import RandomRange
import db.party as party_db
import db.hero as hero_db


def generate_party(name="TestName"):
    party_dict = {
            "ID": party_db.fetch_curr_id() + 1,
            "Name": name,
            "HeroIDs": []
        }
    party_db.add_party(party_dict)


def add_party_hero(id, hero_id):
    curr_party = party_db.get_party_details(id)
    curr_hero = hero_db.get_hero_details(hero_id)
    if curr_hero is None:
        return False, "Hero does not exist"
    elif curr_party is None:
        return False, "Party does not exist"
    elif curr_hero["InParty?"]:
        return False, "Hero already in a party"
    curr_party["HeroIDs"].append(hero_id)
    curr_hero["InParty?"] = True
    curr_hero["PartyID"] = id
    # party_db update party
    party_db.update_party(id, "HeroIDs", curr_party["HeroIDs"])
    # hero_db update hero
    hero_db.update_hero(hero_id, "InParty?", curr_hero["InParty?"])
    hero_db.update_hero(hero_id, "PartyID", curr_hero["PartyID"])
    return True, ""


def remove_party_hero(id, hero_id):
    curr_party = party_db.get_party_details(id)
    curr_hero = hero_db.get_hero_details(hero_id)
    if curr_hero is None:
        return False, "Hero does not exist"
    elif curr_party is None:
        return False, "Party does not exist"
    curr_party["HeroIDs"].remove(hero_id)
    curr_hero["InParty?"] = False
    curr_hero["PartyID"] = 0
    # party_db update party
    party_db.update_party(id, "HeroIDs", curr_party["HeroIDs"])
    # hero_db update hero
    hero_db.update_hero(hero_id, "InParty?", curr_hero["InParty?"])
    hero_db.update_hero(hero_id, "PartyID", curr_hero["PartyID"])
    return True, ""


def test_party_single(id, stat):
    curr_party = party_db.get_party_details(id)
    if curr_party is None:
        return False, "Party does not exist"
    max_stat = 0
    ret_hero_id = ""
    for hero_id in curr_party["HeroIDs"]:
        curr_hero = hero_db.get_hero_details(hero_id)
        if curr_hero is None:
            return False, "Hero does not exist"
        if curr_hero["Health"] > 0 and curr_hero["Stats"][stat] > max_stat:
            ret_hero_id = curr_hero["ID"]
            max_stat = curr_hero["Stats"][stat]
    roll = RandomRange(0, 99)
    return True, roll <= max_stat, int(ret_hero_id)


def test_party_team(id, stat):
    curr_party = party_db.get_party_details(id)
    if curr_party is None:
        return False, "Party does not exist"
    avg_stat = 0
    party_alive_c = 0
    for hero_id in curr_party["HeroIDs"]:
        curr_hero = hero_db.get_hero_details(hero_id)
        if curr_hero is None:
            return False, "Hero does not exist"
        if curr_hero["Health"] > 0:
            avg_stat += curr_hero["Stats"][stat]
            party_alive_c += 1
    avg_stat /= party_alive_c
    roll = RandomRange(0, 99)
    return True, str(roll <= avg_stat)


def test_party_alive(id):
    curr_party = party_db.get_party_details(id)
    if curr_party is None:
        return False, "Party does not exist"
    for hero_id in curr_party["HeroIDs"]:
        curr_hero = hero_db.get_hero_details(hero_id)
        if curr_hero is None:
            return False, "Hero does not exist"
        if curr_hero["Health"] > 0:
            return True
    return False


def get_party_status(id):
    curr_party = party_db.get_party_details(id)
    if curr_party is None:
        return False, "Party does not exist"
    ret_lst = []
    for hero_id in curr_party["HeroIDs"]:
        curr_hero = hero_db.get_hero_details(hero_id)
        if curr_hero is None:
            return False, "Hero does not exist"
        hero_data = {
            "HeroName": curr_hero["Name"],
            "Health": curr_hero["Health"],
            "Exp": curr_hero["Exp"]
        }
        ret_lst.append(hero_data)
    return ret_lst


def disband_party(id):
    curr_party = party_db.get_party_details(id)
    try:
        for hero_id in curr_party["HeroIDs"]:
            remove_party_hero(id, hero_id)
    except TypeError:
        pass
    party_db.del_party(id)
    return True, ""
