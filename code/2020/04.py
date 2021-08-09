import utils
import re


class Passport:
    def __init__(
        self,
        birth_year=None,
        issue_year=None,
        expiration_year=None,
        height=None,
        hair_color=None,
        eye_color=None,
        id=None,
        country_id=None,
    ):
        self.birth_year = birth_year
        self.issue_year = issue_year
        self.expiration_year = expiration_year
        self.height = height
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.id = id
        self.country_id = country_id

    def is_valid(self, type=None):
        if not type:
            if (
                self.birth_year is not None
                and self.issue_year is not None
                and self.expiration_year is not None
                and self.height is not None
                and self.hair_color is not None
                and self.eye_color is not None
                and self.id is not None
            ):
                return True
        if type == "strict":
            if (
                self.birth_year is not None
                and 2002 >= int(self.birth_year) >= 1920
                and self.issue_year is not None
                and 2020 >= int(self.issue_year) >= 2010
                and self.expiration_year is not None
                and 2030 >= int(self.expiration_year) >= 2020
                and self.height_is_valid() is True
                and self.haircolor_is_valid() is True
                and self.eye_color_is_valid() is True
                and self.id_is_valid() is True
            ):
                return True

    def height_is_valid(self):
        if self.height is None:
            return False
        units = self.height[-2:]
        if units == "cm":
            if 193 >= int(self.height[:-2]) >= 150:
                return True
            else:
                return False

        elif units == "in":
            if 76 >= int(self.height[:-2]) >= 59:
                return True
            else:
                return False
        else:
            return False

    def haircolor_is_valid(self):
        if self.hair_color is None:
            return False

        match = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", self.hair_color)

        if match:
            return True
        else:
            return False

    def eye_color_is_valid(self):
        options = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if self.eye_color is None:
            return False

        for color in options:
            if color == self.eye_color:
                return True

        return False

    def id_is_valid(self):
        if self.id is None:
            return False

        match = re.search(r"\b\d{9}\b", self.id)

        if match:
            return True
        else:
            return False


def part_one(data_file):
    print("Part One")
    valid_passports = validate_passports(data_file)
    print(valid_passports)


def part_two(data_file):
    print("Part Two")
    valid_passports = validate_passports(data_file, type="strict")
    print(valid_passports)


def validate_passports(data_file, type=None):
    passports = create_passports(data_file)

    valid_passports = 0
    for passport in passports:
        if type == "strict":
            if passport.is_valid(type="strict") is True:
                valid_passports += 1
        else:
            if passport.is_valid() is True:
                valid_passports += 1
    return valid_passports


def create_passports(filename):
    passports = parse_passports(filename)

    for index, passport in enumerate(passports):
        passports[index] = parse_fields(passport)

    passport_objects = []
    for passport in passports:
        passport_obj = Passport(
            birth_year=passport["birth_year"],
            issue_year=passport["issue_year"],
            expiration_year=passport["expiration_year"],
            height=passport["height"],
            hair_color=passport["hair_color"],
            eye_color=passport["eye_color"],
            id=passport["passport_id"],
            country_id=passport["country_id"],
        )
        passport_objects.append(passport_obj)

    return passport_objects


def split_line(line):
    line = line.strip("\n")
    fields = line.split(" ")
    return fields


def parse_passports(filename):
    lines = utils.read_lines(filename)
    passports = [[]]
    index = 0
    for line in lines:
        if line != "\n":
            for field in split_line(line):
                passports[index].append(field)
        else:
            index += 1
            passports.append([])

    return passports


def parse_fields(passport: list) -> dict:
    keys = {
        "byr": "birth_year",
        "iyr": "issue_year",
        "eyr": "expiration_year",
        "hgt": "height",
        "hcl": "hair_color",
        "ecl": "eye_color",
        "pid": "passport_id",
        "cid": "country_id",
    }
    attributes = {}
    for field in passport:
        attribute = field.split(":")
        for key, value in keys.items():
            if attribute[0] == key:
                field_name = value
        try:
            attributes[field_name] = attribute[1]
        except:
            print(f"No value found for {attribute[0]}")

    # There has to be a better way
    for key, value in keys.items():
        try:
            if attributes[value] is not None:
                pass
        except KeyError:
            attributes[value] = None

    return attributes


def test_parse_fields():
    passports = parse_passports("data/04_tests.data")
    fields = parse_fields(passports[0])
    expected_result = {
        "eye_color": "gry",
        "passport_id": "860033327",
        "expiration_year": "2020",
        "hair_color": "#fffffd",
        "birth_year": "1937",
        "issue_year": "2017",
        "country_id": "147",
        "height": "183cm",
    }
    assert expected_result == fields


def test_parse_passports():
    result = parse_passports("data/04_tests.data")
    expected_result = [
        "ecl:gry",
        "pid:860033327",
        "eyr:2020",
        "hcl:#fffffd",
        "byr:1937",
        "iyr:2017",
        "cid:147",
        "hgt:183cm",
    ]
    assert expected_result in result


def test_validate_passports():
    result = validate_passports("data/04_tests.data")
    assert result == 2


def test_height_is_valid():
    passport = Passport(height="60in")
    assert passport.height_is_valid() is True
    passport = Passport(height="190cm")
    assert passport.height_is_valid() is True
    passport = Passport(height="190in")
    assert passport.height_is_valid() is False
    passport = Passport(height="190")
    assert passport.height_is_valid() is False


def test_haircolor_is_valid():
    passport = Passport(hair_color="#123abc")
    assert passport.haircolor_is_valid() is True

    passport = Passport(hair_color="#123abz")
    assert passport.haircolor_is_valid() is False

    passport = Passport(hair_color="123abc")
    assert passport.haircolor_is_valid() is False


def test_id_is_valid():
    passport = Passport(id="000000001")
    assert passport.id_is_valid() is True

    passport = Passport(id="0123456789")
    assert passport.id_is_valid() is False


if __name__ == "__main__":

    part_one("data/04.data")
    part_two("data/04.data")
