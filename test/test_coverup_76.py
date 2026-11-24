# file: pyinstrument/low_level/stat_profile_python.py:21-54
# asked: {"lines": [21, 29, 30, 31, 33, 34, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 51, 53, 54], "branches": [[31, 33], [31, 35], [33, 34], [33, 35], [39, 40], [39, 41], [41, 42], [41, 44], [44, 45], [44, 49], [45, 46], [45, 47]]}
# gained: {"lines": [21, 29, 30, 31, 33, 34, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 51, 53, 54], "branches": [[31, 33], [31, 35], [33, 34], [33, 35], [39, 40], [39, 41], [41, 42], [41, 44], [44, 45], [44, 49], [45, 46], [45, 47]]}

import timeit
from contextvars import ContextVar
from typing import Any, Callable

import pytest

from pyinstrument.low_level.pyi_timing_thread_python import (
    pyi_timing_thread_get_time,
    pyi_timing_thread_subscribe,
)
from pyinstrument.low_level.stat_profile_python import PythonStatProfiler
from pyinstrument.low_level.types import TimerType


def test_python_stat_profiler_init_with_context_var():
    context_var = ContextVar("test_context_var")
    context_var.set("test_value")

    def target_func(frame, event, arg):
        return None

    profiler = PythonStatProfiler(
        target=target_func,
        interval=0.1,
        context_var=context_var,
        timer_type="walltime",
        timer_func=None,
    )

    assert profiler.target == target_func
    assert profiler.interval == 0.1
    assert profiler.context_var == context_var
    assert profiler.timer_type == "walltime"
    assert profiler.get_time == timeit.default_timer
    assert isinstance(profiler.last_invocation, float)
    assert profiler.last_context_var_value == "test_value"
    assert profiler.await_stack == []


def test_python_stat_profiler_init_with_walltime_thread():
    context_var = ContextVar("test_context_var")

    def target_func(frame, event, arg):
        return None

    profiler = PythonStatProfiler(
        target=target_func,
        interval=0.1,
        context_var=None,
        timer_type="walltime_thread",
        timer_func=None,
    )

    assert profiler.target == target_func
    assert profiler.interval == 0.1
    assert profiler.context_var is None
    assert profiler.timer_type == "walltime_thread"
    assert profiler.get_time == pyi_timing_thread_get_time
    assert isinstance(profiler.last_invocation, float)
    assert profiler.last_context_var_value is None
    assert profiler.await_stack == []


def test_python_stat_profiler_init_with_timer_func():
    context_var = ContextVar("test_context_var")

    def target_func(frame, event, arg):
        return None

    def custom_timer_func():
        return timeit.default_timer()

    profiler = PythonStatProfiler(
        target=target_func,
        interval=0.1,
        context_var=None,
        timer_type="timer_func",
        timer_func=custom_timer_func,
    )

    assert profiler.target == target_func
    assert profiler.interval == 0.1
    assert profiler.context_var is None
    assert profiler.timer_type == "timer_func"
    assert profiler.get_time == custom_timer_func
    assert isinstance(profiler.last_invocation, float)
    assert profiler.last_context_var_value is None
    assert profiler.await_stack == []


def test_python_stat_profiler_init_with_invalid_timer_type():
    context_var = ContextVar("test_context_var")

    def target_func(frame, event, arg):
        return None

    with pytest.raises(ValueError):
        profiler = PythonStatProfiler(
            target=target_func,
            interval=0.1,
            context_var=None,
            timer_type="invalid_timer_type",
            timer_func=None,
        )


def test_python_stat_profiler_init_with_missing_timer_func():
    context_var = ContextVar("test_context_var")

    def target_func(frame, event, arg):
        return None

    with pytest.raises(TypeError):
        profiler = PythonStatProfiler(
            target=target_func,
            interval=0.1,
            context_var=None,
            timer_type="timer_func",
            timer_func=None,
        )


def test_python_stat_profiler_init_with_non_context_var():
    context_var = "not_a_context_var"

    def target_func(frame, event, arg):
        return None

    with pytest.raises(TypeError):
        profiler = PythonStatProfiler(
            target=target_func,
            interval=0.1,
            context_var=context_var,
            timer_type="walltime",
            timer_func=None,
        )
