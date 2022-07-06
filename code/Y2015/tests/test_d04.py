import pytest

from Y2015 import D04


def test_check_leading_zeros():
    assert D04.check_leading_zeros("00000abcdefg") is True
    assert D04.check_leading_zeros("20000abcdefg") is False


@pytest.mark.skip("Solved")
def test_part_one_with_sample_data():
    assert D04.part_one("abcdef") == 609043
    assert D04.part_one("pqrstuv") == 1048970


@pytest.mark.skip("Solved")
def test_part_one_correct_answer():
    assert D04.part_one() == 254575


@pytest.mark.skip("Solved")
def test_part_two_correct_answer():
    assert D04.part_two() == 1038736
