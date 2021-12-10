from typing import List

import utils


def calculate_distance(p1: int, p2: int) -> int:
    """Calculate the absolute value between two points.

    Args:
        p1: Point 1
        p2: Point 2

    Returns:
        int:  distance between p1 and p2
    """
    return abs(p1 - p2)


def calculate_fuel_table(subs: List[int]) -> List[int]:
    """Calculate fuel table where the index represents the distance traveled
    and the value represents the fuel used to dravel that distance.

    Args:
        subs: List containing the horizontal location of each sub.

    Returns:
        list: fuel table
    """
    fuel_table = [0]
    for x in range(1, max(subs) + 1):
        fuel_table.append(x + fuel_table[x - 1])

    return fuel_table


def move_subs(subs: List[int], point: int, fuel_table: List[int] = None) -> int:
    """Moves all the subs and to the point and determines the fuel required.

    Args:
        subs:  List contain the horizontal position of each sub.
        point:  The position to move all the subs to.
        fuel_table: List containing the fuel rates.
    Returns:
        int:  Fuel used to move all subs to point.
    """
    fuel_used = 0

    if not fuel_table:
        for sub in subs:
            fuel_used += calculate_distance(sub, point)
    else:
        for sub in subs:
            fuel_used += fuel_table[calculate_distance(sub, point)]
    return fuel_used


def calculate_central_point(subs: List[int], fuel_rate: bool = False) -> int:
    """Calculates which point all subs can be moved to using the
    least ammount of fuel possible.

    Args:
        subs:  List containing initial position of all subs.
        fuel_rate:  True if fuel rate needed.

    Returns:
        int: Point that uses the least amount of fuel to move all subs to.
    """
    fuel_used = 2147483647
    point = 0
    points = []
    fuel_table = calculate_fuel_table(subs)

    # There has to be a better way
    for x in range(min(subs), max(subs)):
        if x > 0:
            points.append(x)

    for pt in points:
        if fuel_rate:
            fuel = move_subs(subs, pt, fuel_table)
        else:
            fuel = move_subs(subs, pt)
        if fuel < fuel_used:
            fuel_used = fuel
            point = pt

    return point


def part_one(subs: List[int]) -> int:
    point = calculate_central_point(subs)
    fuel = move_subs(subs, point)
    return fuel


def part_two(subs: List[int]) -> int:
    fuel_table = calculate_fuel_table(subs)
    point = calculate_central_point(subs, fuel_rate=True)
    fuel = move_subs(subs, point, fuel_table)
    return fuel


if __name__ == "__main__":
    filename = "data/07.data"
    subs = utils.read_file_of_ints(filename)
    point = calculate_central_point(subs)
    fuel = part_one(subs)

    print("Part One")
    print(f"All subs moved to {point} with a total fuel consumption of {fuel}")

    point = calculate_central_point(subs, fuel_rate=True)
    fuel = part_two(subs)
    print("Part Two")
    print(f"All subs moved to {point} with a total fuel consumption of {fuel}")
