import pytest
from d02 import play_round, decrypt_guide, score_round, get_needed_shape


@pytest.mark.parametrize(
    ("p1", "p2", "expected"),
    (
        ("S", "R", "win"),
        ("P", "S", "win"),
        ("R", "P", "win"),
        ("R", "S", "lose"),
        ("S", "P", "lose"),
        ("P", "R", "lose"),
        ("R", "R", "tie"),
        ("S", "S", "tie"),
        ("P", "P", "tie"),
    ),
)
def test_play_round(p1, p2, expected) -> None:
    assert play_round(p1, p2) == expected


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("A Y", "R P"),
        ("B X", "P R"),
        ("C Z", "S S"),
    ),
)
def test_decrypt_guide(line, expected) -> None:
    assert decrypt_guide(line) == expected


@pytest.mark.parametrize(
    ("shape", "outcome", "expected"),
    (
        ("S", "win", 9),
        ("R", "win", 7),
        ("S", "tie", 6),
    ),
)
def test_score_round(shape, outcome, expected) -> None:
    assert score_round(shape, outcome) == expected


@pytest.mark.parametrize(
    ("shape", "outcome", "expected"),
    (
        ("S", "win", "R"),
        ("S", "lose", "P"),
        ("R", "win", "P"),
        ("R", "lose", "S"),
        ("S", "tie", "S"),
        ("S", "win", "R"),
        ("S", "lose", "P"),
    ),
)
def test_score_round(shape, outcome, expected) -> None:
    assert get_needed_shape(shape, outcome) == expected
