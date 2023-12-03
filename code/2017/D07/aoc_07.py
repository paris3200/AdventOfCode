from typing import Optional, Self


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")
    return data


class Node:
    def __init__(
        self,
        name: str,
        weight: int,
        children: Optional[list[Self]] = None,
        parent: Optional[Self] = None,
    ) -> None:
        self.name = name
        self.weight = weight

        if not children:
            self.children: list[Self] = list()

        if not parent:
            self.parent: list[Self] = list()


def find_parent(input: list[str], orphan: str) -> str | None:
    for line in input:
        if "->" in line:
            name, children = line.split("->")
            name.strip()
            children.strip()

            if orphan in children:
                return name.split(" ")[0]
    return None


def find_root(lines: list[str]) -> str | None:
    for line in lines:
        name = line.split(" ")[0]

        parent = find_parent(lines, name)
        if not parent:
            return name

    return None


def part_one(filename: str) -> str | None:
    lines = read_lines(filename)
    return find_root(lines)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
