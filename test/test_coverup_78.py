# file: pyinstrument/frame.py:360-403
# asked: {"lines": [378], "branches": [[377, 378], [393, 400]]}
# gained: {"lines": [378], "branches": [[377, 378]]}

from typing import Sequence
from unittest.mock import MagicMock, patch

import pytest

from pyinstrument.frame import Frame, FrameGroup


def test_add_frame_with_existing_group_and_exit_frames():
    # Create mock Frame objects
    mock_frame1 = MagicMock()
    mock_frame2 = MagicMock()
    mock_frame3 = MagicMock()

    # Create a FrameGroup object
    frame_group = FrameGroup(mock_frame1)

    # Add a frame to the group
    frame_group.add_frame(mock_frame2)

    # Set the group attribute of mock_frame3 to frame_group
    mock_frame3.group = frame_group

    # Add mock_frame3 to mock_frame2's children
    mock_frame2.children = [mock_frame3]

    # Add mock_frame3 to the group
    with pytest.raises(ValueError):
        frame_group.add_frame(mock_frame3)


def test_exit_frames_property():
    # Create mock Frame objects
    mock_frame1 = MagicMock()
    mock_frame2 = MagicMock()
    mock_frame3 = MagicMock()

    # Create a FrameGroup object
    frame_group = FrameGroup(mock_frame1)

    # Add frames to the group
    frame_group.add_frame(mock_frame1)
    frame_group.add_frame(mock_frame2)
    frame_group.add_frame(mock_frame3)

    # Set the group attribute of mock_frame4 to another FrameGroup object
    mock_frame4 = MagicMock()
    mock_frame4.group = FrameGroup(mock_frame4)

    # Add mock_frame4 to mock_frame2's children
    mock_frame2.children = [mock_frame4]

    # Verify that the exit_frames property returns the correct frames
    assert frame_group.exit_frames == [mock_frame2]
