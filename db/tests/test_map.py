# # A NYU Capstone Project
# # The mpild Manager by JV · CC · ZQ · ZF

# import pytest
# import db.map as mp


# TEST_DEL_NAME = 'map to be deleted'


# def create_map_details():
#     details = {}
#     for field in mp.REQUIRED_FLDS:
#         details[field] = "dummy_data"
#     return details


# @pytest.fixture(scope='function')
# def temp_map():
#     mp.add_map(mp.TEST_MAP, create_map_details())
#     yield
#     mp.del_map(mp.TEST_MAP)


# @pytest.fixture(scope='function')
# def new_map():
#     return mp.add_map(TEST_DEL_NAME, create_map_details())


# def test_del_map(new_map):
#     mp.del_map(TEST_DEL_NAME)
#     assert not mp.map_exists(TEST_DEL_NAME)


# def test_get_maps(temp_map):
#     chs = mp.get_maps()
#     assert isinstance(chs, list)
#     assert len(chs) > 0  # or 1


# def test_get_maps_dict(temp_map):
#     chs = mp.get_maps_dict()
#     assert isinstance(chs, dict)
#     assert len(chs) > 0  # or 1


# def test_get_map_details(temp_map):
#     ch_dets = mp.get_map_details(mp.TEST_MAP)
#     assert isinstance(ch_dets, dict)


# def TEST_MAP_exists(temp_map):
#     assert mp.map_exists(mp.TEST_MAP)


# def TEST_MAP_not_exists(temp_map):
#     assert not mp.map_exists('Surely this is not a map name!')


# def test_add_map():
#     mp.add_map(mp.TEST_MAP, create_map_details())
#     assert mp.map_exists(mp.TEST_MAP)
#     mp.del_map(mp.TEST_MAP)
