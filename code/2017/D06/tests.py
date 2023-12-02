import pytest


from aoc_06 import redistribute, part_one, part_two


def test_redistribute_with_unique_max() -> None:
    assert redistribute([0, 2, 7, 0]) == [2, 4, 1, 2]


def test_redistribute_with_two_maxes() -> None:
    assert redistribute([3, 1, 2, 3]) == [0, 2, 3, 4]


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ([2, 4, 1, 2], [3, 1, 2, 3]),
        ([3, 1, 2, 3], [0, 2, 3, 4]),
        ([1, 3, 4, 1], [2, 4, 1, 2]),
    ),
)
def test_redistribute(input, expected) -> None:
    assert redistribute(input) == expected


def test_part_one_test_data() -> None:
    assert part_one("test_input") == 5


def test_part_two_test_data() -> None:
    assert part_two("test_input") == 4
