"""
This module encapsulates details about enemys.
"""


from telnetlib import TELNET_PORT


TEST_ENEMY = 'test_enemy'
ENEMY = 'enemy'



# We expect the enemy database to change frequently:
# For now, we will consider ID and enemy_ID to be
# our mandatory fields.
REQUIRED_FLDS = [ENEMY]

enemys = {TEST_ENEMY: {ENEMY :[]},
         'enemy2': {ENEMY :[]},
         'enemy3': {ENEMY :[]} }


def enemy_exists(name):
    """
    Returns whether or not a enemy exists.
    """
    return name in enemys


def get_enemys_dict():
    return enemys


def get_enemys():
    return list(enemys.keys())


def get_enemy_details(enemy):
    return enemys.get(enemy, None)


def add_enemy(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    enemys[name] = details


def main():
    enemys = get_enemys()
    print(f'{enemys=}')
    print(f'{get_enemy_details(TEST_ENEMY)=}')


if __name__ == '__main__':
    main()