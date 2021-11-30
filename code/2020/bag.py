import utils


class Bag():

    def __init__(self, parent=None, children={}, color=None):
        self.parent = parent
        self.children = children
        self.color = color

    def add_child(self, child, quanity):
        self.children.update({"child": child, "quanity": quanity})

    def __repr__(self):
        string = f"Parent: {self.parent} \n  color: {self.color} \n  children: {self.children}"
        return string


def create_bag():
    #input = data.split(",")

    a = Bag(color="light red")
    b = Bag(parent=a, color="bright white")
    a.add_child(b, 1)
    breakpoint()


def part_one(data):
    create_bag()
    print("Part One")


def part_two(data):
    print("Part Two")


def test_part_one():
    data = utils.read_lines("data/07_tests.data")
    result = part_one(data)
    assert result is True


def test_part_two():
    data = utils.read_lines("data/07_tests.data")
    result = part_two(data)
    assert result is True


if __name__ == "__main__":
    data = "data/07.data"
    part_one(data)
    part_two(data)
