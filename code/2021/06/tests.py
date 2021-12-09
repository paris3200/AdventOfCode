from aoc_06 import Fish, Model


def test_fish_created_with_default_timer_of_8():
    fish = Fish()
    assert fish.timer == 8


def test_fish_created_with_non_default_timer():
    fish = Fish(5)
    assert fish.timer == 5


def test_fish_age_decreases_timer_by_one():
    fish = Fish()
    fish.age()

    assert fish.timer == 7


def test_fish_age_returns_new_fish_if_timer_is_zero():
    fish = Fish(timer=0)
    result = fish.age()
    assert result.timer == 8


def test_fish_age_sets_timer_to_6_if_timer_is_zero():
    fish = Fish(timer=0)
    fish.age()
    assert fish.timer == 6

def test_model_created_with_no_fish():
    model = Model()
    assert model.count_fish() == 0


def test_adding_fish_increases_count():
    model = Model()
    fish = Fish()
    model.add_fish(fish)

    assert model.count_fish() == 1


def test_model_created_with_fish():
    model = Model([3, 4, 3, 1, 2])
    assert model.count_fish() == 5

def test_model_run_creates_fish():
    model = Model([3, 4, 3, 1, 2], days=3)
    model.run()

    assert model.count_fish() == 7


def test_model_problem_set_18_days():
    model = Model([3, 4, 3, 1, 2], days=18)
    model.run()

    assert model.count_fish() == 26

def test_model_problem_set_18_days():
    model = Model([3, 4, 3, 1, 2], days=80)
    model.run()

    assert model.count_fish() == 5934
