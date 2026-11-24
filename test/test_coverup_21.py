# file: pyinstrument/vendor/decorator.py:219-234
# asked: {"lines": [226, 227, 228], "branches": [[225, 226], [232, 234]]}
# gained: {"lines": [226, 227, 228], "branches": [[225, 226]]}

import pytest

from pyinstrument.vendor.decorator import decorate


def test_decorate_with_extras():
    def caller(func, *args, **kwargs):
        return func(*args, **kwargs)

    def func(*args, **kwargs):
        return None

    extras = [1, 2, 3]
    decorated_func = decorate(func, caller, extras=extras)

    assert decorated_func.__name__ == func.__name__
    assert decorated_func.__qualname__ == func.__qualname__

    # Check if extras are correctly passed to the decorated function
    result = decorated_func()
    assert result == None


def test_decorate_with_qualname():
    def caller(func, *args, **kwargs):
        return func(*args, **kwargs)

    def func():
        pass

    func.__qualname__ = "test.func"
    decorated_func = decorate(func, caller)

    assert decorated_func.__name__ == func.__name__
    assert decorated_func.__qualname__ == func.__qualname__

    # Check if qualname is correctly set
    result = decorated_func()
    assert result == None
