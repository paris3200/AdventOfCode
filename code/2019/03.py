import code.utils as utils


def trace_wire(wire):
    path = [[0, 0]]
    for instruction in wire:
        direction = instruction[:1]
        length = int(instruction[1:]) + 1
        if direction == "U":
            previous = path[-1]
            for i in range(0, length):
                point = [previous[0], previous[1] + i]
                path.append(point)
        elif direction == "D":
            previous = path[-1]
            for i in range(0, length):
                point = [previous[0], previous[1] - i]
                path.append(point)
        elif direction == "R":
            previous = path[-1]
            for i in range(0, length):
                point = [(previous[0] + i), previous[1]]
                path.append(point)
        elif direction == "L":
            previous = path[-1]
            for i in range(0, length):
                point = [previous[0] - i, previous[1]]
                path.append(point)

        # if (path[-1][0] == path[-2][0]) and (path[-2][1] == path[-2][1]):
        #    path.pop()
    return path


def intersection(wire1, wire2):
    lst1 = trace_wire(wire1)
    lst2 = trace_wire(wire2)
    res_set = set(map(tuple, lst1)) & set(map(tuple, lst2))
    lst3 = list(map(list, res_set))
    return lst3


def manhattan_distance(wire1, wire2):
    cross = intersection(wire1, wire2)
    paths = []
    for point in cross:
        distance = abs(0 - point[0]) + abs(0 - point[1])
        if distance != 0:
            paths.append(distance)
    return min(paths)


def closest_intersection(wire1, wire2):
    points = intersection(wire1, wire2)
    wire1 = trace_wire(wire1)
    wire2 = trace_wire(wire2)
    hops = []
    for point in points:
        index1 = wire1.index(point)
        index2 = wire2.index(point)
        hops.append(index1 + index2)
    hops.remove(0)
    return min(hops)


def part_one():
    with open("data/03_input.txt", "r") as f:
        wire = f.readlines()
    wire1 = utils.list_from_string(wire[0])
    wire2 = utils.list_from_string(wire[1])
    distance = manhattan_distance(wire1, wire2)
    print(f"Part One {distance}")


def part_two():
    print(f"Part Two")


def test_part_one_case_one():
    wire1 = utils.list_from_string("R75,D30,R83,U83,L12,D49,R71,U7,L72")
    wire2 = utils.list_from_string("U62,R66,U55,R34,D71,R55,D58,R83")
    assert manhattan_distance(wire1, wire2) == 159


def test_part_one_case_two():
    wire1 = utils.list_from_string("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
    wire2 = utils.list_from_string("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
    assert manhattan_distance(wire1, wire2) == 135


def test_part_two_case_one():
    wire1 = utils.list_from_string("R75,D30,R83,U83,L12,D49,R71,U7,L72")
    wire2 = utils.list_from_string("U62,R66,U55,R34,D71,R55,D58,R83")
    assert closest_intersection(wire1, wire2) == 610


def test_part_two_case_two():
    wire1 = utils.list_from_string("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
    wire2 = utils.list_from_string("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
    assert closest_intersection(wire1, wire2) == 410


if __name__ == "__main__":

    part_one()
    part_two()
