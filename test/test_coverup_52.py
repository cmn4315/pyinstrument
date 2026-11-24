# file: pyinstrument/vendor/decorator.py:48-49
# asked: {"lines": [49], "branches": []}
# gained: {"lines": [49], "branches": []}

import pytest

from pyinstrument.vendor.decorator import get_init


def test_get_init():
    class TestClass:
        def __init__(self):
            pass

    assert get_init(TestClass) is TestClass.__init__


def test_get_init_with_inheritance():
    class BaseClass:
        def __init__(self):
            pass

    class DerivedClass(BaseClass):
        pass

    assert get_init(DerivedClass) is BaseClass.__init__
