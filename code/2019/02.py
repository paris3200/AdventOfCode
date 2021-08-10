import utils


class Computer:
    def __init__(self, intcode):
        self.intcode = list(intcode)

    def process(self, index=0):
        opcode = self.intcode[index]

        if opcode != 99:
            try:
                value1 = self.intcode[self.intcode[index + 1]]
                value2 = self.intcode[self.intcode[(index + 2)]]
                storage = self.intcode[index + 3]
            except IndexError as error:
                raise SystemExit(
                    "The program reached the end of the instructions without encountering a stop code. Please check the input."
                )

            if opcode == 1:
                self.intcode[storage] = value1 + value2
                self.process(index + 4)
            elif opcode == 2:
                self.intcode[storage] = value1 * value2
                self.process(index + 4)

        return self.intcode[0]

    def calculate_solution(self, target):
        CODE = self.intcode
        for noun in range(0, 100):
            for verb in range(0, 100):
                code = CODE.copy()

                code[1] = noun
                code[2] = verb
                self.intcode = code
                solution = self.process()
                if self.process() == target:
                    return [noun, verb]


def part_one():
    code = utils.read_file("data/02.data", "list")

    # Reset to 1202 Program State
    code[1] = 12
    code[2] = 2
    wopr = Computer(code)
    print(f"Part One: {wopr.process()}")


def part_two():
    code = utils.read_file("data/02.data", "list")

    wopr = Computer(code)
    inputs = wopr.calculate_solution(19690720)
    noun = inputs[0]
    verb = inputs[1]
    print(f"Part two: {100 * noun + verb}")


def test_calibration():
    wopr = Computer([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    assert wopr.process() == 3500

    wopr = Computer([1, 1, 1, 4, 99, 5, 6, 0, 99])
    assert wopr.process() == 30


if __name__ == "__main__":

    part_one()
    part_two()
