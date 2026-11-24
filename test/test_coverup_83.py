# file: pyinstrument/vendor/decorator.py:282-287
# asked: {"lines": [285, 286, 287], "branches": []}
# gained: {"lines": [285, 286, 287], "branches": []}

from contextlib import _GeneratorContextManager

import pytest

from pyinstrument.vendor.decorator import ContextManager, FunctionMaker


def test_context_manager_decorator():
    def test_func(a, b):
        return a + b

    # Create a mock generator context manager
    def mock_generator():
        yield

    context_manager = ContextManager(mock_generator)
    decorated_func = context_manager(test_func)

    assert callable(decorated_func)
    assert decorated_func.__wrapped__ == test_func

    # Ensure the function is created correctly
    created_func = FunctionMaker.create(
        test_func,
        "with _self_: return _func_(%(shortsignature)s)",
        dict(_self_=context_manager, _func_=test_func),
        __wrapped__=test_func,
    )

    assert callable(created_func)
    assert created_func.__wrapped__ == test_func

    # Ensure the decorated function behaves as expected
    result = decorated_func(3, 4)
    assert result == 7
