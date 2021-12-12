from typing import Optional, List


display_patterns = []
display_patterns.append({"a", "b", "c", "e", "f", "g"})
display_patterns.append({"c", "f"})
display_patterns.append({"a", "c", "d", "e", "g"})
display_patterns.append({"a", "c", "d", "f", "g"})
display_patterns.append({"b", "c", "d", "f"})
display_patterns.append({"a", "b", "d", "f", "g"})
display_patterns.append({"a", "b", "d", "e", "f", "g"})
display_patterns.append({"a", "c", "f"})
display_patterns.append({"a", "b", "c", "d", "e", "f", "g"})
display_patterns.append({"a", "b", "c", "d", "f", "g"})


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
