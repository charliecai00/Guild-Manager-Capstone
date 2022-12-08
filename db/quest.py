# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

CHALLENGE = 'challenge'
CHECK_STAT = 'check_stat'
CHILDREN = 'children'
TERMINAL = 'terminal'
PARENT = 'parent'
DONE = 'done'
DEPTH = 'depth'

QUEST_KEY = 'name'
QUEST_COLLECT = 'quests'

TEST_QUEST = 'test_quest'
REQUIRED_FLDS = [CHALLENGE, CHILDREN, TERMINAL, PARENT, DONE, DEPTH]
dummy_quest = {TEST_QUEST: {CHALLENGE: "object",
                            CHILDREN: [],
                            TERMINAL: False,
                            PARENT: None,
                            DONE: False,
                            DEPTH: 0
                            }}


def get_quest_details(name):
    dbc.connect_db()
    return dbc.fetch_one(QUEST_COLLECT, {QUEST_KEY: name})


def quest_exists(name):
    return get_quest_details(name) is not None


def get_quests_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(QUEST_KEY, QUEST_COLLECT)


def get_quests():
    dbc.connect_db()
    return dbc.fetch_all(QUEST_COLLECT)


def add_quest(name, details):
    doc = details
    dbc.connect_db()
    doc[QUEST_KEY] = name
    return dbc.insert_one(QUEST_COLLECT, doc)


def del_quest(name):
    return dbc.del_one(QUEST_COLLECT, {QUEST_KEY: name})


# def main():
#     print('Adding a quest')
#     add_quest(TEST_QUEST, dummy_quest[TEST_QUEST])
#     print('Getting quests as a list:')
#     quests = get_quests()
#     print(f'{quests=}')
#     print('Getting quests as a dict:')
#     quests = get_quests_dict()
#     print(f'{quests=}')
#     print(f'{get_quest_details(TEST_QUEST)=}')


# if __name__ == '__main__':
#     main()
