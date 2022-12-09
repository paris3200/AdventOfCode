from d08 import Map, part_one, part_two
from parser import Parser


def test_grid_dimensions() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())

    assert map.get_dimensions(parser.get_lines()) == [5, 5]


grid = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]


def test_map_init() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())

    assert map.grid == grid


def test_is_visible_is_true_for_edges() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())

    assert map.is_visible(0, 0) is True
    assert map.is_visible(0, 4) is True
    assert map.is_visible(4, 0) is True
    assert map.is_visible(4, 4) is True
    assert map.is_visible(0, 2) is True
    assert map.is_visible(4, 2) is True


def test_is_visible_for_interior() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())

    assert map.is_visible(3, 1) is False
    assert map.is_visible(1, 3) is False
    assert map.is_visible(3, 3) is False


def test_row_visible() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())

    assert map.row_visible(1, 1) is True
    assert map.row_visible(3, 1) is False
    assert map.row_visible(1, 2) is True
    assert map.row_visible(1, 3) is False


def test_get_column() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())
    expected = [7, 1, 3, 4, 9]

    assert map.get_column(3, 1) == expected


def test_is_coumn_visible() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())

    assert map.column_visible(1, 1) is True


def test_part_one() -> None:
    assert part_one("data/test_input") == 21


def test_scenic_horizontal() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())

    assert map.scenic_score_horizontal(2, 3) == 4
    assert map.scenic_score_horizontal(2, 1) == 2


def test_scenic_vertical() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())

    assert map.scenic_score_vertical(2, 3) == 2
    assert map.scenic_score_vertical(2, 1) == 2



def test_scenic_score() -> None:
    parser = Parser("data/test_input")
    map = Map(parser.get_lines())

    assert map.scenic_score(2, 3) == 8
    assert map.scenic_score(2, 1) == 4



def test_part_two() -> None:
    assert part_two("data/test_input") == 8
