from itertools import pairwise


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def get_node_difference(node1: int, node2: int) -> int:
    return abs(node2 - node1)


def reduce_sequence(sequence: list[int]) -> list[int]:
    solved_sequence = []
    for x, y in pairwise(sequence):
        solved_sequence.append(get_node_difference(x, y))

    return solved_sequence


def solve_sequence(sequence: list[list[int]]) -> list[list[int]]:
    while set(sequence[-1]) != {0}:
        sequence.append(reduce_sequence(sequence[-1]))

    return sequence


def print_sequence(sequences: list[list[int]]) -> None:
    for index, sequence in enumerate(sequences):
        list_str = map(str, sequence)
        line = ' '.join(list(list_str))
        shift = ' ' * index
        print(shift + line)
    print(" ")


def process_input(lines: list[str]) -> None:
    sequences = []
    for line in lines:
        line = line.split(" ")
        sequences.append(list(map(int, line)))
    return sequences


def part_one(filename: str):
    sequences = process_input(read_lines(filename))

    for sequence in sequences:
        print_sequence(solve_sequence([sequence]))
        break


def part_two(filename: str):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("test_input"))

    print("Part Two")
    print(part_two("input"))
