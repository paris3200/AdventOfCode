def get_lines(data) -> str:
    with open(data) as input:
        data = input.readlines()

    lines = []
    for line in data:
        lines.append(line.strip())

    return lines


def get_sections(line) -> list:
    elves = []
    elf1, elf2 = line.split(",")
    elves.append(elf1)
    elves.append(elf2)

    sections = []
    for elf in elves:
        start, end = elf.split("-")
        section = []
        section.extend(range(int(start), int(end) + 1))
        sections.append(section)
    return sections


def is_subset(sections: list) -> bool:
    if set(sections[1]).issubset(set(sections[0])):
        return True
    elif set(sections[0]).issubset(set(sections[1])):
        return True

    return False


def overlap(sections: list) -> bool:
    overlap = any(item in sections[0] for item in sections[1])
    return overlap


def part_one(data="input"):
    data = get_lines(data)

    sections = []
    for line in data:
        sections.append(get_sections(line.strip()))

    contained_sections = 0

    for section in sections:
        if is_subset(section):
            contained_sections += 1

    return contained_sections

def part_two(data="input"):
    data = get_lines(data)

    sections = []
    for line in data:
        sections.append(get_sections(line.strip()))

    contained_sections = 0

    for section in sections:
        if overlap(section):
            contained_sections += 1

    return contained_sections

if __name__ == "__main__":
    print(part_one())
    print(part_two())
