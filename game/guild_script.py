# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.guild as guild_db
import db.hero as hero_db
import db.quest as quest_db
import game.party_script as ps


def generate_guild(name="TestGuild"):
    guild_dict = {
                "ID": guild_db.fetch_curr_id() + 1,
                "Name": name,
                "HeroIDs": [],
                "PartyIDs": [],
                "QuestIDs": [],
                "Funds": 50,
                "QuestsCompleted": 0
            }
    guild_db.add_guild(guild_dict)


def hire_guild_hero(id, hero_id):
    curr_guild = guild_db.get_guild_details(id)
    curr_hero = hero_db.get_hero_details(hero_id)
    print("curr_guild = {}, curr_hero = {}".format(curr_guild, curr_hero))
    if curr_guild is None:
        return False, "Guild does not exist"
    elif curr_hero is None:
        return False, "Hero does not exist"
    elif curr_hero["Hired?"]:
        return False, "Hero already hired"
    elif curr_hero["Cost"] > curr_guild["Funds"]:
        return False, "Guild does not have enough funds"
    else:
        curr_guild["Funds"] -= curr_hero["Cost"]
        curr_guild["HeroIDs"].append(hero_id)
        curr_hero["Hired?"] = True
        # guild_db update guild
        guild_db.update_guild(id, "Funds", curr_guild["Funds"])
        guild_db.update_guild(id, "HeroIDs", curr_guild["HeroIDs"])
        # hero_db update hero
        hero_db.update_hero(hero_id, "Hired?", curr_hero["Hired?"])
        return True, ""


def fire_guild_hero(id, hero_id):
    curr_guild = guild_db.get_guild_details(id)
    curr_hero = hero_db.get_hero_details(hero_id)
    if hero_id in curr_guild["HeroIDs"]:
        curr_hero = hero_db.get_hero_details(hero_id)
        curr_hero["Hired?"] = False
        curr_guild["HeroIDs"].remove(hero_id)
        if curr_hero["InParty?"]:
            flag, msg = ps.remove_party_hero(curr_hero["PartyID"], hero_id)
            if not flag:
                return flag, msg
        # guild_db update guild
        guild_db.update_guild(id, "Funds", curr_guild["Funds"])
        guild_db.update_guild(id, "HeroIDs", curr_guild["HeroIDs"])
        # hero_db update hero
        hero_db.update_hero(hero_id, "Hired?", curr_hero["Hired?"])
        return True, ""
    else:
        return False, "Hero not in guild"


def add_guild_party(id, party_id):
    curr_guild = guild_db.get_guild_details(id)
    if party_id not in curr_guild["PartyIDs"]:
        curr_guild["PartyIDs"].append(party_id)
        guild_db.update_guild(id, "PartyIDs", curr_guild["PartyIDs"])
        return True, ""
    else:
        return False, "Party already in guild"


def remove_guild_party(id, party_id):
    curr_guild = guild_db.get_guild_details(id)
    if party_id in curr_guild["PartyIDs"]:
        ret = ps.disband_party(party_id)
        if ret[0] is False:
            return False, ret[1]
        curr_guild["PartyIDs"].remove(party_id)
        guild_db.update_guild(id, "PartyIDs", curr_guild["PartyIDs"])
        return True, ""
    else:
        return False, "Party not in guild"


def buy_guild_quest(id, quest_id):
    curr_guild = guild_db.get_guild_details(id)
    curr_quest = quest_db.get_quest_details(quest_id)
    if curr_quest["Cost"] <= curr_guild["Funds"]:
        if quest_id not in curr_guild["QuestIDs"]:
            curr_guild["Funds"] -= curr_quest["Cost"]
            curr_guild["QuestIDs"].append(quest_id)
            # guild_db update guild
            guild_db.update_guild(id, "Funds", curr_guild["Funds"])
            guild_db.update_guild(id, "QuestIDs", curr_guild["QuestIDs"])
            # quest_db update quest
            quest_db.update_quest(quest_id, "Purchase", True)
            return True, ""
    elif curr_quest["Cost"] > curr_guild["Funds"]:
        return False, "Guild does not have enough funds"
    else:
        return False, "Guild already has quest"


def sell_guild_quest(id, quest_id):
    curr_guild = guild_db.get_guild_details(id)
    if quest_id in curr_guild["QuestIDs"]:
        curr_quest = quest_db.get_quest_details(quest_id)
        curr_guild["Funds"] += curr_quest["Resell"]
        curr_guild["QuestIDs"].pop(quest_id)
        # guild_db update guild
        guild_db.update_guild(id, "Funds", curr_guild["Funds"])
        guild_db.update_guild(id, "QuestIDs", curr_guild["QuestIDs"])
        # quest_db update quest
        quest_db.update_quest(quest_id, "Purchase", False)
        return True, ""
    else:
        return False, "Quest not owned by guild"
