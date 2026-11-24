# file: pyinstrument/frame.py:222-239
# asked: {"lines": [230], "branches": [[229, 230]]}
# gained: {"lines": [230], "branches": [[229, 230]]}

import pytest

from pyinstrument.frame import SYNTHETIC_LEAF_IDENTIFIERS, Frame


def test_add_child_raises_value_error_for_leaf_frame():
    frame = Frame()
    frame.identifier = next(iter(SYNTHETIC_LEAF_IDENTIFIERS))
    child_frame = Frame()
    with pytest.raises(ValueError, match="Cannot add children to a leaf-only frame"):
        frame.add_child(child_frame)


def test_add_child_inserts_frame_after_specified_frame():
    frame = Frame()
    child_frame = Frame()
    another_child_frame = Frame()
    frame._children = [child_frame]
    frame.add_child(another_child_frame, after=child_frame)
    assert frame._children == [child_frame, another_child_frame]


def test_add_child_appends_frame_when_no_after_specified():
    frame = Frame()
    child_frame = Frame()
    frame.add_child(child_frame)
    assert frame._children == [child_frame]
