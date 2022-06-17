import pytest

from Y2015 import D03


@pytest.mark.skip()
def test_grid_size():
    assert [1, 0] == D03.grid_size(">")
    assert [2, 2] == D03.grid_size("^>v<")


@pytest.mark.skip()
def test_create_grid():
    assert [[0], [0]] == D03.create_grid([2, 1])
    assert [[0]] == D03.create_grid([1, 1])


@pytest.mark.skip()
def test_count_nonzeros_in_grid():
    assert 1 == D03.count_nonzeros_in_grid([[0], [1]])


@pytest.mark.skip()
def test_deliver_presents():
    assert [[1, 1]] == D03.deliver_presents(">")


@pytest.mark.skip()
def test_part_one():
    result = D03.part_one(">")
    assert result is True


@pytest.mark.skip()
def test_part_two():
    result = D03.part_two(">")
    assert result is True
