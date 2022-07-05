import pytest

from Y2015 import D03


def test_grid_size_creates_minimum():
    assert [5, 5] == D03.grid_size(">")


def test_deliver_presents():
    grid = D03.deliver_presents(">")

    assert grid.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_deliver_presents_delivers_correct_amount():
    #grid = D03.deliver_presents(">")
    #stats = grid.stats()
    #assert stats['on'] == 2

    grid = D03.deliver_presents("^v^v^v^v^v")
    stats = grid.stats()
    assert stats['on'] == 2


@pytest.mark.skip()
def test_part_one():
    result = D03.part_one(">")
    assert result is True


@pytest.mark.skip()
def test_part_two():
    result = D03.part_two(">")
    assert result is True
