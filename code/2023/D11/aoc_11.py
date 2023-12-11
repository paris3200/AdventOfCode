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
    expansion_factor = 10
    grid = create_grid(filename)
    grid.get_rows_to_expand()
    grid.get_columns_to_expand()
    rows = grid.expand_rows
    columns = grid.expand_columns

    print(f"Rows: {rows}")
    print(f"Columns: {columns}")

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

        ex_rows = []
        for row in rows:
            if min(point1[0], point2[0]) < row < max(point1[0], point2[0]):
                ex_rows.append(row)

        ex_columns = []
        for column in columns:
            if min(point1[1], point2[1]) < column < max(point1[1], point2[1]):
                ex_columns.append(column)

        point1_ex = [point1[0]+(len(ex_rows)*expansion_factor), point1[1]+(len(ex_columns)*expansion_factor)]
        point2_ex = [point2[0]+(len(ex_rows)*expansion_factor), point2[1]+(len(ex_columns)*expansion_factor)]

        if len(ex_rows) > 0 and len(ex_columns) > 0:
            breakpoint()

        distance = grid.calculate_distance(point1_ex, point2_ex)
        distances.append(distance)
        # print(f"Distance from {match[0]} to {match[1]}: {distance}")
        # if len(ex_rows) > 0:
        #     print(f"    Rows in path: {ex_rows}")
        # if len(ex_columns) > 0:
        #     print(f"    Columns in path: {ex_columns}")
    return sum(distances)

if __name__ == "__main__":
    # print("Part One")
    # print(part_one("input"))

    print("Part Two")
    print(part_two("test_input"))
