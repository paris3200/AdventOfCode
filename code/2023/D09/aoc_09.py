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
    return node2 - node1


def solve_missing(num1: int, result: int) -> int:
    return result + num1


def reduce_sequence(sequence: list[int]) -> list[int]:
    solved_sequence = []
    for x, y in pairwise(sequence):
        solved_sequence.append(get_node_difference(x, y))
    return solved_sequence


def solve_sequence(sequence: list[int]) -> list[list[int]]:
    solved_sequence = [sequence]
    while True:
        reduced_sequence = reduce_sequence(solved_sequence[-1])
        solved_sequence.append(reduced_sequence)

        if set(solved_sequence[-1]) == {0}:
            return solved_sequence


def solve_sequence_up(sequences: list[list[int]]) -> list[list[int]]:
    end_index = len(sequences) - 1
    sequences[end_index].append(0)
    for index in range(end_index, -1, -1):
        if index != end_index:
            solution = solve_missing(sequences[index + 1][-1], sequences[index][-1])
            sequences[index].append(solution)

    return sequences


def print_sequence(sequences: list[list[int]]) -> None:
    for index, sequence in enumerate(sequences):
        list_str = map(str, sequence)
        line = " ".join(list(list_str))
        shift = " " * index
        print(shift + line)
    print(" ")


def write_sequence(sequences: list[list[int]]) -> None:
    with open("discovery_text", "a") as file:
        for index, sequence in enumerate(sequences):
            list_str = map(str, sequence)
            line = " ".join(list_str)
            shift = " " * index
            file.write(shift + line)
            file.write("\n")
        file.write("\n")


def process_input(lines: list[str]) -> None:
    sequences = []
    for line in lines:
        num = line.split(" ")
        sequences.append(list(map(int, num)))
    return sequences


def part_one(filename: str):
    sequences = process_input(read_lines(filename))
    solved_sequences = []
    for sequence in sequences:
        solution = solve_sequence(sequence)
        # write_sequence(solution)
        solved_sequences.append(solution)

    final_sequences = []
    for sequence in solved_sequences:
        solution = solve_sequence_up(sequence)
        # write_sequence(solution)
        final_sequences.append(solution)

    values = []
    for sequence in final_sequences:
        values.append(sequence[0][-1])

    return sum(values)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
