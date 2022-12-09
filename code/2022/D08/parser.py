
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
