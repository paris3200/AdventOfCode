import pytest

from aoc_03 import create_grid, part_one, part_two, sum_adjacents


@pytest.mark.parametrize(
    ("square", "distance"),
    (
        (1, 0),
        (12, 3),
        (23, 2),
        (1024, 31),
    ),
)
def test_part_one(square, distance):
    assert part_one(square) == distance


def test_create_grid():
    assert create_grid(1) == {"0, 0": 1}
    assert create_grid(2) == {"0, 0": 1, "1, 0": 1}


def test_sum_adjacents():
    points = create_grid(1)
    assert sum_adjacents(points, 0, 1) == 1
