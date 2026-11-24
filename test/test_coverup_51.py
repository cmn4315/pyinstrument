# file: pyinstrument/util.py:87-94
# asked: {"lines": [88, 89, 90, 92, 94], "branches": [[89, 90], [89, 92]]}
# gained: {"lines": [88, 89, 90, 92, 94], "branches": [[89, 90], [89, 92]]}

import codecs
from io import IOBase, StringIO
from unittest.mock import Mock

import pytest

from pyinstrument.util import file_supports_unicode


def test_file_supports_unicode_no_encoding():
    file_obj = Mock(spec=IOBase)
    file_obj.encoding = None

    result = file_supports_unicode(file_obj)

    assert not result


def test_file_supports_unicode_with_encoding():
    file_obj = Mock(spec=IOBase)
    file_obj.encoding = "utf-8"

    result = file_supports_unicode(file_obj)

    assert result


def test_file_supports_unicode_with_invalid_encoding():
    file_obj = Mock(spec=IOBase)
    file_obj.encoding = "invalid-encoding"

    with pytest.raises(LookupError):
        file_supports_unicode(file_obj)


def test_file_supports_unicode_with_utf_encoding():
    file_obj = Mock(spec=IOBase)
    file_obj.encoding = "utf-16"

    result = file_supports_unicode(file_obj)

    assert result


def test_file_supports_unicode_with_non_utf_encoding():
    file_obj = Mock(spec=IOBase)
    file_obj.encoding = "latin-1"

    result = file_supports_unicode(file_obj)

    assert not result
