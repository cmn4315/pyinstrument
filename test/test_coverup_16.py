# file: pyinstrument/renderers/base.py:16-41
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

import pytest

from pyinstrument.renderers.base import Renderer
from pyinstrument.session import Session


def test_render_not_implemented():
    class TestRenderer(Renderer):
        pass

    test_renderer = TestRenderer()
    session = Session(
        frame_records=[],
        start_time=0,
        duration=0,
        min_interval=0,
        max_interval=0,
        sample_count=0,
        start_call_stack=[],
        target_description="",
        cpu_time=0,
        sys_path=[],
        sys_prefixes=[],
    )

    with pytest.raises(NotImplementedError):
        test_renderer.render(session)
