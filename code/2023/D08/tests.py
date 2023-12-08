from aoc_08 import part_one, get_starting_nodes, read_lines, create_nodes, part_two


def test_part_one_test_input() -> None:
    assert part_one("test_input") == 2
    assert part_one("test_input_2") == 6
    assert part_one("input") == 21389


def test_get_starting_nodes() -> None:
    lines = read_lines("test_input_3")
    lines.pop(0)

    nodes = create_nodes(lines)
    start_nodes = get_starting_nodes(nodes)
    labels = []
    for node in start_nodes:
        labels.append(node.label)

    assert labels == ["11A", "22A"]


def test_part_two() -> None:
    assert part_two("input") == 21083806112641
