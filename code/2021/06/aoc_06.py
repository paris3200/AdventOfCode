

class Model:
    def __init__(self, population = None,  days=1, verbose=False):
        self.fish = []
        self.day = days
        self.verbose = verbose

        if population:
            for age in population:
                self.add_fish(Fish(age))

    def add_fish(self, fish):
        self.fish.append(fish)

    def count_fish(self):
        return len(self.fish)

    def run(self):
        while self.day > 0:
            for f in self.fish.copy():
                egg = f.age()
                if egg:
                    self.add_fish(egg)
            self.day -= 1

            if self.verbose:
                self.print_fish()

        return self.count_fish()

    def print_fish(self):
        school = []
        for f in self.fish:
            school.append(f.timer)
        print(school)

    


class Fish:
    def __init__(self, timer=8):
        self.timer = timer

    def age(self):

        if self.timer == 0:
            self.timer = 6
            return Fish()
        else:
            self.timer -= 1





def part_one(data):
    pass


def part_two(data):
    pass


if __name__ == "__main__":
    data = "data/xx.data"
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))

    model = Model([3, 4, 3, 1, 2], days=4, verbose=True)
    model.run()
