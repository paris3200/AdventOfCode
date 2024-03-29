from aoc_09 import get_node_difference, reduce_sequence, part_one, solve_missing


def test_node_difference() -> None:
    assert get_node_difference(3, 6) == 3


def test_node_difference_with_negative_result() -> None:
    assert get_node_difference(0, 2) == 2
    assert get_node_difference(-101, -96) == 5


def test_solve_missting() -> None:
    assert solve_missing(-5, -101) == -106


def test_reduce_sequence() -> None:
    input_sequence = [0, 3, 6, 9, 12, 15]
    result_sequence = [3, 3, 3, 3, 3]
    assert reduce_sequence(input_sequence) == result_sequence


def test_part_one_test_input() -> None:
    assert part_one("test_input") == 114
    assert part_one("input") > 1679257426  # Too Low
