from aoc_07 import find_parent, read_lines, part_one


def test_find_parent():
    lines = read_lines("test_input")
    assert find_parent(lines, "pbga") == "padx"


def test_part_one():
    assert part_one("test_input") == "tknk"


def test_part_one_solution():
    assert part_one("input") == "vgzejbd"
