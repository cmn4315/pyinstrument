# file: pyinstrument/vendor/decorator.py:306-308
# asked: {"lines": [308], "branches": []}
# gained: {"lines": [308], "branches": []}

import pytest

from pyinstrument.vendor.decorator import _contextmanager, contextmanager


def test_contextmanager_returns_contextmanager():
    # Arrange
    def mock_func():
        pass

    # Act
    result = contextmanager(mock_func)

    # Assert
    assert isinstance(result, type(_contextmanager(mock_func)))
