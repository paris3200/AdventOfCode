def read_lines(filename: str) -> list[int]:
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = int(line.rstrip().strip("\n"))
    return data


def part_one(filename: str):
    instructions = read_lines(filename)
    counter = 0
    current_index = 0

    while current_index < len(instructions):
        jump = current_index + instructions[current_index]
        instructions[current_index] += 1
        current_index = jump
        counter += 1

    return counter


def part_two(filename: str):
    instructions = read_lines(filename)
    counter = 0
    current_index = 0

    while current_index < len(instructions):
        jump = current_index + instructions[current_index]
        if instructions[current_index] >= 3:
            instructions[current_index] -= 1
        else:
            instructions[current_index] += 1
        current_index = jump
        counter += 1

    return counter


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
