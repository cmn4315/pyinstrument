# file: pyinstrument/renderers/speedscope.py:130-142
# asked: {"lines": [130, 131, 135, 142], "branches": []}
# gained: {"lines": [130, 131, 135, 142], "branches": []}

import pytest

from pyinstrument.renderers.speedscope import SpeedscopeFrame, SpeedscopeRenderer


def test_speedscope_renderer_init():
    renderer = SpeedscopeRenderer()
    assert renderer._event_time == 0.0
    assert renderer._frame_to_index == {}


def test_speedscope_renderer_frame_to_index():
    renderer = SpeedscopeRenderer()
    frame = SpeedscopeFrame(name="test_frame", file="test_file", line=123)
    renderer._frame_to_index[frame] = 0
    assert frame in renderer._frame_to_index
    assert renderer._frame_to_index[frame] == 0
