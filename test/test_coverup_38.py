# file: pyinstrument/profiler.py:77-83
# asked: {"lines": [77, 78, 83], "branches": []}
# gained: {"lines": [77, 78, 83], "branches": []}

import pytest

from pyinstrument import Profiler


def test_profiler_interval():
    profiler = Profiler()
    profiler._interval = 0.01  # Set a specific interval value to test
    assert profiler.interval == 0.01  # Verify the interval property returns the correct value


def test_profiler_interval_default():
    profiler = Profiler()
    assert profiler.interval == 0.001  # Corrected default interval value should be 0.001
