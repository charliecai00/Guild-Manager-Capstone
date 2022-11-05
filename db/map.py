"""
This module encapsulates details about maps.
"""


# from telnetlib import TELNET_PORT


TEST_MAP = 'test_map'
MAP = 'map'


# We expect the map database to change frequently:
# For now, we will consider ID and map_ID to be
# our mandatory fields.
REQUIRED_FLDS = [MAP]

maps = {TEST_MAP: {MAP: []},
        'map2': {MAP: []},
        'map3': {MAP: []}}


def map_exists(name):
    """
    Returns whether or not a map exists.
    """
    return name in maps


def get_maps_dict():
    return maps


def get_maps():
    return list(maps.keys())


def get_map_details(map):
    return maps.get(map, None)


def add_map(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    maps[name] = details


def main():
    maps = get_maps()
    print(f'{maps=}')
    print(f'{get_map_details(TEST_MAP)=}')


if __name__ == '__main__':
    main()
