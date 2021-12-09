class Model:
    def __init__(self, population=None, days=1, verbose=False):
        self.day = days
        self.verbose = verbose

        self.fish = []
        for x in range(0, 9):
            self.fish.append(0)

        if population:
            for x, age in enumerate(population):
                self.fish[x] += age

    def count_fish(self):
        return sum(self.fish)

    def run(self):
        while self.day > 0:
            b = self.fish.pop(0)
            self.fish.append(b)
            self.fish[6] += b
            self.day -= 1
        return self.count_fish()


def convert_input(input):
    bucket = []
    for x in range(0, 9):
        bucket.append(0)

    for x in range(0, 9):
        bucket[x] = input.count(x)

    return bucket


def part_one(days=80):
    filename = "data/06.data"

    with open(filename, "r") as f:
        data = f.readlines()

    fish = []
    for line in data:
        input = line.rstrip().split(",")

    for i in input:
        fish.append(int(i))

    fish = convert_input(fish)

    model = Model(fish, days=days, verbose=False)
    count = model.run()

    print(f"Sun fish after {days} days: {count} \n")


def part_two():
    part_one(days=256)


if __name__ == "__main__":
    print("Part One")
    part_one()

    print("Part Two")
    part_two()
