# file: pyinstrument/frame.py:169-178
# asked: {"lines": [173, 176], "branches": [[172, 173], [175, 176]]}
# gained: {"lines": [173, 176], "branches": [[172, 173], [175, 176]]}

import pytest

from pyinstrument.frame import Frame


@pytest.fixture
def context_fixture():
    class MockContext:
        def shorten_path(self, path):
            return path + "_shortened"

    yield MockContext


@pytest.fixture
def frame_fixture(context_fixture):
    class MockFrame(Frame):
        def __init__(self, is_synthetic, parent, file_path, context):
            self._is_synthetic = is_synthetic
            self._parent = parent
            self._file_path = file_path
            self._context = context

        @property
        def is_synthetic(self):
            return self._is_synthetic

        @property
        def parent(self):
            return self._parent

        @property
        def file_path(self):
            return self._file_path

        @property
        def context(self):
            return self._context

    yield MockFrame


def test_file_path_short_synthetic_with_parent(frame_fixture, context_fixture):
    parent_frame = frame_fixture(
        is_synthetic=True,
        parent=frame_fixture(
            is_synthetic=False, parent=None, file_path="parent_file_path", context=context_fixture()
        ),
        file_path=None,
        context=context_fixture(),
    )
    frame = frame_fixture(
        is_synthetic=True, parent=parent_frame, file_path=None, context=context_fixture()
    )
    assert frame.file_path_short == "parent_file_path_shortened"


def test_file_path_short_synthetic_without_parent(frame_fixture, context_fixture):
    frame = frame_fixture(is_synthetic=True, parent=None, file_path=None, context=context_fixture())
    assert frame.file_path_short is None


def test_file_path_short_non_synthetic_with_file_path(frame_fixture, context_fixture):
    frame = frame_fixture(
        is_synthetic=False, parent=None, file_path="file_path", context=context_fixture()
    )
    assert frame.file_path_short == "file_path_shortened"


def test_file_path_short_non_synthetic_without_file_path(frame_fixture, context_fixture):
    frame = frame_fixture(
        is_synthetic=False, parent=None, file_path=None, context=context_fixture()
    )
    assert frame.file_path_short is None
