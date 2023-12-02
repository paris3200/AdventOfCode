from typing import List


def read_lines(filename: str) -> list[int]:
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")

    memory_banks = data[0].split("\t")

    input_bank: List[int] = []
    for value in memory_banks:
        input_bank.append(int(value))

    return input_bank


def redistribute(memory_banks: List[int]) -> List[int]:
    max_index = memory_banks.index(max(memory_banks))
    stack = memory_banks[max_index]
    memory_banks[max_index] = 0

    last_index = len(memory_banks) - 1
    current_index = max_index
    if max_index >= last_index:
        current_index = 0
    else:
        current_index += 1

    while stack > 0:
        memory_banks[current_index] += 1
        if current_index >= last_index:
            current_index = 0
        else:
            current_index += 1

        stack -= 1
    return memory_banks


def part_one(filename: str) -> int:
    memory_bank = read_lines(filename)
    counter = 1
    results: List[List[int]] = list()

    while True:
        resulted_bank = redistribute(memory_bank)
        for result in results:
            if result == resulted_bank:
                return counter
        results.append(resulted_bank.copy())
        memory_bank = resulted_bank
        counter += 1


def part_two(filename: str) -> int:
    memory_bank = read_lines(filename)
    counter = 0
    results: List[List[int]] = list()

    while True:
        resulted_bank = redistribute(memory_bank)
        for result in results:
            if result == resulted_bank:
                first_occurance = results.index(result)
                return counter - first_occurance
        results.append(resulted_bank.copy())
        memory_bank = resulted_bank
        counter += 1


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
