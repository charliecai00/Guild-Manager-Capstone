# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import copy
import db.guild as db

def generate_guild(id, name="TestGuild"):
    guild_dict = {
                "ID": id,
                "Name": name,
                "HeroIDs": [],
                "PartyIDs": [],
                "QuestIDs": [],
                "Funds": 50,
                "QuestsCompleted": 0
            }
    db.add_guild(guild_dict)


def hire_guild_hero(id, hero_id):
    pass


def add_guild_party(id, party_id):
    pass


def buy_guild_quest(id, quest_id):
    pass


def sell_guild_quest(id, quest_id):
    pass