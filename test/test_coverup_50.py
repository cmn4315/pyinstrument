# file: pyinstrument/frame.py:222-239
# asked: {"lines": [230, 238, 239], "branches": [[229, 230], [235, 238]]}
# gained: {"lines": [230, 238, 239], "branches": [[229, 230], [235, 238]]}

import pytest

from pyinstrument.frame import SYNTHETIC_LEAF_IDENTIFIERS, Frame


@pytest.fixture
def frame_with_children():
    frame = Frame()
    frame.identifier = "test_id"
    frame._children = [Frame(), Frame()]
    return frame


def test_add_child_raises_value_error_for_synthetic_leaf_frame(frame_with_children):
    leaf_identifier = next(iter(SYNTHETIC_LEAF_IDENTIFIERS))
    frame_with_children.identifier = leaf_identifier
    child_frame = Frame()
    with pytest.raises(ValueError, match="Cannot add children to a leaf-only frame"):
        frame_with_children.add_child(child_frame)


def test_add_child_appends_to_children_when_after_is_none(frame_with_children):
    child_frame = Frame()
    frame_with_children.add_child(child_frame)
    assert child_frame in frame_with_children._children


def test_add_child_inserts_after_specified_frame(frame_with_children):
    child_frame = Frame()
    after_frame = frame_with_children._children[0]
    frame_with_children.add_child(child_frame, after=after_frame)
    index = frame_with_children._children.index(after_frame) + 1
    assert frame_with_children._children[index] == child_frame
