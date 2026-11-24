# file: pyinstrument/renderers/base.py:105-109
# asked: {"lines": [109], "branches": []}
# gained: {"lines": [109], "branches": []}

import pytest

from pyinstrument.renderers.base import FrameRenderer, ProcessorList


def test_default_processors_raises_notimplementederror():
    with pytest.raises(NotImplementedError):
        FrameRenderer().default_processors()


