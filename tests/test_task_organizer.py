import pytest
from argparse import ArgumentParser


def parse_args(args):
    parser = ArgumentParser()
    parser.add_argument('function', nargs='?', choices=['add', 'list', 'update', 'remove'])
    return parser.parse_args(args)


def test_parse_args_default():
    choice = parse_args([])
    assert not choice.function


@pytest.mark.parametrize('choice', (
    parse_args(['add']),
    parse_args(['update']),
    parse_args(['remove']),
    parse_args(['list'])
))
def test_parse_args_main_choices(choice):
    assert choice.function


# test arguments
# test sqlite
# test functions add update remove etc
