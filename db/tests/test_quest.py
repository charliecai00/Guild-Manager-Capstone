# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import db.quest as qs


TEST_DEL_NAME = 'quest to be deleted'


def create_quest_details():
    details = {}
    for field in qs.REQUIRED_FLDS:
        details[field] = "dummy_data"
    return details


@pytest.fixture(scope='function')
def temp_quest():
    qs.add_quest(qs.TEST_QUEST, create_quest_details())
    yield
    qs.del_quest(qs.TEST_QUEST)


@pytest.fixture(scope='function')
def new_quest():
    return qs.add_quest(TEST_DEL_NAME, create_quest_details())


def test_del_quest(new_quest):
    qs.del_quest(TEST_DEL_NAME)
    assert not qs.quest_exists(TEST_DEL_NAME)


def test_get_quests(temp_quest):
    chs = qs.get_quests()
    assert isinstance(chs, list)
    assert len(chs) > 0  # or 1


def test_get_quests_dict(temp_quest):
    chs = qs.get_quests_dict()
    assert isinstance(chs, dict)
    assert len(chs) > 0  # or 1


def test_get_quest_details(temp_quest):
    ch_dets = qs.get_quest_details(qs.TEST_QUEST)
    assert isinstance(ch_dets, dict)


def test_quest_exists(temp_quest):
    assert qs.quest_exists(qs.TEST_QUEST)


def test_quest_not_exists(temp_quest):
    assert not qs.quest_exists('Surely this is not a quest name!')


def test_add_quest():
    qs.add_quest(qs.TEST_QUEST, create_quest_details())
    assert qs.quest_exists(qs.TEST_QUEST)
    qs.del_quest(qs.TEST_QUEST)
