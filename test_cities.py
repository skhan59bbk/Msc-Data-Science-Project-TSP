import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    assert type(compute_total_distance(road_map1)) == float


def test_swap_cities():
    assert type(swap_cities(road_map1,5,12)) == tuple


def test_shift_cities():
    assert type(shift_cities(road_map)) == list

