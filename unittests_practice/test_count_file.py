import pytest
import sys

sys.path.append("../")
from unittests_practice.count_file import num_to_digits


@pytest.mark.parametrize("number, result", (
        (12345, ["1", "2", "3", "4", "5"]),
        (3210, ["3", "2", "1", "0"]),
        (1924223, ["1", "9", "2", "4", "2", "2", "3"])
))
def test_num_to_digits(number, result):
    assert num_to_digits(number) == result
