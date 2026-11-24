# file: pyinstrument/session.py:112-141
# asked: {"lines": [125], "branches": [[123, 125]]}
# gained: {"lines": [125], "branches": [[123, 125]]}

import pytest

from pyinstrument.session import Session


def test_combine_session1_start_time_greater():
    session1 = Session(
        start_time=2,
        frame_records=[],
        min_interval=0,
        max_interval=0,
        duration=0,
        sample_count=0,
        start_call_stack=[],
        target_description="",
        cpu_time=0,
        sys_path=[],
        sys_prefixes=[],
    )
    session2 = Session(
        start_time=1,
        frame_records=[],
        min_interval=0,
        max_interval=0,
        duration=0,
        sample_count=0,
        start_call_stack=[],
        target_description="",
        cpu_time=0,
        sys_path=[],
        sys_prefixes=[],
    )

    result = Session.combine(session1, session2)

    assert result.start_time == session2.start_time
    assert result.frame_records == session1.frame_records + session2.frame_records
    assert result.min_interval == min(session1.min_interval, session2.min_interval)
    assert result.max_interval == max(session1.max_interval, session2.max_interval)
    assert result.duration == session1.duration + session2.duration
    assert result.sample_count == session1.sample_count + session2.sample_count
    assert result.start_call_stack == session1.start_call_stack
    assert result.target_description == session1.target_description
    assert result.cpu_time == session1.cpu_time + session2.cpu_time
    assert result.sys_path == session1.sys_path + [
        p for p in session2.sys_path if p not in session1.sys_path
    ]
    assert result.sys_prefixes == list(set([*session1.sys_prefixes, *session2.sys_prefixes]))
