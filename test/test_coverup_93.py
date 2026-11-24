# file: pyinstrument/frame.py:254-256
# asked: {"lines": [256], "branches": []}
# gained: {"lines": [256], "branches": []}

import pytest

from pyinstrument.frame import SYNTHETIC_FRAME_IDENTIFIERS, Frame


@pytest.fixture
def frame(monkeypatch):
    class MockFrame(Frame):
        def __init__(self, identifier=""):
            self.identifier = identifier
            self.parent = None
            self.time = 0.0
            self.group = None
            self.absorbed_time = 0.0
            self._context = None
            self._identifier_parts = identifier.split("\x00")
            self.attributes = {}
            self._children = []

    return MockFrame()


def test_is_synthetic_true(frame, monkeypatch):
    synthetic_identifier = next(iter(SYNTHETIC_FRAME_IDENTIFIERS))
    monkeypatch.setattr(frame, "identifier", synthetic_identifier)
    assert frame.is_synthetic == True


def test_is_synthetic_false(frame, monkeypatch):
    non_synthetic_identifier = "non_synthetic_identifier"
    monkeypatch.setattr(frame, "identifier", non_synthetic_identifier)
    assert frame.is_synthetic == False
