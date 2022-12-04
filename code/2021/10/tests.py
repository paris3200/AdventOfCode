import pytest

from aoc_10 import is_valid, part_one, complete_lines, score_autocomplete, part_two


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
        ("[({(<(())[]>[[{[]{<()<>>", True),
    ),
)
def test_is_valid(line, expected) -> None:
    assert is_valid(line) == expected


def test_part_one() -> None:
    assert part_one("data/test_input") == 26397


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
        ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
    ),
)
def test_complete_lines(line, expected) -> None:
    assert complete_lines(line) == expected


@pytest.mark.parametrize(
    ("completion", "expected"),
    (
        ("}}]])})]", 288957),
        (")}>]})", 5566),
    ),
)
def test_complete_lines(completion, expected) -> None:
    assert score_autocomplete(completion) == expected


def test_part_two() -> None:
    assert part_two("data/test_input") == 288957
