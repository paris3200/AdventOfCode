def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def get_stronger(hand_1: str, hand_2: str, wildcard: bool = False) -> str:
    if wildcard:
        order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    else:
        order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    for x in range(0, len(hand_1)):
        hand_1_index = order.index(hand_1[x])
        hand_2_index = order.index(hand_2[x])
        if hand_1_index != hand_2_index:
            if hand_1_index < hand_2_index:
                return [hand_1, hand_2]
            else:
                return [hand_2, hand_1]


def get_five_of_a_kind(hands: list[str], wild: bool = False) -> list[str]:
    matches = []
    for hand in hands:
        unique_cards = list(set(hand))
        if len(unique_cards) == 1:
            matches.append(hand)

        if len(unique_cards) == 2 and wild is True:
            if "J" in unique_cards:
                matches.append(hand)

    return matches


def get_four_of_a_kind(hands: list[str], wildcard: bool = False) -> list[str]:
    matches = []
    for hand in hands:
        unique_cards = list(set(hand))
        if len(unique_cards) == 2:
            if hand.count(unique_cards[0]) == 4 or hand.count(unique_cards[1]) == 4:
                matches.append(hand)

        if wildcard is True:
            if "J" in hand:
                if len(unique_cards) == 3:
                    card_count = []
                    for card in unique_cards:
                        card_count.append(hand.count(card))
                    card_count.sort()
                    if (card_count.pop() == 3) or (hand.count("J") >= 2):
                        matches.append(hand)

    return matches


def get_full_house(hands: list[str], wildcard: bool = False) -> list[str]:
    matches = []
    for hand in hands:
        unique_cards = list(set(hand))
        if len(unique_cards) == 2:
            card_count = []
            for card in unique_cards:
                card_count.append(hand.count(card))
            card_count.sort()
            if card_count.pop() == 3 and card_count.pop() == 2:
                matches.append(hand)

        if len(unique_cards) == 3 and wildcard:
            card_count = []
            for card in unique_cards:
                card_count.append(hand.count(card))
            card_count.sort()

            if card_count.pop() <= 2 and "J" in hand:
                matches.append(hand)

    return matches


def get_three_of_a_kind(hands: list[str], wildcard: bool = False) -> list[str]:
    matches = []
    for hand in hands:
        unique_cards = list(set(hand))
        if len(unique_cards) == 3:
            for card in unique_cards:
                if hand.count(card) == 3:
                    matches.append(hand)
        if wildcard and "J" in hand:
            if len(unique_cards) == 4:
                card_count = []
                for card in unique_cards:
                    card_count.append(hand.count(card))
                card_count.sort()
                most_cards = card_count.pop()
                if most_cards <= 2 or hand.count("J") >= 2:
                    matches.append(hand)

    return matches


def get_two_pair(hands: list[str], wildcard: bool = False) -> list[str]:
    matches = []
    for hand in hands:
        unique_cards = list(set(hand))
        if len(unique_cards) == 3:
            card_count = []
            for card in unique_cards:
                card_count.append(hand.count(card))
            card_count.sort()

            if card_count.pop() == card_count.pop():
                matches.append(hand)

        if len(unique_cards) == 4 and wildcard and "J" in hand:
            card_count = []
            for card in unique_cards:
                card_count.append(hand.count(card))
            card_count.sort()

            if card_count.pop() == 2 and card_count.pop() == 1:
                matches.append(hand)
    return matches


def get_pairs(hands: list[str], wildcard: bool = False) -> list[str]:
    matches = []
    for hand in hands:
        unique_cards = list(set(hand))
        if len(unique_cards) == 4:
            for card in unique_cards:
                if hand.count(card) == 2:
                    matches.append(hand)

        if wildcard and "J" in hand:
            if len(unique_cards) == 5:
                matches.append(hand)

    return matches


def get_high_cards(hands: list[str], wildcard: bool = False) -> list[str]:
    matches = []
    for hand in hands:
        unique_cards = list(set(hand))
        if len(unique_cards) == 5 and not wildcard:
            matches.append(hand)
        if len(unique_cards) == 5 and "J" not in hand and wildcard:
            matches.append(hand)

    return matches


def bubble_sort(hands: list[str], wildcard: bool = False) -> list[str]:
    length = len(hands)

    for i in range(length):
        for j in range(0, length - i - 1):
            high, low = get_stronger(hands[j], hands[j + 1], wildcard)
            hands[j], hands[j + 1] = high, low

    return hands


def part_one(filename: str):
    lines = read_lines(filename)

    hand = []
    for line in lines:
        hand.append(line.split(" ")[0])

    fives = bubble_sort(get_five_of_a_kind(hand))
    fours = bubble_sort(get_four_of_a_kind(hand))
    full_house = bubble_sort(get_full_house(hand))
    threes = bubble_sort(get_three_of_a_kind(hand))
    two_pairs = bubble_sort(get_two_pair(hand))
    pairs = bubble_sort(get_pairs(hand))
    high_cards = bubble_sort(get_high_cards(hand))

    sorted_cards = []
    sorted_cards.extend(fives)
    sorted_cards.extend(fours)
    sorted_cards.extend(full_house)
    sorted_cards.extend(threes)
    sorted_cards.extend(two_pairs)
    sorted_cards.extend(pairs)
    sorted_cards.extend(high_cards)

    sorted_cards.reverse()

    total_winnings = 0
    for rank, card in enumerate(sorted_cards):
        for line in lines:
            hand, bid = line.split(" ")
            if card == hand:
                total_winnings += (int(rank) + 1) * int(bid)

    return total_winnings


def remove_allocated(input_list: list[str], removal_list: list[str]) -> list[str]:
    for hand in removal_list:
        input_list.remove(hand)

    return input_list


def part_two(filename: str):
    lines = read_lines(filename)
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

    high_cards = get_high_cards(hands)

    sorted_cards = []
    sorted_cards.extend(bubble_sort(fives, True))
    sorted_cards.extend(bubble_sort(fours, True))
    sorted_cards.extend(bubble_sort(full_house, True))
    sorted_cards.extend(bubble_sort(threes, True))
    sorted_cards.extend(bubble_sort(two_pairs, True))
    sorted_cards.extend(bubble_sort(pairs, True))
    sorted_cards.extend(bubble_sort(high_cards, True))

    sorted_cards.reverse()

    total_winnings = 0
    for rank, card in enumerate(sorted_cards):
        for line in lines:
            hand, bid = line.split(" ")
            if card == hand:
                total_winnings += (int(rank) + 1) * int(bid)

    return total_winnings


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
