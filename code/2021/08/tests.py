import pytest

from aoc_08 import (
    Display,
    get_eight,
    get_four,
    get_one,
    get_seven,
    observations_len_5,
    part_one,
    part_two,
    read_file,
    solve_display,
)


def test_get_four():
    input = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split()
    result = get_four(input)

    assert result == "cgeb"


def test_get_one():
    input = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split()
    result = get_one(input)

    assert result == "be"


def test_get_seven():
    input = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split()
    result = get_seven(input)

    assert result == "edb"


def test_get_eight():
    input = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split()
    result = get_eight(input)

    assert result == "cfbegad"


def test_read_file():
    data = "data/08_test.data"
    result = read_file(data)

    observations = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split()
    readings = "fdgacbe cefdb cefbgd gcbe".split()

    assert result[0][0] == observations
    assert result[0][1] == readings


def test_part_one_with_test_data():
    data = "data/08_test.data"
    result = part_one(data)

    assert result == 26


def test_observations_len_5():
    data = "data/08_test.data"
    observations = read_file(data)

    result = observations_len_5(observations[0][0])
    expected = ["fdcge", "fecdb", "fabcd"]
    assert result == expected


def test_solve_display():
    observations = [
        "acedgfb",
        "cdfbe",
        "gcdfa",
        "fbcad",
        "dab",
        "cefabd",
        "cdfgeb",
        "eafb",
        "cagedb",
        "ab",
    ]
    readings = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]

    result = solve_display([observations, readings])
    expected = {
        "a": "d",
        "b": "a",
        "c": "b",
        "d": "c",
        "e": "g",
        "f": "e",
        "g": "f",
    }
    assert result == expected


def test_solve_display_test_data_line_1():
    observations = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split()
    readings = ["fdgacbe", "cefdb", "cefbgd", "gcbe"]

    mapping = solve_display([observations, readings])
    display = Display(mapping)
    result = display.convert_to_int(readings)
    assert result == 8394


def test_solve_display_test_data_line_3():
    observations = "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef ".split()
    readings = ["cg", "cg", "fdcagb",  "cbg"]


    mapping = solve_display([observations, readings])
    display = Display(mapping)
    result = display.convert_to_int(readings)
    assert result == 1197


def test_display_convert_to_int():
    readings = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]
    mapping = {
        "a": "d",
        "b": "a",
        "c": "b",
        "d": "c",
        "e": "g",
        "f": "e",
        "g": "f",
    }
    display = Display(mapping)
    result = display.convert_to_int(readings)
    assert result == 5353

def test_part_two_with_test_data():
    filename = "data/08_test.data"
    result = part_two(filename)

    assert result == 61229


def test_part_two_with_problem_data():
    filename = "data/08.data"
    result = part_two(filename)

    assert result == 1070188
