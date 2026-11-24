# file: pyinstrument/frame.py:164-167
# asked: {"lines": [166, 167], "branches": [[166, 0], [166, 167]]}
# gained: {"lines": [166, 167], "branches": [[166, 0], [166, 167]]}

import pytest

from pyinstrument.frame import Frame


def test_frame_line_no_with_more_than_two_identifier_parts():
    class MockFrame(Frame):
        def __init__(self, identifier_parts):
            self._identifier_parts = identifier_parts

    frame = MockFrame(["part1", "part2", "167", "part4"])
    assert frame.line_no == 167


def test_frame_line_no_with_less_than_two_identifier_parts():
    class MockFrame(Frame):
        def __init__(self, identifier_parts):
            self._identifier_parts = identifier_parts

    frame = MockFrame(["part1"])
    assert frame.line_no is None

    frame = MockFrame(["part1", "part2"])
    assert frame.line_no is None
