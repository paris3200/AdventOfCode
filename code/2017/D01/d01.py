def read_lines(filename):
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")
    return data


def part_one(input: str) -> int:
    matches = []
    values = []
    for value in list(input):
        values.append(int(value))

    last = len(values)

    for count, value in enumerate(values):
        if count+1 != last:
            next_value = values[count+1]
        else:
            next_value = values[0]

        if value == next_value:
            matches.append(value)

    return sum(matches)


def part_two(input: str) -> int:
    matches = []
    values = []
    for value in list(input):
        values.append(int(value))

    step = int(len(values)/2)
    value_length = len(values)

    for count, value in enumerate(values):
        remainder = (step+count) % value_length

        if value == values[remainder]:
            matches.append(value)

    return sum(matches)


if __name__ == "__main__":
    line = read_lines("input")
    print(part_one(line[0]))
    print(part_two(line[0]))
