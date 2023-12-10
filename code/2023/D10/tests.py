from aoc_10 import read_lines, get_next_node, create_grid, part_one


def test_get_next_node() -> None:
    grid = create_grid("test_input")

    point = get_next_node(grid, 1, 2, [1, 1])
    assert point == [[1, 3]]

    point = get_next_node(grid, 1, 3, [1, 2])
    assert point == [[2, 3]]

    point = get_next_node(grid, 2, 1, [1, 1])
    assert point == [[3, 1]]

    point = get_next_node(grid, 2, 1, [1, 1])
    assert point == [[3, 1]]


def test_get_next_node_input() -> None:
    grid = create_grid("input")
    point = get_next_node(grid, 35, 117, [36, 117])
    assert point == [[35, 118]]


def test_part_1_real_input() -> None:
    assert part_one("input") < 6691
    assert part_one("input") == 6690
    assert part_one("test_input") == 4
