import utils



bags = []

class Bag():

    def __init__(self, name):
        self.parent = None
        self.children = []
        self.name = name

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent

    def print_tree(self):
        offset = "--" * self.get_level() * 2
        print(f"{offset}{self.name}")
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        parent = self.parent

        while parent:
            level += 1
            parent = parent.parent

        return level

def create_bag(name):
    current_bag = False
    if not bags:
        current_bag = Bag(name=name)
        bags.append(current_bag)
    else:
        for bag in bags:
            if bag.name == name:
                current_bag = bag

        if not current_bag:
            current_bag = Bag(name=name)
            bags.append(current_bag)


    return current_bag


def print_tree():
    for bag in bags:
        if bag.parent == None and bag.name == "light red":
            bag.print_tree()


def process_bags(data):
    for line in data:
        line = line.strip(".").strip(",")
        input = line.split()

        # Every line starts with a bag name
        name = input.pop(0) + " " + input.pop(0)

        root_bag = create_bag(name)

        while(input[0] == "bags" or input[0] == "contain" or input[0] == "contains"):
            input.pop(0)
        
        while(len(input) > 0):
            if input[0] == "no":
                input.clear()
            else:
                qty = int(input.pop(0))
                name = input.pop(0) + " " + input.pop(0)

                #Remove "bag"
                input.pop(0)

                bag = create_bag(name)

                while qty > 0:
                    root_bag.add_child(bag)
                    qty = qty-1


def part_one(data):
    process_bags(data)
    print("Part One")


def part_two(data):
    print("Part Two")


def test_part_one(data):
    data = utils.read_lines("data/07_tests.data")
    result = part_one(data)
    print_tree()


def test_part_two():
    data = utils.read_lines("data/07_tests.data")
    result = part_two(data)
    assert True is True


if __name__ == "__main__":
    data = "data/07.data"
    test_part_one(data)
    #part_two(data)
