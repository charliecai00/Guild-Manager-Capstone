# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.guild as guild_db
# import db.hero as hero_db
# import db.quest as quest_db


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
    guild_db.add_guild(guild_dict)


def hire_guild_hero(id, hero_id):
    curr_guild = {} # guild_db get single guild
    curr_hero = {}  # hero_db get single hero
    if curr_hero["Cost"] <= curr_guild["Funds"] and not curr_hero["Hired?"]:
        curr_guild["Funds"] -= curr_hero["Cost"]
        curr_guild["HeroIDs"].append(hero_id)
        curr_hero["Hired?"] = True
        # guild_db update guild
        # hero_db update hero
        return True, ""
    elif curr_hero["Hired?"]:
        return False, "Hero already hired"
    elif curr_hero["Cost"] > curr_guild["Funds"]:
        return False, "Guild does not have enough funds"


def fire_guild_hero(id, hero_id):
    curr_guild = {} # guild_db get single guild
    if hero_id in curr_guild["HeroIDs"]:
        curr_hero = {}  # hero_db get single hero
        curr_hero["Hired?"] = False
        curr_guild["HeroIDs"].pop(hero_id)
        # guild_db update guild
        # hero_db update hero
        return True, ""
    else:
        return False, "Hero not in guild"


def add_guild_party(id, party_id):
    curr_guild = {} # guild_db get single guild
    if not party_id in curr_guild["PartyIDs"]:
        curr_guild["PartyIDs"].append(party_id)
        return True, ""
    else:
        return False, "Party already in guild"


def remove_guild_party(id, party_id):
    curr_guild = {} # guild_db get single guild
    if party_id in curr_guild["PartyIDs"]:
        curr_guild["PartyIDs"].pop(party_id)
        return True, ""
    else:
        return False, "Party already in guild"


def buy_guild_quest(id, quest_id):
    curr_guild = {} # guild_db get single guild
    curr_quest = {} # quest_db get single quest
    if curr_quest["Cost"] <= curr_guild["Funds"] and not quest_id in curr_guild["QuestIDs"]:
        curr_guild["Funds"] -= curr_quest["Cost"]
        curr_guild["QuestIDs"].append(quest_id)
        # guild_db update guild
        # quest_db update hero
        return True, ""
    elif curr_quest["Cost"] > curr_guild["Funds"]:
        return False, "Guild does not have enough funds"
    else:
        return False, "Guild already has quest"


def sell_guild_quest(id, quest_id):
    curr_guild = {} # guild_db get single guild
    if quest_id in curr_guild["QuestIDs"]:
        curr_quest = {} # quest_db get single quest
        curr_guild["Funds"] += curr_quest["Resell"]
        curr_guild["QuestIDs"].pop(quest_id)
        # guild_db update guild
        # quest_db update hero
        return True, ""
    else:
        return False, "Quest not owned by guild"
