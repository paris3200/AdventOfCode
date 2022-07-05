if __name__ != "__main__":
    from Y2015.utils import Grid
    import utils
else:
    from utils import Grid
    import utils

def grid_size(directions: str) -> list:
    """Returns the max gride size"""
    y = directions.count("^") + directions.count("v")
    x = directions.count(">") + directions.count("<")
    if x < 5:
        x = 5
    if y < 5:
        y = 5
    return [x, y]


def deliver_presents(nav_list: str) -> Grid:
    """Increases the present count at the grid location based on nav_list locations."""
    size = grid_size(nav_list)
    index = [int(size[0] / 2), int(size[1] / 2)]
    current_index = index
    grid = Grid(size[0], size[1])

    # Deliver present to start point
    grid.increase_point(current_index[0], current_index[1])

    directions = list(nav_list)
    for instruction in directions:
        if instruction == "^":
            current_index[1] += 1
        elif instruction == "v":
            current_index[1] -= 1
        elif instruction == ">":
            current_index[0] += 1
        elif instruction == "<":
            current_index[0] -= 1

        grid.increase_point(current_index[0], current_index[1])

    return grid


def part_one(data):
    grid = deliver_presents(data)

    stats = grid.stats()
    return stats['on']


def part_two(data):
    pass


if __name__ == "__main__":
    data = "data/03.data"
    input = utils.read_lines(data)
    print("Part One")
    print(part_one(input[0]))
    print("Part Two")
    print(part_two(input))
