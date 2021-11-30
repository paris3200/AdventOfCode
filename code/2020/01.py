from utils import read_file


def part_one(data):
    print(f"Part One")
    return multiple_numbers_in_list(get_two_numbers_that_sum(data, 2020))


def get_two_numbers_that_sum(data, sum):
    for num1 in data:
        for num2 in data:
            if num1 + num2 == sum:
                return [num1, num2]


def get_three_numbers_that_sum(data, sum):
    for num1 in data:
        for num2 in data:
            for num3 in data:
                if num1 + num2 + num3 == sum:
                    return [num1, num2, num3]


def multiple_numbers_in_list(data):
    product = 1
    for x in data:
        product *= x
    return product


def part_two(data):
    print(f"Part Two")
    return multiple_numbers_in_list(get_three_numbers_that_sum(data, 2020))


def test_get_two_numbers_that_sum():
    test_data = [1721, 979, 366, 299, 675, 1456]
    assert get_two_numbers_that_sum(test_data, 2020) == [1721, 299]


def test_get_three_numbers_that_sum():
    test_data = [1721, 979, 366, 299, 675, 1456]
    assert get_three_numbers_that_sum(test_data, 2020) == [979, 366, 675]

def test_multiple_numbers():
    assert multiple_numbers_in_list([1721, 299]) == 514579


if __name__ == "__main__":

    data = read_file("data/01.data", "list")
    print(f"  {part_one(data)}")
    print(f"  {part_two(data)}")
