from typing import List


class Model:
    def __init__(self, population: List[int], days: int = 1) -> None:
        """Setup the simulation.

        Args:
            population: The starting population as a list.  The index
                represents the timer value and the value represents the number of fish
                with that timer value.
            days: The number of days in the simulation.
        """
        self.days = days
        self.fish = self.sum_population(population)

    def count_fish(self) -> int:
        """Counts the total number of fish in the model.

        Returns:
            int: total number of fish
        """
        return sum(self.fish)

    def run(self) -> int:
        """Runs the simulation for prescribed number of days.

        Returns:
            The total number of fish alive at the end of the simulation.
        """
        while self.days > 0:
            b = self.fish.pop(0)
            self.fish.append(b)
            self.fish[6] += b
            self.days -= 1
        return self.count_fish()

    @staticmethod
    def sum_population(input: List[int]) -> List[int]:
        """
        Sums the number of fish in the input list and returns a list
        where the index corresponds to the fish timer and the value
        represents the number of fish with that timer.

        Args:
            input (list):  A list of fish timer values.

        Returns:
            list: Index mapped to fish timer value, value mapped to
                number of fish with that timer.
        """
        bucket = []
        for x in range(0, 9):
            bucket.append(0)

        for x in range(0, 9):
            bucket[x] = input.count(x)

        return bucket


def part_one(days: int = 80):
    filename = "data/06.data"

    with open(filename, "r") as f:
        data = f.readlines()

    for line in data:
        input = line.rstrip().split(",")

    fish = []
    for i in input:
        fish.append(int(i))

    model = Model(fish, days=days)
    count = model.run()

    print(f"Sun fish after {days} days: {count} \n")


def part_two():
    part_one(days=256)


if __name__ == "__main__":
    print("Part One")
    part_one()

    print("Part Two")
    part_two()
