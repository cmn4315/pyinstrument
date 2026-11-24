# file: pyinstrument/session.py:187-215
# asked: {"lines": [192, 193, 195, 198, 199, 205, 206, 207, 208, 210, 211, 213, 215], "branches": [[192, 193], [192, 195], [198, 199], [198, 213], [199, 205], [199, 213], [210, 199], [210, 211]]}
# gained: {"lines": [192, 193, 195, 198, 199, 205, 206, 210, 211, 213, 215], "branches": [[192, 193], [192, 195], [198, 199], [198, 213], [199, 205], [199, 213], [210, 199], [210, 211]]}

import pytest

from pyinstrument.session import Session


@pytest.fixture
def session():
    return Session(
        sys_path=["/usr/lib", "/usr/local/lib"],
        frame_records=[],
        start_time=0,
        duration=0,
        min_interval=0,
        max_interval=0,
        sample_count=0,
        start_call_stack=[],
        target_description="",
        cpu_time=0,
        sys_prefixes=[],
    )


def test_shorten_path_cached(session):
    session._short_file_path_cache = {"/usr/lib/some/path": "/some/path"}
    result = session.shorten_path("/usr/lib/some/path")
    assert result == "/some/path"


def test_shorten_path_not_cached(session):
    session._short_file_path_cache = {}
    result = session.shorten_path("/usr/lib/some/path")
    assert result == "some/path"
    assert session._short_file_path_cache["/usr/lib/some/path"] == "some/path"


def test_shorten_path_not_a_file_path(session):
    result = session.shorten_path("<built-in>")
    assert result == "<built-in>"


def test_shorten_path_relpath_exception(session):
    session._short_file_path_cache = {}
    result = session.shorten_path("C:/some/path")
    assert result == "C:/some/path"
    assert session._short_file_path_cache["C:/some/path"] == "C:/some/path"


def test_shorten_path_relpath_success(session):
    session._short_file_path_cache = {}
    result = session.shorten_path("/usr/lib/some/path")
    assert result == "some/path"
    assert session._short_file_path_cache["/usr/lib/some/path"] == "some/path"
