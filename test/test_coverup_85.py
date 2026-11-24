# file: pyinstrument/frame.py:360-403
# asked: {"lines": [], "branches": [[393, 400]]}
# gained: {"lines": [], "branches": [[393, 400]]}

import pytest

from pyinstrument.frame import Frame, FrameGroup


def test_exit_frames_property():
    class Frame:
        def __init__(self, group=None, children=None):
            self.group = group
            self.children = children if children is not None else []

    frame1 = Frame()
    frame2 = Frame()
    frame3 = Frame()
    frame4 = Frame()

    frame1.children = [frame2]
    frame2.children = [frame3]
    frame3.children = [frame4]

    frame_group = FrameGroup(frame1)
    frame_group.add_frame(frame2)
    frame_group.add_frame(frame3)

    # Ensure that frame4 is not part of the frame_group
    frame4.group = None

    # Test that exit_frames property calculates correctly
    exit_frames = frame_group.exit_frames
    assert exit_frames == [frame3]

    # Test that exit_frames property returns the cached value
    exit_frames = frame_group.exit_frames
    assert exit_frames == [frame3]
