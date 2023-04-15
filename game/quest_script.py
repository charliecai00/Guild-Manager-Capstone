# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

# import db.quest as db
from pathlib import Path
import db.quest as quest_db
import db.guild as guild_db
import db.hero as hero_db
import game.party_script as ps
from game.game_math.random import RandomRange
from random import sample


def generate_quest():
    quest_name = get_quest_name()
    quest_dict = {
            "ID": quest_db.fetch_curr_id() + 1,
            "Name": quest_name,
            "Challenges": [],
            "ChallengeLevel": 0,
            "Cost": 2,
            "Resell": 0,
            "Purchase": False
        }
    quest_dict["Challenges"] = sample(get_challenges(), RandomRange(2, 5))
    for ch in quest_dict["Challenges"]:
        quest_dict["ChallengeLevel"] += int(ch["Difficulty"])
    quest_dict["Cost"] *= quest_dict["ChallengeLevel"]
    quest_dict["Resell"] = int(quest_dict["Cost"] // 2)
    quest_db.add_quest(quest_dict)


def get_quest_name() -> str:
    q_names = []
    data_folder = Path("game/resources/quest_name_rsc.txt")
    with open(data_folder, "r") as txtfile:
        for line in txtfile:
            q_names.append(line.strip())
    return q_names[RandomRange(0, len(q_names))]


def get_challenges() -> list:
    challenges = []
    data_folder = Path("game/resources/challenge_rsc.csv")
    file_len = 0
    with open(data_folder, "r") as csvfile:
        file_len = len(csvfile.readlines())
    with open(data_folder, "r") as csvfile:
        csvfile.readline()
        for x in range(1, file_len):
            line = csvfile.readline().strip().split(",")
            if len(line) > 0:
                ch_details = {
                        "ID": line[0],
                        "Name": line[1],
                        "TestStat": line[2],
                        "SingleHero": line[3],
                        "SuccessMsg": line[4],
                        "FailureMsg": line[5],
                        "DeathMsg": line[6],
                        "GoldReward": line[7],
                        "ExpReward": line[8],
                        "DmgFail": line[9],
                        "Type": line[10],
                        "Difficulty": line[11]
                    }
                challenges.append(ch_details)
    return challenges


# def get_challenge_id(id) -> list:
#     details = []
#     data_folder = Path("game/resources/challenge_rsc.csv")
#     with open(data_folder, "r") as csvfile:
#         challenge_details = csv.DictReader(csvfile)
#         # bug: challenge_details is a dict, below treats it like a list
#         for x in range(len(challenge_details)):
#             if list(challenge_details)[x] == id:
#                 details.append(list(challenge_details))
#     return details


def start_quest(id, party_id):
    quest = quest_db.get_quest_details(id)
    if quest is None:
        return "Quest not found"
    event_list = []
    reward = 0
    for ch in quest["Challenges"]:
        if (not ps.test_party_alive(party_id)):
            break
        # curr_ch = get_challenge_id(ch_id)
        if (ch["SingleHero"] == "True"):
            result = ps.test_party_single(party_id, ch["TestStat"])
            curr_hero = hero_db.get_hero_details(result[2])
            if (result[0]):
                # success
                event_list.append(
                    ch["SuccessMsg"].replace("[Hero]", curr_hero["Name"]))
                hero_db.update_hero(
                    curr_hero["ID"],
                    "Exp",
                    curr_hero["Exp"] + int(ch["ExpReward"]))
                reward += int(ch["GoldReward"])
            else:
                # failure
                event_list.append(
                    ch["FailureMsg"].replace("[Hero]", curr_hero["Name"]))
                hero_db.update_hero(
                    curr_hero["ID"],
                    "Health",
                    curr_hero["Health"] - int(ch["DmgFail"]))
                # check for death
                if (curr_hero["Health"] - int(ch["DmgFail"]) <= 0):
                    event_list.append(
                        ch["DeathMsg"].replace("[Hero]", curr_hero["Name"]))
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
    curr_guild["QuestIDs"].append(id)
    curr_quest["Purchase"] = True
    guild_db.update_guild(guild_id, "Funds", curr_guild["Funds"])
    guild_db.update_guild(guild_id, "QuestIDs", curr_guild["QuestIDs"])
    quest_db.update_quest(id, "Purchase", curr_quest["Purchase"])
    return True, "Quest purchased"


def sell_quest(id, guild_id):
    curr_quest = quest_db.get_quest_details(id)
    curr_guild = guild_db.get_guild_details(guild_id)
    if not curr_quest["Purchase"]:
        return False, "Quest hasn't been bought yet"
    curr_guild["Funds"] += (curr_quest["Cost"] // 2)
    curr_guild["PartyIDs"].remove(id)
    curr_quest["Purchase"] = False
    guild_db.update_guild(guild_id, "Funds", curr_guild["Funds"])
    guild_db.update_guild(guild_id, "PartyIDs", curr_guild["PartyIDs"])
    quest_db.update_quest(id, "Purchase", curr_quest["Purchase"])
    return True, "Quest sold"
