# file: pyinstrument/renderers/pstatsrenderer.py:87-96
# asked: {"lines": [88, 89, 90, 91, 92, 93, 94, 95], "branches": []}
# gained: {"lines": [88, 89, 90, 91, 92, 93, 94, 95], "branches": []}

import pytest

from pyinstrument import processors
from pyinstrument.renderers.pstatsrenderer import PstatsRenderer


@pytest.fixture
def pstats_renderer():
    return PstatsRenderer()


def test_default_processors(pstats_renderer):
    default_processors = pstats_renderer.default_processors()
    assert isinstance(default_processors, list)
    assert len(default_processors) == 7
    assert callable(default_processors[0])
    assert callable(default_processors[1])
    assert callable(default_processors[2])
    assert callable(default_processors[3])
    assert callable(default_processors[4])
    assert callable(default_processors[5])
    assert callable(default_processors[6])
