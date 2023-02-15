# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

GUILD_ID = 'GUILD_ID'
HERO_ID = "HERO_ID"
QUEST_ID = "QUEST_ID"

GAME_COLLECT = 'Games'

TEST_GAME_NAME1 = 'test_game1'
REQUIRED_FLDS = [HERO_ID, QUEST_ID, GUILD_ID]
dummy_game = {TEST_GAME_NAME1: {HERO_ID: [1, 2, 3],
                                QUEST_ID: [1, 2, 3],
                                GUILD_ID: [1, 2, 3]}}


def initialize_game(details):
    """
    details shoudld be:
    {HERO_ID: [],
    QUEST_ID: [],
    GUILD_ID: []}
    """
    dbc.connect_db()
    return dbc.insert_one(GAME_COLLECT, details)


def get_field(field):
    """
    parameter: takes a field, ex. HERO_ID
    return: a list of values, [1,2,3]
    """
    dbc.connect_db()
    return dbc.fetch_field(field, GAME_COLLECT)


def del_game():
    """
    delete all guild
    """
    dbc.connect_db()
    return dbc.del_many(GAME_COLLECT,{})


# def get_game_details(game):
#     dbc.connect_db()
#     return dbc.fetch_one(GAME_COLLECT, {GAME_KEY: game})


# def game_exists(name):
#     return get_game_details(name) is not None


# def get_games_dict():
#     dbc.connect_db()
#     return dbc.fetch_all_as_dict(GAME_KEY, GAME_COLLECT)


# def main():
    # print('Adding games')
    # initialize_game(dummy_game[TEST_GAME_NAME1])
    # print('Getting games as a list:')
    # games = get_games()
    # print(f'{games=}')
    # print('Getting games as a dict:')
    # games = get_games_dict()
    # print(f'{games=}')
    # print(f'{get_game_details(TEST_GAME_NAME1)=}')


# if __name__ == '__main__':
    # main()
