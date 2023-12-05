from aoc_05 import map_to_dict, category_map, get_destination, read_lines, part_one


def test_map_to_table() -> None:
    assert map_to_dict(50, 98, 2) == {"source_start": 98, "source_end": 100, "dest_offset": -48}


def test_category_map() -> None:
    input = ["50 98 2", "52 50 3"]
    result = [{"source_start": 98, "source_end": 100, "dest_offset": -48}, {"source_start": 50, "source_end": 53, "dest_offset": 2}]
    assert category_map(input) == result


def test_get_destination() -> None:
    lines = read_lines("test_input")
    seed_line = lines.pop(0)
    seed_line = seed_line.split(':')
    seeds = seed_line[1].strip().split(" ")
    seeds = list(map(int, seeds))
    lines.pop(0)
    soil_map = category_map([lines[0], lines[1]])

    soil = get_destination(soil_map, 79)

    assert soil == 81


def test_part_one_test_data() -> None:
    assert part_one("test_input") == 35


def test_part_one_input_data() -> None:
    assert part_one("input") != 247422950
    assert part_one("input") != 278959799
    assert part_one("input") == 226172555
