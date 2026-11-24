# file: pyinstrument/frame.py:308-313
# asked: {"lines": [308, 309, 313], "branches": []}
# gained: {"lines": [308, 309, 313], "branches": []}

import pytest

from pyinstrument.frame import Frame
from pyinstrument.frame_info import ATTRIBUTE_MARKER_TRACEBACKHIDE


def test_frame_has_tracebackhide_true():
    frame = Frame()
    frame.get_attribute_value = lambda x: "1"
    assert frame.has_tracebackhide is True


def test_frame_has_tracebackhide_false():
    frame = Frame()
    frame.get_attribute_value = lambda x: "0"
    assert frame.has_tracebackhide is False


def test_frame_has_tracebackhide_none():
    frame = Frame()
    frame.get_attribute_value = lambda x: None
    assert frame.has_tracebackhide is False
