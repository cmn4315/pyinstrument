# file: pyinstrument/util.py:56-69
# asked: {"lines": [59, 60, 61, 62, 63, 64, 67, 69], "branches": [[60, 61], [60, 67]]}
# gained: {"lines": [59, 60, 61, 62, 63, 64, 67, 69], "branches": [[60, 61], [60, 67]]}

from typing import Any

import pytest

from pyinstrument.util import deprecated_option
from pyinstrument.vendor.decorator import decorator


def test_deprecated_option_with_warning():
    @deprecated_option("deprecated_option", "This option is deprecated.")
    def test_function(arg1, **kwargs):
        return arg1

    with pytest.warns(DeprecationWarning) as record:
        test_function("test", deprecated_option="value")

    assert len(record) == 1
    assert str(record[0].message) == "deprecated_option is deprecated. This option is deprecated."


def test_deprecated_option_without_warning():
    @deprecated_option("deprecated_option", "This option is deprecated.")
    def test_function(arg1, **kwargs):
        return arg1

    result = test_function("test")
    assert result == "test"
