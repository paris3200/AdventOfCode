from Y2015 import utils


def grid_size(directions: str):
    """Returns the max gride size"""
    y = directions.count("^") + directions.count("v")
    x = directions.count(">") + directions.count("<")
    return [x, y]


def create_grid(grid_size: list[int]):
    """Creates a 2D grid with a max x and y values defined in gride_size."""
    grid = [[0 for y in range(grid_size[1])] for x in range(grid_size[0])]
    return grid


def count_nonzeros_in_grid(grid) -> int:
    """Returns the number of grid points that are non zero."""
    sum = 0
    for y, value in enumerate(grid):
        for x, value in enumerate(value):
            if grid[y][x] > 0:
                sum += 1
    return sum


def deliver_presents(nav_list):
    """Increases the present count at the grid location based on nav_list locations."""
    size = grid_size(nav_list)
    index = [int(size[0] / 2), int(size[1] / 2)]
    current_index = index
    grid = create_grid(size)

    # Deliver present to start point
    grid[current_index[1]][current_index[0]] += 1

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

    grid[current_index[1]][current_index[0]] += 1

    return grid


def part_one(data):
    grid = deliver_presents(data)
    return count_nonzeros_in_grid(grid)


def part_two(data):
    pass


if __name__ == "__main__":
    data = "../data/03.data"
    input = utils.read_lines(data)
    print("Part One")
    print(part_one(input[0]))
    print("Part Two")
    print(part_two(input))
