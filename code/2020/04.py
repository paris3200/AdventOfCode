import utils


class Passport:
    def __init__(self, birth_year, issue_year, expiration_year, height, hair_color, eye_color, id, country_id):
        self.birth_year = birth_year
        self.issue_year = issue_year
        self.expiration_year = expiration_year
        self.height = height
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.id = id
        self.country_id = country_id


def part_one():
    print(f"Part One")


def part_two():
    print(f"Part Two")


def split_line(line):
    line = line.strip("\n")
    fields = line.split(" ")
    return fields


def parse_passports(filename):
    lines = utils.read_lines(filename)
    passports = [0]
    i = 0
    for line in lines:
        breakpoint()
        if line != "\n":
            passports[i] = [i]
            for field in split_line(line):
                passports[i].append(field)
        else:
            i += 1


def test_if_it_works():
    assert True is True


def test_parse_passports():
    result = parse_passports("data/04_tests.data")
    assert result == "foo"


if __name__ == "__main__":

    part_one()
    part_two()
