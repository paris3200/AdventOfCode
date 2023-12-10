from grid import Grid
from math import floor


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def get_next_node(grid: Grid, x: int, y: int, previous: list[int] | bool = None) -> list[list[int]]:
    valid_points = []
    current_pipe = grid.get_point(x, y)

    if current_pipe == "S":
        point = check_up(grid, x, y)
        if point:
            valid_points.append(point)
        point = check_down(grid, x, y)
        if point:
            valid_points.append(point)
        point = check_left(grid, x, y)
        if point:
            valid_points.append(point)
        point = check_right(grid, x, y)
        if point:
            valid_points.append(point)

    if current_pipe == "|":
        point = check_up(grid, x, y)
        if point:
            valid_points.append(point)

        point = check_down(grid, x, y)
        if point:
            valid_points.append(point)

    if current_pipe == "-":
        point = check_right(grid, x, y)
        if point:
            valid_points.append(point)
        point = check_left(grid, x, y)
        if point:
            valid_points.append(point)

    if current_pipe == "L":
        point = check_up(grid, x, y)
        if point:
            valid_points.append(point)
        point = check_right(grid, x, y)
        if point:
            valid_points.append(point)

    if current_pipe == "J":
        point = check_up(grid, x, y)
        if point:
            valid_points.append(point)
        point = check_left(grid, x, y)
        if point:
            valid_points.append(point)

    if current_pipe == "7":
        point = check_down(grid, x, y)
        if point:
            valid_points.append(point)
        point = check_left(grid, x, y)
        if point:
            valid_points.append(point)

    if current_pipe == "F":
        point = check_down(grid, x, y)
        if point:
            valid_points.append(point)
        point = check_right(grid, x, y)
        if point:
            valid_points.append(point)

    if previous in valid_points:
        valid_points.remove(previous)

    return valid_points


def check_up(grid: Grid, x: int, y: int) -> list[int] | None:
    up_valid = ["|", "7", "F", "S"]
    up_pipe = grid.get_point(x, y-1)
    if up_pipe in up_valid:
        return [x, y-1]


def check_down(grid: Grid, x: int, y: int) -> list[int] | None:
    down_valid = ["|", "L", "J", "S"]
    down_pipe = grid.get_point(x, y+1)
    if down_pipe in down_valid:
        return [x, y+1]


def check_right(grid: Grid, x: int, y: int) -> list[int] | None:
    right_valid = ["-", "J", "7", "S"]
    right_pipe = grid.get_point(x+1, y)
    if right_pipe in right_valid:
        return [x+1, y]


def check_left(grid: Grid, x: int, y: int) -> list[int] | None:
    left_valid = ["-", "L", "F", "S"]
    left_pipe = grid.get_point(x-1, y)
    if left_pipe in left_valid:
        return [x-1, y]


def create_grid(filename: str) -> Grid:
    lines = read_lines(filename)
    length_x = len(lines[0])
    length_y = len(lines)
    grid = Grid(length_x, length_y, default_value=".")

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid.set_point(x=x, y=y, value=char)

    return grid


def visualize_path(filename: str) -> None:
    grid = create_grid(filename)
    path = solve_grid(filename)
    for y in range(0, grid.max_y):
        for x, char in enumerate(grid.grid[y]):
            if [x, y] in path:
                grid.grid[y][x] = "\033[31;47m" + char + "\033[m"

    for y in range(0, grid.max_y):
        line = "".join(grid.grid[y])
        print(line)


def solve_grid(filename) -> list[list[int]]:
    grid = create_grid(filename)

    # print(grid)
    start = grid.get_start()
    nodes = get_next_node(grid, start[0], start[1])
    paths = []
    for index, node in enumerate(nodes):
        paths.append([start])
        paths[index].append(node)

    paths = [[start, nodes[0]]]

    while True:
        for path in paths:
            point = path[-1]
            if point == start:
                return path
            else:
                nodes = get_next_node(grid, point[0], point[1], path[-2])
                if len(nodes) < 1:
                    breakpoint()
                path.append(nodes[0])


def part_one(filename: str):
    visualize_path(filename)
    path = solve_grid(filename)
    return floor(len(path) / 2)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
