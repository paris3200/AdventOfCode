if __name__ != "__main__":
    from Y2015.utils import Grid
    from Y2015 import utils
else:
    from utils import Grid
    import utils

input = utils.read_lines("data/03.data")
DATA = input[0]


def grid_size(directions: str) -> list:
    """Returns the max gride size"""
    y = directions.count("^") + directions.count("v")
    x = directions.count(">") + directions.count("<")
    if x <= 5:
        x = 5
    if y <= 5:
        y = 5
    return [x, y]


def process_instruction(instruction: str, start: list) -> list:
    if instruction == "^":
        start[1] += 1
    elif instruction == "v":
        start[1] -= 1
    elif instruction == ">":
        start[0] += 1
    elif instruction == "<":
        start[0] -= 1

    return start


def create_grid(x: int, y: int) -> list[Grid, int, int]:
    index = [int(x / 2), int(y / 2)]
    grid = Grid(x, y)
    return [grid, index[0], index[1]]


def deliver_presents(nav_list: str, grid: Grid, index_x: int, index_y: int) -> Grid:
    """Increases the present count at the grid location based on nav_list locations."""

    # Deliver present to start point
    grid.increase_point(index_x, index_y)

    directions = list(nav_list)
    current_index = [index_x, index_y]
    for instruction in directions:
        current_index = process_instruction(instruction, current_index)
        grid.increase_point(current_index[0], current_index[1])

    return grid


def part_one(data=DATA):
    directions = data
    size = grid_size(directions)
    grid_properties = create_grid(size[0], size[1])
    grid = deliver_presents(
        directions, grid_properties[0], grid_properties[1], grid_properties[2]
    )

    stats = grid.stats()
    return stats["on"]


def part_two(data=DATA):
    directions = data
    santa_directions = str(directions[::2])
    robo_directions = str(directions[1::2])

    santa_size = grid_size(santa_directions)
    robot_size = grid_size(robo_directions)

    if santa_size[0] > robot_size[0]:
        x = santa_size[0]
    else:
        x = robot_size[0]

    if santa_size[1] > robot_size[1]:
        y = santa_size[1]
    else:
        y = robot_size[1]

    grid_properties = create_grid(x, y)
    santa_grid = deliver_presents(
        santa_directions, grid_properties[0], grid_properties[1], grid_properties[2]
    )
    grid = deliver_presents(
        robo_directions, santa_grid, grid_properties[1], grid_properties[2]
    )
    stats = grid.stats()
    return stats["on"]


if __name__ == "__main__":
    print("Part One")
    print(part_one())
    print("Part Two")
    print(part_two())
