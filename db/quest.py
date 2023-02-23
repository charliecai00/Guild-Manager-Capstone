# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

ID = 'ID'
NAME = 'Name'
CHALLENGE = 'Challenge'
DIFFICULTY = 'Difficulty'
COST = 'Cost'
RESELL = 'Resell'
PURCHASE = 'Purchase'

QUEST_KEY = 'ID'
QUEST_COLLECT = 'Quests'

TEST_QUEST = 'TEST_QUEST'
REQUIRED_FLDS = [ID, NAME, CHALLENGE, DIFFICULTY, COST, RESELL]
dummy_quest = {TEST_QUEST: {ID: 1,
                            NAME: "Temporary Quest",
                            CHALLENGE: [1, 2, 3],
                            DIFFICULTY: 5,
                            COST: 999999,
                            RESELL: 999999,
                            PURCHASE: False}}


def get_unpurchase_quest():
    """
    return: a list of values, [1,2,3]
    """
    dbc.connect_db()
    all_quest = dbc.fetch_all(QUEST_COLLECT)

    unpurchase = []
    for i in all_quest:
        if i[PURCHASE] is False:
            del i['_id']
            unpurchase.append(i)
    return unpurchase


# def get_quest_details(name):
#     dbc.connect_db()
#     return dbc.fetch_one(QUEST_COLLECT, {QUEST_KEY: name})


# def quest_exists(name):
#     return get_quest_details(name) is not None


# def get_quests_dict():
#     dbc.connect_db()
#     return dbc.fetch_all_as_dict(QUEST_KEY, QUEST_COLLECT)


# def get_quests():
#     dbc.connect_db()
#     return dbc.fetch_all(QUEST_COLLECT)


def add_quest(details):
    dbc.connect_db()
    return dbc.insert_one(QUEST_COLLECT, details)


# def del_quest(name):
#     dbc.connect_db()
#     return dbc.del_one(QUEST_COLLECT, {QUEST_KEY: name})


def main():
    print('Adding a quest')
    add_quest(dummy_quest[TEST_QUEST])
#     print('Getting quests as a list:')
#     quests = get_quests()
#     print(f'{quests=}')
#     print('Getting quests as a dict:')
#     quests = get_quests_dict()
#     print(f'{quests=}')
#     print(f'{get_quest_details(TEST_QUEST)=}')


if __name__ == '__main__':
    main()
