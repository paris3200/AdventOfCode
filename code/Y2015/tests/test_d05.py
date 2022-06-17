import pytest

from Y2015 import D05


def test_check_repeat_charactes():
    assert True is D05.check_repeat_characters("aabcde")
    assert False is D05.check_repeat_characters("abcde")
    assert True is D05.check_repeat_characters("abccde")


def test_check_three_vowels():
    assert True is D05.check_three_vowels("aei")
    assert True is D05.check_three_vowels("xazegov")
    assert True is D05.check_three_vowels("aeiouaeiouaeiou")
    assert False is D05.check_three_vowels("dvszwmarrgswjxmb")


def test_forbidden_characters():
    assert True is D05.check_forbidden_characters("haegwjzuvuyypxyu")


def test_check_letter_paris():
    assert True is D05.check_letter_pairs("xyxy")
    assert True is D05.check_letter_pairs("aabcdefgaa")
    assert False is D05.check_letter_pairs("aaa")


def test_check_single_letter_repeat_with_single_char_between():
    assert True is D05.check_single_letter_repeat_with_single_char_between("xyx")
    assert True is D05.check_single_letter_repeat_with_single_char_between("abcdefeghi")


def test_nice_words():
    assert True is D05.check_nice_words("ugknbfddgicrmopn")
    assert True is D05.check_nice_words("aaa")
    assert False is D05.check_nice_words("jchzalrnumimnmhp")
    assert False is D05.check_nice_words("haegwjzuvuyypxyu")
    assert False is D05.check_nice_words("haegwjzuvuyypxyu")


def test_nice_words_version_2():
    assert True is D05.check_nice_words("qjhvhtzxzqqjkmpb", version="2.0")
    assert True is D05.check_nice_words("xxyxx", version="2.0")
    assert False is D05.check_nice_words("uurcxstgmygtbstg", version="2.0")
    assert False is D05.check_nice_words("ieodomkazucvgmuy", version="2.0")




def test_part_one():
    result = D05.part_one()
    assert result == 236


def test_part_two():
    result = D05.part_two()
    assert result == 51
