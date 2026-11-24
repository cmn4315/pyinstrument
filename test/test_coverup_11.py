# file: pyinstrument/typing.py:15-16
# asked: {"lines": [16], "branches": []}
# gained: {"lines": [16], "branches": []}

import pytest

from pyinstrument.typing import assert_never


def test_assert_never():
    with pytest.raises(ValueError):
        assert_never("test value")
