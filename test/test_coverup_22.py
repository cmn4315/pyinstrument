# file: pyinstrument/renderers/base.py:117-121
# asked: {"lines": [121], "branches": []}
# gained: {"lines": [121], "branches": []}

import pytest

from pyinstrument.renderers.base import FrameRenderer
from pyinstrument.session import Session


class MockFrameRenderer(FrameRenderer):
    def default_processors(self):
        return []


def test_frame_renderer_raises_not_implemented_error():
    session = Session(
        frame_records=[],
        start_time=0.0,
        duration=0.0,
        min_interval=0.0,
        max_interval=0.0,
        sample_count=0,
        start_call_stack=[],
        target_description="",
        cpu_time=0.0,
        sys_path=[],
        sys_prefixes=[],
    )
    renderer = MockFrameRenderer()
    with pytest.raises(NotImplementedError):
        renderer.render(session)
