# file: pyinstrument/magic/magic.py:36-41
# asked: {"lines": [41], "branches": []}
# gained: {"lines": [41], "branches": []}

from unittest.mock import Mock

import pytest

from pyinstrument.magic.magic import _get_active_profiler


@pytest.fixture
def mock_active_profiler(monkeypatch):
    # Mock the _active_profiler variable to have a value
    mock_profiler = Mock()
    monkeypatch.setattr("pyinstrument.magic.magic._active_profiler", mock_profiler)
    return mock_profiler


def test_get_active_profiler(mock_active_profiler):
    # Call the function to ensure the line is executed
    profiler = _get_active_profiler()
    # Assert that the returned value is the mocked _active_profiler
    assert profiler == mock_active_profiler
