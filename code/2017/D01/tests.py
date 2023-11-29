from d01 import part_one, part_two


def test_part_one():
    assert part_one("1122") == 3
    assert part_one("1111") == 4
    assert part_one("1234") == 0
    assert part_one("91212129") == 9


def test_part_two():
    assert part_two("1212") == 6
    assert part_two("1221") == 0
    assert part_two("123425") == 4
    assert part_two("123123") == 12
    assert part_two("12131415") == 4
