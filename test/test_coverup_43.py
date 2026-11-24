# file: pyinstrument/session.py:112-141
# asked: {"lines": [123, 125, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138, 140], "branches": [[123, 125], [123, 127]]}
# gained: {"lines": [123, 125, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138, 140], "branches": [[123, 125], [123, 127]]}

import pytest

from pyinstrument.session import Session


@pytest.fixture
def session_objects():
    session1 = Session(
        frame_records=[1, 2, 3],
        start_time=10,
        duration=100,
        min_interval=1,
        max_interval=10,
        sample_count=10,
        start_call_stack="call_stack1",
        target_description="target1",
        cpu_time=50,
        sys_path=["path1", "path2"],
        sys_prefixes=["prefix1"],
    )

    session2 = Session(
        frame_records=[4, 5, 6],
        start_time=5,
        duration=50,
        min_interval=0.5,
        max_interval=5,
        sample_count=5,
        start_call_stack="call_stack2",
        target_description="target2",
        cpu_time=25,
        sys_path=["path2", "path3"],
        sys_prefixes=["prefix2"],
    )

    return session1, session2


def test_combine_sessions_order(session_objects):
    session1, session2 = session_objects

    combined_session = Session.combine(session1, session2)

    assert combined_session.start_time == session2.start_time
    assert combined_session.frame_records == session2.frame_records + session1.frame_records
    assert combined_session.min_interval == session2.min_interval
    assert combined_session.max_interval == session1.max_interval
    assert combined_session.duration == session2.duration + session1.duration
    assert combined_session.sample_count == session2.sample_count + session1.sample_count
    assert combined_session.start_call_stack == session2.start_call_stack
    assert combined_session.target_description == session2.target_description
    assert combined_session.cpu_time == session2.cpu_time + session1.cpu_time
    assert combined_session.sys_path == session2.sys_path + [
        p for p in session1.sys_path if p not in session2.sys_path
    ]
    assert combined_session.sys_prefixes == list(
        set([*session2.sys_prefixes, *session1.sys_prefixes])
    )


def test_combine_sessions_same_start_time(session_objects):
    session1, session2 = session_objects
    session1.start_time = 5

    combined_session = Session.combine(session1, session2)

    assert combined_session.start_time == session1.start_time
    assert combined_session.frame_records == session1.frame_records + session2.frame_records
    assert combined_session.min_interval == min(session1.min_interval, session2.min_interval)
    assert combined_session.max_interval == max(session1.max_interval, session2.max_interval)
    assert combined_session.duration == session1.duration + session2.duration
    assert combined_session.sample_count == session1.sample_count + session2.sample_count
    assert combined_session.start_call_stack == session1.start_call_stack
    assert combined_session.target_description == session1.target_description
    assert combined_session.cpu_time == session1.cpu_time + session2.cpu_time
    assert combined_session.sys_path == session1.sys_path + [
        p for p in session2.sys_path if p not in session1.sys_path
    ]
    assert combined_session.sys_prefixes == list(
        set([*session1.sys_prefixes, *session2.sys_prefixes])
    )
