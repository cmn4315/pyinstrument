# file: pyinstrument/renderers/pstatsrenderer.py:34-75
# asked: {"lines": [35, 36, 38, 40, 44, 45, 46, 47, 48, 50, 53, 54, 56, 57, 58, 59, 60, 61, 62, 64, 66, 67, 69, 71, 73, 74, 75], "branches": [[35, 36], [35, 38], [40, 44], [40, 50], [56, 57], [56, 71], [58, 59], [58, 64], [73, 0], [73, 74], [74, 73], [74, 75]]}
# gained: {"lines": [35, 36, 38, 40, 44, 45, 46, 47, 48, 50, 53, 54, 56, 57, 58, 59, 60, 61, 62, 66, 67, 69, 71, 73, 74, 75], "branches": [[35, 36], [35, 38], [40, 44], [40, 50], [56, 57], [56, 71], [58, 59], [73, 0], [73, 74], [74, 73], [74, 75]]}

import pytest

from pyinstrument.frame import Frame
from pyinstrument.renderers.base import FrameRenderer
from pyinstrument.renderers.pstatsrenderer import PstatsRenderer


class MockFrame:
    def __init__(self, total_self_time=0, time=0, parent=None, children=None, is_synthetic=False):
        self.total_self_time = total_self_time
        self.time = time
        self.parent = parent
        self.children = children if children is not None else []
        self.is_synthetic = is_synthetic


class MockPstatsRenderer(PstatsRenderer):
    def frame_key(self, frame: Frame) -> str:
        return f"{frame.total_self_time}_{frame.time}"


@pytest.fixture
def renderer():
    return MockPstatsRenderer()


@pytest.fixture
def stats():
    return {}


def test_render_frame_none_frame(renderer, stats):
    renderer.render_frame(None, stats)
    assert stats == {}


def test_render_frame_new_entry(renderer, stats):
    frame = MockFrame(total_self_time=1, time=2)
    renderer.render_frame(frame, stats)
    assert stats == {"1_2": (-1, -1, 1, 2, {})}


def test_render_frame_existing_entry(renderer, stats):
    frame = MockFrame(total_self_time=1, time=2)
    stats["1_2"] = (-1, -1, 0, 0, {})
    renderer.render_frame(frame, stats)
    assert stats["1_2"] == (-1, -1, 1, 2, {})


def test_render_frame_with_parent(renderer, stats):
    parent_frame = MockFrame(total_self_time=3, time=4)
    frame = MockFrame(total_self_time=1, time=2, parent=parent_frame)
    stats["3_4"] = (-1, -1, 0, 0, {})
    renderer.render_frame(frame, stats)
    assert stats["1_2"] == (-1, -1, 1, 2, {"3_4": (-1, -1, 1, 2)})


def test_render_frame_with_children(renderer, stats):
    child_frame = MockFrame(total_self_time=5, time=6)
    frame = MockFrame(total_self_time=1, time=2, children=[child_frame])
    renderer.render_frame(frame, stats)
    assert "5_6" in stats


def test_render_frame_with_synthetic_child(renderer, stats):
    synthetic_child_frame = MockFrame(total_self_time=5, time=6, is_synthetic=True)
    frame = MockFrame(total_self_time=1, time=2, children=[synthetic_child_frame])
    renderer.render_frame(frame, stats)
    assert "5_6" not in stats
