# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

# import db.quest as db
from pathlib import Path
import csv
import random
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


def start_quest(id, party_id):
    pass


def buy_quest(id):
    pass


def sell_quest(id):
    pass
