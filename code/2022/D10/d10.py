class Parser:
    def __init__(self, filename: str = None) -> None:

        if filename:
            with open(filename) as file:
                self.lines = file.readlines()

    def get_lines(self) -> list[str]:
        lines = []
        for line in self.lines:
            lines.append(line.strip())

        return lines


class Register:
    def __init__(self) -> None:
        self.cycle = 0
        self.value = 1
        self.signal_strength = []
        self.log = []

    def addx(self, value):
        self.execute_cycle()
        self.execute_cycle()
        self.value += value

    def noop(self):
        self.execute_cycle()

    def execute_cycle(self):
        self.cycle += 1
        self.log.append(self.value)
        if self.cycle == 20 or (self.cycle % 40) == 20:
            self.signal_strength.append(self.cycle * self.value)


class CRT:
    def __init__(self, input: list[int]) -> None:
        self.screen = " "
        self.input = input
        self.pixel_position = 0
        self.sprite_position = 1

    def execute_cycle(self) -> None:
        for cycle in self.input:
            self.sprite_position = cycle
            self.draw()
            self.pixel_position += 1

            if self.pixel_position == 40:
                self.pixel_position = 0

    def draw(self) -> None:
        if self.sprite_visible():
            self.screen += "#"
        else:
            self.screen += "."

    def sprite_visible(self) -> bool:
        position = self.pixel_position
        if (
            self.sprite_position == position
            or self.sprite_position == position + 1
            or self.sprite_position == position - 1
        ):
            return True
        else:
            return False

    def __repr__(self) -> str:
        output = ""
        for i, char in enumerate(self.screen):
            if i % 40 == 0:
                output += "\n"
            else:
                output += char

        return output


def part_one(file: str) -> int:
    parser = Parser(file)
    r = Register()
    for line in parser.get_lines():
        if line == "noop":
            r.noop()
        else:
            command, value = line.split(" ")

            if command == "addx":
                r.addx(int(value))

    return sum(r.signal_strength)


def part_two(file: str) -> int:
    parser = Parser(file)
    r = Register()

    for line in parser.get_lines():
        if line == "noop":
            r.noop()
        else:
            command, value = line.split(" ")

            if command == "addx":
                r.addx(int(value))
    log = r.log

    crt = CRT(log)
    crt.execute_cycle()

    return crt


if __name__ == "__main__":
    print(part_one("data/input"))
    print(part_two("data/input"))
