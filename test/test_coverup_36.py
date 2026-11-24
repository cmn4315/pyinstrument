# file: pyinstrument/profiler.py:215-220
# asked: {"lines": [215, 216, 220], "branches": []}
# gained: {"lines": [215, 216, 220], "branches": []}

import pytest

from pyinstrument import Profiler


def test_profiler_is_running():
    profiler = Profiler()
    assert not profiler.is_running  # Initially, the profiler should not be running

    profiler.start()
    assert profiler.is_running  # After starting, the profiler should be running

    profiler.stop()
    assert not profiler.is_running  # After stopping, the profiler should not be running
