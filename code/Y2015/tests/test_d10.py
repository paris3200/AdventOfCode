import pytest

from Y2015 import D10


@pytest.mark.parametrize(
    "given, expected", [("1", ["1"]), ("11", ["11"]), ("1122", ["11", "22"])]
)
def test_create_segments_returns_segment(given, expected) -> None:
    assert D10.create_segments(given) == expected


def test_look_say_segment_single_numbers() -> None:
    assert D10.look_say_segment("1") == "11"


def test_look_say_segment_multiple_numbers() -> None:
    assert D10.look_say_segment("11") == "21"


@pytest.mark.parametrize("given, expected", [("1211", "111221"), ("111221", "312211")])
def test_look_say_test_data(given: str, expected: str) -> None:
    assert D10.look_say(given) == expected

def test_part_one()-> None:
    assert D10.part_one("1113222113", 40) == 1

@pytest.mark.skip()
def test_part_two_correct_answer():
    pass
