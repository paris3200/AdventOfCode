import pytest

from Y2015 import D08



def test_proccess_str():
    assert D08.process_str("\"\"") == [2, 0]

@pytest.mark.skip()
def test_part_one_with_sample_data():
    pass

@pytest.mark.skip()
def test_part_two_correct_answer():
    pass
