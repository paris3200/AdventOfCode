from aoc_07 import (
    get_four_of_a_kind,
    get_three_of_a_kind,
    get_two_pair,
    get_pairs,
    get_high_cards,
    read_lines,
    get_five_of_a_kind,
    get_full_house,
    get_stronger,
    part_one,
    part_two,
    remove_allocated,
    bubble_sort,
)


def test_all_lines_are_accounted_for() -> None:
    lines = read_lines("input")
    hands = []
    for line in lines:
        hands.append(line.split(" ")[0])

    fives = get_five_of_a_kind(hands)
    fours = get_four_of_a_kind(hands)
    full_house = get_full_house(hands)
    threes = get_three_of_a_kind(hands)
    two_pairs = get_two_pair(hands)
    pairs = get_pairs(hands)
    high_cards = get_high_cards(hands)

    count = (
        len(fives)
        + len(fours)
        + len(full_house)
        + len(threes)
        + len(two_pairs)
        + len(pairs)
        + len(high_cards)
    )
    assert count == len(lines)


def test_all_lines_are_accounted_for_wildcard() -> None:
    lines = read_lines("input")
    hands = []
    for line in lines:
        hands.append(line.split(" ")[0])

    fives = get_five_of_a_kind(hands, True)
    hands = remove_allocated(hands, fives)

    fours = get_four_of_a_kind(hands, True)
    hands = remove_allocated(hands, fours)

    full_house = get_full_house(hands, True)
    hands = remove_allocated(hands, full_house)

    threes = get_three_of_a_kind(hands, True)
    hands = remove_allocated(hands, threes)

    two_pairs = get_two_pair(hands, True)
    hands = remove_allocated(hands, two_pairs)

    pairs = get_pairs(hands, True)
    hands = remove_allocated(hands, pairs)

    high_cards = get_high_cards(hands, True)
    hands = remove_allocated(hands, high_cards)

    count = (
        len(fives)
        + len(fours)
        + len(full_house)
        + len(threes)
        + len(two_pairs)
        + len(pairs)
        + len(high_cards)
    )
    assert count == len(lines)


def test_all_lines_are_accounted_for_wildcard_test_input() -> None:
    lines = read_lines("test_input")
    hands = []
    for line in lines:
        hands.append(line.split(" ")[0])

    fives = get_five_of_a_kind(hands, True)
    hands = remove_allocated(hands, fives)

    fours = get_four_of_a_kind(hands, True)
    fours = bubble_sort(fours, True)
    fours.reverse()

    assert fours == ["T55J5", "QQQJA", "KTJJT"]
    hands = remove_allocated(hands, fours)

    full_house = get_full_house(hands, True)
    hands = remove_allocated(hands, full_house)

    threes = get_three_of_a_kind(hands, True)
    assert threes == []
    hands = remove_allocated(hands, threes)

    two_pairs = get_two_pair(hands, True)
    assert two_pairs == ["KK677"]
    hands = remove_allocated(hands, two_pairs)

    pairs = get_pairs(hands, True)
    hands = remove_allocated(hands, pairs)

    high_cards = get_high_cards(hands, True)
    hands = remove_allocated(hands, high_cards)

    count = (
        len(fives)
        + len(fours)
        + len(full_house)
        + len(threes)
        + len(two_pairs)
        + len(pairs)
        + len(high_cards)
    )
    assert count == len(lines)


def test_get_stronger() -> None:
    assert get_stronger("KK677", "KTJJT") == ["KK677", "KTJJT"]
    assert get_stronger("KTJJT", "KK677") == ["KK677", "KTJJT"]


def test_part_one() -> None:
    assert part_one("test_input") == 6440
    assert part_one("input") != 289783073
    assert part_one("input") == 248836197


def test_part_two() -> None:
    assert part_two("test_input") == 5905
    assert part_two("input") != 249909933
    assert part_two("input") != 250723382
    assert part_two("input") != 250958498  # Too Low
    assert part_two("input") != 248571883
    assert part_two("input") == 251195607


def test_get_five_of_a_kind_wildcard() -> None:
    assert get_five_of_a_kind(["JJKJJ", "22222"], True) == ["JJKJJ", "22222"]
    assert get_five_of_a_kind(["KTJJT"], True) == []


def test_get_four_of_a_kind_wildcard() -> None:
    assert get_four_of_a_kind(["AA8JA"], True) == ["AA8JA"]
    assert get_four_of_a_kind(["KTJJT"], True) == ["KTJJT"]


def test_get_full_house_wildcard() -> None:
    assert get_full_house(["KKAQQ", "KKJQQ"], True) == ["KKJQQ"]


def test_get_three_of_a_kind_wildcard() -> None:
    assert get_three_of_a_kind(["KKJ45", "KKJQQ"], True) == ["KKJ45"]
    assert get_three_of_a_kind(["Q525J"], True) == ["Q525J"]
    assert get_three_of_a_kind(["32T3K"], True) == []


def test_get_two_pair() -> None:
    test_hands = ["KKJ45", "KK677"]
    assert get_two_pair(test_hands, True) == ["KKJ45", "KK677"]
