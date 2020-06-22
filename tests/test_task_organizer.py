import pytest
import sqlite3
from unittest.mock import MagicMock
from argparse import ArgumentParser
import sys


def test_sqlite3_connect_success():
    sqlite3.connect = MagicMock(return_value="connected")
    db = sqlite3.connect("tasks.sqlite")
    assert db == "connected"


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
