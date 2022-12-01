from collections import defaultdict

with open("input") as input:
    data = input.readlines()

elves = defaultdict(int)


elf_index = 0
most_calories = 0
for line in data:
    if line != "\n":
        elves[elf_index] += int(line.strip())
    else:
        if elves[elf_index] > most_calories:
            most_calories = elves[elf_index]
        elf_index += 1

print(most_calories)
