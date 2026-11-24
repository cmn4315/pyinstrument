# file: pyinstrument/frame.py:334-340
# asked: {"lines": [335, 336, 337, 338, 339], "branches": []}
# gained: {"lines": [335, 336, 337, 338, 339], "branches": []}

import pytest

from pyinstrument.frame import Frame


def test_frame_repr():
    # Create a Frame object with specific attributes
    frame = Frame(time=1.234567, children=[Frame(), Frame()])
    frame.identifier = "test_identifier"
    frame.group = "test_group"

    # Call the __repr__ method
    result = repr(frame)

    # Assert that the result matches the expected format
    expected = (
        "Frame(identifier=test_identifier, time=1.234567, len(children)=2), group='test_group'"
    )
    assert result == expected
