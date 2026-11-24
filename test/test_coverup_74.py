# file: pyinstrument/vendor/keypath.py:62-90
# asked: {"lines": [75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 89, 90], "branches": [[76, 77], [76, 83], [77, 78], [77, 79], [79, 80], [79, 82], [84, 85], [84, 86], [86, 87], [86, 89]]}
# gained: {"lines": [75, 76, 77, 78, 83, 84, 85, 86, 87, 89, 90], "branches": [[76, 77], [76, 83], [77, 78], [84, 85], [84, 86], [86, 87], [86, 89]]}

import pytest

from pyinstrument.vendor.keypath import set_value_at_keypath


def test_set_value_at_keypath_dict():
    x = {"a": 1, "b": 2, "c": {"d": 3, "e": 4, "f": [2, {"x": "foo", "y": "bar"}, 5]}}
    assert set_value_at_keypath(x, "a", 2)
    assert x["a"] == 2
    assert set_value_at_keypath(x, "c.f.-1", 6)
    assert x["c"]["f"][-1] == 6


def test_set_value_at_keypath_list():
    x = [1, 2, 3]
    assert set_value_at_keypath(x, "1", 2)
    assert x[1] == 2
    assert set_value_at_keypath(x, "-1", 6)
    assert x[-1] == 6


def test_set_value_at_keypath_object():
    class TestClass:
        pass

    x = TestClass()
    x.a = 1
    x.b = 2
    assert set_value_at_keypath(x, "a", 2)
    assert x.a == 2
    assert set_value_at_keypath(x, "b", 6)
    assert x.b == 6
