import string


def get_lines() -> str:
    with open("input") as input:
        data = input.readlines()

    lines = []
    for line in data:
        lines.append(line.strip())

    return lines


def load_sack(line: str) -> str:
    split = int(len(line) / 2)
    compartment1, compartment2 = line[:split], line[split:]
    commmon_item = "".join(set(compartment1).intersection(compartment2))

    return commmon_item


def get_badge(group: list) -> str:
    commmon_item = "".join(set(group[0]).intersection(group[1]))
    badge = "".join(set(commmon_item).intersection(group[2]))

    return badge


def get_priority(item: str) -> int:
    return string.ascii_letters.index(item) + 1


def part_one(data=None) -> int:
    if data is None:
        data = get_lines()

    items = []
    for line in data:
        items.append(load_sack(line))

    sum = 0
    for item in items:
        sum += get_priority(item)
    return sum


def part_two(data=None) -> int:
    if data is None:
        data = get_lines()

    sum = 0
    badges = []

    for index, item in enumerate(data, start=1):
        if index % 3 == 0:
            group = [data[index - 1], data[index - 2], data[index - 3]]
            badges.append(get_badge(group))

    for badge in badges:
        sum += get_priority(badge)

    return sum


if __name__ == "__main__":
    print(part_one())
    print(part_two())
