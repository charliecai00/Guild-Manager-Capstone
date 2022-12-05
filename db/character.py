# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

"""
This module encapsulates details about characters.
"""


# from telnetlib import TELNET_PORT


TEST_CHARACTER = 'test_character'
ATTRIBUTES = 'attributes'


# We expect the CHARACTER database to change frequently:
# For now, we will consider ID and CHARACTER_ID to be
# our mandatory fields.
REQUIRED_FLDS = [ATTRIBUTES]

characters = {TEST_CHARACTER: {ATTRIBUTES: []},
              'CHARACTER2': {ATTRIBUTES: []},
              'CHARACTER3': {ATTRIBUTES: []}}


def character_exists(name):
    """
    Returns whether or not a CHARACTER exists.
    """
    return name in characters


def get_characters_dict():
    return characters


def get_characters():
    return list(characters.keys())


def get_character_details(CHARACTER):
    return characters.get(CHARACTER, None)


def add_character(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    characters[name] = details

# test
def main():
    characters = get_characters()
    print(f'{characters=}')
    print(f'{get_character_details(TEST_CHARACTER)=}')


if __name__ == '__main__':
    main()
