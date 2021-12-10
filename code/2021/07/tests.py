import utils
from aoc_07 import (calculate_central_point, calculate_distance, move_subs,
                    part_one)


def test_calculate_distance_between_points_returns_distance():
    result = calculate_distance(10, 0)

    assert 10 == result


def test_calculate_distance_returns_distance_regardless_of_direction():
    result = calculate_distance(0, 10)

    assert 10 == result


def test_move_subs_returns_fuel_used():
    subs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    result = move_subs(subs, 2)

    assert result == 37


def test_part_one_with_test_data():
    subs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    result = part_one(subs)

    assert result == 37


def test_calculate_central_point():
    subs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    result = calculate_central_point(subs)

    assert result == 2


def test_part_one_with_problem_data():
    filename = "data/07.data"
    subs = utils.read_file_of_ints(filename)
    result = part_one(subs)

    assert result == 341534
