# file: pyinstrument/util.py:30-36
# asked: {"lines": [32], "branches": [[31, 32]]}
# gained: {"lines": [32], "branches": [[31, 32]]}

import pytest

from pyinstrument.util import object_with_import_path


def test_object_with_import_path_invalid_path():
    with pytest.raises(ValueError) as exc_info:
        object_with_import_path("invalid_path")
    assert "Can't import 'invalid_path', it is not a valid import path" in str(exc_info.value)


def test_object_with_import_path_valid_path():
    import_path = "pyinstrument.util.object_with_import_path"
    result = object_with_import_path(import_path)
    assert callable(result)
