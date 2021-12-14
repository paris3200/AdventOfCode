from typing import List, Optional, Dict


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
    Get all observations that are 5 characters long.


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


def read_file(filename) -> List[str]:
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


def part_two():
    pass


if __name__ == "__main__":
    filename = "data/08.data"
    print("Part One")
    count = part_one(filename)
    print(f"In the output values, 1, 4, 7, 8 appear:  {count} times")

    print("Part Two")
    part_two()
