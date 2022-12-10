import pytest

from parser import Parser
from d09 import Rope, part_one


def test_calculate_limits() -> None:
    parser = Parser("data/test_input")

    assert parser.calculate_limits(parser.get_lines()) == [6, 5]


def test_move_right() -> None:
    rope = Rope()
    rope.move_right(4)
    assert rope.tail_visted == [[0, 0], [1, 0], [2, 0], [3, 0]]
    assert rope.head == [4, 0]
    assert rope.tail == [3, 0]


def test_move_up() -> None:
    rope = Rope()
    rope.tail = [3, 0]
    rope.head = [4, 0]
    rope.tail_visted = []
    rope.move_up(4)

    assert rope.tail_visted == [[4, 1], [4, 2], [4, 3]]
    assert rope.head == [4, 4]
    assert rope.tail == [4, 3]


def test_is_diagonal() -> None:
    rope = Rope()
    rope.head = [4, 1]
    rope.tail = [3, 0]
    assert rope.is_diagnoal(rope.head, rope.tail) is True

    rope.head = [4, 1]
    rope.tail = [4, 0]
    assert rope.is_diagnoal(rope.head, rope.tail) is False

    rope.head = [4, 0]
    rope.tail = [3, 0]
    assert rope.is_diagnoal(rope.head, rope.tail) is False


def test_is_touching() -> None:
    rope = Rope()
    rope.head = [4, 0]
    rope.tail = [3, 0]
    assert rope.is_touching() is True

    rope.head = [2, 0]
    rope.tail = [0, 0]
    assert rope.is_touching() is False

    rope.head = [2, 0]
    rope.tail = [2, 0]
    assert rope.is_touching() is True

    rope.head = [2, 3]
    rope.tail = [2, 4]
    assert rope.is_touching() is True


def test_part_one() -> None:
    assert part_one("data/test_input") == 13
