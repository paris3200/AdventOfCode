import pytest

from d06 import Parser, part_one, part_two


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ),
)
def test_start_of_packets(line: str, expected: int) -> None:
    parser = Parser()
    assert parser.start_of_packet(line) == expected


@pytest.mark.parametrize(
    ("line", "expected"),
    (("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),),
)
def test_start_of_message(line: str, expected: int) -> None:
    parser = Parser()
    assert parser.start_of_message(line) == expected


def test_part_two():
    assert part_one() == 1658
    assert part_two() == 2260
