from aoc_06 import get_number_wins 


def test_get_number_wins() -> None:
    assert get_number_wins(7, 9) == 4
    assert get_number_wins(15, 40) == 8
