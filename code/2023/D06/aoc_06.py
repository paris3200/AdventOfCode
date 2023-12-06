import re

def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def get_number_wins(time: int, record: int) -> None:
    wins = []
    for x in range(1, time+1):
        d = x * (time - x)
        if d > record:
            wins.append(x)

    return len(wins)


def part_one(filename: str):
    lines = read_lines(filename)

    pattern = re.compile(r"[0-9]+")
    time_str = pattern.findall(lines[0])
    dist_str = pattern.findall(lines[1])

    times = list(map(int, time_str))
    record = list(map(int, dist_str))

    moe = 1
    for index, time in enumerate(times):
        moe = moe * get_number_wins(time, record[index])

    return moe



def part_two(filename: str):
    lines = read_lines(filename)

    pattern = re.compile(r"[0-9]+")
    time_str = pattern.findall(lines[0])
    dist_str = pattern.findall(lines[1])

    time = int(''.join(time_str))
    dist = int(''.join(dist_str))

    moe = get_number_wins(time, dist)

    return moe

if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
