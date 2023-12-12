from aoc_12 import Record, get_input, solve_record


def test_get_input() -> None:
    result = Record("???.###", [1, 1, 3])
    input = get_input("test_input")
    assert input[0] == result


def test_solve_record() -> None:
    record = Record("???.###", [1, 1, 3])
    assert solve_record(record.line, record.count) == 1


def test_solve_record_simple() -> None:
    record = Record(".???", [3])
    assert solve_record(record.line, record.count) == 1
