import pytest
from d03 import load_sack, get_priority, get_badge, part_two


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrVvPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJQctTZtZT", "t"),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
    ),
)
def test_load_sack_returns_common_items(line, expected) -> None:
    assert load_sack(line) == expected


@pytest.mark.parametrize(
    ("item", "expected"),
    (
        ("p", 16),
        ("L", 38),
        ("P", 42),
        ("v", 22),
        ("t", 20),
        ("s", 19),
    ),
)
def test_get_priority_returns_value(item, expected) -> None:
    assert get_priority(item) == expected


def test_get_badge_returns_common_item() -> None:
    lines = []
    lines.append("vJrwpWtwJgWrhcsFMMfFFhFp")
    lines.append("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    lines.append("PmmdzqPrVvPwwTWBwg")

    assert "r" == get_badge(lines)


test_input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]


def test_part_two() -> None:
    result = part_two(test_input)
    assert result == 70
