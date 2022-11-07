"""
This module encapsulates details about challenges.
"""

# from telnetlib import TELNET_PORT

TEST_CHALLENGE = 'test_CHALLENGE'
TEST_SKILL = 'test_skill'
NAME = 'name'

# We expect the CHALLENGE database to change frequently:
# For now, we will consider ID and CHALLENGE_ID to be
# our mandatory fields.
REQUIRED_FLDS = [TEST_SKILL]


challenges = {TEST_CHALLENGE: {TEST_SKILL: 'swimming'},
              'Seven Hells': {TEST_SKILL: 'surviving'},
              'Spacing Void': {TEST_SKILL: 'breathing'}}


def challenge_exists(name):
    """
    Returns whether or not a CHALLENGE exists.
    """
    return name in challenges


def get_challenges_dict():
    return challenges


def get_challenges():
    return list(challenges.keys())


def get_challenge_details(challenge):
    return challenges.get(challenge, None)


def add_challenge(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    challenges[name] = details


def main():
    challenges = get_challenges()
    print(f'{challenges=}')
    print(f'{get_challenge_details(TEST_CHALLENGE)=}')


if __name__ == '__main__':
    main()
