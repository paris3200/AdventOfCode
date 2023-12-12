from aoc_03 import is_symbol, part_one, validate_row, get_numbers, create_grid, get_gear_numbers


def test_is_symbol_false() -> None:
    assert is_symbol(".") is False
    assert is_symbol("4") is False


def test_is_symbol_true() -> None:
    assert is_symbol("*") is True
    assert is_symbol("$") is True


def test_get_numbers() -> None:
    line = ".100..200."
    assert get_numbers(line) == ["100", "200"]

    line = "..113.......100.100..............992.......373#......791.....775.873.................................227..849=.357.........................."
    result = [
        "113",
        "100",
        "100",
        "992",
        "373",
        "791",
        "775",
        "873",
        "227",
        "849",
        "357",
    ]
    assert get_numbers(line) == result

    line = ".307............564..........353............442...153.*.......................516..5.......414................131.......................*..."
    result = ["307", "564", "353", "442", "153", "516", "5", "414", "131"]
    assert get_numbers(line) == result


def test_validate_row() -> None:
    result = "467......."
    assert validate_row("test_input", 0) == result


def test_validate_row_error() -> None:
    result = "................564..........353............442...153.*............................5.......414..........................................*..."
    assert validate_row("input", 120) == result


def test_part_one() -> None:
    assert part_one("test_input", "results") == 4361


def test_part_one_wrong_answers() -> None:
    assert part_one("input", "results") != 572801
    assert part_one("input", "results") != 552433
    assert part_one("input", "results") == 556367


def test_get_gear_numbers() -> None:
    grid = create_grid("test_input")
    points = [[5, 9], [6, 7], [6, 9]]
    assert get_gear_numbers(grid, points) == [598, 755]
