from typing import Dict, List, Optional


class Display:
    def __init__(self, mapping: Dict[str, str]) -> None:
        self.map = mapping

        self.numbers = {}
        self.numbers[0] = set(
            self.map["a"]
            + self.map["b"]
            + self.map["c"]
            + self.map["d"]
            + self.map["e"]
            + self.map["f"]
        )
        self.numbers[1] = set(self.map["b"] + self.map["c"])
        self.numbers[2] = set(
            self.map["a"]
            + self.map["b"]
            + self.map["d"]
            + self.map["e"]
            + self.map["g"]
        )
        self.numbers[3] = set(
            self.map["a"]
            + self.map["b"]
            + self.map["c"]
            + self.map["d"]
            + self.map["g"]
        )
        self.numbers[4] = set(
            self.map["b"] + self.map["c"] + self.map["f"] + self.map["g"]
        )
        self.numbers[5] = set(
            self.map["a"]
            + self.map["c"]
            + self.map["d"]
            + self.map["f"]
            + self.map["g"]
        )
        self.numbers[6] = set(
            self.map["a"]
            + self.map["c"]
            + self.map["d"]
            + self.map["e"]
            + self.map["f"]
            + self.map["g"]
        )
        self.numbers[7] = set(self.map["a"] + self.map["b"] + self.map["c"])
        self.numbers[8] = set(
            self.map["a"]
            + self.map["b"]
            + self.map["c"]
            + self.map["d"]
            + self.map["e"]
            + self.map["f"]
            + self.map["g"]
        )
        self.numbers[9] = set(
            self.map["a"]
            + self.map["b"]
            + self.map["c"]
            + self.map["d"]
            + self.map["f"]
            + self.map["g"]
        )

    def convert_to_int(self, output: List[str]) -> int:
        displayed_number = ""
        for num in output:
            num = set(list(num))
            for key, value in self.numbers.items():
                if num == value:
                    displayed_number += str(key)
        return int(displayed_number)


def get_one(input: list) -> Optional[str]:
    for segment in input:
        if len(segment) == 2:
            return segment
    return None


def get_four(input: list) -> Optional[str]:
    for segment in input:
        if len(segment) == 4:
            return segment
    return None


def get_seven(input: list) -> Optional[str]:
    for segment in input:
        if len(segment) == 3:
            return segment
    return None


def get_eight(input: list) -> Optional[str]:
    for segment in input:
        if len(segment) == 7:
            return segment
    return None


def observations_len_5(input: List[str]) -> List[str]:
    """
    Get all observations that could be 5, 3, or 2.


    Parameters
    ----------
    input : List[str]
        All of the observations.

    Returns
    -------
    List[str]
        The options with a length of 5.
    """
    possibles = []
    for segment in input:
        if len(segment) == 5:
            possibles.append(segment)

    return possibles


def solve_display(input: List[List[str]]) -> Dict[str, str]:
    top = {"a", "b", "c", "d", "e", "f", "g"}
    topl = {"a", "b", "c", "d", "e", "f", "g"}
    topr = {"a", "b", "c", "d", "e", "f", "g"}
    middle = {"a", "b", "c", "d", "e", "f", "g"}
    bottoml = {"a", "b", "c", "d", "e", "f", "g"}
    bottomr = {"a", "b", "c", "d", "e", "f", "g"}
    bottom = {"a", "b", "c", "d", "e", "f", "g"}

    # Solve top if 1 and 7 present
    seven = get_seven(input[0])
    one = get_one(input[0])
    four = get_four(input[0])
    if seven and one and four:
        seven = set(list(seven))
        one = set(list(one))

        # Top Solved
        top = seven.difference(one)

        # Right side narrowed down
        topr = set(list(one))
        bottomr = set(list(one))

        # Narrow down topl and middle
        four = set(list(four))
        middle = four.difference(one)
        topl = four.difference(one)

        bottom = bottom.difference(top, topr, bottomr, middle, topl)
        bottoml = bottoml.difference(top, topr, bottomr, middle, topl)

        # Solve 5 and bottoml, bottomr, bottom
        options = []
        # Get possibles for 5, 3, 2
        for option in observations_len_5(input[0]):
            options.append(set(list(option)))

        for option in options:
            # If true, the option is number 5
            if (
                len(bottomr.intersection(option)) == 1
                and len(bottom.intersection(option)) == 1
                and len(topl.intersection(option)) == 2
            ):
                diff = option.difference(top, topl, middle, bottom)
                bottomr = diff
                topr = topr.difference(bottomr)
                bottom = option.difference(top, topl, middle, bottomr)
                bottoml = bottoml.difference(bottom)
                break

        # Get possibles for 5, 3, 2
        for option in observations_len_5(input[0]):
            options.append(set(list(option)))

        for option in options:
            # If true, option is number 2
            if (
                len(option.intersection(middle)) == 1
                and len(option.intersection(bottomr)) == 0
                and not (
                    # Not Number 5
                    len(bottomr.intersection(option)) == 1
                    and len(bottom.intersection(option)) == 1
                    and len(topl.intersection(option)) == 2
                )
            ):
                middle = option.difference(top, topr, bottoml, bottom)
                topl = topl.difference(middle)

        mapping = {
            "a": "".join(top),
            "b": "".join(topr),
            "c": "".join(bottomr),
            "d": "".join(bottom),
            "e": "".join(bottoml),
            "f": "".join(topl),
            "g": "".join(middle),
        }

        return mapping


def read_file(filename) -> List[List[str]]:
    with open(filename, "r") as contents:
        readings = []
        for line in contents:
            data = line.strip()
            data = data.split(" | ")
            observations = data[0].split()
            output = data[1].split()
            readings.append([observations, output])

    return readings


def get_occurances(data) -> int:
    occurances = 0

    for line in data:
        for observation in line[1]:
            if (
                len(observation) == 3
                or len(observation) == 7
                or len(observation) == 4
                or len(observation) == 2
            ):
                occurances += 1

    return occurances


def part_one(filename: str) -> int:
    readings = read_file(filename)
    return get_occurances(readings)


def part_two(filename: str) -> int:
    sum_output = 0
    readings = read_file(filename)
    for line in readings:
        mapping = solve_display(line)
        display = Display(mapping)
        sum_output += display.convert_to_int(line[1])
    return sum_output


if __name__ == "__main__":
    filename = "data/08.data"
    print("Part One")
    count = part_one(filename)
    print(f"In the output values, 1, 4, 7, 8 appear:  {count} times")

    print("Part Two")
    print(f"The sum of the output values: {part_two(filename)}")
