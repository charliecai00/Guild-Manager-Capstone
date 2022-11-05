import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

def test_MainMenu():
    # res = TEST_CLIENT.get(ep.MAIN_MENU).get_json()
    # assert isinstance(res[ep.MAIN_MENU], json)
    pass

test_input = {
    "Type": "Add_To_Party",
    "Data1": "test1",
    "Data2": "test2"
}

def test_input():
    # res = TEST_CLIENT.post(ep.INPUT, json=test_input)
    res = TEST_CLIENT.post(ep.INPUT)
