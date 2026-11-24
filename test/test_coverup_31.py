# file: pyinstrument/frame.py:262-267
# asked: {"lines": [262, 263, 267], "branches": []}
# gained: {"lines": [262, 263, 267], "branches": []}

from typing import Sequence

import pytest

from pyinstrument.frame import Frame


def test_frame_children_property():
    frame = Frame()
    frame._children = [Frame(), Frame(), Frame()]

    children = frame.children

    assert isinstance(children, tuple)
    assert len(children) == 3
    assert all(isinstance(child, Frame) for child in children)
