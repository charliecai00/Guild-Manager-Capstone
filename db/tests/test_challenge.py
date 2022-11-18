import os 

import pytest

import challenge as ch

RUNNING_ON_GIT = os.environ.get("CI", False)

def test_get_challenges():
    chs = ch.get_challenges()
    assert isinstance(chs, list)
    assert len(chs) > 0 #or 1


def test_get_challenge_details():
    ch_dets = ch.get_challenge_details(ch.TEST_CHALLENGE_NAME)
    assert isinstance(ch_dets, dict)


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
    details = {}
    for field in ch.REQUIRED_FLDS:
        details[field] = 2
    ch.add_challenge(ch.TEST_CHALLENGE_NAME, details)
    assert ch.challenge_exists(ch.TEST_CHALLENGE_NAME)