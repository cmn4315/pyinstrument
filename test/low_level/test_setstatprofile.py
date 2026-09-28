import sys
import time
from typing import Any, cast
from unittest.mock import patch

import pytest

from pyinstrument.low_level.stat_profile_python import PythonStatProfiler

from ..util import busy_wait, flaky_in_ci
from .util import parametrize_setstatprofile


class CallCounter:
    def __init__(self) -> None:
        self.count = 0

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.count += 1


@flaky_in_ci
@parametrize_setstatprofile
def test_100ms(setstatprofile):
    counter = CallCounter()
    setstatprofile(counter, 0.1)
    busy_wait(1.0)
    setstatprofile(None)
    assert 8 < counter.count < 12


@flaky_in_ci
@parametrize_setstatprofile
def test_10ms(setstatprofile):
    counter = CallCounter()
    setstatprofile(counter, 0.01)
    busy_wait(1.0)
    setstatprofile(None)
    assert 70 <= counter.count <= 130


@parametrize_setstatprofile
def test_internal_object_compatibility(setstatprofile):
    setstatprofile(CallCounter(), 1e6)

    profile_state = sys.getprofile()

    print(repr(profile_state))
    print(str(profile_state))
    print(profile_state)
    print(type(profile_state))
    print(type(profile_state).__name__)  # type: ignore

    setstatprofile(None)


# Noah Lago - added for 777 project


def test_profiler_requires_timer_function():
    with pytest.raises(TypeError, match="timer_func must be provided"):
        PythonStatProfiler(lambda frame, event, arg: None, 0.1, None, "timer_func", None)


def test_profiler_rejects_invalid_timer():
    with pytest.raises(ValueError, match="invalid timer_type"):
        PythonStatProfiler(lambda frame, event, arg: None, 0.1, None, cast(Any, "invalid"), None)


def test_profiler_uses_timer_function():
    profiler = PythonStatProfiler(
        lambda frame, event, arg: None, 0.1, None, "timer_func", lambda: 1.0
    )

    assert profiler.last_invocation == 1.0


def test_profiler_profile_calls_target():
    calls = []
    times = iter((0.0, 1.0))

    profiler = PythonStatProfiler(
        lambda frame, event, arg: calls.append((frame, event, arg)),
        0.5,
        None,
        "timer_func",
        lambda: next(times),
    )

    frame = sys._getframe()
    profiler.profile(frame, "call", None)

    assert calls == [(frame, "call", None)]


def test_profiler_walltime_thread_subscribes():
    with patch(
        "pyinstrument.low_level.stat_profile_python.pyi_timing_thread_get_time", return_value=1.0
    ), patch(
        "pyinstrument.low_level.stat_profile_python.pyi_timing_thread_subscribe", return_value=123
    ) as subscribe:
        profiler = PythonStatProfiler(
            lambda frame, event, arg: None, 0.1, None, "walltime_thread", None
        )

        subscribe.assert_called_once_with(0.1)
        assert profiler.timing_thread_subscription == 123
