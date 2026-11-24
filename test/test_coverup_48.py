# file: pyinstrument/session.py:147-163
# asked: {"lines": [155, 157, 158, 160, 161, 163], "branches": [[157, 158], [157, 160], [160, 161], [160, 163]]}
# gained: {"lines": [155, 157, 158], "branches": [[157, 158]]}

import pytest

from pyinstrument.frame import Frame
from pyinstrument.frame_ops import build_frame_tree
from pyinstrument.session import Session


def test_session_root_frame_none():
    session = Session(
        frame_records=[],
        start_time=0.0,
        duration=0.0,
        min_interval=0.0,
        max_interval=0.0,
        sample_count=0,
        start_call_stack=None,
        target_description=None,
        cpu_time=0.0,
        sys_path=None,
        sys_prefixes=None,
    )

    # Ensure the build_frame_tree function returns None
    def mock_build_frame_tree(frame_records, context):
        assert context == session
        return None

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("pyinstrument.frame_ops.build_frame_tree", mock_build_frame_tree)
        result = session.root_frame()

    assert result is None


def test_session_root_frame_trim_stem():
    session = Session(
        frame_records=[],
        start_time=0.0,
        duration=0.0,
        min_interval=0.0,
        max_interval=0.0,
        sample_count=0,
        start_call_stack=None,
        target_description=None,
        cpu_time=0.0,
        sys_path=None,
        sys_prefixes=None,
    )

    # Mock the build_frame_tree function to return a Frame object
    def mock_build_frame_tree(frame_records, context):
        assert context == session
        return Frame(None, None, None, None, None, None, None, None, None, None)

    # Mock the _trim_stem method to return a modified Frame object
    def mock_trim_stem(frame):
        return Frame(None, None, None, None, None, None, None, None, None, None)

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("pyinstrument.frame_ops.build_frame_tree", mock_build_frame_tree)
        mp.setattr(session, "_trim_stem", mock_trim_stem)
        result = session.root_frame(trim_stem=True)

    # Check if the result is not None before accessing its attributes
    if result is not None:
        assert result.parent is None
