import pytest

from Y2015 import D03


def test_grid_size_creates_minimum():
    assert [5, 5] == D03.grid_size(">")


@pytest.mark.skip()
def test_part_one_with_sample_data():
    presents = D03.part_one(">")
    assert presents == 2

    presents = D03.part_one("^v^v^v^v^v")
    assert presents == 2

def test_part_one_correct_answer():
    presents = D03.part_one()
    assert presents == 2592


def test_part_two_correct_answer():
    presents = D03.part_two('^v')
    assert presents == 3

    presents = D03.part_two('^>v<')
    assert presents == 3

