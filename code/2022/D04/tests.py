import pytest

from d04 import get_sections, is_subset, part_one, part_two


INPUT = """
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("2-4,6-8", [[2, 3, 4], [6, 7, 8]]),
        ("2-3,4-5", [[2, 3], [4, 5]]),
    ),
)
def test_get_sections_returns_expanded_sections(input, expected) -> None:
    assert get_sections(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ([[2, 3, 4], [6, 7, 8]], False),
        ([[4, 5, 6], [6]], True),
        ([[6], [4, 5, 6]], True),
    ),
)
def test_is_subset(input, expected) -> None:
    assert is_subset(input) == expected


def test_part_one() -> None:
    assert part_one("test_input") == 2


def test_part_two() -> None:
    assert part_two("test_input") == 4

