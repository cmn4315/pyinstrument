# file: pyinstrument/renderers/pstatsrenderer.py:31-32
# asked: {"lines": [32], "branches": []}
# gained: {"lines": [32], "branches": []}

import pytest

from pyinstrument.frame import Frame
from pyinstrument.renderers.pstatsrenderer import PstatsRenderer


@pytest.fixture
def pstats_renderer():
    return PstatsRenderer()


def test_frame_key_with_none_values(pstats_renderer, monkeypatch):
    class MockFrame(Frame):
        @property
        def file_path(self):
            return None

        @property
        def line_no(self):
            return None

        @property
        def function(self):
            return "test_function"

    frame = MockFrame()
    result = pstats_renderer.frame_key(frame)
    assert result == ("", 0, "test_function")


def test_frame_key_with_valid_values(pstats_renderer, monkeypatch):
    class MockFrame(Frame):
        @property
        def file_path(self):
            return "test_file.py"

        @property
        def line_no(self):
            return 10

        @property
        def function(self):
            return "test_function"

    frame = MockFrame()
    result = pstats_renderer.frame_key(frame)
    assert result == ("test_file.py", 10, "test_function")
