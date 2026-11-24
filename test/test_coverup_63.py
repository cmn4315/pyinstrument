# file: pyinstrument/magic/magic.py:50-52
# asked: {"lines": [51, 52], "branches": []}
# gained: {"lines": [51, 52], "branches": []}

import pytest
from IPython.core.interactiveshell import InteractiveShell

from pyinstrument.magic.magic import PyinstrumentMagic


@pytest.fixture
def mock_shell(monkeypatch):
    class MockShell(InteractiveShell):
        pass

    shell = MockShell()
    yield shell


def test_pyinstrument_magic_init(mock_shell):
    pyinstrument_magic = PyinstrumentMagic(mock_shell)
    assert pyinstrument_magic._transformer is None
