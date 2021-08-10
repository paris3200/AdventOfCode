import math


def calculate_fuel(mass, part=1):
    if part == 1:
        fuel = math.floor(mass / 3) - 2
        return fuel
    elif part == 2:
        fuel = math.floor(mass / 3) - 2
        if fuel <= 0:
            return 0
        else:
            return fuel + calculate_fuel(fuel, part=2)


def test_calculate():
    assert calculate_fuel(1969) == 654
    assert calculate_fuel(100756) == 33583


def part_one():
    print("Part One:")
    with open("data/01.data", "r") as payload:
        total_fuel = 0
        for line in payload:
            total_fuel += calculate_fuel(int(line))

    print(f"  Total Fuel Required: {total_fuel}")


def part_two():
    print("Part Two:")
    with open("data/01.data", "r") as payload:
        total_fuel = 0
        for line in payload:
            total_fuel += calculate_fuel(int(line), part=2)

    print(f"  Total Fuel Required: {total_fuel}")

if __name__ == "__main__":
    part_one()
    part_two()
