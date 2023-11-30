import pytest

from aoc_04 import validate_passphrase, is_anagram


@pytest.mark.parametrize(
    ("passphrase", "is_valid"),
    (
        ("a bb cc dd ee", True),
        ("aa bb cc dd aa", False),
        ("aa bb cc dd aaa", True),
    ),
)
def test_validate_passphrase(passphrase, is_valid) -> None:
    assert validate_passphrase(passphrase) == is_valid


@pytest.mark.parametrize(
    ("passphrase", "is_valid"),
    (
        ("abcde fghij", False),
        ("abcde xyz ecdab", True),
        ("a ab abc abd abf abj", False),
        ("iiii oiii ooii oooi oooo", False),
        ("oiii ioii iioi iiio", True),
    ),
)
def test_is_anagram(passphrase, is_valid) -> None:
    assert is_anagram(passphrase) == is_valid
