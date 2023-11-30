def read_lines(filename):
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")
    return data


def convert_line(line: list[str]) -> list[int]:
    converted_line = []
    string_list = line.split("\t")

    for value in string_list:
        converted_line.append(int(value))

    return converted_line


def part_one(lines: list[str]) -> int:
    line_checksums = []
    for line in lines:
        converted_line = convert_line(line)

        line_checksum = max(converted_line) - min(converted_line)
        line_checksums.append(line_checksum)

    return sum(line_checksums)


def part_two(lines: list[str]) -> int:
    line_checksums = []
    for line in lines:
        converted_line = convert_line(line)

        for index, numerator in enumerate(converted_line):
            denominators = converted_line.copy()
            denominators.pop(index)

            for denominator in denominators:
                if numerator % denominator == 0:
                    line_checksums.append(int(numerator / denominator))

    return sum(line_checksums)


if __name__ == "__main__":
    lines = read_lines("input")

    print("Part One")
    print(part_one(lines))

    print("Part Two")
    print(part_two(lines))
