from aoc_11 import create_grid


def test_grid_expansion_count() -> None:
    grid = create_grid("test_input")
    grid.get_rows_to_expand()
    grid.get_columns_to_expand()
    point1 = grid.find_point("1")
    point2 = grid.find_point("7")

    assert grid.get_expansion_count(point1, point2) == [1, 2]


def test_get_rows_to_expand() -> None:
    grid = create_grid("test_input")
    grid.get_rows_to_expand()

    assert grid.expand_rows == [3, 7]


def test_get_columns_to_expand() -> None:
    grid = create_grid("test_input")
    grid.get_columns_to_expand()

    assert grid.expand_columns == [2, 5, 8]
