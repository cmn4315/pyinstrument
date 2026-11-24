# file: pyinstrument/frame.py:360-403
# asked: {"lines": [378, 384, 385, 386, 403], "branches": [[377, 378], [393, 400]]}
# gained: {"lines": [384, 385, 386, 403], "branches": []}

from typing import Sequence

import pytest

from pyinstrument.frame import Frame, FrameGroup


def test_add_frame_with_existing_group():
    # Create a FrameGroup and a Frame
    root_frame = Frame()
    group = FrameGroup(root_frame)
    new_frame = Frame()

    # Add the new frame to the group
    group.add_frame(new_frame)

    # Verify that the new frame was removed from its previous group
    assert new_frame.group == group


def test_remove_frame():
    # Create a FrameGroup and a Frame
    root_frame = Frame()
    group = FrameGroup(root_frame)
    frame = Frame()

    # Add the frame to the group
    group.add_frame(frame)

    # Remove the frame from the group
    group.remove_frame(frame)

    # Verify that the frame was removed from the group and its group reference is None
    assert frame not in group.frames
    assert frame.group is None


def test_exit_frames_property():
    # Create a FrameGroup and Frames
    root_frame = Frame()
    group = FrameGroup(root_frame)
    frame1 = Frame()
    frame2 = Frame()
    frame3 = Frame()

    # Add frames to the group
    group.add_frame(frame1)
    group.add_frame(frame2)
    group.add_frame(frame3)

    # Add a child frame to frame1 that is outside of the group
    outside_frame = Frame()
    outside_frame.group = None
    frame1._children = [outside_frame]  # Use the private attribute _children

    # Access the exit_frames property
    exit_frames = group.exit_frames

    # Verify that the exit_frames property contains the correct frames
    assert exit_frames == [frame1]
    assert group._exit_frames == [frame1]


def test_frame_group_repr():
    # Create a FrameGroup with frames
    root_frame = Frame()
    group = FrameGroup(root_frame)
    frame1 = Frame()
    frame2 = Frame()

    # Add frames to the group
    group.add_frame(frame1)
    group.add_frame(frame2)

    # Verify the __repr__ output
    assert repr(group) == f"FrameGroup(len(frames)={len(group.frames)})"
