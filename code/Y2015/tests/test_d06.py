import pytest

from Y2015.D06 import Grid, process_instruction


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


def test_process_instruction_toggle():
    result = process_instruction("toggle 660,55 through 986,197")
    expected = {"action": "toggle", "start_x": 660, "start_y": 55, "end_x": 986, "end_y": 197}
    assert result == expected

def test_process_instruction_on():
    result = process_instruction("turn on 660,55 through 986,197")
    expected = {"action": "on", "start_x": 660, "start_y": 55, "end_x": 986, "end_y": 197}
    assert result == expected

def test_process_instruction_off():
    result = process_instruction("turn off 660,55 through 986,197")
    expected = {"action": "off", "start_x": 660, "start_y": 55, "end_x": 986, "end_y": 197}
    assert result == expected

@pytest.mark.skip("Not solved")
def test_part_one():
    result = D06.part_one()
    assert result is True


@pytest.mark.skip("Not solved")
def test_part_two():
    result = D06.part_two()
    assert result is True
