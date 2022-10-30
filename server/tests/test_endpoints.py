import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

def test_command_list():
    res = TEST_CLIENT.get(ep.COMMAND_LIST).get_json()
    assert isinstance(res[ep.COMMANDS], list)

test_input = {
    "Type": "Add_To_Party",
    "Data": "specific data goes here"
}

def test_input():
    res = TEST_CLIENT.post(ep.INPUT, json=test_input)
    pass
