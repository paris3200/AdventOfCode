class Computer:
    def __init__(self, intcode):
        self.intcode = list(intcode)

    def process(self, index=0):
        opcode = self.intcode[index]

        if opcode != 99:
            value1 = self.intcode[self.intcode[index + 1]]
            value2 = self.intcode[self.intcode[(index + 2)]]
            storage = self.intcode[index + 3]

            if opcode == 1:
                self.intcode[storage] = value1 + value2
                self.process(index + 4)
            elif opcode == 2:
                self.intcode[storage] = value1 * value2
                self.process(index + 4)

        return self.intcode[0]


def test_calibration():
    wopr = Computer([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    assert wopr.process() == 3500

    wopr = Computer([1, 1, 1, 4, 99, 5, 6, 0, 99])
    assert wopr.process() == 30


if __name__ == "__main__":
    with open("02_input.txt", "r") as procedure:
        for line in procedure:
            data = line.strip().split(",")
            code = []
            for num in data:
                code.append(int(num))

    # Reset to 1202 Program State
    code[1] = 12
    code[2] = 2
    wopr = Computer(code)
    print(wopr.process())
