# file: pyinstrument/low_level/pyi_timing_thread_python.py:83-84
# asked: {"lines": [84], "branches": []}
# gained: {"lines": [84], "branches": []}

from unittest.mock import Mock

import pytest


def test_pyi_timing_thread_get_interval_thread_alive(monkeypatch):
    # Mock the get_interval function
    get_interval_mock = Mock(return_value=10.0)
    monkeypatch.setattr(
        "pyinstrument.low_level.pyi_timing_thread_python.get_interval", get_interval_mock
    )

    # Set thread_alive to True
    monkeypatch.setattr("pyinstrument.low_level.pyi_timing_thread_python.thread_alive", True)

    from pyinstrument.low_level.pyi_timing_thread_python import pyi_timing_thread_get_interval

    # Call the function
    result = pyi_timing_thread_get_interval()

    # Assert that get_interval was called with float('inf')
    get_interval_mock.assert_called_once_with(float("inf"))

    # Assert that the result is the return value of get_interval
    assert result == 10.0


def test_pyi_timing_thread_get_interval_thread_not_alive(monkeypatch):
    # Mock the get_interval function (though it shouldn't be called)
    get_interval_mock = Mock()
    monkeypatch.setattr(
        "pyinstrument.low_level.pyi_timing_thread_python.get_interval", get_interval_mock
    )

    # Set thread_alive to False
    monkeypatch.setattr("pyinstrument.low_level.pyi_timing_thread_python.thread_alive", False)

    from pyinstrument.low_level.pyi_timing_thread_python import pyi_timing_thread_get_interval

    # Call the function
    result = pyi_timing_thread_get_interval()

    # Assert that get_interval was not called
    get_interval_mock.assert_not_called()

    # Assert that the result is -1.0
    assert result == -1.0
