# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import os 
import pytest
import db.hero as hr


TEST_DEL_NAME = 'hero to be deleted'


def create_hero_details():
    details = {}
    for field in hr.REQUIRED_FLDS:
        details[field] = "dummy_data"
    return details


@pytest.fixture(scope='function')
def temp_hero():
    hr.add_hero(hr.TEST_HERO, create_hero_details())
    yield
    hr.del_hero(hr.TEST_HERO)
    

@pytest.fixture(scope='function')
def new_hero():
    return hr.add_hero(TEST_DEL_NAME, create_hero_details())


def test_del_hero(new_hero):
    hr.del_hero(TEST_DEL_NAME)
    assert not hr.hero_exists(TEST_DEL_NAME)


def test_get_heros(temp_hero):
    chs = hr.get_heros()
    assert isinstance(chs, list)
    assert len(chs) > 0 #or 1


def test_get_heros_dict(temp_hero):
    chs = hr.get_heros_dict()
    assert isinstance(chs, dict)
    assert len(chs) > 0 #or 1


def test_get_hero_details(temp_hero):
    ch_dets = hr.get_hero_details(hr.TEST_HERO)
    assert isinstance(ch_dets, dict)

    
def test_hero_exists(temp_hero):
    assert hr.hero_exists(hr.TEST_HERO)


def test_hero_not_exists(temp_hero):
    assert not hr.hero_exists('Surely this is not a hero name!')


def test_add_hero():
    hr.add_hero(hr.TEST_HERO, create_hero_details())
    assert hr.hero_exists(hr.TEST_HERO)
    hr.del_hero(hr.TEST_HERO)
