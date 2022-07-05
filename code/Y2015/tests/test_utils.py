from Y2015.utils import Grid


def test_grid_is_created_with_proper_dimensions():
    grid = Grid(5, 5)
    assert grid.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

def test_grid_is_created_with_proper_x_dimensions():
    grid = Grid(3, 5)
    assert grid.grid == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

def test_turn_on_point():
    grid = Grid(5, 5)
    grid.turn_on_point(2, 4)
    assert grid.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
    ]


def test_turn_off_point():
    grid = Grid(5, 5)
    grid.turn_on_point(2, 4)
    grid.turn_off_point(2, 4)
    assert grid.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_toggle_point():
    grid = Grid(5, 5)
    grid.toggle_point(1, 4)
    assert grid.grid == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
    ]


def test_stats():
    grid = Grid(5, 5)
    grid.toggle_point(1, 4)
    grid.toggle_point(4, 4)
    stats = grid.stats()
    assert stats['on'] == 2
