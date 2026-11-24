# file: pyinstrument/frame.py:119-122
# asked: {"lines": [119, 120, 121, 122], "branches": [[121, 0], [121, 122]]}
# gained: {"lines": [119, 120, 121, 122], "branches": [[121, 0], [121, 122]]}

import pytest

from pyinstrument.frame import Frame


class MockFrameContext:
    pass


def test_set_context_with_children():
    # Arrange
    parent_frame = Frame()
    child_frame1 = Frame()
    child_frame2 = Frame()
    parent_frame._children = [child_frame1, child_frame2]
    context = MockFrameContext()

    # Act
    parent_frame.set_context(context)

    # Assert
    assert parent_frame._context == context
    assert child_frame1._context == context
    assert child_frame2._context == context


def test_set_context_no_children():
    # Arrange
    frame = Frame()
    context = MockFrameContext()

    # Act
    frame.set_context(context)

    # Assert
    assert frame._context == context
    assert not frame._children
