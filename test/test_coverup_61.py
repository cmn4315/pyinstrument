# file: pyinstrument/frame.py:124-127
# asked: {"lines": [127], "branches": []}
# gained: {"lines": [127], "branches": []}

import pytest

from pyinstrument.frame import Frame


def test_new_subclass_with_frame_info():
    frame_info = "test_frame_info"
    result = Frame.new_subclass_with_frame_info(frame_info)
    assert isinstance(result, Frame)
    assert result.identifier == frame_info
