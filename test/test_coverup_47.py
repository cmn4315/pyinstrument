# file: pyinstrument/context_manager.py:47-63
# asked: {"lines": [50, 52, 53, 54, 55, 56, 58, 59, 61, 63], "branches": [[50, 53], [50, 63], [55, 56], [55, 58]]}
# gained: {"lines": [50, 52, 53, 61, 63], "branches": [[50, 53], [50, 63]]}

from functools import wraps
from types import FunctionType

import pytest

from pyinstrument.context_manager import ProfileContext, ProfileContextOptions


def test_profile_context_with_function():
    def test_func():
        pass

    profile_context = ProfileContext(options={})
    wrapped_func = profile_context(test_func)

    assert wrapped_func.__name__ == test_func.__name__
    assert wrapped_func.__qualname__ == test_func.__qualname__


def test_profile_context_without_function():
    profile_context = ProfileContext(options={"option": "value"})
    new_context = profile_context()

    assert isinstance(new_context, ProfileContext)
    assert new_context.options == {"options": {"option": "value"}}


def test_profile_context_target_description():
    def test_func():
        pass

    profile_context = ProfileContext(options={"target_description": "Custom Description"})
    wrapped_func = profile_context(test_func)

    assert wrapped_func.__name__ == test_func.__name__
    assert wrapped_func.__qualname__ == test_func.__qualname__
