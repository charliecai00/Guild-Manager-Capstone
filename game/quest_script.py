# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

# import db.quest as db
from game.game_math.random import RandomRange

def generate_quest(id):
    quest_name = get_quest_name()
    quest_dict = {
            "ID": id,
            "Name": quest_name,
            "ChallengeIDs": [0, 1, 2, 3, 4],
            "ChallengeLevel": 0,
            "Cost": 0,
            "Resell": 0
        }
    return quest_dict   # just for linter rn
    # add quest to db

def get_quest_name() -> str:
    q_names = []
    with open("game\resources\quest_name_rsc.txt", "r") as file:
        for line in file:
            q_names.append(line)
    # print(q_names)
    return q_names[RandomRange(0, len(q_names))]

def start_quest(id, party_id):
    pass
