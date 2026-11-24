# file: pyinstrument/frame.py:129-137
# asked: {"lines": [131, 132, 133, 134, 135, 137], "branches": [[131, 132], [131, 137]]}
# gained: {"lines": [131, 132, 133, 134, 135, 137], "branches": [[131, 132], [131, 137]]}

import pytest

from pyinstrument.frame import Frame


@pytest.fixture
def frame_with_parent():
    parent = Frame()
    parent.time = 10
    frame = Frame()
    frame.time = 5
    frame.parent = parent
    return frame


@pytest.fixture
def frame_without_parent():
    frame = Frame()
    frame.time = 5
    return frame


def test_proportion_of_parent_with_parent(frame_with_parent):
    result = frame_with_parent.proportion_of_parent
    assert result == 0.5


def test_proportion_of_parent_with_parent_zero_division(frame_with_parent):
    frame_with_parent.parent.time = 0
    result = frame_with_parent.proportion_of_parent
    assert result != result


def test_proportion_of_parent_without_parent(frame_without_parent):
    result = frame_without_parent.proportion_of_parent
    assert result == 1.0
