# file: pyinstrument/profiler.py:222-229
# asked: {"lines": [222, 226, 227, 229], "branches": [[226, 227], [226, 229]]}
# gained: {"lines": [222, 226, 227, 229], "branches": [[226, 227], [226, 229]]}

import pytest

from pyinstrument import Profiler


def test_profiler_reset_when_running():
    profiler = Profiler()
    profiler.start()
    profiler.reset()
    assert not profiler.is_running
    assert profiler._last_session is None


def test_profiler_reset_when_not_running():
    profiler = Profiler()
    profiler.reset()
    assert profiler._last_session is None
