# file: pyinstrument/magic/magic.py:44-45
# asked: {"lines": [44, 45], "branches": []}
# gained: {"lines": [44, 45], "branches": []}

import pytest

from pyinstrument.magic.magic import InterruptSilently


def test_interrupt_silently_exception():
    # Test that the InterruptSilently exception can be raised
    try:
        raise InterruptSilently("Test interruption")
    except InterruptSilently as e:
        assert str(e) == "Test interruption"


def test_interrupt_silently_docstring():
    # Test that the docstring of InterruptSilently is as expected
    assert (
        InterruptSilently.__doc__
        == "Exception used to interrupt execution without showing traceback"
    )
