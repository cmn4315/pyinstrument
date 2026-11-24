# file: pyinstrument/util.py:39-42
# asked: {"lines": [40, 41, 42], "branches": [[40, 41], [40, 42]]}
# gained: {"lines": [40, 41, 42], "branches": [[40, 41], [40, 42]]}

import pytest


@pytest.fixture
def truncate_function():
    from pyinstrument.util import truncate

    return truncate


def test_truncate_string_longer_than_max_length(truncate_function):
    result = truncate_function("This is a very long string", 10)
    assert result == "This is..."  # Ensure the string is truncated correctly


def test_truncate_string_shorter_than_max_length(truncate_function):
    result = truncate_function("Short", 10)
    assert result == "Short"  # Ensure the string is not modified if it's shorter


def test_truncate_string_equal_to_max_length(truncate_function):
    result = truncate_function("EqualLength", 13)
    assert result == "EqualLength"  # Ensure the string is not modified if it's equal to max_length


def test_truncate_string_empty(truncate_function):
    result = truncate_function("", 10)
    assert result == ""  # Ensure an empty string is returned as is
