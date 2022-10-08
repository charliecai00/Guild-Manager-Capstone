
import pytest

import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

TEST_CHAR_TYPE = 'Warrior'


def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)

# def test_command_list():
#     res = TEST_CLIENT.get(ep.command_list).get_json()
#     assert isinstance(res[ep.MESSAGE], list)

# def test_input():
#     res = TEST_CLIENT.get(ep.input).get_json()
#     assert isinstance(res[ep.MESSAGE],str)

# def test_dummy():
#     assert True