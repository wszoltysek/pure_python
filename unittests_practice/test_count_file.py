import pytest
import sys

sys.path.append("../")
from unittests_practice.count_file import \
    num_to_digits, is_there_two_identical_adjacent_digits


@pytest.mark.parametrize("number, result", (
        (12345, ["1", "2", "3", "4", "5"]),
        (3210, ["3", "2", "1", "0"]),
        (1924223, ["1", "9", "2", "4", "2", "2", "3"])
))
def test_num_to_digits(number, result):
    assert num_to_digits(number) == result


def test_is_there_two_identical_adjacent_digits():
    assert is_there_two_identical_adjacent_digits("1234567") is False
    assert is_there_two_identical_adjacent_digits("122345567") is True
