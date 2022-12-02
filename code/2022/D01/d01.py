from collections import defaultdict


def main(file="input") -> None:
    with open(file) as input:
        data = input.readlines()

    elves = defaultdict(int)

    elf_index = 0
    for line in data:
        if line != "\n":
            elves[elf_index] += int(line.strip())
        else:
            elf_index += 1

    calories = list(elves.values())
    calories.sort(reverse=True)

    # Part 1
    print(calories[0])

    # Part 2
    print(sum(calories[:3]))


if __name__ == "__main__":
    main()
