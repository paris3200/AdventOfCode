import utils

def calculate_surface_area(s1: int, s2: int, s3: int) -> int:
    """Returns the surface area of a right rectangular prism."""
    return (2*(s1*s2) + 2*(s1*s3) + 2*(s2*s3))


def calculate_smallest_area(s1: int, s2: int, s3: int) -> int:
    """Returns the surface are of the smallest side of a right rectangular prism."""
    area = []
    area.append(s1*s2)
    area.append(s1*s3)
    area.append(s2*s3)

    return min(area)


def calculate_smallest_perimeter(s1: int, s2: int, s3:int):
    """Calculates the smallest path around a right rectangular prisim."""
    sides = [s1, s2, s3]
    sides.remove(max(sides))
    return sides[0]*2+sides[1]*2


def calculate_wrapping_paper(s1: int, s2: int, s3: int) -> int:
    """Returns amount of wrapping paper needed for a box."""
    return calculate_surface_area(s1, s2, s3) + calculate_smallest_area(s1, s2, s3)


def calculate_perimeter(s1: int, s2: int) -> int:
    return s1+s1+s2+s2

def calculate_ribbon(s1: int, s2: int, s3: int):
    return calculate_smallest_perimeter(s1, s2, s3) + (s1*s2*s3)

def process_input(filename: str):
    data = utils.read_lines(filename)
    dimensions = []
    for box in data:
        dimensions_strings = box.split("x")
        dimensions.append([int(x) for x in dimensions_strings])
    return dimensions


def part_one(data):
    boxes = process_input(data)
    sum = 0
    for box in boxes:
        sum += calculate_wrapping_paper(box[0], box[1], box[2])
    return sum


def part_two(data):
    boxes = process_input(data)
    sum = 0
    for box in boxes:
        sum += calculate_ribbon(box[0], box[1], box[2])
    return sum


def test_calculate_smallest_perimeter():
    assert 10 == calculate_smallest_perimeter(2, 3, 4)
    assert 4 == calculate_smallest_perimeter(1, 1, 10)


def test_calculate_surface_area():
    assert 52 == calculate_surface_area(2, 3, 4)
    assert 42 == calculate_surface_area(1, 1, 10)


def test_calculate_smallest_area():
    assert 6 == calculate_smallest_area(2, 3, 4)
    assert 1 == calculate_smallest_area(1, 1, 10)


def test_calculate_wrapping_paper():
    assert calculate_wrapping_paper(2, 3, 4) == 58

def test_caculate_ribbon():
    assert 34 == calculate_ribbon(2, 3, 4)

def test_part_one():
    data = "../data/02.txt"
    result = part_one(data)
    assert 1606483 == result


def test_part_two():
    result = part_two()
    assert result is True


if __name__ == "__main__":
    data = "../data/02.txt"
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
