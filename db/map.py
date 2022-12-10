# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import db.db_connect as dbc

TEST_MAP = 'test_map'
MAP = 'map'

MAP_KEY = 'name'
MAP_COLLECT = 'Maps'

# We expect the map database to change frequently:
# For now, we will consider ID and map_ID to be
# our mandatory fields.
REQUIRED_FLDS = [MAP]

maps = {TEST_MAP: {MAP: []},
        'map2': {MAP: []},
        'map3': {MAP: []}}


def get_map_details(map):
    dbc.connect_db()
    return dbc.fetch_one(MAP_COLLECT, {MAP_KEY: map})


def map_exists(name):
    return get_map_details(name) is not None


def get_maps_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(MAP_KEY, MAP_COLLECT)


def get_maps():
    dbc.connect_db()
    return dbc.fetch_all(MAP_COLLECT)


def add_map(name, details):
    doc = details
    dbc.connect_db()
    doc[MAP_KEY] = name
    return dbc.insert_one(MAP_COLLECT, doc)


def del_map(name):
    dbc.connect_db()
    return dbc.del_one(MAP_COLLECT, {MAP_KEY: name})


def main():
    maps = get_maps()
    print(f'{maps=}')
    print(f'{get_map_details(TEST_MAP)=}')


if __name__ == '__main__':
    main()
