# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

# import db.quest as db


def generate_quest(id):
    quest_dict = {
            "ID": id,
            "Name": "String",
            "ChallengeIDs": [0, 1, 2, 3, 4],
            "ChallengeLevel": 0,
            "Cost": 0,
            "Resell": 0
        }
    return quest_dict   # just for linter rn
    # add quest to db


def start_quest(id, party_id):
    pass
