# file: pyinstrument/vendor/decorator.py:313-327
# asked: {"lines": [318, 319, 320, 321, 322, 323, 324, 325, 326, 327], "branches": [[319, 320], [319, 326], [320, 321], [320, 323], [323, 319], [323, 324], [326, 0], [326, 327]]}
# gained: {"lines": [318, 319, 320, 321, 322, 323, 324, 325, 326, 327], "branches": [[319, 320], [319, 326], [320, 321], [320, 323], [323, 319], [323, 324], [326, 0], [326, 327]]}

import pytest

from pyinstrument.vendor.decorator import append


def test_append_no_subclass():
    class A:
        pass

    class B:
        pass

    vancestors = [B]
    a = A
    append(a, vancestors)
    assert vancestors == [B, A]


def test_append_issubclass_va():
    class A:
        pass

    class B(A):
        pass

    vancestors = [B]
    a = A
    append(a, vancestors)
    assert vancestors == [B]


def test_append_issubclass_a():
    class A:
        pass

    class B(A):
        pass

    vancestors = [A]
    a = B
    append(a, vancestors)
    assert vancestors == [B]
