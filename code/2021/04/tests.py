import pytest

from aoc_d4 import BingoCard
from aoc_d4 import Bingo


def test_card_with_bingo_marked_bingo_and_scored():
    card = [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    board = BingoCard()
    for line in card:
        board.add_row(line)
    numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]
    for num in numbers:
        board.mark_number(num)

    assert board.bingo is True
    assert board.get_score() == 4512

    matched = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]

    assert board.matched == matched


def test_bingocard_sums():
    card = [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    board = BingoCard()
    for line in card:
        board.add_row(line)

    assert board.get_sum() == 325
    board.matched = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert board.get_sum() == 302


def test_bingo_in_coumns():
    card = [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    board = BingoCard()
    for line in card:
        board.add_row(line)
    numbers = [4, 19, 20, 5, 7]
    for num in numbers:
        board.mark_number(num)

    assert board.bingo is True

    card = [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    board = BingoCard()
    for line in card:
        board.add_row(line)
    numbers = [24, 9, 26, 6, 3]
    for num in numbers:
        board.mark_number(num)

    assert board.bingo is True

    card = [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    board = BingoCard()
    for line in card:
        board.add_row(line)
    numbers = [17, 15, 23, 13, 12]
    for num in numbers:
        board.mark_number(num)

    assert board.bingo is True

    card = [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    board = BingoCard()
    for line in card:
        board.add_row(line)
    numbers = [21, 16, 8, 11, 0]
    for num in numbers:
        board.mark_number(num)
    assert board.bingo is True


def test_part_one_with_sample_data():
    data = "data/04_test.data"
    game = Bingo(data)
    game.play()
    board = game.winner
    assert board.get_score() == 4512
    assert board.get_sum() == 188
    assert board.last_number == 24


def test_Bingo_with_sample_data_v2():
    data = "data/04_tests_v2.data"
    game = Bingo(data)
    game.play()
    board = game.winner
    assert board.get_score() == 4862
    assert board.get_sum() == 187
    assert board.last_number == 26


def test_part_two_with_sample_data():
    data = "data/04_test.data"
    game = Bingo(data)
    pool = [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]
    assert game.number_pool == pool
    game.play()
    board = game.loser
    assert board.matched_numbers == [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
    ]
    loser_card = [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ]
    matched = [
        [0, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0],
    ]
    assert board.card == loser_card
    assert board.last_number == 13
    assert board.get_sum() == 148
    assert board.get_score() == 1924


def test_board_gets_bingo():
    card = [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ]
    matched = [
        [0, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0],
    ]
    numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13]

    board = BingoCard()
    for line in card:
        board.add_row(line)
    for num in numbers:
        board.mark_number(num)
    assert board.bingo is True
    assert board.matched == matched


def test_mark_number():
    card = [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ]
    board = BingoCard()
    for line in card:
        board.add_row(line)

    board.mark_number(16)
    matched = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
    ]
    assert board.matched == matched


def test_numbers_matched_not_equal_to_numbers_played():
    card = [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ]
    board = BingoCard()
    for line in card:
        board.add_row(line)
    numbers = [1, 2, 3, 15, 18, 12, 99]
    for num in numbers:
        board.mark_number(num)

    assert board.checked_numbers != board.matched_numbers
