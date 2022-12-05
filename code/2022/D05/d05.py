import pprint


def get_lines(data) -> str:
    with open(data) as input:
        data = input.readlines()

    lines = []
    for line in data:
        if line[0] == "m":
            line = line.strip()
            line = line.replace("move", "")
            line = line.replace("from", ",")
            line = line.replace("to", ",")
            line = line.replace(" ", "")
            line = line.split(",")
            instruction = []

            for item in line:
                if item != ",":
                    instruction.append(int(item))
            lines.append(instruction)

    return lines


class CargoHold:
    def __init__(self, type="input") -> None:
        self.stacks = {}
        if type == "test":
            self.stacks[1] = ["Z", "N"]
            self.stacks[2] = ["M", "C", "D"]
            self.stacks[3] = ["P"]

        if type == "input":
            self.stacks[1] = ["R", "N", "F", "V", "L", "J", "S", "M"]
            self.stacks[2] = ["P", "N", "D", "Z", "F", "J", "W", "H"]
            self.stacks[3] = ["W", "R", "C", "D", "G"]
            self.stacks[4] = ["N", "B", "S"]
            self.stacks[5] = ["M", "Z", "W", "P", "C", "B", "F", "N"]
            self.stacks[6] = ["P", "R", "M", "W"]
            self.stacks[7] = ["R", "T", "N", "G", "L", "S", "W"]
            self.stacks[8] = ["Q", "T", "H", "F", "N", "B", "V"]
            self.stacks[9] = ["L", "M", "H", "Z", "N", "F"]

    def move_crates(self, count: int, start_stack: int, end_stack: int) -> None:
        while count > 0:
            self.stacks[end_stack].append(self.stacks[start_stack].pop())
            count -= 1

    def move_stack(self, count: int, start_stack: int, end_stack: int) -> None:
        stack = self.stacks[start_stack][-count:]

        while count > 0:
            self.stacks[start_stack].pop()
            count -= 1

        for item in stack:
            self.stacks[end_stack].append(item)

    def top_crates(self) -> str:
        top_crates = ""
        for count, stack in self.stacks.items():
            top_crates += stack[-1]

        return top_crates

    def __repr__(self) -> str:
        output = ""
        for key, stack in self.stacks.items():
            output += f"{key}: {stack}\n"
        return output


def part_one():
    lines = get_lines("input")
    cargo = CargoHold(type="input")
    for line in lines:
        try:
            quantity, start, stop = line
        except ValueError:
            print(f"Error: {line}")

        cargo.move_crates(quantity, start, stop)

    print(cargo.top_crates())


def part_two():
    lines = get_lines("input")
    cargo = CargoHold(type="input")
    for line in lines:
        try:
            quantity, start, stop = line
        except ValueError:
            print(f"Error: {line}")

        cargo.move_stack(quantity, start, stop)

    print(cargo.top_crates())


if __name__ == "__main__":
    part_one()
    part_two()
