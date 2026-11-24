# file: pyinstrument/util.py:101-104
# asked: {"lines": [102, 103, 104], "branches": []}
# gained: {"lines": [102, 103, 104], "branches": []}

import pytest

from pyinstrument.util import unwrap


def test_unwrap_with_newlines():
    input_string = "Hello\nWorld\n"
    expected_output = "Hello World"
    assert unwrap(input_string) == expected_output


def test_unwrap_with_multiple_spaces():
    input_string = "Hello   World"
    expected_output = "Hello World"
    assert unwrap(input_string) == expected_output


def test_unwrap_with_both_newlines_and_spaces():
    input_string = "Hello\n  World\n"
    expected_output = "Hello World"
    assert unwrap(input_string) == expected_output


def test_unwrap_with_leading_and_trailing_spaces():
    input_string = "  Hello World  "
    expected_output = "Hello World"
    assert unwrap(input_string) == expected_output
