"""
This module encapsulates details about parties.
"""


# from telnetlib import TELNET_PORT


TEST_PARTY = 'test_party'
HEROS = 'hero_list'
NAME = 'name'


# We expect the party database to change frequently:
# For now, we will consider ID and PARTY_ID to be
# our mandatory fields.
REQUIRED_FLDS = [HEROS]

parties = {TEST_PARTY: {HEROS: []},
           'party2': {HEROS: []},
           'party3': {HEROS: []}}


def party_exists(name):
    """
    Returns whether or not a party exists.
    """
    return name in parties


def get_parties_dict():
    return parties


def get_parties():
    return list(parties.keys())


def get_party_details(party):
    return parties.get(party, None)


def add_party(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    parties[name] = details


def main():
    parties = get_parties()
    print(f'{parties=}')
    print(f'{get_party_details(TEST_PARTY)=}')


if __name__ == '__main__':
    main()
