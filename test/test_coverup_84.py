# file: pyinstrument/__init__.py:13-21
# asked: {"lines": [19, 21], "branches": []}
# gained: {"lines": [19, 21], "branches": []}

from unittest.mock import MagicMock, patch

import pytest

from pyinstrument import load_ipython_extension


@pytest.fixture
def mock_ipython():
    with patch("pyinstrument.magic.PyinstrumentMagic") as mock_magic:
        yield mock_magic


def test_load_ipython_extension_imports_PyinstrumentMagic(mock_ipython):
    mock_ipython_instance = MagicMock()
    with patch(
        "IPython.core.interactiveshell.InteractiveShell.instance",
        return_value=mock_ipython_instance,
    ):
        load_ipython_extension(mock_ipython_instance)
        mock_ipython_instance.register_magics.assert_called_once_with(mock_ipython)


def test_load_ipython_extension_registers_magics(mock_ipython):
    mock_ipython_instance = MagicMock()
    with patch(
        "IPython.core.interactiveshell.InteractiveShell.instance",
        return_value=mock_ipython_instance,
    ):
        load_ipython_extension(mock_ipython_instance)
        mock_ipython_instance.register_magics.assert_called_once_with(mock_ipython)
