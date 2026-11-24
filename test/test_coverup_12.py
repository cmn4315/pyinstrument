# file: pyinstrument/util.py:87-94
# asked: {"lines": [90], "branches": [[89, 90]]}
# gained: {"lines": [90], "branches": [[89, 90]]}

from typing import IO, AnyStr
from unittest.mock import Mock

import pytest

from pyinstrument.util import file_supports_unicode


def test_file_supports_unicode_no_encoding():
    file_obj = Mock(spec=IO[AnyStr])
    file_obj.encoding = None
    assert not file_supports_unicode(file_obj)


def test_file_supports_unicode_with_encoding():
    file_obj = Mock(spec=IO[AnyStr])
    file_obj.encoding = "utf-8"
    assert file_supports_unicode(file_obj)


def test_file_supports_unicode_non_utf_encoding():
    file_obj = Mock(spec=IO[AnyStr])
    file_obj.encoding = "latin-1"
    assert not file_supports_unicode(file_obj)
