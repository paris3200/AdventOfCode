import pytest

from aoc_05 import *


def test_create_line_short_line_vertical():
    result = create_line([1, 1], [1, 3])
    assert result == [[1, 1], [1, 2], [1, 3]]

def test_create_line_short_line_vertical():
    result = create_line([2, 2], [2, 1])
    assert result == [[2, 1], [2, 2]]

def test_create_line_long_line_vertical():
    result = create_line([1, 1], [1, 6])
    assert result == [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]


def test_create_line_short_line_horizontal():
    result = create_line([9, 7], [7, 7])
    assert result == [[7, 7], [8, 7], [9, 7]]

def test_create_line_short_line_horizontal_line_v2():
    result = create_line([0, 9], [5, 9])
    assert result == [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9]]

def test_create_line_long_line_horizontal():
    result = create_line([6, 9], [1, 9])
    assert result == [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9]]

def test_create_line_order_irrevelant():
    result = create_line([9, 4], [3, 4])
    assert result == [[3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4]]

def test_get_list_limits_returns_maximum_of_each_coordinate():
    input = [[6, 9], [5, 9], [4, 9], [3, 9], [2, 9], [1, 9]]
    result = get_list_limits(input)
    assert result == [6, 9]

def test_get_list_limits_returns_maximum_of_each_coordinate():
    input = [[6, 9], [5, 9], [4, 9], [3, 9], [2, 9], [1, 9]]
    result = get_list_limits(input)
    assert result == [6, 9]

def test_create_grid():
    result = create_grid([3, 3])
    grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    assert result == grid


def test_mark_grid_single_line_horizontal():
    grid = create_grid([3, 3])
    line = create_line([3, 1], [1, 1])
    result = mark_grid(grid, line)

    expected = [
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    assert result == expected


def test_mark_grid_single_line_vertical():
    grid = create_grid([3, 3])
    line = create_line([1, 0], [1, 3])

    result = mark_grid(grid, line)
    expected = [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
    ]

    assert result == expected


def test_mark_grid_multiple_lines():
    grid = create_grid([3, 3])
    line1 = create_line([1, 1], [1, 3])
    line2 = create_line([3, 3], [0, 3])

    grid = mark_grid(grid, line1)
    result = mark_grid(grid, line2)

    expected = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [1, 2, 1, 1]
    ]
    assert result == expected


def test_count_intersection_one_intersection():
    grid = create_grid([3, 3])
    line1 = create_line([1, 1], [1, 3])
    line2 = create_line([3, 3], [0, 3])

    grid = mark_grid(grid, line1)
    grid = mark_grid(grid, line2)

    result = count_intersections(grid)

    assert result == 1


def test_count_intersection_two():
    grid = create_grid([3, 3])
    line1 = create_line([1, 1], [1, 3])
    line2 = create_line([3, 3], [0, 3])
    line3 = create_line([3, 1], [0, 1])

    grid = mark_grid(grid, line1)
    grid = mark_grid(grid, line2)
    grid = mark_grid(grid, line3)

    result = count_intersections(grid)

    assert result == 2

def test_read_file():
    data = "data/05_test.data"
    result = read_file(data)
    expected = [[0,9],[5,9]]

    assert result[0] == expected

def test_part_one_with_test_data():
    data = "data/05_test.data"
    result = part_one(data)

    assert result == 5

# Warning:  Very Slow test ~ 43m
@pytest.mark.skip
def test_part_one_with_problem_set():
    data = "data/05.data"
    result = part_one(data)

    assert result == 6564
