import pytest
from aoc_09 import get_lowpoints, calculate_risk_level


def test_get_lowpoints():
    input = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    result = get_lowpoints(input)

    assert result == [1, 0, 5, 5]


def test_get_lowpoints_left_top_corner_not_low_point():
    input = [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    result = get_lowpoints(input)

    assert result == []


def test_get_lowpoints_left_top_corner_low_point():
    input = [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    result = get_lowpoints(input)

    assert result == [0]


def test_get_lowpoints_right_top_corner_not_low_point():
    input = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    ]

    result = get_lowpoints(input)

    assert result == []


def test_get_lowpoints_right_top_corner_low_point():
    input = [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    result = get_lowpoints(input)

    assert result == [0]


def test_get_lowpoints_right_bottom_edge_low_point():
    input = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    ]

    result = get_lowpoints(input)

    assert result == [0]


def test_get_lowpoints_left_bottom_corner_low_point():
    input = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    result = get_lowpoints(input)

    assert result == [0]


def test_get_lowpoints_right_bottom_corner_low_point():
    input = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    ]

    result = get_lowpoints(input)

    assert result == [0]


def test_get_lowpoints_left_edge():
    input = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    result = get_lowpoints(input)

    assert result == [0]


def test_get_lowpoints_right_edge():
    input = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    result = get_lowpoints(input)

    assert result == [0]


def test_get_lowpoints_right_edge_one_lower_neighbor():
    input = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    result = get_lowpoints(input)

    assert result == []


def test_get_lowpoints_center():
    input = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    result = get_lowpoints(input)

    assert result == [0]


def test_calculate_risk_level():
    low_points = [1, 0, 5, 5]

    assert 15 == calculate_risk_level(low_points)
