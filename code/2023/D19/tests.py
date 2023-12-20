from aoc_19 import create_function, Part, part_one


def test_part_one() -> None:
    parts = []
    parts.append(Part(x=787, m=2655, a=1222, s=2876))
    parts.append(Part(x=1679, m=44, a=2067, s=496))
    parts.append(Part(x=2036, m=264, a=79, s=2244))
    parts.append(Part(x=2461, m=1339, a=466, s=291))
    parts.append(Part(x=2127, m=1623, a=2188, s=1013))
    assert part_one("test_input") == 19114
