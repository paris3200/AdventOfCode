from aoc_08 import (
    get_eight,
    get_four,
    get_one,
    get_seven,
    observations_len_5,
    part_one,
    part_two,
    read_file,
    solve_display,
    Display,
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
