# file: pyinstrument/frame.py:164-167
# asked: {"lines": [], "branches": [[166, 0]]}
# gained: {"lines": [], "branches": [[166, 0]]}

import pytest

from pyinstrument.frame import Frame


def test_frame_line_no_with_more_than_two_parts():
    frame = Frame()
    frame._identifier_parts = ["part1", "part2", "166"]
    assert frame.line_no == 166


def test_frame_line_no_with_less_than_two_parts():
    frame = Frame()
    frame._identifier_parts = ["part1"]
    assert frame.line_no is None


def test_frame_line_no_with_non_integer_part():
    frame = Frame()
    frame._identifier_parts = ["part1", "part2", "not_an_integer"]
    with pytest.raises(ValueError):
        frame.line_no
