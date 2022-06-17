import Y2015.utils


def part_one(data):
    input = list(data[0])
    floor = 0
    for instruction in input:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
    return floor



def part_two(data):
    input = list(data[0])
    floor = 0
    for i, instruction in enumerate(input):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1

        if floor == -1:
            return i+1



if __name__ == "__main__":
    data = utils.read_lines("data/01.data")

    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
