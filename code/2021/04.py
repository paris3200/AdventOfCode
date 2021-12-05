import utils

def setup_game(filename):
    with open(filename, "r") as f:
        first_line = f.readline().rstrip()

    drawn_numbers = []
    for num in first_line.strip().split(","):
        drawn_numbers.append(int(num))

    breakpoint()


def part_one(data):
    setup_game("data/04_test.data")


def part_two(data):
    pass


def test_part_one():
    data = "data/04_test.data"
    result = part_one(data)
    assert result is True

def test_part_two():
    data = "data/04_test.data"
    result = part_two(data)
    assert result is True


if __name__ == "__main__":
    data = "data/04_test.data"
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
