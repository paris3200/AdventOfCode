import pytest

from person import Person
from D01 import part_two

@pytest.mark.parametrize(
        ("start_direction, rotation, end_direction"),
        (
            ("N", "R", "E"),
            ("N", "L", "W"),
            ("S", "R", "W"),
            ("S", "L", "E"),
            ("E", "R", "S"),
            ("E", "L", "N"),
            ("W", "R", "N"),
            ("W", "L", "S"),
        )
        )
def test_rotate(start_direction, rotation, end_direction):
    person = Person()
    person.direction = start_direction
    person.rotate(rotation)
    assert person.direction ==  end_direction

def test_part_two():
    distance = part_two(["R8", "R4", "R4", "R8"])
    assert distance == 4
