import re


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


# Convert input to list[list[str]]
# Find Number on line, and store value
# Create cordinates of number
# Check all adjacent points of each coordinate for a symbol
# If symbol found append number value to result list.
# Sum the result list and return it


def get_adjacent_points(x: int, y: int, max_x: int, max_y: int) -> list[list[int]]:
    adjacent_points = []
    adjacent_points.append([x - 1, y])
    adjacent_points.append([x - 1, y - 1])
    adjacent_points.append([x - 1, y + 1])
    adjacent_points.append([x, x - 1])
    adjacent_points.append([x, x + 1])
    adjacent_points.append([x + 1, y + 1])
    adjacent_points.append([x + 1, y])
    adjacent_points.append([x + 1, y - 1])

    for point in adjacent_points.copy():
        if point[0] > max_y or point[0] == -1 or point[1] == -1 or point[1] > max_x:
            adjacent_points.remove(point)

    adjacent_points.sort()
    return adjacent_points


def is_symbol(char: str) -> bool:
    if char.isdigit() or char == ".":
        return False
    else:
        return True


def validate_number(filename: str, points: list[list[int]]) -> bool:
    rows = []
    for row in read_lines(filename):
        rows.append(list(row))

    max_y = len(rows)-1
    max_x = len(rows[0])-1

    points_to_check = []
    for point in points:
        adjacent_points = get_adjacent_points(point[1], point[0], max_x, max_y)
        for p in adjacent_points:
            points_to_check.append(p)

    points_checked = []
    for point in points_to_check:
        if point not in points_checked:
            if is_symbol(rows[point[1]][point[0]]) is True:
                return True

    return False


def number_to_points(filename: str, row_index: int, number: str) -> list[list[int]]:
    rows = read_lines(filename)
    start_index = rows[row_index].index(number)
    end_index = start_index+len(number)-1
    counter = start_index
    points = []
    while counter <= end_index:
        points.append([row_index, counter])
        counter += 1

    return points


def validate_row(filename: str, row_index: int) -> str:
    rows = read_lines(filename)
    numbers = re.findall(r"\d+", rows[row_index])
    row = rows[row_index]
    max_y = len(rows)-1
    max_x = len(rows[0])-1

    for number in numbers:
        start_index = rows[row_index].index(number)
        end_index = start_index+len(number)+1

        if end_index > max_x:
            end_index -= 1

        if start_index == 0:
            start_index = 1

        if row_index > 0:
            row_above = rows[row_index-1][start_index-1: end_index]
        else:
            row_above = ""

        row = rows[row_index][start_index-1: end_index]

        if row_index != max_y:
            row_below = rows[row_index+1][start_index-1: end_index]
        else:
            row_below = ""

        characters = row_above+row+row_below
        count = 0
        for char in characters:
            if is_symbol(char):
                count += 1
        if count == 0:
            replacement_string = len(number)*"."
            rows[row_index] = rows[row_index].replace(number, replacement_string, 1)

    return rows[row_index]


def part_one(filename: str):
    rows = read_lines(filename)

    for index, row in enumerate(rows):
        rows[index] = validate_row(filename, index)

    # row_2 = ''.join(row_grid[2])
    # print(row_2)
    # print(row_2.index('10'))

    rows_as_strings = []
    valid_numbers = []
    for row in rows:
        numbers = re.findall(r"\d+", row)
        for num in numbers:
            valid_numbers.append(int(num))

    with open("results", "w") as file1:
        for row in rows:
            file1.write(row+"\n")
    return sum(valid_numbers)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
