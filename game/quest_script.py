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
    # challenge_ids = get_challenges()
    quest_dict = {
            "ID": id,
            "Name": quest_name,
            "ChallengeIDs": [0, 1, 2, 3, 4],
            "ChallengeLevel": 0,
            "Cost": 0,
            "Resell": 0,
            "Purchase": True
        }
    return quest_dict   # just for linter rn
    # add quest to db


def get_quest_name() -> str:
    q_names = []
    data_folder = Path("game/resources/quest_name_rsc.txt")
    with open(data_folder, "r") as txtfile:
        for line in txtfile:
            q_names.append(line)
    # print(q_names)
    return q_names[RandomRange(0, len(q_names))]


def get_challenges() -> list:
    ids = []
    data_folder = Path("game/resources/challenge_rsc.csv")
    with open(data_folder, "r") as csvfile:
        challenges = csv.DictReader(csvfile)
        for x in range(5):
            ids.append(random.choice(list(challenges))[0])
    return challenges[RandomRange(0, len(challenges))]


def get_challenge_id(id) -> list:
    pass


def start_quest(id, party_id):
    quest = quest_db.get_quest_details(id)
    event_list = []
    reward = 0
    for ch_id in quest["ChallengeIDs"]:
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
    if curr_quest["Purchase"]:
        return False, "Quest already purchased"
    elif curr_guild["Funds"] < curr_quest["Cost"]:
        return False, "Not enough funds"
    curr_guild["Funds"] -= curr_quest["Cost"]
    curr_quest["Purchase"] = True
    return True, "Quest purchased"


def sell_quest(id, guild_id):
    curr_quest = quest_db.get_quest_details(id)
    curr_guild = guild_db.get_guild_details(guild_id)
    if not curr_quest["Purchase"]:
        return False, "Quest hasn't been bought yet"
    curr_guild["Funds"] += (curr_quest["Cost"] // 2)
    curr_quest["Purchase"] = False
    return True, "Quest sold"
