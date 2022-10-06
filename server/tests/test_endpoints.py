<<<<<<< HEAD
import pytest
# import server.endpoints as ep
=======
import server.endpoints as ep
>>>>>>> b3b5bcedd2f80ce88b7f1220f5739a1b1360a7e3

# TEST_CLIENT = ep.app.test_client()


def dummy_api():
    # res = TEST_CLIENT.get(ep.dummy_api).get_json()
    # assert isinstance(res[ep.MESSAGE], str)
    assert True

<<<<<<< HEAD
# def command_list():
#     res = TEST_CLIENT.get(ep.command_list).get_json()
#     assert isinstance(res[ep.MESSAGE], str)

# def input():
#     res = TEST_CLIENT.get(ep.input).get_json()
#     assert isinstance(res[ep.MESSAGE],str)

=======

def command_list():
    res = TEST_CLIENT.get(ep.command_list).get_json()
    assert isinstance(res[ep.MESSAGE], str)


def input():
    res = TEST_CLIENT.get(ep.input).get_json()
    assert isinstance(res[ep.MESSAGE], str)
>>>>>>> b3b5bcedd2f80ce88b7f1220f5739a1b1360a7e3
