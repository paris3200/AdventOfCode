from aoc_03 import get_adjacent_points, is_symbol, validate_number, part_one, validate_row, number_to_points


def test_get_adjacent_points_away_from_edge() -> None:
    expected = [[5, 6], [5, 7], [5, 5], [6, 7], [6, 5], [7, 6], [7, 7], [7, 5]]
    expected.sort()
    assert get_adjacent_points(6, 6, 10, 10) == expected


def test_get_adjacent_points_at_edge() -> None:
    expected = [[5, 6], [5, 5], [6, 5]]
    expected.sort()
    assert get_adjacent_points(6, 6, 6, 6) == expected


def test_is_symbol_false() -> None:
    assert is_symbol(".") is False
    assert is_symbol("4") is False


def test_is_symbol_true() -> None:
    assert is_symbol("*") is True
    assert is_symbol("$") is True


# def test_validate_number() -> None:
#     check_point = [[0, 0], [0, 1], [0, 2]]
#     assert validate_number("test_input", check_point) is True
#
#     check_point = [[0, 7], [0, 8], [0, 9]]
#     assert validate_number("test_input", check_point) is False


def test_validate_number_row_2() -> None:
    check_point = [[2, 85], [2, 86]]
    assert validate_number("input", check_point) is False


def test_validate_row() -> None:
    result = "467......."
    assert validate_row("test_input", 0) == result


def test_number_to_point() -> None:
    check_point = [[0, 0], [0, 1], [0, 2]]
    assert number_to_points("test_input", 0, "467") == check_point


def test_part_one_wrong_answers() -> None:
    assert part_one("input") != 572801
    assert part_one("input") != 552433


def test_part_one() -> None:
    assert part_one("test_input") == 4361
