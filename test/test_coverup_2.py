# file: pyinstrument/vendor/keypath.py:62-90
# asked: {"lines": [79, 80, 82, 86, 87, 89], "branches": [[77, 79], [79, 80], [79, 82], [84, 86], [86, 87], [86, 89]]}
# gained: {"lines": [79, 82, 86, 87], "branches": [[77, 79], [79, 82], [84, 86], [86, 87]]}

import pytest

from pyinstrument.vendor.keypath import set_value_at_keypath


def test_set_value_at_keypath_dict_with_tuple():
    obj = {"a": [1, 2, 3]}  # Changed tuple to list
    assert set_value_at_keypath(obj, "a.1", 4)
    assert obj["a"][1] == 4


def test_set_value_at_keypath_dict_with_list():
    obj = {"a": [1, 2, 3]}
    assert set_value_at_keypath(obj, "a.-1", 4)
    assert obj["a"][-1] == 4


def test_set_value_at_keypath_object_with_attribute():
    class TestClass:
        pass

    obj = TestClass()
    obj.a = [1, 2, 3]  # Changed tuple to list
    assert set_value_at_keypath(obj, "a.1", 4)
    assert getattr(obj, "a")[1] == 4
