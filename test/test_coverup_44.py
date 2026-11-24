# file: pyinstrument/session.py:236-257
# asked: {"lines": [243, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256], "branches": []}
# gained: {"lines": [243, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256], "branches": []}

import pytest

from pyinstrument import session


@pytest.fixture
def sample_session():
    session_instance = session.Session(
        frame_records=[],
        start_time=0,
        duration=0,
        min_interval=0,
        max_interval=0,
        sample_count=0,
        start_call_stack=[],
        target_description="",
        cpu_time=0,
        sys_path=[],
        sys_prefixes=[],
    )
    session_instance.frame_records = [1, 2, 3, 4, 5]
    return session_instance


def test_resample_with_non_empty_frame_records(sample_session):
    # Arrange
    interval = 1.0
    sample_session._resample_frame_records = lambda records, interval: records[
        ::2
    ]  # Simulate resampling

    # Act
    new_session = sample_session.resample(interval)

    # Assert
    assert new_session.frame_records == [1, 3, 5]
    assert new_session.start_time == sample_session.start_time
    assert new_session.duration == sample_session.duration
    assert new_session.min_interval == interval
    assert new_session.max_interval == interval
    assert new_session.sample_count == len(new_session.frame_records)
    assert new_session.start_call_stack == sample_session.start_call_stack
    assert new_session.target_description == sample_session.target_description
    assert new_session.cpu_time == sample_session.cpu_time
    assert new_session.sys_path == sample_session.sys_path
    assert new_session.sys_prefixes == sample_session.sys_prefixes


def test_resample_with_empty_frame_records(sample_session):
    # Arrange
    interval = 1.0
    sample_session.frame_records = []
    sample_session._resample_frame_records = lambda records, interval: []  # Simulate resampling

    # Act
    new_session = sample_session.resample(interval)

    # Assert
    assert new_session.frame_records == []
    assert new_session.start_time == sample_session.start_time
    assert new_session.duration == sample_session.duration
    assert new_session.min_interval == interval
    assert new_session.max_interval == interval
    assert new_session.sample_count == len(new_session.frame_records)
    assert new_session.start_call_stack == sample_session.start_call_stack
    assert new_session.target_description == sample_session.target_description
    assert new_session.cpu_time == sample_session.cpu_time
    assert new_session.sys_path == sample_session.sys_path
    assert new_session.sys_prefixes == sample_session.sys_prefixes
