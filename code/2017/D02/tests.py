from aoc_02 import read_lines, part_one


def test_part_one():
    lines = read_lines("input")
    assert part_one(lines) == 47136
