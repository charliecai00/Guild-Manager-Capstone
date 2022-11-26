import os 

import pytest

import db.challenge as ch


TEST_DEL_NAME = 'Challenge to be deleted'


def create_challenge_details():
    details = {}
    for field in ch.REQUIRED_FLDS:
        details[field] = 2
    return details


@pytest.fixture(scope='function')
def temp_challenge():
    ch.add_challenge(ch.TEST_CHALLENGE_NAME, create_challenge_details())
    yield
    ch.del_challenge(ch.TEST_CHALLENGE_NAME)
    

@pytest.fixture(scope='function')
def new_challenge():
    return ch.add_challenge(TEST_DEL_NAME, create_challenge_details())


def test_del_challenge(new_challenge):
    ch.del_challenge(TEST_DEL_NAME)
    assert not ch.challenge_exists(TEST_DEL_NAME)


def test_get_challenges(temp_challenge):
    chs = ch.get_challenges()
    assert isinstance(chs, list)
    assert len(chs) > 0 #or 1


def test_get_challenges_dict(temp_challenge):
    chs = ch.get_challenges_dict()
    assert isinstance(chs, dict)
    assert len(chs) > 0 #or 1


def test_get_challenge_details(temp_challenge):
    ch_dets = ch.get_challenge_details(ch.TEST_CHALLENGE_NAME)
    assert isinstance(ch_dets, dict)

    
def test_challenge_exists(temp_challenge):
    assert ch.challenge_exists(ch.TEST_CHALLENGE_NAME)


def test_challenge_not_exists(temp_challenge):
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
    ch.add_challenge(ch.TEST_CHALLENGE_NAME, create_challenge_details())
    assert ch.challenge_exists(ch.TEST_CHALLENGE_NAME)
    ch.del_challenge(ch.TEST_CHALLENGE_NAME)
