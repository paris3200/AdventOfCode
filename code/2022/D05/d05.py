class Parser:
    def __init__(self, file):
        self.file = file
        self.name_index = 0
        self.stacks = {}
        for stack in self.get_stack_names():
            self.stacks[stack] = []

        stack_lines = self.get_inital_stacks()
        for line in stack_lines:
            for index, stack in enumerate(list(line)[1::4], 1):
                if stack != " ":
                    self.stacks[index].insert(0, stack)

    def get_stack_names(self) -> list[int]:
        """Parse the input file and exract the stack names.

        Return
        -------
        List[str]
            The stack names as ints.
        """
        with open(self.file) as input:
            data = input.readlines()

        for index, line in enumerate(data):
            if line == "\n":
                self.name_index = index - 1

        stacks = []
        for stack in list(data[self.name_index])[1::4]:
            stacks.append(int(stack))

        return stacks

    def get_inital_stacks(self) -> list:
        """Parse the input file and exract the lines with the initial stack makeup.

        Return
        -------
        List[str]
            The lines containing the initial stack makeup.
        """
        crate_lines = []

        with open(self.file) as input:
            data = input.readlines()

        for line_index, line in enumerate(data):
            if line_index < self.name_index:
                crate_lines.append(line)

        return crate_lines

    def get_instructions(self) -> list[list[int]]:
        """ Get instructions as a list.

        Return
        -------
        List[List[int]]
            The instructions.
        """
        with open(self.file) as input:
            data = input.readlines()

        lines = []
        for line in data:
            if line[0] == "m":
                # TODO There has to be a better way.
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
    """CargoHold with stacks of crates.

    Attributes
    ----------
    stacks: dict[int: list[str]]
        The stacks of crates.

    Parameters
    ----------
    file: str
        Filename as a string.

    """

    def __init__(self, file: str = "input") -> None:
        parser = Parser(file)
        self.stacks = parser.stacks

    def move_crates(self, count: int, origin: int, destination: int) -> None:
        """Move each crate one at a time.

        Parameters
        ----------
        count: int
            Number of crates to move.
        origin: int
            Stack to pull the crates from.
        destination: int
            Stack to place the crates on.
        """
        while count > 0:
            self.stacks[destination].append(self.stacks[origin].pop())
            count -= 1

    def move_stack(self, count: int, origin: int, destination: int) -> None:
        """Move the crates as a single unit.

        Parameters
        ----------
        count: int
            Number of crates to move.
        origin: int
            Stack to pull the crates from.
        destination: int
            Stack to place the crates on
        """
        stack = self.stacks[origin][-count:]

        while count > 0:
            self.stacks[origin].pop()
            count -= 1

        for item in stack:
            self.stacks[destination].append(item)

    def get_top_crates(self) -> str:
        """Get the top crate in each stack as a string.

        Return
        ------
        str
            The crate on top of each stack.
        """
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
    parser = Parser("input")
    lines = parser.get_instructions()
    cargo = CargoHold(file="input")
    for line in lines:
        try:
            quantity, start, stop = line
        except ValueError:
            print(f"Error: {line}")

        cargo.move_crates(quantity, start, stop)

    return cargo.get_top_crates()


def part_two():
    parser = Parser("input")
    lines = parser.get_instructions()
    cargo = CargoHold(file="input")
    for line in lines:
        try:
            quantity, start, stop = line
        except ValueError:
            print(f"Error: {line}")

        cargo.move_stack(quantity, start, stop)

    return cargo.get_top_crates()


if __name__ == "__main__":
    print(part_one())
    print(part_two())
