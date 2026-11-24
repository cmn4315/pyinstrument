# file: pyinstrument/renderers/jsonrenderer.py:65-76
# asked: {"lines": [66, 68, 69, 70, 71, 72, 73, 74, 76], "branches": []}
# gained: {"lines": [66, 68, 69, 70, 71, 72, 73, 74, 76], "branches": []}

import pytest

from pyinstrument.frame import Frame
from pyinstrument.renderers.jsonrenderer import JSONRenderer
from pyinstrument.session import Session


def test_json_renderer_render_missing_lines():
    def mock_preprocess(session):
        return Frame()

    session = Session(
        frame_records=[],
        start_time=1.0,
        duration=2.0,
        min_interval=0.01,
        max_interval=1.0,
        sample_count=3,
        start_call_stack=[],
        target_description="test",
        cpu_time=4.0,
        sys_path=[],
        sys_prefixes=[],
    )
    session.root_frame = lambda: Frame()

    renderer = JSONRenderer()
    renderer.preprocess = mock_preprocess
    renderer.render_frame = lambda frame: '"frame_data"'

    result = renderer.render(session)

    assert (
        result
        == '{"start_time": 1.000000,"duration": 2.000000,"sample_count": 3,"target_description": "test","cpu_time": 4.000000,"root_frame": "frame_data"}\n'
    )
