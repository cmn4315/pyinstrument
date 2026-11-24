# file: pyinstrument/low_level/pyi_timing_thread_python.py:79-80
# asked: {"lines": [80], "branches": []}
# gained: {"lines": [80], "branches": []}

import pytest

from pyinstrument.low_level.pyi_timing_thread_python import current_time, pyi_timing_thread_get_time


def test_pyi_timing_thread_get_time():
    # Arrange
    expected_time = 123.456  # Example time value
    # Using monkeypatch to set the value of current_time
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("pyinstrument.low_level.pyi_timing_thread_python.current_time", expected_time)
        # Act
        result = pyi_timing_thread_get_time()
        # Assert
        assert result == expected_time, "The function should return the current_time value"
