import utils


class Compiler:
    def __init__(self, program):
        self.accumaltor = 0
        self.current_index = 0
        self.commands_run = []
        self.program = program

    def excute_program(self):
        return self.execute_instruction(self.parse_instruction(self.program[0]))

    def parse_instruction(self, instruction):
        split = instruction.split()
        command = {}
        command["type"] = split[0]
        command["argument"] = int(split[1])
        return command

    def execute_instruction(self, instruction):

        if self.current_index not in self.commands_run:
            self.commands_run.append(self.current_index)
        else:
            return self.accumaltor

        if instruction["type"] == "acc":
            self.accumaltor += instruction["argument"]
            self.current_index += 1

        elif instruction["type"] == "jmp":
            self.current_index += instruction["argument"]

        elif instruction["type"] == "nop":
            self.current_index += 1

        return self.execute_instruction(
            self.parse_instruction(self.program[self.current_index])
        )


def part_one(data):
    print("Part One")
    program = utils.read_lines(data)
    compiler = Compiler(program)
    return compiler.excute_program()


def part_two(data):
    print("Part Two")


def test_part_one():
    data = "data/08_tests.data"
    result = part_one(data)
    assert result == 5


def test_part_two():
    data = "data/08_tests.data"
    result = part_two(data)
    assert result is True


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
    part_two(data)
