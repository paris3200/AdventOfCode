

def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def hash_char(char: str, current_value: int) -> int:
    ascii = ord(char)
    print(f"\nAscii value of {char}: {ascii}")
    print(f"Add to current_value of {current_value}: {current_value+ascii}")
    current_value += ascii
    current_value = current_value*17
    print(f"Multiply by 17: {current_value}")
    current_value = current_value % 256
    print(f"Modulus of 256: {current_value}")

    return current_value


def part_one(filename: str):
    lines = read_lines(filename)
    sequence = lines[0].split(",")
    current_value = 0

    results = []
    for word in sequence:
        current_value = 0
        for char in word:
            current_value = hash_char(char, current_value)
        results.append(current_value)
        print(f"{word} becomes {current_value}")
    return sum(results)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
