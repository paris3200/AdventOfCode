import pytest

from aoc_05 import *


def test_create_line_short_line_vertical():
    result = create_line([1, 1], [1, 3])
    assert result == [[1, 1], [1, 2], [1, 3]]


def test_create_line_long_line_vertical():
    result = create_line([1, 1], [1, 6])
    assert result == [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]


def test_create_line_short_line_horizontal():
    result = create_line([9, 7], [7, 7])
    assert result == [[9, 7], [8, 7], [7, 7]]


def test_create_line_long_line_horizontal():
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


def test_mark_grid_single_line_horizontal():
    grid = create_grid([3, 3])
    line = create_line([3, 1], [1, 1])
    result = mark_grid(grid, line)

    expected = [
        [".", ".", ".", "."],
        [".", 1, 1, 1],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
        ]

    assert result == expected

def test_mark_grid_single_line_vertical():
    grid = create_grid([3, 3])
    line = create_line([1, 0], [1, 3])

    result = mark_grid(grid, line)
    expected = [
        [".", 1, ".", "."],
        [".", 1, ".", "."],
        [".", 1, ".", "."],
        [".", 1, ".", "."],
    ]

    assert result == expected

def test_mark_grid_multiple_lines():
    grid = create_grid([3, 3])
    line1 = create_line([1, 1], [1, 3])
    line2= create_line([3, 3], [0, 3])

    grid = mark_grid(grid, line1)
    result = mark_grid(grid, line2)


    expected = [
        [".", ".", ".", "."],
        [".", 1, ".", "."],
        [".", 1, ".", "."],
        [1, 2, 1, 1],
    ]
    assert result == expected
