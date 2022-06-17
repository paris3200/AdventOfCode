from Y2015.D01 import part_one, part_two

def test_part_one():
    assert part_one(["(())"]) == 0
    assert part_one(["((("]) == 3
    assert part_one(["(()(()("]) == 3
    assert part_one(["))((((("]) == 3
    assert part_one(["())"]) == -1
    assert part_one(["))("]) == -1
    assert part_one([")))"]) == -3

def test_part_two():
    assert part_two([")"]) == 1
    assert part_two(["()())"]) == 5
