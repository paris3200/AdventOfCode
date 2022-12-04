import math

CHUNKS = {"(": ")", "[": "]", "{": "}", "<": ">"}

VALUES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

COMPLETE_VALUES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def get_lines(path: str) -> str:
    with open(path) as input:
        data = input.readlines()

    lines = []
    for line in data:
        lines.append(line.strip())

    return lines


def get_key(val):
    for key, value in CHUNKS.items():
        if val == value:
            return key

    return "key doesn't exists"


def is_valid(line: str) -> bool | str:
    open = []
    for char in line:
        if char in CHUNKS.keys():
            open.append(char)
        elif char in CHUNKS.values():
            if open.pop() != get_key(char):
                return char

    return True


def complete_lines(line: str) -> str:
    open = []
    for char in line:
        if char in CHUNKS.keys():
            open.append(char)
        elif char in CHUNKS.values():
            open.pop()

    completion = ""
    for char in reversed(open):
        completion += CHUNKS[char]
    return completion


def part_one(path="data/input"):
    lines = get_lines(path)

    sum = 0
    for line in lines:
        char = is_valid(line)
        if char is not True:
            sum += VALUES[char]

    return sum


def score_autocomplete(completion: str) -> int:
    sum = 0

    for char in completion:
        sum = sum * 5 + COMPLETE_VALUES[char]

    return sum


def part_two(path="data/input"):
    lines = get_lines(path)

    scores = []
    for line in lines:
        if is_valid(line) is True:
            scores.append(score_autocomplete(complete_lines(line)))

    scores.sort()
    index = math.trunc(len(scores)/2)
    return scores[index]


if __name__ == "__main__":
    print("Part One")
    print(part_one())

    print("Part Two")
    print(part_two())
