from Y2015 import D02


def test_calculate_smallest_perimeter():
    assert 10 == D02.calculate_smallest_perimeter(2, 3, 4)
    assert 4 == D02.calculate_smallest_perimeter(1, 1, 10)


def test_calculate_surface_area():
    assert 52 == D02.calculate_surface_area(2, 3, 4)
    assert 42 == D02.calculate_surface_area(1, 1, 10)


def test_calculate_smallest_area():
    assert 6 == D02.calculate_smallest_area(2, 3, 4)
    assert 1 == D02.calculate_smallest_area(1, 1, 10)


def test_calculate_wrapping_paper():
    assert D02.calculate_wrapping_paper(2, 3, 4) == 58


def test_caculate_ribbon():
    assert 34 == D02.calculate_ribbon(2, 3, 4)


def test_part_one():
    data = "data/02.data"
    result = D02.part_one(data)
    assert 1606483 == result


def test_part_two():
    data = "data/02.data"
    result = D02.part_two(data)
    assert result == 3842356
