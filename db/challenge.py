"""
This module encapsulates details about challenges.
"""
import db.db_connect as dbc

TEST_CHALLENGE_NAME = 'test_challenge'
TEST_SKILL = 'test_skill'
NAME = 'name'


# We expect the CHALLENGE database to change frequently:
# For now, we will consider ID and CHALLENGE_ID to be
# our mandatory fields.
REQUIRED_FLDS = [TEST_SKILL]
challenges = {TEST_CHALLENGE_NAME: {TEST_SKILL: 'swimming'},
              'Seven_Hells': {TEST_SKILL: 'climb'},
              'Spacing_Void': {TEST_SKILL: 'breathing'}}

CHALLENGE_COLLECT = "challenges"
CHALLENGE_KEY = "name"


def get_challenge_details(challenge):
    return dbc.fetch_one(CHALLENGE_COLLECT, {CHALLENGE_KEY: challenge})
    # return challenges.get(challenge, None)


def challenge_exists(name):
    """
    Returns whether or not a challenge exists.
    """
    return name in challenges


def get_challenges_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(CHALLENGE_KEY, CHALLENGE_COLLECT)


def get_challenges():
    dbc.connect_db()
    return dbc.fetch_all(CHALLENGE_COLLECT)


def add_challenge(name, details):
    doc = details
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    dbc.connect_db()
    doc[CHALLENGE_KEY] = name
    return dbc.insert_one(CHALLENGE_COLLECT, doc)


def main():
    print("Geting challenges as a list:")
    challenges = get_challenges()
    print(f'{challenges=}')
    print("Geting challenges a s a dict:")
    challenges = get_challenges_dict()
    print(f'{challenges=}')
    print(f'{get_challenge_details(TEST_CHALLENGE_NAME)=}')


if __name__ == '__main__':
    main()
