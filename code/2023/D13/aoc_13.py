from grid import Grid


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            line = line.rstrip()
            lines.append(line)
        else:
            lines.append("---")
    return lines


def create_grid(lines: list[str]) -> Grid:
    if lines[-1] == "---":
        lines.pop()
    length_x = len(lines[0])
    length_y = len(lines)
    grid = Grid(length_x, length_y, default_value=".")

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid.set_point(x=x, y=y, value=char)

    return grid


def find_horizontal_mirror(grid: Grid) -> list[int]:
    for x in range(0, grid.max_y - 1):
        row1 = grid.get_row(x)
        row2 = grid.get_row(x + 1)
        if row1 == row2:
            return [x, x + 1]


def check_horizontal(grid: Grid) -> int:
    fold = find_horizontal_mirror(grid)

    # breakpoint()

    if fold:
        above_indexes = list(range(0, fold[0]))
        below_indexes = list(range(fold[1] + 1, grid.max_y))

        # breakpoint()

        if above_indexes == [] or below_indexes == []:
            return fold[0] + 1

        min_length = min(len(above_indexes), len(below_indexes))
        above_indexes = above_indexes[-1:-(min_length+1):-1]
        below_indexes = below_indexes[:min_length]

        if grid.get_row(above_indexes[-1]) == grid.get_row(below_indexes[-1]):
            return fold[0] + 1

        return 0

    return 0


def find_vertical_mirror(grid: Grid) -> list[int]:
    for x in range(0, grid.max_x - 1):
        row1 = grid.get_column(x)
        row2 = grid.get_column(x + 1)
        breakpoint()
        if row1 == row2:
            return [x, x + 1]


def check_vertical(grid: Grid) -> int:
    fold = find_vertical_mirror(grid)
    if fold:
        above_indexes = list(range(0, fold[0]))
        below_indexes = list(range(fold[1] + 1, grid.max_x))

        if above_indexes == [] or below_indexes == []:
            return fold[0] + 1

        min_length = min(len(above_indexes), len(below_indexes))
        above_indexes = above_indexes[-1:-(min_length+1):-1]
        below_indexes = below_indexes[:min_length]

        if grid.get_column(above_indexes[-1]) == grid.get_column(below_indexes[-1]):
            return fold[0]+1

        return 0
    return 0


def part_one(filename: str):
    lines = read_lines(filename)
    grid_chunks = []

    line_chunk = []
    for x in range(0, len(lines)):
        if lines[x] != "---":
            line_chunk.append(lines[x])
        else:
            grid_lines = line_chunk.copy()
            grid_chunks.append(grid_lines)
            line_chunk.clear()

    grids = []
    for chunk in grid_chunks:
        grid = create_grid(chunk)
        grids.append(grid)

    columns = []
    rows = []

    for grid in grids:
        # print(grid)
        horizontal = check_horizontal(grid)
        if horizontal == 0:
            vertical = check_vertical(grid)
            columns.append(vertical)
            # print(f"{vertical} lines to the left of the mirror line found. \n")
        else:
            # print(f"{horizontal} lines above the mirror line found.")
            rows.append(horizontal)

    return sum(columns) + (sum(rows) * 100)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    # print("Part One")
    print(part_one("input"))

    # print("Part Two")
    # print(part_two("input"))
