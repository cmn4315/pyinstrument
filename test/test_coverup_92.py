# file: pyinstrument/util.py:39-42
# asked: {"lines": [40, 41, 42], "branches": [[40, 41], [40, 42]]}
# gained: {"lines": [40, 41, 42], "branches": [[40, 41], [40, 42]]}

import pytest

from pyinstrument.util import truncate


def test_truncate_long_string():
    string = "a" * 10
    max_length = 5
    expected = "a" * 2 + "..."
    result = truncate(string, max_length)
    assert result == expected


def test_truncate_short_string():
    string = "a" * 3
    max_length = 5
    expected = string
    result = truncate(string, max_length)
    assert result == expected
