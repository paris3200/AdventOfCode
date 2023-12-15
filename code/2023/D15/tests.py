from aoc_15 import hash_char


def test_hash_char() -> None:
    current_value = 253
    for char in "qp=3":
        current_value = hash_char(char, current_value)
    assert current_value == 97
