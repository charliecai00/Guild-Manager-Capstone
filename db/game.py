# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

GUILD_ID = 'GUILD_ID'
HERO_ID = "HERO_ID"
QUEST_ID = "QUEST_ID"
LOCALE_ID = "LOCALE_ID"
GUILD = "guild"
MAP = "map"
FULL_HERO_LIST = "full_hero_list"
FULL_QUEST_LIST = "full_quest_list"

GAME_KEY = 'name'
GAME_COLLECT = 'Games'

TEST_GAME_NAME1 = 'test_game1'
TEST_GAME_NAME2 = 'test_game2'
REQUIRED_FLDS = [GUILD_ID, HERO_ID, QUEST_ID, LOCALE_ID, GUILD_ID, MAP, FULL_HERO_LIST, FULL_QUEST_LIST]
dummy_game = {TEST_GAME_NAME1: {GUILD_ID: 0, 
                          HERO_ID: 0, 
                          QUEST_ID: 0, 
                          LOCALE_ID: 0,
                          GUILD: "refer to guild object",
                          MAP: "refer to map object",
                          FULL_HERO_LIST: [], 
                          FULL_QUEST_LIST: []},
         TEST_GAME_NAME2: {GUILD_ID: 1, 
                          HERO_ID: 1, 
                          QUEST_ID: 1, 
                          LOCALE_ID: 1,
                          GUILD: "refer to guild object",
                          MAP: "refer to map object",
                          FULL_HERO_LIST: [], 
                          FULL_QUEST_LIST: []}}


def get_game_details(game):
    dbc.connect_db()
    return dbc.fetch_one(GAME_COLLECT, {GAME_KEY: game})


def game_exists(name):
    return get_game_details(name) is not None


def get_games_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(GAME_KEY, GAME_COLLECT)


def get_games():
    dbc.connect_db()
    return dbc.fetch_all(GAME_COLLECT)


def add_game(name, details):
    doc = details
    dbc.connect_db()
    doc[GAME_KEY] = name
    return dbc.insert_one(GAME_COLLECT, doc)


def del_game(name):
    dbc.connect_db()
    return dbc.del_one(GAME_COLLECT, {GAME_KEY: name})


# def main():
#     print('Adding games')
#     add_game(TEST_GAME_NAME1, dummy_game[TEST_GAME_NAME1])
#     add_game(TEST_GAME_NAME2, dummy_game[TEST_GAME_NAME2])
#     print('Getting games as a list:')
#     games = get_games()
#     print(f'{games=}')
#     print('Getting games as a dict:')
#     games = get_games_dict()
#     print(f'{games=}')
#     print(f'{get_game_details(TEST_GAME_NAME1)=}')


# if __name__ == '__main__':
#     main()
