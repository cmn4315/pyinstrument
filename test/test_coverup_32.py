# file: pyinstrument/util.py:101-104
# asked: {"lines": [101, 102, 103, 104], "branches": []}
# gained: {"lines": [101, 102, 103, 104], "branches": []}

import pytest

from pyinstrument.util import unwrap


def test_unwrap_with_newlines():
    input_string = "Hello,\nWorld!\n"
    expected_output = "Hello, World!"
    assert unwrap(input_string) == expected_output


def test_unwrap_with_spaces():
    input_string = "Hello,   World!   "
    expected_output = "Hello, World!"
    assert unwrap(input_string) == expected_output


def test_unwrap_with_both():
    input_string = "Hello,\n  World!   "
    expected_output = "Hello, World!"
    assert unwrap(input_string) == expected_output


def test_unwrap_empty_string():
    input_string = ""
    expected_output = ""
    assert unwrap(input_string) == expected_output


def test_unwrap_strip_whitespace():
    input_string = "   Hello, World!   "
    expected_output = "Hello, World!"
    assert unwrap(input_string) == expected_output
