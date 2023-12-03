import pytest

from aoc_02 import (
    Game,
    Hand,
    create_bags,
    game_number,
    process_hand,
    split_hands,
    part_one,
    part_one_dataclass,
    part_two,
)


@pytest.mark.parametrize(
    ("record", "game"),
    (
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 2),
        ("Game 100: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 100),
    ),
)
def test_game_number(record: str, game: int) -> None:
    assert game_number(record) == game


@pytest.mark.parametrize(
    ("record", "rounds"),
    (
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"],
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            ["1 blue, 2 green", "3 green, 4 blue, 1 red", "1 green, 1 blue"],
        ),
    ),
)
def test_split_hands(record: str, rounds: list[str]) -> None:
    assert split_hands(record) == rounds


@pytest.mark.parametrize(
    ("hand", "result"),
    (
        (
            "3 blue, 4 red",
            Hand(4, 3, 0),
        ),
    ),
)
def test_process_hands(hand: str, result: dict[str, int]) -> None:
    assert process_hand(hand) == result


def test_create_bags() -> None:
    hands = []
    hands.append(Hand(4, 3, 0))
    hands.append(Hand(1, 6, 2))
    hands.append(Hand(0, 0, 2))
    games = []
    games.append(Game(1, hands))

    assert (
        create_bags(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]) == games
    )


def test_part_one_with_test_input() -> None:
    assert part_one("test_input") == 8


def test_part_one_with_real_input() -> None:
    assert part_one("input") == 1867


def test_part_one_with_data_class() -> None:
    assert part_one_dataclass("input") == 1867


def test_part_two_with_test_input() -> None:
    assert part_two("test_input") == 2286
