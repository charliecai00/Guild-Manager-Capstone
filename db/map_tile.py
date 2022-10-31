"""
This module encapsulates details about mapTiles.
"""


from telnetlib import TELNET_PORT

from matplotlib.backend_bases import LocationEvent


TEST_MAPTile = 'test_mapTile'
TERRAIN = 'terrain'
LOCATIONS = 'locations'


# We expect the mapTile database to change frequently:
# For now, we will consider ID and mapTile_ID to be
# our mandatory fields.
REQUIRED_FLDS = [TERRAIN, LOCATIONS]

mapTiles = {TEST_MAPTile: {TERRAIN : '', LOCATIONS : []},
         'mapTile2': {TERRAIN : '', LOCATIONS : []},
         'mapTile3': {TERRAIN : '', LOCATIONS : []} }


def mapTile_exists(name):
    """
    Returns whether or not a mapTile exists.
    """
    return name in mapTiles


def get_mapTiles_dict():
    return mapTiles


def get_mapTiles():
    return list(mapTiles.keys())


def get_mapTile_details(mapTile):
    return mapTiles.get(mapTile, None)


def add_mapTile(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    mapTiles[name] = details


def main():
    mapTiles = get_mapTiles()
    print(f'{mapTiles=}')
    print(f'{get_mapTile_details(TEST_MAPTile)=}')


if __name__ == '__main__':
    main()