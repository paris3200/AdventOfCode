from dataclasses import dataclass
import re


@dataclass
class Card:
    id: int
    matches: int


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")
    return data


def game_number(card: str) -> int:
    card = re.sub(" +", " ", card)
    line_parts = card.split(":")
    game_id = line_parts[0].split(" ")[1]
    return int(game_id)


def split_cards(card: str) -> list[str]:
    line_parts = card.split(":")
    card_list = line_parts[1].split(" | ")

    card_list[0] = card_list[0].replace("  ", " ")
    card_list[1] = card_list[1].replace("  ", " ")

    for index, side in enumerate(card_list):
        card_list[index] = side.strip().split(" ")

        for y, num in enumerate(card_list[index]):
            card_list[index][y] = int(num.strip())

    return card_list


def get_matches(card: list[list[int]]) -> list[int]:
    winning_numbers = card[0]
    card_numbers = card[1]

    matched_numbers = []
    for num in winning_numbers:
        if num in card_numbers:
            matched_numbers.append(num)

    return matched_numbers


def score_card(card: list[list[int]]) -> int:
    matched_numbers = get_matches(card)
    score = 0
    number_of_matches = len(matched_numbers)

    if number_of_matches == 0:
        return 0
    else:
        score = 1
        number_of_matches -= 1

    while number_of_matches > 0:
        score = score * 2
        number_of_matches -= 1

    return score


def part_one(filename: str) -> int:
    lines = read_lines(filename)
    cards = []
    for card in lines:
        cards.append(split_cards(card))

    total_score = 0
    for card in cards:
        total_score += score_card(card)

    return total_score


# Do not do this.  Took 30 minutes to solve.
def part_two(filename: str):
    lines = read_lines(filename)
    cards = []
    for card in lines:
        game_id = game_number(card)
        matches = get_matches(split_cards(card))
        cards.append(Card(id=game_id, matches=len(matches)))

    hand = cards.copy()
    total_cards = 0

    card_counts = {}
    for card in hand:
        card_counts[card.id] = 0

    while len(hand) != 0:
        card = hand.pop(0)
        id = card.id
        matches = card.matches

        current_card = id
        while matches > 0:
            hand.append(cards[current_card])
            card_counts[cards[current_card].id] += 1
            matches -= 1
            current_card += 1

        total_cards += 1

    return total_cards


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
