from aoc_13 import create_grid, check_horizontal


def test_check_horizontal() -> None:
    grid = create_grid("test_input")

    assert check_horizontal(grid) == 3

def test_check_get_vertical() -> None:
    grid = create_grid("test_input")
    assert grid.get_column(0) == "##.##.#"
