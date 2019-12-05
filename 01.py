import math


def calculate_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calculate_fuel(fuel)


with open("01_input.txt", "r") as payload:
    total_fuel = 0
    for line in payload:
        total_fuel += calculate_fuel(int(line))


print(f"Total Fuel Required: {total_fuel}")


def test_calculate():
    assert calculate_fuel(1969) == 966
    assert calculate_fuel(100756) == 50346
