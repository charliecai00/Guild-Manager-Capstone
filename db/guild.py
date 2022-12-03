# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

"""
This module encapsulates details about guilds.
"""


# from telnetlib import TELNET_PORT


TEST_GUILD = 'test_guild'
ID = 'id'
GUILD_ID = 'PART_ID'
HIRED_HEROS = 'hired_heros_list'
GROUPS = 'groups_list'
QEUSTS = 'quest_list'
QUEST_HISTORY = 'quest_history'
PARTIES = 'party_list'
FUNDS = 'funds'


# We expect the guild database to change frequently:
# For now, we will consider ID and guild_ID to be
# our mandatory fields.
REQUIRED_FLDS = [ID, GUILD_ID, HIRED_HEROS]

guilds = {TEST_GUILD: {ID: 9, GUILD_ID: 9, HIRED_HEROS: 2, GROUPS: [],
                       QEUSTS: [], QUEST_HISTORY: [], PARTIES: [], FUNDS: 0},
          'guild2': {ID: 9, GUILD_ID: 9, HIRED_HEROS: 2, GROUPS: [],
                     QEUSTS: [], QUEST_HISTORY: [], PARTIES: [], FUNDS: 0},
          'guild3': {ID: 6, GUILD_ID: 1, HIRED_HEROS: 2, GROUPS: [],
                     QEUSTS: [], QUEST_HISTORY: [], PARTIES: [], FUNDS: 0}}


def guild_exists(name):
    """
    Returns whether or not a guild exists.
    """
    return name in guilds


def get_guilds_dict():
    return guilds


def get_guilds():
    return list(guilds.keys())


def get_guild_details(guild):
    return guilds.get(guild, None)


def add_guild(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    guilds[name] = details


def main():
    guilds = get_guilds()
    print(f'{guilds=}')
    print(f'{get_guild_details(TEST_GUILD)=}')


if __name__ == '__main__':
    main()
