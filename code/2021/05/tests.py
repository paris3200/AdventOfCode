from aoc_05 import *


def test_create_line_short_line_horizontal():
    result = create_line([1, 1], [1, 3])
    assert result == [[1, 1], [1, 2], [1, 3]]


def test_create_line_long_horizontal():
    result = create_line([1, 1], [1, 6])
    assert result == [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]


def test_create_line_short_line_vertical():
    result = create_line([9, 7], [7, 7])
    assert result == [[9, 7], [8, 7], [7, 7]]


def test_create_line_long_line_vertical():
    result = create_line([6, 9], [1, 9])
    assert result == [[6, 9], [5, 9], [4, 9], [3, 9], [2, 9], [1, 9]]


def test_get_list_limits_returns_maximum_of_each_coordinate():
    input = [[6, 9], [5, 9], [4, 9], [3, 9], [2, 9], [1, 9]]
    result = get_list_limits(input)
    assert result == [6, 9]


def test_create_grid():
    result = create_grid([3, 3])
    grid = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
    ]
    assert result == grid
