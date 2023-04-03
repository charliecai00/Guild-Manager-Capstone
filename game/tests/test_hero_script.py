# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

import pytest
import hero_script as hs
# from game.object_classes.map import Map


@pytest.fixture(scope='class', autouse=True)
def temp_hero_script():
    test_hero = hs.generate_hero(0)
    yield test_hero
    test_hero = None

def test_heal_hero(temp_hero_script):
    pass