import pytest

from aoc_04 import validate_passphrase


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
