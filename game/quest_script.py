# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

# import db.quest as db
from pathlib import Path
import csv
import random
import db.quest as quest_db
import db.guild as guild_db
import db.hero as hero_db
import game.party_script as ps
from game.game_math.random import RandomRange


def generate_quest(id):
    quest_name = get_quest_name()
    quest_dict = {
            "ID": quest_db.fetch_curr_id() + 1,
            "Name": quest_name,
            "Challenges": [],
            "ChallengeLevel": 0,
            "Cost": 0,
            "Resell": 0,
            "Purchase": False
        }
    for i in range(RandomRange(1, 5)):
        for ch in get_challenges():
            quest_dict["Challenges"].append(ch[0])
    quest_db.add_quest(quest_dict)


def get_quest_name() -> str:
    q_names = []
    data_folder = Path("game/resources/quest_name_rsc.txt")
    with open(data_folder, "r") as txtfile:
        for line in txtfile:
            q_names.append(line.strip())
    return q_names[RandomRange(0, len(q_names))]


def get_challenges() -> list:
    ids = []
    data_folder = Path("game/resources/challenge_rsc.csv")
    with open(data_folder, "r") as csvfile:
        challenges = csv.DictReader(csvfile)
        for x in range(5):
            ids.append(random.choice(list(challenges))[0])
    # return challenges[RandomRange(0, len(challenges))]
    return ids


def get_challenge_id(id) -> list:
    details = []
    data_folder = Path("game/resources/challenge_rsc.csv")
    with open(data_folder, "r") as csvfile:
        challenge_details = csv.DictReader(csvfile)
        for x in range(len(challenge_details)):
            if list(challenge_details)[x] == id:
                details.append(list(challenge_details))
    return details


def start_quest(id, party_id):
    quest = quest_db.get_quest_details(id)
    if quest is None:
        return "Quest not found"
    event_list = []
    reward = 0
    for ch_id in quest["Challenges"]:
        if (not ps.test_party_alive(party_id)):
            break
        curr_ch = get_challenge_id(ch_id)
        if (curr_ch[3] == "True"):
            result = ps.test_party_single(party_id, curr_ch[2])
            curr_hero = hero_db.get_hero_details(result[2])
            if (result[0]):
                # success
                event_list.append(
                    curr_ch[4].replace("[Hero]",
                                       curr_hero["Name"]))
                hero_db.update_hero(
                    curr_hero["ID"],
                    "Exp",
                    curr_hero["Exp"] + int(curr_ch[8]))
                reward += int(curr_ch[7])
            else:
                # failure
                event_list.append(
                    curr_ch[5].replace("[Hero]",
                                       curr_hero["Name"]))
                hero_db.update_hero(
                    curr_hero["ID"],
                    "Health",
                    curr_hero["Health"] - int(curr_ch[9]))
                # check for death
                if (curr_hero["Health"] - int(curr_ch[9]) <= 0):
                    event_list.append(
                        curr_ch[6].replace("[Hero]", curr_hero["Name"]))
    final_report = {
        "EventList": event_list,
        "Reward": reward,
        "PartyStatus": ps.get_party_status(party_id)
    }
    return final_report


def buy_quest(id, guild_id):
    curr_quest = quest_db.get_quest_details(id)
    curr_guild = guild_db.get_guild_details(guild_id)
    if curr_quest is not None or curr_quest is not None:
        if curr_quest["Purchase"]:
            return False, "Quest already purchased"
        elif curr_guild["Funds"] < curr_quest["Cost"]:
            return False, "Not enough funds"
        curr_guild["Funds"] -= curr_quest["Cost"]
        curr_guild["PartyIDs"].append(id)
        curr_quest["Purchase"] = True
        guild_db.update_guild(guild_id, "Funds", curr_guild["Funds"])
        guild_db.update_guild(guild_id, "PartyIDs", curr_guild["PartyIDs"])
        quest_db.update_quest(id, "Purchase", curr_quest["Purchase"])
        return True, "Quest purchased"
    return False, "Quest or guild does not exist"


def sell_quest(id, guild_id):
    curr_quest = quest_db.get_quest_details(id)
    curr_guild = guild_db.get_guild_details(guild_id)
    if curr_quest is not None or curr_guild is not None:
        if not curr_quest["Purchase"]:
            return False, "Quest hasn't been bought yet"
        curr_guild["Funds"] += (curr_quest["Cost"] // 2)
        curr_guild["PartyIDs"].remove(id)
        curr_quest["Purchase"] = False
        guild_db.update_guild(guild_id, "Funds", curr_guild["Funds"])
        guild_db.update_guild(guild_id, "PartyIDs", curr_guild["PartyIDs"])
        quest_db.update_quest(id, "Purchase", curr_quest["Purchase"])
        return True, "Quest sold"
    return False, "Quest or guild does not exist"
