import re
from grid import Grid


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")

    rows = []
    for line in data:
        rows.append(line)

    return rows


def is_symbol(char: str) -> bool:
    if char.isdigit() or char == ".":
        return False
    else:
        return True


def get_numbers(line: str) -> list[str]:
    numbers = re.findall(r"[0-9]+", line)
    return numbers


def validate_row(filename: str, row_index: int) -> str:
    rows = read_lines(filename)
    row = rows[row_index]
    max_y = len(rows) - 1
    max_x = len(rows[0]) - 1

    pattern = re.compile(r"[0-9]+")
    numbers = pattern.finditer(rows[row_index])

    for number in numbers:
        start_index = int(number.start())
        end_index = int(number.end()) - 1

        if end_index < max_x:
            end_index += 1

        if start_index == 0:
            start_index = 1

        if row_index > 0:
            row_above = rows[row_index - 1][start_index - 1 : end_index + 1]
        else:
            row_above = ""

        row = rows[row_index][start_index - 1 : end_index + 1]

        if row_index != max_y:
            row_below = rows[row_index + 1][start_index - 1 : end_index + 1]
        else:
            row_below = ""

        characters = row_above + row + row_below
        count = 0
        for char in characters:
            if is_symbol(char):
                count += 1
        if count == 0:
            start_index = int(number.start())
            replacement_string = len(number.group()) * "."
            if start_index != 0:
                pre_string = rows[row_index][:start_index]
            else:
                pre_string = ""

            if end_index != max_x:
                post_string = rows[row_index][end_index:]
            else:
                post_string = ""
            rows[row_index] = pre_string + replacement_string + post_string

    return rows[row_index]


def part_one(filename: str, result_file: str):
    rows = read_lines(filename)

    for index, row in enumerate(rows):
        rows[index] = validate_row(filename, index)

    valid_numbers = []
    for row in rows:
        numbers = re.findall(r"[0-9]+", row)
        for num in numbers:
            valid_numbers.append(int(num))

    with open(result_file, "w") as file1:
        for row in rows:
            file1.write(row + "\n")
    return sum(valid_numbers)


def create_grid(filename: str) -> Grid:
    lines = read_lines(filename)
    length_x = len(lines[0])
    length_y = len(lines)
    grid = Grid(length_x, length_y, default_value=".")

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid.set_point(x=x, y=y, value=char)

    return grid


def expand_number(grid: Grid, coordinates: list[list[int]]) -> int:
    x_range = []
    y_range = []
    for coordinate in coordinates:
        x_range.append(coordinate[0])
        y_range.append(coordinate[1])

    # Check left
    next_point = grid.get_point(min(x_range) - 1, y_range[0])
    while next_point.isnumeric() is True:
        x_range.append(min(x_range)-1)
        if min(x_range) > 0:
            next_point = grid.get_point(min(x_range) - 1, y_range[0])
        else:
            next_point = "."

    # Check right
    next_point = grid.get_point(max(x_range) + 1, y_range[0])
    while next_point.isnumeric() is True:
        x_range.append(max(x_range)+1)
        if max(x_range) < grid.max_x-1:
            next_point = grid.get_point(max(x_range) + 1, y_range[0])
        else:
            next_point = "."

    x_range.sort()
    numbers = []
    for x in x_range:
        numbers.append(grid.get_point(x, y_range[0]))

    return int("".join(numbers))


def get_gear_numbers(grid, numeric_points: list[list[int]]) -> list[int] | None:
    num1 = []
    num2 = []
    for point in numeric_points:
        if len(num1) == 0:
            num1.append(point)
        elif num1[0][1] == point[1]:
            num1.append(point)
        elif len(num2) == 0:
            num2.append(point)
        elif num2[0][1] == point[1]:
            num2.append(point)

    if num2 == []:
        return 0


    num1_int = expand_number(grid, num1)
    num2_int = expand_number(grid, num2)

    return num1_int * num2_int


def part_two(filename: str):
    grid = create_grid(filename)
    asterisks = grid.get_matching_points("*")

    gear_numbers = []
    for asterisk in asterisks:
        points = grid.get_adjacent_points(asterisk[0], asterisk[1])
        numeric_points = []

        for point in points:
            if grid.get_point(point[0], point[1]).isnumeric():
                numeric_points.append(point)

        gear_numbers.append(get_gear_numbers(grid, numeric_points))


    return sum(gear_numbers)


if __name__ == "__main__":
    # print("Part One")
    # print(part_one("input", "results"))

    print("Part Two")
    print(part_two("input"))
