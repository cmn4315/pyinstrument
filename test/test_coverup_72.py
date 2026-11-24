# file: pyinstrument/frame.py:258-260
# asked: {"lines": [260], "branches": []}
# gained: {"lines": [260], "branches": []}

import pytest

from pyinstrument.frame import Frame


def test_is_synthetic_leaf_true(monkeypatch):
    # Arrange
    synthetic_identifier = "synthetic_identifier"
    monkeypatch.setattr("pyinstrument.frame.SYNTHETIC_LEAF_IDENTIFIERS", {synthetic_identifier})
    frame = Frame()
    frame.identifier = synthetic_identifier

    # Act
    result = frame.is_synthetic_leaf

    # Assert
    assert result is True


def test_is_synthetic_leaf_false(monkeypatch):
    # Arrange
    non_synthetic_identifier = "non_synthetic_identifier"
    monkeypatch.setattr("pyinstrument.frame.SYNTHETIC_LEAF_IDENTIFIERS", {"synthetic_identifier"})
    frame = Frame()
    frame.identifier = non_synthetic_identifier

    # Act
    result = frame.is_synthetic_leaf

    # Assert
    assert result is False
