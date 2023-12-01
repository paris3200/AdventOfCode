import pytest

from aoc_01 import get_calibration_digits, get_calibration_words, part_two


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ),
)
def test_get_calibration_digits(input, expected):
    assert get_calibration_digits(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("six", 66),
        ("6", 66),
        ("eighthree", 83),
        ("sevenine", 79),
        ("twone", 21),
        ("31absce", 31),
        ("3fiveeightoneightg", 38),
    ),
)
def test_get_calibration_words(input, expected):
    assert get_calibration_words(input) == expected


def test_part_two() -> None:
    assert part_two("test_input") == 281
