import re
import string

from Y2015 import utils


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


def part_one():
    data = utils.read_lines("data/05.data")
    sum = 0
    for word in data:
        if check_nice_words(word):
            sum += 1
    return sum


def part_two():
    data = utils.read_lines("data/05.data")
    sum = 0
    for word in data:
        if check_nice_words(word, version="2.0"):
            sum += 1
    return sum

if __name__ == "__main__":
    print("Part One")
    print(part_one())
    print("Part Two")
    print(part_two())
