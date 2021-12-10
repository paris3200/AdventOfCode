from typing import List

import utils


def calculate_distance(p1: int, p2: int) -> int:
    return abs(p1 - p2)


def move_subs(subs: List[int], point: int) -> int:
    fuel_used = 0
    for sub in subs:
        fuel_used += calculate_distance(sub, point)
    return fuel_used


def part_one(subs: List[int]) -> int:
    point = calculate_central_point(subs)
    fuel = move_subs(subs, point)
    return fuel


def calculate_central_point(subs: List[int]) -> int:
    fuel_used = 2147483647
    point = 0
    points = []

    # There has to be a better way
    for x in range(min(subs), max(subs)):
        if x > 0:
            points.append(x)

    for pt in points:
        fuel = move_subs(subs, pt)
        if fuel < fuel_used:
            fuel_used = fuel
            point = pt

    return point


def part_two():
    pass


if __name__ == "__main__":
    filename = "data/07.data"
    subs = utils.read_file_of_ints(filename)
    point = calculate_central_point(subs)
    fuel = part_one(subs)

    print("Part One")
    print(f"All subs moved to {point} with a total fuel consumption of {fuel}")

    print("Part Two")
    part_two()
