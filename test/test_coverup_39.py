# file: pyinstrument/renderers/base.py:117-121
# asked: {"lines": [117, 121], "branches": []}
# gained: {"lines": [117], "branches": []}

import pytest

from pyinstrument.renderers.base import FrameRenderer
from pyinstrument.session import Session


def test_frame_renderer_render_method_raises_notimplementederror():
    with pytest.raises(NotImplementedError):
        renderer = FrameRenderer()
        renderer.render(Session())
