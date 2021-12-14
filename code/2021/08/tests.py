from aoc_08 import (build_numbers, display_patterns, get_eight, get_four,
                    get_one, get_seven, observations_len_5, part_one, part_two,
                    read_file, solve_display)


def test_set0_has_6_characters():
    assert len(display_patterns[0]) == 6


def test_set1_has_2_characters():
    assert len(display_patterns[1]) == 2


def test_set2_has_5_characters():
    assert len(display_patterns[2]) == 5


def test_set3_has_5_characters():
    assert len(display_patterns[3]) == 5


def test_set4_has_4_characters():
    assert len(display_patterns[4]) == 4


def test_set5_has_5_characters():
    assert len(display_patterns[5]) == 5


def test_set6_has_6_characters():
    assert len(display_patterns[6]) == 6


def test_set7_has_3_characters():
    assert len(display_patterns[7]) == 3


def test_set8_has_7_characters():
    assert len(display_patterns[8]) == 7


def test_set9_has_6_characters():
    assert len(display_patterns[9]) == 6


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


