from dataclasses import dataclass
import re


@dataclass
class Record:
    line: str
    count: list[int]

def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def get_input(filename: str):
    lines = read_lines(filename)
    records = []
    for line in lines:
        record, int_str = line.split(" ")
        counts_str = int_str.split(",")
        counts = list(map(int, counts_str))

        records.append(Record(record, counts))

    return records


def solve_record(line, count, result=0) -> str:
    if line == "" and count == []:
        result += 1
        return result
    if line[0] == ".":
        line = line[1:]
        return solve_record(line, count, result)
    if line[0] == "?":
        line = "." + line[1:]
        return solve_record(line, count, result)
    if line[0] == "?":
        line = "#" + line[1:]
        return solve_record(line, count)
    if line[0] == "#":
        breakpoint()
        pattern = r'^[#?]+(?=[^.]*.)'
        matches = re.findall(pattern, line)
        if matches != []:
            if len(matches[0]) == count[0]:
                count.pop()
                return solve_record(line[len(matches[0])-1:], count, result)
            return result



def part_one(filename: str):
    pass


def part_two(filename: str):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
