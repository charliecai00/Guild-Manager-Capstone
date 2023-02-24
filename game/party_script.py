# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.party as db


def generate_party(name="TestName"):
    party_dict = {
            "ID": 0,
            "Name": name,
            "HeroIDs": []
        }
    db.add_party(party_dict)


def add_party_hero(id, hero_id):
    pass


def remove_party_hero(id, hero_id):
    pass


def test_party_single(id, stat):
    pass


def test_party_team(id, stat):
    pass


def disband_party(id):
    pass
