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

    def calculate_limits(self, lines: list) -> list[int, int]:
        x = 0
        y = 0
        max_x = x
        max_y = y
        for line in self.lines:
            direction, value = line.split(" ")
            if direction == "R":
                x += int(value)
            elif direction == "L":
                x -= int(value)
            elif direction == "U":
                y += int(value)
            elif direction == "D":
                y -= int(value)

            if x > max_x:
                max_x = x

            if y > max_y:
                max_y = y

        return [max_x+1, max_y+1]
