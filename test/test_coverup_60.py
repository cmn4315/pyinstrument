# file: pyinstrument/frame.py:155-157
# asked: {"lines": [157], "branches": []}
# gained: {"lines": [157], "branches": []}

import pytest

from pyinstrument.frame import Frame


def test_frame_function_property():
    # Create a Frame instance with a valid identifier
    identifier = "some_function\x00some_module"
    frame = Frame(identifier_or_frame_info=identifier)

    # Access the function property
    function = frame.function

    # Assert that the function property returns the expected value
    assert function == "some_function"
