# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.party as db
# import db.party as party_db


def generate_party(name="TestName"):
    party_dict = {
            "ID": 0,
            "Name": name,
            "HeroIDs": []
        }
    db.add_party(party_dict)

# possible redundancy with hero_script
def add_party_hero(id, hero_id):
    curr_party = {} # db get single party
    curr_hero = {} # db get single hero
    if curr_hero["InParty?"]:
        return False, "Hero is already in another party"
    elif curr_hero["PartyID"] == curr_party["ID"]:
        return False, "Hero is already in this party"
    curr_party["HeroIDs"].append(hero_id)
    return True, "Hero added to party"

# possible redundancy with hero_script
def remove_party_hero(id, hero_id):
    pass


def test_party_single(id, stat):
    pass


def test_party_team(id, stat):
    pass


def disband_party(id):
    pass
