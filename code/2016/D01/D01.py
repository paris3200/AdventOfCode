from person import Person
from parser import Parser

def part_one():
    parser = Parser("input.txt")
    instructions = parser.to_list()

    person = Person()
    for instruction in instructions:
        person.move(instruction)

    print(person)

def part_two(instructions = None):
    if not instructions:
        parser = Parser("input.txt")
        instructions = parser.to_list()

    person = Person()
    for instruction in instructions:
        print(person.current_pos)
        person.move(instruction)

    return person.distance_traveled()

if __name__ == "__main__":
    part_one()
    print(part_two())


