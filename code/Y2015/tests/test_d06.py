import pytest

from Y2015.D06 import Grid


def test_grid_is_created_with_default_value():
    grid = Grid(5, 5)
    assert grid.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_turn_on_point():
    grid = Grid(5, 5)
    grid.turn_on_point(2, 2)
    assert grid.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_toggle():
    grid = Grid(5, 5)
    grid.toggle_point(2, 2)
    grid.toggle_point(1, 1)
    grid.turn_on_point(3, 3)
    grid.toggle_point(3, 3)
    assert grid.grid == [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_turn_on_range():
    grid = Grid(5, 5)
    grid.switch_range(0, 0, 2, 2, "on")
    assert grid.grid == [
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_switch_range_toggle():
    grid = Grid(5, 5)
    grid.switch_range(0, 0, 2, 2, "on")
    grid.switch_range(1, 1, 3, 3, "toggle")
    assert grid.grid == [
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]


def test_stats():
    grid = Grid(5, 5)
    grid.switch_range(0, 0, 2, 2, "on")
    grid.switch_range(1, 1, 3, 3, "toggle")
    assert grid.grid == [
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    assert grid.stats() == {"on": 10, "off": 15}

@pytest.mark.skip("Not solved")
def test_part_one():
    result = D06.part_one()
    assert result is True


@pytest.mark.skip("Not solved")
def test_part_two():
    result = D06.part_two()
    assert result is True
