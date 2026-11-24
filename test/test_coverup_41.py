# file: pyinstrument/renderers/pstatsrenderer.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28], "branches": []}

from unittest.mock import Mock, patch

import pytest

from pyinstrument.renderers.pstatsrenderer import PstatsRenderer


@pytest.fixture
def mock_super_init():
    with patch.object(PstatsRenderer, "__init__", return_value=None) as mock_init:
        yield mock_init


def test_pstatsrenderer_init(mock_super_init):
    instance = PstatsRenderer(arg1="value1", arg2="value2")
    mock_super_init.assert_called_once_with(arg1="value1", arg2="value2")
    assert isinstance(instance, PstatsRenderer)
