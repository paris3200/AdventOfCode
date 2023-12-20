from dataclasses import dataclass
import re


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int


def format_conditional(conditional: str) -> str:
    if "x" in conditional:
        conditional = conditional.replace("x", "part.x")
    elif "m" in conditional:
        conditional = conditional.replace("m", "part.m")
    elif "a" in conditional:
        conditional = conditional.replace("a", "part.a")
    elif "s" in conditional:
        conditional = conditional.replace("s", "part.s")
    return conditional


def create_part(description: str) -> str:
    values = description.split(",")
    ratings = []
    pattern = r"\d+"
    for value in values:
        ratings.append(re.findall(pattern, value)[0])

    return f"Part(x={ratings[0]}, m={ratings[1]}, a={ratings[2]}, s={ratings[3]})"


def create_function(workflow: str) -> str:
    name = workflow.split("{")[0]  # } Needed for treesitter to format properly
    instructions = workflow[(len(name) + 1): -1]
    instructions = instructions.split(",")

    if name == "in":
        name = "start"
    function_list = []
    function_list.append(f"def {name}(part: Part) -> bool:\n")
    for instruction in instructions:
        if ":" in instruction:
            condition, result = instruction.split(":")
            condition = format_conditional(condition)

            function_list.append(f"  if {condition}:\n")

            if result == "A":
                function_list.append("    return True\n")
            elif result == "R":
                function_list.append("    return False\n")
            else:
                function_list.append(f"    return {result}(part)\n")

        elif instruction == "A":
            function_list.append("  return True\n")
        elif instruction == "R":
            function_list.append("  return False\n")
        else:
            function_list.append(f"  return {instruction}(part)\n")

    function_list.append("\n\n")
    function_str = "".join(function_list)
    return function_str


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def part_one(filename: str) -> int:
    lines = read_lines(filename)

    compiled_code = []
    parts = []
    for line in lines:
        if line[0] != "{":  # }
            compiled_code.append(create_function(line))
        if line[0] == "{":  # }
            part = line[1:-1]
            parts.append(create_part(part))

    with open("compiled_code.py", "w") as file:
        file.write("from aoc_19 import Part\n\n\n")
        for funct in compiled_code:
            file.write(funct)

        file.write('if __name__ == "__main__":\n')
        file.write("\n\n  parts = []\n")
        for part in parts:
            file.write(f"  parts.append({part})\n")

    # parts = []
    # parts.append(Part(x=787, m=2655, a=1222, s=2876))
    # parts.append(Part(x=1679, m=44, a=2067, s=496))
    # parts.append(Part(x=2036, m=264, a=79, s=2244))
    # parts.append(Part(x=2461, m=1339, a=466, s=291))
    # parts.append(Part(x=2127, m=1623, a=2188, s=1013))
    #
    # accepted_parts = []
    # for part in parts:
    #     if start(part) is True:
    #         accepted_parts.append(part.x + part.m + part.a + part.s)
    #
    # print(sum(accepted_parts))


def part_two(filename: str):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    # print("Part Two")
    # print(part_two("input"))
