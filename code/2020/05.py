import utils


def parse_seat_code(ticket):
    rows = [i for i in range(0, 128, 1)]
    seats = [i for i in range(0, 8, 1)]

    row_code = ticket[:7]
    seat_code = ticket[-3:]

    result = parse_row(row_code, rows)
    row = result[0]

    seat = parse_seat(seat_code, seats)
    column = seat[0]

    id = row * 8 + column

    return [row, column, id]


def parse_row(row_code, range):
    if len(range) == 1:
        return range
    else:
        operator = row_code[:1]

        code = row_code[1:]
        if operator == "F":
            length = int(len(range) / 2)
            result = range[:(length)]
        elif operator == "B":
            length = int(len(range) / 2)
            result = range[(length):]

        return parse_row(code, result)


def parse_seat(seat_code, range):
    if len(range) == 1:
        return range
    else:
        operator = seat_code[:1]

        code = seat_code[1:]
        if operator == "L":
            length = int(len(range) / 2)
            result = range[:(length)]
        elif operator == "R":
            length = int(len(range) / 2)
            result = range[(length):]

        return parse_seat(code, result)


def part_one(data):
    print("Part One")
    max_id = 0
    for line in utils.read_lines(data):
        result = parse_seat_code(line)
        if result[2] >= max_id:
            max_id = result[2]
    print(f"  Max ID: {max_id}")


def part_two(data):
    print("Part Two")
    ids = []
    for line in utils.read_lines(data):
        result = parse_seat_code(line)
        ids.append(int(result[2]))

    ids.sort()

    max = len(ids)
    for index, id in enumerate(ids):
        if index != 0 and index < max - 2:
            forward = int(ids[index + 1])
            back = int(ids[index - 1])

            if int(id) + 1 != forward:
                print(f"  {int(id)+1}")


def test_parse_seat_code():
    row = parse_seat_code("FBFBBFFRLR")
    assert row[0] == 44
    assert row[1] == 5
    assert row[2] == 357

    row = parse_seat_code("BFFFBBFRRR")
    assert row[0] == 70
    assert row[1] == 7
    assert row[2] == 567

    row = parse_seat_code("FFFBBBFRRR")
    assert row[0] == 14
    assert row[1] == 7
    assert row[2] == 119

    row = parse_seat_code("BBFFBBFRLL")
    assert row[0] == 102
    assert row[1] == 4
    assert row[2] == 820


def test_parse_seat():
    seats = [i for i in range(0, 8, 1)]
    seat = parse_seat("RLR", seats)
    assert seat[0] == 5


if __name__ == "__main__":
    data = "data/05.data"
    part_one(data)
    part_two(data)
