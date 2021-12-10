from aoc_06 import *


def test_sum_population():
    input = [3, 4, 3, 1, 2]
    result = Model.sum_population(input)
    expected = [0, 1, 1, 2, 1, 0, 0, 0, 0]
    assert result == expected


def test_model_created_with_fish():
    input = [3, 4, 3, 1, 2]
    model = Model(input, days=0)
    assert model.count_fish() == 5


def test_model_run_creates_fish():
    input = [3, 4, 3, 1, 2]
    model = Model(input, days=18)

    result = model.run()
    assert result == 26


def test_model_run_test_data_80_days():
    input = [3, 4, 3, 1, 2]
    model = Model(input, days=80)

    result = model.run()
    assert result == 5934


def test_model_run_test_data_256_days():
    input = [3, 4, 3, 1, 2]
    model = Model(input, days=256)

    result = model.run()
    assert result == 26984457539
