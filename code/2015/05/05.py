import re
import pytest
import string

import utils


def check_three_vowels(text: str) -> bool:
    """Checks if the input text has 3 or more vowels [aeiou]."""
    result = re.search("^(.*[aeuio].*){3,}$", text)
    if result:
        return True
    else:
        return False


def check_repeat_characters(text: str) -> bool:
    """Checks if two characters repeat one after another in the text."""
    chars = list(string.ascii_lowercase)
    for char in chars:
        regex_str = char + "{2}"
        result = re.search(regex_str, text)
        if result:
            return True
    return False


def check_forbidden_characters(text: str) -> bool:
    """Checks if the forbidden characters are found in the text."""
    forbidden_characters = ["ab", "cd", "pq", "xy"]

    for chars in forbidden_characters:
        result = re.search(chars, text)
        if result:
            return True
    return False


def check_letter_pairs(text: str) -> bool:
    """Checks if a pair of letters occurs twice in the text without overlapping."""
    result = re.search("(\\w{2}).*?(\\1)", text)
    if result:
        return True
    else:
        return False


def check_single_letter_repeat_with_single_char_between(text: str) -> bool:
    """Returns true if a single letter is repeated in the string with exactly one character between the repeats."""
    result = re.search("(\\w)\\w{1}?(\\1)", text)
    if result:
        return True
    else:
        return False


def check_nice_words(text: str, version="1.0") -> bool:
    """Returns True for nice words, False for naughty words."""
    if version == "1.0":
        if (
            check_repeat_characters(text) is True
            and check_three_vowels(text) is True
            and check_forbidden_characters(text) is False
        ):
            return True

    elif version == "2.0":
        if (
            check_letter_pairs(text) is True
            and check_single_letter_repeat_with_single_char_between(text) is True
        ):
            return True

    return False


def test_check_repeat_charactes():
    assert True is check_repeat_characters("aabcde")
    assert False is check_repeat_characters("abcde")
    assert True is check_repeat_characters("abccde")


def test_check_three_vowels():
    assert True is check_three_vowels("aei")
    assert True is check_three_vowels("xazegov")
    assert True is check_three_vowels("aeiouaeiouaeiou")
    assert False is check_three_vowels("dvszwmarrgswjxmb")


def test_forbidden_characters():
    assert True is check_forbidden_characters("haegwjzuvuyypxyu")


def test_check_letter_paris():
    assert True is check_letter_pairs("xyxy")
    assert True is check_letter_pairs("aabcdefgaa")
    assert False is check_letter_pairs("aaa")


def test_check_single_letter_repeat_with_single_char_between():
    assert True is check_single_letter_repeat_with_single_char_between("xyx")
    assert True is check_single_letter_repeat_with_single_char_between("abcdefeghi")


def test_nice_words():
    assert True is check_nice_words("ugknbfddgicrmopn")
    assert True is check_nice_words("aaa")
    assert False is check_nice_words("jchzalrnumimnmhp")
    assert False is check_nice_words("haegwjzuvuyypxyu")
    assert False is check_nice_words("haegwjzuvuyypxyu")


def test_nice_words_version_2():
    assert True is check_nice_words("qjhvhtzxzqqjkmpb", version="2.0")
    assert True is check_nice_words("xxyxx", version="2.0")
    assert False is check_nice_words("uurcxstgmygtbstg", version="2.0")
    assert False is check_nice_words("ieodomkazucvgmuy", version="2.0")


def part_one(data):
    sum = 0
    for word in data:
        if check_nice_words(word):
            sum += 1
    return sum


def part_two(data):
    sum = 0
    for word in data:
        if check_nice_words(word, version="2.0"):
            sum += 1
    return sum


def test_part_one():
    data = "../data/05.data"
    input = utils.read_lines(data)
    result = part_one(inputdata)
    assert result == 236


@pytest.mark.skip
def test_part_two(data):
    result = part_two(data)
    assert result is True


if __name__ == "__main__":
    data = "../data/05.data"
    input = utils.read_lines(data)
    print("Part One")
    print(part_one(input))
    print("Part Two")
    print(part_two(input))
