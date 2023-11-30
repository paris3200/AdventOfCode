def validate_passphrase(passphrase: str) -> bool:
    passphrase_list = passphrase.split(" ")
    passphrase_set = set(passphrase_list)

    if len(passphrase_list) == len(passphrase_set):
        return True

    return False


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")
    return data


def part_one(filename: str) -> int:
    lines = read_lines(filename)
    counter = 0
    for line in lines:
        if validate_passphrase(line) is True:
            counter += 1

    return counter


def part_two():
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    part_two()
