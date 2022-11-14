"""
This module encapsulates details about quests.
"""


# import challenge
# from telnetlib import TELNET_PORT


TEST_QUEST = 'test_quest'
NAME = 'name'
HEROS = 'hero_list'
CHALLENGE = 'challenge'
CHECK_STAT = 'check_stat'
CHILDREN = 'children'
TERMINAL = 'terminal'
PARENT = 'parent'
DONE = 'done'

# We expect the quest database to change frequently:
# For now, we will consider ID and quest_ID to be
# our mandatory fields.
REQUIRED_FLDS = [HEROS]

quests = {TEST_QUEST: {HEROS: [], CHALLENGE: 'challenge', CHECK_STAT: None,
          CHILDREN: [], TERMINAL: False, PARENT: None, DONE: False},
           'quest2': {HEROS: [], CHALLENGE: 'challenge', CHECK_STAT: None,
          CHILDREN: [], TERMINAL: False, PARENT: None, DONE: False},
           'quest3': {HEROS: [], CHALLENGE: 'challenge', CHECK_STAT: None,
          CHILDREN: [], TERMINAL: False, PARENT: None, DONE: False}}


def quest_exists(name):
    """
    Returns whether or not a quest exists.
    """
    return name in quests


def get_quests_dict():
    return quests


def get_quests():
    return list(quests.keys())


def get_quest_details(quest):
    return quests.get(quest, None)


def add_quest(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    quests[name] = details


def main():
    quests = get_quests()
    print(f'{quests=}')
    print(f'{get_quest_details(TEST_QUEST)=}')


if __name__ == '__main__':
    main()
