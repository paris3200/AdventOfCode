from parser import Parser
from grid import Grid


class Rope:
    def __init__(self, length: int = 1) -> None:
        self.head = [0, 0]
        self.tail = [0, 0]
        self.length = length
        self.tail_visted = [self.tail[:]]

    def move(self, direction: str, quantity: int) -> None:
        if direction == "R":
            self.move_right(quantity)
        elif direction == "L":
            self.move_left(quantity)
        elif direction == "U":
            self.move_up(quantity)
        elif direction == "D":
            self.move_down(quantity)

    def move_right(self, quantity):
        for i in range(0, quantity):
            self.head[0] += 1
            if self.is_touching() is False:
                if (
                    self.is_diagnoal([self.head[0] - 1, self.head[1]], self.tail)
                    is True
                ):
                    self.tail = [self.head[0] - 1, self.head[1]]
                else:
                    self.tail[0] += 1

                self.tail_visted.append(self.tail[:])

    def move_left(self, quantity):
        for i in range(0, quantity):
            self.head[0] -= 1
            if self.is_touching() is False:
                if (
                    self.is_diagnoal([self.head[0] + 1, self.head[1]], self.tail)
                    is True
                ):
                    self.tail = [self.head[0] + 1, self.head[1]]
                else:
                    self.tail[0] -= 1

                self.tail_visted.append(self.tail[:])

    def move_up(self, quantity):
        for i in range(0, quantity):
            self.head[1] += 1
            if self.is_touching() is False:
                if (
                    self.is_diagnoal([self.head[0], self.head[1] - 1], self.tail)
                    is True
                ):
                    self.tail = [self.head[0], self.head[1] - 1]
                else:
                    self.tail[1] += 1

                self.tail_visted.append(self.tail[:])

    def move_down(self, quantity):
        for i in range(0, quantity):
            self.head[1] -= 1
            if self.is_touching() is False:
                if (
                    self.is_diagnoal([self.head[0], self.head[1] + 1], self.tail)
                    is True
                ):
                    self.tail = [self.head[0], self.head[1] + 1]
                else:
                    self.tail[1] -= 1

                self.tail_visted.append(self.tail[:])

    def is_diagnoal(self, head: list, tail: list) -> bool:
        if head[1] != tail[1] and head[0] != tail[0]:
            return True
        else:
            return False

    def is_touching(self) -> bool:
        x, y = self.tail
        for point in self.adjecent(x, y):
            if point == self.head or self.head == self.tail:
                return True

        return False

    @staticmethod
    def adjecent(x: int, y: int):
        yield [x - 1, y - 1]
        yield [x, y - 1]
        yield [x + 1, y - 1]
        yield [x - 1, y]
        yield [x + 1, y]
        yield [x - 1, y + 1]
        yield [x, y + 1]
        yield [x + 1, y + 1]


def part_one(input: str):
    parser = Parser(input)
    rope = Rope()
    for line in parser.get_lines():
        direction, quantity = line.split(" ")
        rope.move(direction, int(quantity))

    unique = []
    for point in rope.tail_visted:
        if point not in unique:
            unique.append(point)
    return len(unique)


if __name__ == "__main__":
    print(part_one("data/input"))
