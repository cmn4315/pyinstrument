# file: pyinstrument/util.py:72-84
# asked: {"lines": [79, 80, 82, 84], "branches": []}
# gained: {"lines": [79, 80, 82, 84], "branches": []}

import os
import sys
from unittest.mock import MagicMock

import pytest

from pyinstrument.util import file_is_a_tty, file_supports_color


@pytest.fixture
def mock_file_obj(monkeypatch):
    file_obj = MagicMock()
    monkeypatch.setattr("pyinstrument.util.file_is_a_tty", lambda x: file_obj.isatty())
    return file_obj


def test_file_supports_color_supported_platform_tty(monkeypatch, mock_file_obj):
    monkeypatch.setattr(sys, "platform", "linux")
    monkeypatch.setitem(os.environ, "ANSICON", "true")
    mock_file_obj.isatty.return_value = True
    assert file_supports_color(mock_file_obj) == True


def test_file_supports_color_supported_platform_not_tty(monkeypatch, mock_file_obj):
    monkeypatch.setattr(sys, "platform", "linux")
    monkeypatch.setitem(os.environ, "ANSICON", "true")
    mock_file_obj.isatty.return_value = False
    assert file_supports_color(mock_file_obj) == False


def test_file_supports_color_unsupported_platform_tty(monkeypatch, mock_file_obj):
    monkeypatch.setattr(sys, "platform", "win32")
    monkeypatch.delitem(os.environ, "ANSICON", raising=False)
    mock_file_obj.isatty.return_value = True
    assert file_supports_color(mock_file_obj) == False


def test_file_supports_color_unsupported_platform_not_tty(monkeypatch, mock_file_obj):
    monkeypatch.setattr(sys, "platform", "win32")
    monkeypatch.delitem(os.environ, "ANSICON", raising=False)
    mock_file_obj.isatty.return_value = False
    assert file_supports_color(mock_file_obj) == False


def test_file_supports_color_pocket_pc_tty(monkeypatch, mock_file_obj):
    monkeypatch.setattr(sys, "platform", "Pocket PC")
    mock_file_obj.isatty.return_value = True
    assert file_supports_color(mock_file_obj) == False


def test_file_supports_color_pocket_pc_not_tty(monkeypatch, mock_file_obj):
    monkeypatch.setattr(sys, "platform", "Pocket PC")
    mock_file_obj.isatty.return_value = False
    assert file_supports_color(mock_file_obj) == False
