from grid import Grid


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def create_grid(filename: str) -> Grid:
    lines = read_lines(filename)
    length_x = len(lines[0])
    length_y = len(lines)
    count = 1
    grid = Grid(length_x, length_y, default_value=".")

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                char = str(count)
                grid.galaxies.append(char)
                count += 1
            grid.set_point(x=x, y=y, value=char)

    return grid


def calculate_distance(
    point1: list[int], point2: list[int], rows: int, columns: int, expansion_factor: int
) -> int:
    distance = (abs(point1[0] - point2[0]) + (rows * expansion_factor - (rows * 1))) + (
        abs(point1[1] - point2[1]) + (columns * expansion_factor - (columns * 1))
    )
    return abs(distance)


def part_one(filename: str):
    grid = create_grid(filename)
    grid.expand_grid()
    # print(grid)

    num = len(grid.galaxies)
    matches = []
    for x in range(0, num):
        match = grid.galaxies.pop(0)
        for galaxy in grid.galaxies:
            matches.append([match, galaxy])

    # print(f"Number of pairs: {len(matches)}")

    distances = []
    for match in matches:
        point1 = grid.find_point(match[0])
        point2 = grid.find_point(match[1])
        distance = grid.calculate_distance(point1, point2)
        distances.append(distance)
        # print(f"Distance from {match[0]} to {match[1]}: {distance}")

    # print(distances)
    return sum(distances)


def part_two(filename: str):
    expansion_factor = 1000000
    grid = create_grid(filename)
    grid.get_rows_to_expand()
    grid.get_columns_to_expand()

    num = len(grid.galaxies)
    matches = []
    for x in range(0, num):
        match = grid.galaxies.pop(0)
        for galaxy in grid.galaxies:
            matches.append([match, galaxy])

    print(f"Number of pairs: {len(matches)}")

    distances = []
    for match in matches:
        point1 = grid.find_point(match[0])
        point2 = grid.find_point(match[1])

        ex_rows, ex_columns = grid.get_expansion_count(point1, point2)

        distance = calculate_distance(point1, point2, rows=ex_rows, columns=ex_columns, expansion_factor=expansion_factor,)
        distances.append(distance)
        print(f"Distance from {match[0]} to {match[1]}: {distance}")
    return sum(distances)


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
