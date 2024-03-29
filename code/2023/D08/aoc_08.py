from dataclasses import dataclass
from math import lcm
from itertools import cycle


@dataclass
class Node:
    label: str
    left: str
    right: str


def create_nodes(lines: list[str]) -> list[Node]:
    nodes = []
    for line in lines:
        label = line[:3]
        left = line[7:10]
        right = line[12:15]

        nodes.append(Node(label, left, right))
    return nodes


def replace_with_index(nodes: list[Node]) -> list[Node]:
    for node in nodes:
        left = get_node_index(nodes, node.left)
        right = get_node_index(nodes, node.right)
        node.left = left
        node.right = right

    return nodes


def get_Node(nodes: list[Node], label: str) -> Node:
    for node in nodes:
        if node.label == label:
            return node


def get_node_index(nodes: list[Node], label: str) -> int:
    for index, node in enumerate(nodes):
        if node.label == label:
            return index


def get_starting_nodes(nodes: list[Node]) -> list[Node]:
    starting_nodes = []
    for node in nodes:
        if node.label[2] == "A":
            starting_nodes.append(node)
    return starting_nodes


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def solve_loop(instructions: list[str], nodes: list[Node], starting_node: Node) -> int:
    pool = cycle(instructions)
    result = ""
    current_node = starting_node
    counter = 0
    while result != "Z":
        instruction = next(pool)
        if instruction == "L":
            next_node = current_node.left
        elif instruction == "R":
            next_node = current_node.right

        current_node = nodes[next_node]
        result = current_node.label[2]
        counter += 1
    return counter


def part_one(filename: str):
    lines = read_lines(filename)

    instructions = []
    for instruction in lines.pop(0):
        instructions.append(instruction)

    nodes = create_nodes(lines)
    pool = cycle(instructions)

    current_node = get_Node(nodes, "AAA")
    counter = 0
    while current_node.label != "ZZZ":
        # print(current_node.label)
        instruction = next(pool)
        if instruction == "L":
            next_node = current_node.left
        elif instruction == "R":
            next_node = current_node.right
        # print(f"Instruction: {instruction}")

        current_node = get_Node(nodes, next_node)
        # print(f"Next Node: {current_node}")
        counter += 1

    return counter


def part_two(filename: str):
    lines = read_lines(filename)

    instructions = []
    for instruction in lines.pop(0):
        instructions.append(instruction)

    nodes = replace_with_index(create_nodes(lines))
    start_nodes = get_starting_nodes(nodes)

    loop_result = []
    for node in start_nodes:
        loop_result.append(solve_loop(instructions, nodes, node))
    return lcm(
        loop_result[0],
        loop_result[1],
        loop_result[2],
        loop_result[3],
        loop_result[4],
        loop_result[5],
    )


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
