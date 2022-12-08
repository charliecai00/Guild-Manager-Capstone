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


def game_exists(name):
    return get_quest_details(name) is not None


def get_games_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(QUEST_KEY, QUEST_COLLECT)


def get_games():
    dbc.connect_db()
    return dbc.fetch_all(QUEST_COLLECT)


def add_game(name, details):
    doc = details
    dbc.connect_db()
    doc[QUEST_KEY] = name
    return dbc.insert_one(QUEST_COLLECT, doc)


def del_game(name):
    return dbc.del_one(QUEST_COLLECT, {QUEST_KEY: name})


def main():
    print('Adding a quest')
    add_game(TEST_QUEST, dummy_quest[TEST_QUEST])
    
    print('Getting games as a list:')
    games = get_games()
    print(f'{games=}')
    
    print('Getting games as a dict:')
    games = get_games_dict()
    print(f'{games=}')
    
    print(f'{get_quest_details(TEST_QUEST)=}')


if __name__ == '__main__':
    main()