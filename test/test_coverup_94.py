# file: pyinstrument/low_level/stat_profile_python.py:96-113
# asked: {"lines": [103, 104, 105, 106, 107, 108, 109, 111, 113], "branches": [[103, 104], [103, 113]]}
# gained: {"lines": [103, 104, 105, 106, 107, 108, 109, 111, 113], "branches": [[103, 104], [103, 113]]}

import sys
from unittest.mock import MagicMock

import pytest

from pyinstrument.low_level.stat_profile_python import PythonStatProfiler, setstatprofile


def test_setstatprofile_with_target():
    target = MagicMock()
    interval = 0.001
    context_var = None
    timer_type = "walltime"
    timer_func = None

    original_profile = sys.getprofile()

    setstatprofile(target, interval, context_var, timer_type, timer_func)

    # Verify that the profiler was set
    assert sys.getprofile() is not original_profile

    # Reset the profiler to its original state
    setstatprofile(None)


def test_setstatprofile_without_target():
    target = None
    interval = 0.001
    context_var = None
    timer_type = "walltime"
    timer_func = None

    original_profile = sys.getprofile()

    setstatprofile(target, interval, context_var, timer_type, timer_func)

    # Verify that the profiler was reset to None
    assert sys.getprofile() is None

    # Reset the profiler to its original state
    setstatprofile(None)
