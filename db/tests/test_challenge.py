# A NYU Capstone Project
# The Guild Manager made by JV · CC · ZQ · ZF

import os 

import pytest

import db.challenge as ch

RUNNING_ON_CICD_SERVER = os.environ.get("CI", False)


def create_challenge_details():
    details = {}
    for field in ch.REQUIRED_FLDS:
        details[field] = 2
    return details

@pytest.fixture(scope='function')
def temp_challenge():
    if not RUNNING_ON_CICD_SERVER:
        ch.add_challenge(ch.TEST_CHALLENGE_NAME, create_challenge_details())
        yield
        return True
        # ch.del_challenge(ch.TEST_CHALLENGE_NAME)
    else:
        yield
        return True


def test_get_challenges():
    if not RUNNING_ON_CICD_SERVER:
        chs = ch.get_challenges()
        assert isinstance(chs, list)
        assert len(chs) > 0 #or 1


def test_get_challenges_dict():
    if not RUNNING_ON_CICD_SERVER:
        chs = ch.get_challenges_dict()
        assert isinstance(chs, dict)
        assert len(chs) > 0 #or 1


def test_get_challenge_details():
    if not RUNNING_ON_CICD_SERVER:
        ch_dets = ch.get_challenge_details(ch.TEST_CHALLENGE_NAME)
        assert isinstance(ch_dets, dict)

    
def test_challenge_exists(temp_challenge):
    assert ch.challenge_exists(ch.TEST_CHALLENGE_NAME)


def test_challenge_not_exists():
    assert not ch.challenge_exists('Surely this is not a challenge name!')


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        ch.add_challenge(7, {})


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        ch.add_challenge('a new challenge', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        ch.add_challenge('a new challenge', {'foo': 'bar'})


def test_add_challenge():
    if not RUNNING_ON_CICD_SERVER:
        ch.add_challenge(ch.TEST_CHALLENGE_NAME, create_challenge_details())
    # assert gm.game_exists(gm.TEST_GAME_NAME)
