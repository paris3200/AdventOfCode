import utils


class Submarine():

    def __init__(self):
        self.xvalue = 0
        self.yvalue = 0

    def move(self, command):
        command = command.split()

        if command[0] == "forward":
            self.xvalue += int(command[1])
        elif command[0] == "down":
            self.yvalue += int(command[1])
        elif command[0] == "up":
            self.yvalue -= int(command[1])


def part_one(data):
    sub = Submarine()
    for command in utils.read_lines(data):
        sub.move(command)
    return (sub.xvalue * sub.yvalue)

def part_two(data):
    print("Part Two")


def test_part_one():
    data = "data/02_test.data"
    result = part_one(data)
    assert result == 150


def test_part_two():
    data = "data/02_test.data"
    result = part_two(data)
    assert result is True


if __name__ == "__main__":
    data = "data/02.data"
    print("Part One")
    print(part_one(data))
    part_two(data)
