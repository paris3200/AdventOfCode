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
            row_above = rows[row_index - 1][start_index - 1: end_index + 1]
        else:
            row_above = ""

        row = rows[row_index][start_index - 1: end_index + 1]

        if row_index != max_y:
            row_below = rows[row_index + 1][start_index - 1: end_index + 1]
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


def part_two(filename: str):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one("input", "results"))

    print("Part Two")
    print(part_two("input"))
