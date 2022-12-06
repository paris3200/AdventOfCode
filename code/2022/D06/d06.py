class Parser:
    def __init__(self, filename: str = None) -> None:
        self.signal_start = None
        self.message_start = None

        if filename:
            with open(filename) as file:
                self.lines = file.readlines()

    def start_of_packet(self, line: str):
        index = 0

        while self.signal_start is None:
            chunk = list(line[index : index + 4])

            if len(set(chunk)) == len(chunk):
                self.signal_start = index + 4
            else:
                index += 1

        return self.signal_start

    def start_of_message(self, line: str):
        index = 0

        while self.message_start is None:
            chunk = list(line[index : index + 14])

            if len(set(chunk)) == len(chunk):
                self.message_start = index + 14
            else:
                index += 1

        return self.message_start


def part_one():
    parser = Parser(filename="input")
    return parser.start_of_packet(parser.lines[0])


def part_two():
    parser = Parser(filename="input")
    return parser.start_of_message(parser.lines[0])


if __name__ == "__main__":
    print(part_one())
    print(part_two())
