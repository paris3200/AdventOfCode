import utils
import pytest


def part_one(data):
    report = utils.read_file(data, "list", False)

    gama = ""
    epislon = ""
    position = flatten_list(report)

    for digit in position:
        gama += most_frequent(digit.copy())
        epislon += least_frequent(digit.copy())

    return convert(gama) * convert(epislon)


def part_two(data):
    report = utils.read_file(data, "list", False)
    oxygen = oxygen_generator_rating(report)
    co2 = co2_scrubber_rating(report)

    return convert(oxygen) * convert(co2)


def oxygen_generator_rating(input, digitplace=0):
    position = flatten_list(input)
    max = most_frequent(position[digitplace])

    if max == "-":
        keep_digit = "1"
    else:
        keep_digit = max

    keep_list = filter_list(input, digitplace, keep_digit)
    if len(keep_list) == 1:
        return keep_list[0]
    else:
        return oxygen_generator_rating(keep_list, digitplace + 1)


def co2_scrubber_rating(input, digitplace=0):
    position = flatten_list(input)
    min = least_frequent(position[digitplace])

    if min == "-":
        keep_digit = "0"
    else:
        keep_digit = min

    keep_list = filter_list(input, digitplace, keep_digit)

    if len(keep_list) == 1:
        return keep_list[0]
    else:
        return co2_scrubber_rating(keep_list, digitplace + 1)


def flatten_list(rawlist):
    position = []
    for x in range(0, len(rawlist[0])):
        position.append([])

    for reading in rawlist:
        for i, value in enumerate(list(reading)):
            position[i].append(value)

    return position


def filter_list(rawlist, place, digit):
    """Returns sublist of rawlist that matches the digit in the place defined by place."""
    filtered_list = []
    for item in rawlist:
        if item[place] == digit:
            filtered_list.append(item)
    return filtered_list


def most_frequent(input):
    """Returns the most frequently occuring item on a list."""
    on = 0
    off = 0
    for x in input:
        if x == "1":
            on += 1
        else:
            off += 1

    if on == off:
        return "-"
    elif on > off:
        return "1"
    else:
        return "0"


def least_frequent(input):
    """Returns the least frequently occuring item on a list."""
    on = 0
    off = 0
    for x in input:
        if x == "1":
            on += 1
        else:
            off += 1

    if on == off:
        return "-"
    elif on > off:
        return "0"
    else:
        return "1"


def convert(binary):
    """Return converted binary string to an int."""
    return int(binary, 2)


def test_filter_list():
    data = "data/03_test.data"
    rawlist = utils.read_file(data, "list", False)
    result = filter_list(rawlist, 0, "1")
    solution = ["11110", "10110", "10111", "10101", "11100", "10000", "11001"]
    assert solution == result

    rawlist = ["10110", "10111"]
    result = filter_list(rawlist, 4, "1")
    assert ["10111"] == result


def test_oxygen_generator_rating():
    input = ["10110", "10111"]
    assert oxygen_generator_rating(input, 4) == "10111"

    data = "data/03_test.data"
    input = utils.read_file(data, "list", False)
    assert (
        oxygen_generator_rating(
            input,
        )
        == "10111"
    )

    data = "data/03_test_2.data"
    input = utils.read_file(data, "list", False)
    assert (
        oxygen_generator_rating(
            input,
        )
        == "1111"
    )


def test_co2_scrubber_rating():
    data = "data/03_test.data"
    input = utils.read_file(data, "list", False)
    assert (
        co2_scrubber_rating(
            input,
        )
        == "01010"
    )

    data = "data/03_test_2.data"
    input = utils.read_file(data, "list", False)
    assert (
        co2_scrubber_rating(
            input,
        )
        == "0001"
    )


def test_part_one():
    result = part_one("data/03_test.data")
    assert result == 198

    result = part_one("data/03.data")
    assert result == 3882564


def test_part_two():
    result = part_two("data/03_test.data")
    assert result == 230

    result = part_two("data/03_test_2.data")
    assert result == 15

    result = part_two("data/03.data")
    assert result == 3385170


def test_binary_conversion():
    assert convert("10110") == 22
    assert convert("01001") == 9


if __name__ == "__main__":
    data = "data/03.data"
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
