import pytest
from other.unittests_practice.count_file import \
    num_to_digits, is_there_two_identical_adjacent_digits, is_never_decreasing, might_be_password


@pytest.mark.parametrize("number, result", (
        (12345, ["1", "2", "3", "4", "5"]),
        (3210, ["3", "2", "1", "0"]),
        (1924223, ["1", "9", "2", "4", "2", "2", "3"])
))
def test_num_to_digits(number, result):
    assert num_to_digits(number) == result


def test_is_there_two_identical_adjacent_digits():
    assert is_there_two_identical_adjacent_digits("1234567") is False
    assert is_there_two_identical_adjacent_digits(["1", "2", "3", "4", "5", "6", "7"]) is False
    assert is_there_two_identical_adjacent_digits("122345567") is True
    assert is_there_two_identical_adjacent_digits(["1", "2", "2", "3", "4", "5", "5", "6", "7"]) is True


def test_is_never_decreasing():
    assert is_never_decreasing(["1", "2", "3"]) is True
    assert is_never_decreasing(["1", "2", "3", "1"]) is False
    assert is_never_decreasing("123456") is True
    assert is_never_decreasing("123156") is False
    assert is_never_decreasing("1231562") is False


def test_might_be_password():
    assert might_be_password("123422522") is False
    assert might_be_password("12234566") is True
