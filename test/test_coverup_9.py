# file: pyinstrument/session.py:187-215
# asked: {"lines": [207, 208], "branches": [[198, 213]]}
# gained: {"lines": [207, 208], "branches": [[198, 213]]}

from unittest.mock import Mock, patch

import pytest

from pyinstrument.session import Session


@pytest.fixture
def session():
    sys_path = ["/usr/lib", "/usr/local/lib"]
    sys_prefixes = ["/usr"]
    frame_records = []
    start_time = 0.0
    duration = 1.0
    min_interval = 0.01
    max_interval = 1.0
    sample_count = 100
    start_call_stack = []
    target_description = "test"
    cpu_time = 0.5
    return Session(
        frame_records,
        start_time,
        duration,
        min_interval,
        max_interval,
        sample_count,
        start_call_stack,
        target_description,
        cpu_time,
        sys_path,
        sys_prefixes,
    )


def test_shorten_path_no_sep(session):
    result = session.shorten_path("<built-in>")
    assert result == "<built-in>"


def test_shorten_path_with_sep(session):
    result = session.shorten_path("/usr/lib/python3.8/site-packages/pyinstrument/session.py")
    assert result == "python3.8/site-packages/pyinstrument/session.py"


def test_shorten_path_different_drives(session):
    result = session.shorten_path("D:\\path\\to\\file.py")
    assert result == "D:\\path\\to\\file.py"


def test_shorten_path_value_error(session):
    with patch("os.path.relpath", side_effect=ValueError):
        result = session.shorten_path("/usr/lib/python3.8/site-packages/pyinstrument/session.py")
    assert result == "/usr/lib/python3.8/site-packages/pyinstrument/session.py"
