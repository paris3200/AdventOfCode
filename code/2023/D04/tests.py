from aoc_04 import split_cards, score_card, part_one, part_two


def test_split_cards_returnts_list() -> None:
    card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert split_cards(card) == [[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]]


def test_score_card_returns_int() -> None:
    card = [[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]]
    assert score_card(card) == 8


def test_part_one_test_data() -> None:
    assert part_one("test_input") == 13


def test_part_one_solution() -> None:
    assert part_one("input") == 21919


def test_part_two_test_data() -> None:
    assert part_two("test_input") == 30


def test_part_two_solution() -> None:
    assert part_two("input") == 9881048
