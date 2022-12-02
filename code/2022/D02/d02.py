def part_one(file="input") -> None:
    with open(file) as input:
        data = input.readlines()

    decrypted_lines = []
    for line in data:
        decrypted_lines.append(decrypt_guide(line.strip()))

    score = 0
    for line in decrypted_lines:
        p1, p2 = line.split(" ")
        outcome = play_round(p1, p2)

        score += score_round(p2, outcome)

    print(score)


def part_two(file="input") -> None:
    with open(file) as input:
        data = input.readlines()

    decrypted_lines = []
    key = {"X": "lose", "Y": "tie", "Z": "win"}
    for line in data:
        p1, outcome = line.strip().split(" ")
        p1 = decrypt_player_one(p1)
        outcome = decrypt_player_two(outcome, key)
        p2 = get_needed_shape(p1, outcome)
        decrypted_lines.append(f"{p1} {p2}")


    score = 0
    for line in decrypted_lines:
        p1, p2 = line.split(" ")
        outcome = play_round(p1, p2)

        score += score_round(p2, outcome)

    print(score)

def decrypt_guide(line: str) -> str:
    p1, p2 = line.split(" ")
    key = {"X": "R", "Y": "P", "Z": "S"}
    p1_decoded = decrypt_player_one(p1)
    p2_decoded = decrypt_player_two(p2, key)

    return f"{p1_decoded} {p2_decoded}"


def decrypt_player_one(p1: str) -> str:
    key = {"A": "R", "B": "P", "C": "S"}
    return key[p1]


def decrypt_player_two(player: str, key: dict) -> str:
    return key[player]


def play_round(p1: int, p2: int) -> str:
    if p1 == "S" and p2 == "R":
        # Rock beats Scissors
        return "win"
    elif p1 == "P" and p2 == "S":
        # Scissors beats Paper
        return "win"
    elif p1 == "R" and p2 == "P":
        # Paper beats Rock
        return "win"
    elif p1 == p2:
        return "tie"
    else:
        return "lose"


def get_needed_shape(p1: str, outcome: str) -> str:
    if outcome == "tie":
        return p1

    if p1 == "R":
        if outcome == "win":
            shape = "P"
        elif outcome == "lose":
            shape = "S"
    elif p1 == "P":
        if outcome == "win":
            shape = "S"
        elif outcome == "lose":
            shape = "R"
    elif p1 == "S":
        if outcome == "win":
            shape = "R"
        elif outcome == "lose":
            shape = "P"

    return shape


def score_round(shape: str, outcome: str) -> int:
    if shape == "R":
        shape_score = 1
    elif shape == "P":
        shape_score = 2
    elif shape == "S":
        shape_score = 3

    if outcome == "win":
        outcome_score = 6
    elif outcome == "tie":
        outcome_score = 3
    else:
        outcome_score = 0

    return shape_score + outcome_score


if __name__ == "__main__":
    part_one()
    part_two()
