import utils


class Compiler:
    def __init__(self, program, bootable=False):
        """
        A compiler for Advent of Code 2020, day 8.

        Sets of the compiler to be run

        Parameters
        ----------
        program : list
            The list of instructions to be run.
        bootable : bool, default=False
            If the program should result in a bootable program.

        Attributes
        ----------
        program : list
            The list of instructions to be run.
        bootable : bool, default=False
            If the program should result in a bootable program.
        accumaltor : int
            The value of the accaltor at the current point of the program.
        current_index : int
            The current index position in the program list.
        commands_run : list
            A list of the commands previously run for the current program execution.
        original_program : list
            A copy of the original program to be used to reset the compiler.
        commands_changed : list
            The program commands changed which failed to boot.
        """
        self.accumaltor = 0
        self.current_index = 0
        self.commands_run = []
        self.program = program
        self.bootable = bootable

        if self.bootable:
            self.original_program = program.copy()
            self.commands_changed = []
            self.reset_compliler()

    def reset_compliler(self):
        """
        Reset the compiler to process a new program.
        """
        self.program = self.original_program.copy()
        self.changed = False
        self.commands_run = []
        self.accumaltor = 0
        self.current_index = 0

    def excute_program(self):
        result = self.execute_instruction(self.parse_instruction(self.program[0]))
        if result is False:
            self.reset_compliler()
            return self.excute_program()
        else:
            return result

    def parse_instruction(self, instruction: str) -> dict:
        """
        Converts an instruction string to a dict.


        Parameters
        ----------
        instruction : str
            i.e. "jmp +4"

        Returns
        -------
        dict:
            ["type"] -> str: type of command (acc, jmp, nop)
            ["instruction"] -> int:  action to be taken (+99)
        """
        split = instruction.split()
        command = {}
        command["type"] = split[0]
        command["argument"] = int(split[1])
        return command

    def execute_instruction(self, instruction):
        if self.current_index in self.commands_run:
            if not self.bootable:
                return self.accumaltor
            else:
                return False
        else:
            self.commands_run.append(self.current_index)

        if instruction["type"] == "acc":
            self.accumaltor += instruction["argument"]
            self.current_index += 1

        if not self.bootable:

            if instruction["type"] == "jmp":
                self.current_index += instruction["argument"]

            elif instruction["type"] == "nop":
                self.current_index += 1

        if self.bootable:

            if instruction["type"] == "jmp":
                if (
                    self.changed is False
                    and self.current_index not in self.commands_changed
                ):
                    # Change command to nop and rerun index
                    self.changed = True
                    self.program[self.current_index] = f"nop {instruction['argument']}"
                    self.commands_changed.append(self.current_index)
                    self.commands_run.remove(self.current_index)

                else:

                    self.current_index += instruction["argument"]

            elif instruction["type"] == "nop":

                if (
                    self.changed is False
                    and self.current_index not in self.commands_changed
                    and (self.current_index != 0 and instruction["argument"] == 0)
                ):
                    # Change command to jmp and rerun index
                    self.changed = True
                    self.program[self.current_index] = f"jmp {instruction['argument']}"
                    self.commands_changed.append(self.current_index)
                    self.commands_run.remove(self.current_index)

                else:
                    self.commands_run.append(self.current_index)
                    self.current_index += 1

        try:
            return self.execute_instruction(
                self.parse_instruction(self.program[self.current_index])
            )
        except IndexError:
            return self.accumaltor


def part_one(data):
    print("Part One")
    program = utils.read_lines(data)
    compiler = Compiler(program)
    return compiler.excute_program()


def part_two(data):
    print("Part Two")
    program = utils.read_lines(data)
    compiler = Compiler(program, bootable=True)
    return compiler.excute_program()


def test_part_one():
    data = "data/08_tests.data"
    result = part_one(data)
    assert result == 5


def test_part_one_real_data():
    data = "data/08.data"
    result = part_one(data)
    assert result == 1584


def test_part_two():
    data = "data/08_tests.data"
    result = part_two(data)
    assert result == 8


def test_part_two_real_data():
    data = "data/08.data"
    result = part_two(data)
    assert result == 920


def test_parse_instructions():
    program = utils.read_lines("data/08_tests.data")
    compiler = Compiler(program)
    instruction = "acc -99"
    expected = {"type": "acc", "argument": -99}
    result = compiler.parse_instruction(instruction)
    assert expected == result


if __name__ == "__main__":
    data = "data/08.data"
    print(part_one(data))
    print(part_two(data))
