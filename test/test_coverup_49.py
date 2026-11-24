# file: pyinstrument/frame.py:159-162
# asked: {"lines": [161, 162], "branches": [[161, 0], [161, 162]]}
# gained: {"lines": [161, 162], "branches": [[161, 0], [161, 162]]}

import pytest

from pyinstrument.frame import Frame


@pytest.fixture
def frame_instance():
    class MockFrame(Frame):
        def __init__(self, identifier_parts):
            self._identifier_parts = identifier_parts

    return MockFrame


def test_file_path_with_parts(frame_instance):
    instance = frame_instance(identifier_parts=["part1", "part2"])
    assert instance.file_path == "part2"


def test_file_path_without_parts(frame_instance):
    instance = frame_instance(identifier_parts=[])
    assert instance.file_path is None


def test_file_path_with_one_part(frame_instance):
    instance = frame_instance(identifier_parts=["part1"])
    assert instance.file_path is None
