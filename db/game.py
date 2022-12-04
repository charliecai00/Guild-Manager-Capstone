# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

"""
This module encapsulates details about games.
"""
import db.db_connect as dbc

TEST_GAME_NAME = 'test_game'
GUILD_ID = 'GUILD_ID'
HERO_ID = "HERO_ID"
QUEST_ID = "QUEST_ID"
LOCALE_ID = "LOCALE_ID"
GUILD = "guild"
MAP = "map"
FULL_HERO_LIST = "full_hero_list"
FULL_QUEST_LIST = "full_quest_list"


# We expect the game database to change frequently:
# For now, we will consider ID and game_ID to be
# our mandatory fields.
REQUIRED_FLDS = [GUILD_ID]
games = {TEST_GAME_NAME: {GUILD_ID: 0, HERO_ID: 0, QUEST_ID: 0, LOCALE_ID: 0,
                          GUILD: "refer to guild object",
                          MAP: "refer to map object",
                          FULL_HERO_LIST: [], FULL_QUEST_LIST: []},
         "ANOTHER TEST": {GUILD_ID: 0, HERO_ID: 0, QUEST_ID: 0, LOCALE_ID: 0,
                          GUILD: "refer to guild object",
                          MAP: "refer to map object",
                          FULL_HERO_LIST: [], FULL_QUEST_LIST: []}}

GAME_COLLECT = "games"
GAME_KEY = "name"


def get_game_details(game):
    return dbc.fetch_one(GAME_COLLECT, {GAME_KEY: game})
    # return games.get(game, None)


def game_exists(name):
    """
    Returns whether or not a game exists.
    """
    return name in games


def get_games_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(GAME_KEY, GAME_COLLECT)


def get_games():
    dbc.connect_db()
    return dbc.fetch_all(GAME_COLLECT)


def add_game(name, details):
    doc = details
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    dbc.connect_db()
    doc[GAME_KEY] = name
    return dbc.insert_one(GAME_COLLECT, doc)


def del_game(name):
    return dbc.del_one(GAME_COLLECT, {GAME_KEY: name})


def main():
    print("Geting games as a list:")
    games = get_games()
    print(f'{games=}')
    print("Geting games a s a dict:")
    games = get_games_dict()
    print(f'{games=}')
    print(f'{get_game_details(TEST_GAME_NAME)=}')


if __name__ == '__main__':
    main()
