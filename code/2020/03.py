import utils
from pytest import skip


def part_one(data):
    print(f"Part One")
    slope = [3, 1]
    return check_trees(data, slope)


def build_map(data, lines, slope):
    x_length = len(data[0])
    if x_length < lines*slope[0]:
        for i, line in enumerate(data):
            raw_line = line.strip("\n")
            data[i] = raw_line + raw_line
        build_map(data, lines, slope)
    return data


def check_trees(data, slope):
    current_pos = [0, 0]
    trees = 0
    total_lines = int(len(data))
    map = build_map(data, total_lines, slope)
    for i, line in enumerate(map, start=1):
        if i % slope[1] == 0:
            if current_pos[0] == 0:
                current_pos[0] = 1
            elif line[current_pos[0]-1] == "#":
                trees = trees + 1

            current_pos[0] = current_pos[0] + slope[0]
            current_pos[1] = current_pos[1] + slope[1]

    return trees


def test_check_trees_slope():
    with open("data/03_tests.data") as f:
        test_data = f.readlines()
    slope = [1, 1]
    slope1 = check_trees(test_data, slope)
    assert 2 == slope1

    slope = [3, 1]
    slope2 = check_trees(test_data, slope)
    assert 7 == slope2

    slope = [5, 1]
    slope3 = check_trees(test_data, slope)
    assert 3 == slope3

    slope = [7, 1]
    slope4 = check_trees(test_data, slope)
    assert 4 == slope4

    slope = [1, 2]
    slope5 = check_trees(test_data, slope)
    assert 2 == slope5

    product = slope1 * slope2 * slope3 * slope4 * slope5
    assert product == 336


def part_two():
    print(f"Part Two")
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    result = []
    for slope in slopes:
        result.append(check_trees(data, slope))

    product = 1
    for trees in result:
        breakpoint()
        product = product * trees
    print(product)


def test_check_trees():
    with open("data/03_tests.data") as f:
        test_data = f.readlines()
    slope = [3, 1]
    assert 7 == check_trees(test_data, slope)


def test_build_map():
    with open("data/03_tests.data") as f:
        test_data = f.readlines()

    lines = int(len(test_data))
    slope = [3, 1]
    result = '..##.........##.........##.........##.......'
    assert result in build_map(test_data, len(test_data), slope)


if __name__ == "__main__":

    with open("data/03.data") as f:
        data = f.readlines()
    print(part_one(data))
    part_two()
