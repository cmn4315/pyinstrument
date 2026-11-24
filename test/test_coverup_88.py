# file: pyinstrument/__main__.py:677-680
# asked: {"lines": [679, 680], "branches": []}
# gained: {"lines": [679, 680], "branches": []}

import pytest

from pyinstrument.__main__ import ValueWithRemainingArgs


def test_value_with_remaining_args_init():
    value = "test_value"
    remaining_args = ["arg1", "arg2"]

    vwra = ValueWithRemainingArgs(value, remaining_args)

    assert vwra.value == value, "The 'value' attribute was not set correctly."
    assert vwra.remaining_args == remaining_args, (
        "The 'remaining_args' attribute was not set correctly."
    )
