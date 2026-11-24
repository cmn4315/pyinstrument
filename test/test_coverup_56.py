# file: pyinstrument/processors.py:237-293
# asked: {"lines": [245, 246, 249, 250, 251, 252, 253, 256, 257, 258, 259, 260, 261, 264, 265, 266, 267, 268, 269, 272, 274, 275, 277, 279, 280, 282, 287, 288, 291, 293], "branches": [[245, 246], [245, 249], [274, 275], [274, 277], [279, 280], [279, 282], [287, 288], [287, 291]]}
# gained: {"lines": [245, 246, 249, 250, 251, 252, 253, 256, 257, 258, 259, 260, 261, 264, 265, 266, 267, 268, 269, 272, 274, 275, 277, 279, 280, 282, 287, 288, 291, 293], "branches": [[245, 246], [245, 249], [274, 275], [274, 277], [279, 280], [279, 282], [287, 288], [287, 291]]}

from unittest.mock import Mock

import pytest

from pyinstrument.frame import Frame
from pyinstrument.processors import remove_first_pyinstrument_frames_processor


def test_remove_first_pyinstrument_frames_processor():
    # Create mock frames
    frame_pyinstrument = Mock(spec=Frame)
    frame_pyinstrument.file_path = "/path/to/pyinstrument/__main__.py"
    frame_pyinstrument.proportion_of_parent = 0.9
    frame_pyinstrument.children = []

    frame_exec = Mock(spec=Frame)
    frame_exec.file_path = "<string>"
    frame_exec.proportion_of_parent = 0.9
    frame_exec.children = []

    frame_runpy = Mock(spec=Frame)
    frame_runpy.file_path = "/path/to/runpy.py"
    frame_runpy.proportion_of_parent = 0.9
    frame_runpy.children = []

    frame_target = Mock(spec=Frame)
    frame_target.file_path = "/path/to/target.py"
    frame_target.proportion_of_parent = 0.9
    frame_target.children = []

    # Set up the frame hierarchy
    frame_pyinstrument.children = [frame_exec]
    frame_exec.children = [frame_runpy]
    frame_runpy.children = [frame_target]

    # Execute the function
    result = remove_first_pyinstrument_frames_processor(frame_pyinstrument, None)

    # Assertions to verify the result
    assert result == frame_target
    assert frame_pyinstrument not in result.children
    assert frame_exec not in result.children
    assert frame_runpy not in result.children


def test_remove_first_pyinstrument_frames_processor_none_frame():
    # Test with None frame
    result = remove_first_pyinstrument_frames_processor(None, None)
    assert result is None


def test_remove_first_pyinstrument_frames_processor_no_initial_pyinstrument_frame():
    # Create mock frames
    frame_target = Mock(spec=Frame)
    frame_target.file_path = "/path/to/target.py"
    frame_target.proportion_of_parent = 0.9
    frame_target.children = []

    # Execute the function
    result = remove_first_pyinstrument_frames_processor(frame_target, None)

    # Assertions to verify the result
    assert result == frame_target


def test_remove_first_pyinstrument_frames_processor_no_exec_frame():
    # Create mock frames
    frame_pyinstrument = Mock(spec=Frame)
    frame_pyinstrument.file_path = "/path/to/pyinstrument/__main__.py"
    frame_pyinstrument.proportion_of_parent = 0.9
    frame_pyinstrument.children = []

    frame_target = Mock(spec=Frame)
    frame_target.file_path = "/path/to/target.py"
    frame_target.proportion_of_parent = 0.9
    frame_target.children = []

    # Set up the frame hierarchy
    frame_pyinstrument.children = [frame_target]

    # Execute the function
    result = remove_first_pyinstrument_frames_processor(frame_pyinstrument, None)

    # Assertions to verify the result
    assert result == frame_pyinstrument


def test_remove_first_pyinstrument_frames_processor_no_runpy_frame():
    # Create mock frames
    frame_pyinstrument = Mock(spec=Frame)
    frame_pyinstrument.file_path = "/path/to/pyinstrument/__main__.py"
    frame_pyinstrument.proportion_of_parent = 0.9
    frame_pyinstrument.children = []

    frame_exec = Mock(spec=Frame)
    frame_exec.file_path = "<string>"
    frame_exec.proportion_of_parent = 0.9
    frame_exec.children = []

    frame_target = Mock(spec=Frame)
    frame_target.file_path = "/path/to/target.py"
    frame_target.proportion_of_parent = 0.9
    frame_target.children = []

    # Set up the frame hierarchy
    frame_pyinstrument.children = [frame_exec]
    frame_exec.children = [frame_target]

    # Execute the function
    result = remove_first_pyinstrument_frames_processor(frame_pyinstrument, None)

    # Assertions to verify the result
    assert result == frame_target
    assert frame_pyinstrument not in result.children
    assert frame_exec not in result.children
