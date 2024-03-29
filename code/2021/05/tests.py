import pytest
import numpy as np

from aoc_05 import *


def test_create_line_short_line_vertical():
    result = create_line([1, 1], [1, 3])
    expected = np.array([[1, 1], [1, 2], [1, 3]])
    assert np.array_equal(result, expected)


def test_create_line_long_line_vertical():
    result = create_line([1, 1], [1, 6])
    expected = np.array([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6]])
    assert np.array_equal(result, expected)


def test_create_line_short_line_horizontal():
    result = create_line([9, 7], [7, 7])
    expected = np.array([[7, 7], [8, 7], [9, 7]])
    assert np.array_equal(result, expected)


def test_create_line_short_line_horizontal_line_v2():
    result = create_line([0, 9], [5, 9])
    expected = np.array([[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9]])
    assert np.array_equal(result, expected)


def test_create_line_long_line_horizontal():
    result = create_line([6, 9], [1, 9])
    expected = np.array([[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9]])
    assert np.array_equal(result, expected)


def test_create_line_order_irrevelant():
    result = create_line([9, 4], [3, 4])
    expected = np.array([[3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4]])
    assert np.array_equal(result, expected)


def test_create_line_diagonal_line_short():
    result = create_line([1, 1], [3, 3], True)
    expected = np.array([[1, 1], [2, 2], [3, 3]])

    assert np.array_equal(result, expected)


def test_create_line_diagonal_line_short_reversed():
    result = create_line([3, 3], [1, 1], True)
    expected = np.array([[1, 1], [2, 2], [3, 3]])

    assert np.array_equal(result, expected)


def test_create_line_diagonal_line_long_negative_slope():
    result = create_line([0, 0], [8, 8], True)
    expected = np.array(
        [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]
    )

    assert np.array_equal(result, expected)


def test_create_line_diagonal_line_long_negative_slope_reversed_inputs():
    result = create_line([8, 8], [0, 0], True)
    expected = np.array(
        [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]
    )

    assert np.array_equal(result, expected)


def test_create_line_diagonal_line_long_positive_slope():
    result = create_line([8, 0], [0, 8], True)
    expected = np.array(
        [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4], [5, 3], [6, 2], [7, 1], [8, 0]]
    )

    assert np.array_equal(result, expected)


def test_create_line_diagonal_line_long_positive_slope_reversed_inputs():
    result = create_line([0, 8], [8, 0], True)
    expected = np.array(
        [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4], [5, 3], [6, 2], [7, 1], [8, 0]]
    )

    assert np.array_equal(result, expected)


def test_create_grid():
    result = create_grid([3, 3])
    expected = np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )
    assert np.array_equal(result, expected)


def test_mark_grid_single_line_horizontal():
    grid = create_grid([3, 3])
    line = create_line([3, 1], [1, 1])
    result = mark_grid(grid, line)

    expected = np.array(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )

    assert np.array_equal(result, expected)


def test_mark_grid_single_line_vertical():
    grid = create_grid([3, 3])
    line = create_line([1, 0], [1, 3])

    result = mark_grid(grid, line)
    expected = np.array(
        [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
        ]
    )

    assert np.array_equal(result, expected)


def test_mark_grid_single_line_diagonal():
    grid = create_grid([3, 3])
    line = create_line([3, 3], [1, 1], True)

    result = mark_grid(grid, line)
    expected = np.array(
        [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )

    assert np.array_equal(result, expected)


def test_mark_grid_multiple_lines():
    grid = create_grid([3, 3])
    line1 = create_line([1, 1], [1, 3])
    line2 = create_line([3, 3], [0, 3])

    grid = mark_grid(grid, line1)
    result = mark_grid(grid, line2)

    expected = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [1, 2, 1, 1]])
    assert np.array_equal(result, expected)


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
    expected = [[0, 9], [5, 9]]

    assert result[0] == expected


def test_part_one_with_test_data():
    data = "data/05_test.data"
    result = part_one(data, grid_size=[9, 9])

    assert result == 5


def test_part_two_with_test_data():
    data = "data/05_test.data"
    result = part_one(data, grid_size=[9, 9], diagonal=True)

    assert result == 12


def test_part_one_with_problem_set():
    data = "data/05.data"
    result = part_one(data)

    assert result == 6564


def test_part_two_with_problem_set():
    data = "data/05.data"
    result = part_one(data, diagonal=True)

    assert result != 19139
