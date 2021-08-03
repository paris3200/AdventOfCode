import utils


def part_one(data):
    print(f"Part One")
    valid = 0
    for line in data:
        if validate_password(line):
            valid += 1
    return(valid)


def part_two(data):
    print(f"Part Two")
    valid = 0
    for line in data:
        if validate_corporate_password(line):
            valid += 1
    return(valid)


def validate_password(line):
    min, max = get_max_min_occurances(line)
    char = get_character(line)
    password = line.split(":")[1]

    occurances = password.count(char)

    if occurances >= min and occurances <= max:
        return True


def validate_corporate_password(line):
    min, max = get_max_min_occurances(line)
    char = get_character(line)
    password = line.split(":")[1].strip()

    if password[min-1] is char and password[max-1] is not char:
        return True
    if password[min-1] is not char and password[max-1] is char:
        return True



def get_max_min_occurances(data):
    min = int(data.split("-")[0])
    max = data.split("-")[1]
    max = int(max.split(" ")[0])

    return [min, max]


def get_character(data):
    char = data.split(":")[0]
    char = char.split(" ")[1]
    return(char)


def test_validate_password():
    test_data = "1-3 a: abcde"
    assert True is validate_password(test_data)
    test_data = "1-3 b: cdefg"
    assert None is validate_password(test_data)


def test_part_one():
    test_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert 2 == part_one(test_data)


def test_part_two():
    test_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert 1 == part_two(test_data)


def test_get_max_min_occurances():
    assert get_max_min_occurances("1-3 a: abcde") == [1, 3]


def test_get_character():
    assert get_character("1-3 a: abcde") == "a"


if __name__ == "__main__":
    with open("data/02.data") as f:
        data = f.readlines()

    print(part_one(data))
    print(part_two(data))
