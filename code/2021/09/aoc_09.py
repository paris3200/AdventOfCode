from typing import List

import utils


def get_lowpoints(input) -> List[int]:
    low_points = []
    for y, line in enumerate(input):
        for x, reading in enumerate(line):
            # Top Edge
            if y == 0 and x > 0 and x + 1 < len(line):
                if (
                    line[x - 1] > reading
                    and line[x + 1] > reading
                    and input[y + 1][x] > reading
                ):
                    low_points.append(reading)

            # Top Left Corner
            elif y == 0 and x == 0 and x + 1 < len(line):
                if (
                    line[x + 1] > reading
                    and input[y + 1][x] > reading
                    and input[y + 1][x] > reading
                ):
                    low_points.append(reading)

            # Top Right Corner
            elif y == 0 and x == len(line) - 1:
                if line[x - 1] > reading and input[y + 1][x] > reading:
                    low_points.append(reading)

            # Bottom Edge
            elif y == len(input) - 1 and x > 0 and x + 1 < len(line):
                if (
                    input[y - 1][x] > reading
                    and line[x - 1] > reading
                    and line[x + 1] > reading
                ):
                    low_points.append(reading)

            # Bottom Left Corner
            elif y == len(input) - 1 and x == 0:
                if input[y - 1][x] > reading and line[x + 1] > reading:
                    low_points.append(reading)

            # Bottom Right Corner
            elif y == len(input) - 1 and x == len(line) - 1:
                if input[y - 1][x] > reading and line[x - 1] > reading:
                    low_points.append(reading)

            # Left Edge
            elif 0 < y < len(input) - 1 and x == 0:
                if (
                    input[y - 1][x] > reading
                    and input[y + 1][x] > reading
                    and line[x + 1] > reading
                ):
                    low_points.append(reading)

            # Right Edge
            elif 0 < y < len(input) - 1 and x == len(line) - 1:
                if (
                    input[y - 1][x] > reading
                    and input[y + 1][x] > reading
                    and line[x - 1] > reading
                ):
                    low_points.append(reading)
            # Center
            elif 0 < y < len(input) - 1 and x != len(line) - 1 and x != 0:
                if (
                    input[y - 1][x] > reading
                    and input[y + 1][x] > reading
                    and line[x - 1] > reading
                    and line[x + 1] > reading
                ):
                    low_points.append(reading)

    return low_points


def calculate_risk_level(low_points: List[int]) -> int:
    return sum(low_points) + len(low_points)


def part_one(filename: str) -> List[int]:
    input = utils.read_file_of_ints(filename)
    low_points = get_lowpoints(input)
    risk_level = calculate_risk_level(low_points)
    return [len(low_points), risk_level]
    


def part_two():
    pass


if __name__ == "__main__":
    filename = "data/09.data"
    result = part_one(filename)
    print("Part One")
    print(
        f"A total of {result[0]} were found leading to a risk level of {result[1]}."
    )

    print("Part Two")
    part_two()
