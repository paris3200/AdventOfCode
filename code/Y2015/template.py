import pytest
import utils


def part_one(data):
    pass


def part_two(data):
    pass


@pytest.mark.skip
def test_part_one():
    result = part_one(data)
    assert result is True

@pytest.mark.skip
def test_part_two():
    result = part_two(data)
    assert result is True


if __name__ == "__main__":
    data = "../data/xx.data"
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
