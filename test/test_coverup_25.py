# file: pyinstrument/renderers/speedscope.py:17-29
# asked: {"lines": [17, 18, 19, 27, 28, 29], "branches": []}
# gained: {"lines": [17, 18, 19, 27, 28, 29], "branches": []}

from dataclasses import dataclass

import pytest

from pyinstrument.renderers.speedscope import SpeedscopeFrame


@pytest.fixture
def speedscope_frame():
    return SpeedscopeFrame(name="test_name", file="test_file", line=123)


def test_speedscope_frame_creation(speedscope_frame):
    assert speedscope_frame.name == "test_name"
    assert speedscope_frame.file == "test_file"
    assert speedscope_frame.line == 123


def test_speedscope_frame_hashability():
    frame1 = SpeedscopeFrame(name="test_name", file="test_file", line=123)
    frame2 = SpeedscopeFrame(name="test_name", file="test_file", line=123)
    assert hash(frame1) == hash(frame2)


def test_speedscope_frame_inequality():
    frame1 = SpeedscopeFrame(name="test_name", file="test_file", line=123)
    frame2 = SpeedscopeFrame(name="another_name", file="test_file", line=123)
    assert frame1 != frame2
