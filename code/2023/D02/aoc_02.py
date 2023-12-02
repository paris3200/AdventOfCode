import re

from dataclasses import dataclass


@dataclass
class Hand:
    red: int
    blue: int
    green: int


@dataclass
class Game:
    id: int
    hands: list[Hand]


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")
    return data


def game_number(game: str) -> int:
    line_parts = game.split(":")
    game_id = int(line_parts[0].split(" ")[1])
    return game_id


def split_hands(game: str) -> list[str]:
    line_parts = game.split(":")
    game_list = line_parts[1].split(";")
    for index, item in enumerate(game_list):
        game_list[index] = item.strip()
    return game_list


def process_hand(hand: str) -> dict[str:int]:
    red = re.search(r"(\d+)\s+(?=red)", hand)
    blue = re.search(r"(\d+)\s+(?=blue)", hand)
    green = re.search(r"(\d+)\s+(?=green)", hand)

    if not red:
        red = 0
    else:
        red = int(red.group(1))

    if not green:
        green = 0
    else:
        green = int(green.group(1))

    if not blue:
        blue = 0
    else:
        blue = int(blue.group(1))

    return Hand(red, blue, green)


def create_bags(games: list[str]) -> list[Game]:
    game_bag = []

    for game in games:
        hands = []
        id = game_number(game)

        hands_str = split_hands(game)
        for hand in hands_str:
            hands.append(process_hand(hand))

        game_bag.append(Game(id, hands))

    return game_bag


def part_one(filename: str) -> int:
    lines = read_lines(filename)
    sum_id = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    possible_games = []
    for line in lines:
        game_id = game_number(line)
        valid = True
        reds = re.findall(r"(\d+)\s+(?=red)", line)
        blues = re.findall(r"(\d+)\s+(?=blue)", line)
        greens = re.findall(r"(\d+)\s+(?=green)", line)

        for red in reds:
            if int(red) > max_red:
                valid = False

        for blue in blues:
            if int(blue) > max_blue:
                valid = False
        for green in greens:
            if int(green) > max_green:
                valid = False

        if valid is True:
            sum_id += game_number(line)
            possible_games.append(game_id)

    return sum_id


def part_one_dataclass(filename: str) -> int:
    lines = read_lines(filename)
    games = create_bags(lines)

    max_red = 12
    max_green = 13
    max_blue = 14
    sum_ids = 0

    possible_games = []

    for game in games:
        hands_possible = []
        for hand in game.hands:
            if (
                max_red >= hand.red
                and max_blue >= hand.blue
                and max_green >= hand.green
            ):
                hands_possible.append(True)
            else:
                hands_possible.append(False)

        if len(set(hands_possible)) == 1 and hands_possible[0] is True:
            possible_games.append(game.id)
            sum_ids += game.id
    return sum_ids


def part_two(filename: str) -> int:
    lines = read_lines(filename)
    sum_id = 0
    max_red = 0
    max_green = 0
    max_blue = 0
    for line in lines:
        reds = re.findall(r"(\d+)\s+(?=red)", line)
        blues = re.findall(r"(\d+)\s+(?=blue)", line)
        greens = re.findall(r"(\d+)\s+(?=green)", line)

        for red in reds:
            if int(red) > max_red:
                max_red = int(red)

        for blue in blues:
            if int(blue) > max_blue:
                max_blue = int(blue)
        for green in greens:
            if int(green) > max_green:
                max_green = int(green)

        sum_id += max_red * max_green * max_blue

        max_red = 0
        max_green = 0
        max_blue = 0

    return sum_id


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
