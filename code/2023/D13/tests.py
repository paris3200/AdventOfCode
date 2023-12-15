from aoc_13 import create_grid, check_horizontal, check_vertical, read_lines, part_one, find_horizontal_mirror, find_vertical_mirror


def test_check_horizontal() -> None:
    lines = read_lines("test_input")
    grid = create_grid(lines)
    assert check_horizontal(grid) == 4


def test_check_horizontal_test_input5() -> None:
    lines = read_lines("test_input5")
    grid = create_grid(lines)
    assert check_horizontal(grid) == 3


def test_check_horizontal_test_input6() -> None:
    lines = read_lines("test_input6")
    grid = create_grid(lines)
    assert check_horizontal(grid) == 1


def test_find_vertical_mirror_test_data7() -> None:
    lines = read_lines("test_input7")
    grid = create_grid(lines)
    assert find_vertical_mirror(grid) == [[1, 2],[5, 6]]


def test_check_get_vertical() -> None:
    lines = read_lines("test_input")
    grid = create_grid(lines)
    assert grid.get_column(0) == "##.##.#"

    lines = read_lines("test_input3")
    grid = create_grid(lines)
    assert grid.get_column(0) == "#.##..#"


def test_check_vertical() -> None:
    lines = read_lines("test_input3")
    grid = create_grid(lines)
    assert check_vertical(grid) == 5


def test_part_one_test_data() -> None:
    assert part_one("test_input2") == 405
    assert part_one("test_input4") == 709


# def test_part_one() -> None:
#     assert part_one("input") > 34575
